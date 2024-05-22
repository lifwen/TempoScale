import tool.tools as tools
import time

node_name = ["node1", "node2"]
node_ip = ["192.168.144.101", "192.168.144.102"]
namespace = "sock-shop"
scaling_pod_name = "front-end"
mode = "hyscale"
interval_time = 15
i = 0
while True:
    pod_name = tools.collect_metrics(namespace)
    if i >= 200:
        if (i - 200) % 48 == 0:
            result = []
        resource = result[(i - 200) % 48]
        tools.scaling(tools.locate_node(namespace, node_name), pod_name, scaling_pod_name, mode, namespace, resource)
    time.sleep(interval_time)
    i = i + 1

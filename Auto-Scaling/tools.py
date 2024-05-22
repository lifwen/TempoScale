import os
import csv
import time
import numpy as np
import subprocess
import pandas as pd


def collect_metrics(namespace):
    pod_name = []
    try:
        result = subprocess.check_output("kubectl top pod -n " + namespace, shell=True, text=True)
        top_pod_output = result.strip().split('\n')
        current_time = str(time.time())
        for i in range(1, len(top_pod_output)):
            top_pod_value = top_pod_output[i].split()
            top_pod_value.append(current_time)
            pod_name.append(top_pod_value[0])
            if not os.path.exists("./history/" + top_pod_value[0] + '.csv'):
                with open("./history/" + top_pod_value[0] + '.csv', 'a', newline='') as out:
                    csv_writer = csv.writer(out, dialect='excel')
                    csv_writer.writerow(["POD", "CPU", "MEMORY", "TIME"])
                    csv_writer.writerow(top_pod_value)
            else:
                with open("./history/" + top_pod_value[0] + '.csv', 'a', newline='') as out:
                    csv_writer = csv.writer(out, dialect='excel')
                    csv_writer.writerow(top_pod_value)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    return pod_name


def collect_pod_id(pod_name, namespace):
    command = ''
    pod_id = []
    for i in range(0, len(pod_name)):
        command_temp = "kubectl get pod -n " + namespace + " " + pod_name[i] + " -o jsonpath='{.metadata.uid}'"
        command = command + command_temp + " ; "
    pod_id_result = subprocess.check_output(command, shell=True)
    pod_id_result = pod_id_result.strip().decode('utf-8')
    for i in range(0, len(pod_id_result), 36):
        pod_id.append(pod_id_result[i:i + 8])
    return pod_id


def locate_node(namespace, node_name):
    pod_locate = []
    for i in range(0, len(node_name)):
        pod_locate.append([node_name[i]])
    for i in range(0, len(node_name)):
        try:
            pod_node = subprocess.check_output(
                "kubectl get pod -n " + namespace + " -o wide | grep '" + pod_locate[i][0] + "'", shell=True, text=True)
            pod_node = pod_node.strip().split('\n')
            for line in pod_node:
                line = line.replace(',', '\t')
                list0 = line.split()
                pod_locate[i].append(list0[0])
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
    return pod_locate


def maxfilesize(replicas_name, base_path):
    max_file_size = 0
    max_file_path = ''
    for file_name in replicas_name:
        file_path = os.path.join(base_path, file_name + ".csv")
        if os.path.exists(file_path):
            file_size = os.path.getsize(file_path)
        else:
            file_size = 0
        if file_size > max_file_size:
            max_file_size = file_size
            max_file_path = file_path
    return max_file_path


def scaling(pod_locate, pod_name, scaling_pod_name, mode, namespace, resource):
    replicas_name = []
    replicas_locate = []
    replicas_id = []
    try:
        all_replicas = subprocess.check_output(
            "kubectl get pod -n " + namespace + " -o wide | grep " + scaling_pod_name + " | grep Running",
            shell=True, text=True)
        all_replicas = all_replicas.strip().split('\n')
        for line in all_replicas:
            line = line.replace(',', '\t')
            list0 = line.split()
            replicas_name.append(list0[0])
            replicas_locate.append(list0[6])
            try:
                all_replicas_id = subprocess.check_output(
                    "kubectl get pod -n " + namespace + " " + list0[0] + " -o jsonpath='{.metadata.uid}'",
                    shell=True, text=True)
                all_replicas_id = all_replicas_id.strip().split('\n')
                for element in all_replicas_id:
                    replicas_id.append(element)
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    history_file = maxfilesize(replicas_name, './history/')

    tag_title = True
    memory_usage = []
    cpu_usage = []
    timestamp = []
    with open(history_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if tag_title:
                tag_title = False
                continue
            cpu_usage.append(float(row[1][:-1]))
            memory_usage.append(float(row[2][:-2]))
            timestamp.append(float(row[3]))

    if not os.path.exists("./scale/front-end.csv"):
        with open("./scale/front-end.csv", 'a', newline='') as out:
            csv_writer = csv.writer(out, dialect='excel')
            csv_writer.writerow(["Resource", "Time"])
    scale_file = "./scale/front-end.csv"

    row = [resource / 0.8, timestamp[-1]]

    for i in range(0, len(replicas_id)):
        print("ssh root@" + replicas_locate[i] + " 'python scale.py " + str(
            min(max(int(row[0]) * 100, 1000), 30000)) + " " + str(
            replicas_id[i]) + "'")
        os.system("ssh root@" + replicas_locate[i] + " 'python scale.py " + str(
            min(max(int(row[0]) * 100, 1000), 30000)) + " " + str(
            replicas_id[i]) + "'")

    with open(scale_file, "a", newline='') as out:
        csv_writer = csv.writer(out, dialect="excel")
        csv_writer.writerow(row)

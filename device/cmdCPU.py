import time
import subprocess
import re
import pandas as pd

monitoring_interval = 0.2


def get_cpu_usage(pid):
    stat_file = "/proc/{}/stat".format(pid)
    with open(stat_file, 'r') as File:
        stat_data = File.read().split()

    utime = float(stat_data[13])
    stime = float(stat_data[14])

    total_time = utime + stime
    return total_time

def run_command():
    cmd = "ps -ef | grep simple_switch"
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if process.returncode != 0:
        print("Error:", error)
        return []
    output_lines = output.split('\n')
    output_lines = filter(lambda x: x, output_lines)
    switch_process_list= {}
    for line in output_lines:
        if '--device-id' in str(line):
            switch_name=re.findall(r'@s\d+', line)[0].split('@')[1]
            switch_process_id = line.split()[1]
            switch_process_list[switch_name]=switch_process_id
    return switch_process_list

def main(pid_to_monitor):
    start_time = time.time()
    start_cpu_time = get_cpu_usage(pid_to_monitor)

    time.sleep(monitoring_interval)

    end_time = time.time()
    end_cpu_time = get_cpu_usage(pid_to_monitor)

    cpu_usage_percentage = ((end_cpu_time - start_cpu_time) / (end_time - start_time))

    print("CPU avg: {:.2f}%".format(cpu_usage_percentage))
    return cpu_usage_percentage

if __name__ == "__main__":
    pid_to_monitor = run_command()
    print("top -p {},{},{},{},{}".format(pid_to_monitor['s1'],pid_to_monitor['s2'],pid_to_monitor['s3'],pid_to_monitor['s4'],pid_to_monitor['s5']))
    cpu_list =[]
    flag = [False,0]
    while(1):
        cpu=main(pid_to_monitor['s3'])
        if cpu>20:
            flag[0]=True
        if flag[0]:
            if flag[1] > 10:
                break
            cpu_list.append('{:.2f}%'.format(cpu))
            if cpu <1:
                flag[1]+=1
    dataFrame = pd.DataFrame(cpu_list, columns=['cpu'])
    dataFrame.to_csv('./s3.csv', index=False, header=False)
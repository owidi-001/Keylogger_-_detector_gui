import datetime
import psutil

# cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks,
# network, sensors) in Python
pid = psutil.pids()

all_process = []

print('Dectection Underway!')

# Checks for processes running
for i in pid:
    # Returns featurers of the current running processes
    process = psutil.Process(i)
    cmd = process.cmdline()

    if cmd:
        prop = {
            'pid': process.pid,
            'user': process.username(),
            'cmdline': {
                'cmd': cmd[0],
                'pname': cmd[-1]
            },
            'ptype': process.name(),
            'status': process.status(),
            'time': datetime.datetime.fromtimestamp(process.create_time()).strftime('%Y-%m-%d %H:%M:%S')
        }

    else:
        prop = {
            'pid': process.pid,
            'user': process.username(),
            'ptype': process.name(),
            'status': process.status(),
            'time': datetime.datetime.fromtimestamp(process.create_time()).strftime('%Y-%m-%d %H:%M:%S')
        }
    all_process.append(prop)

for i in all_process:
    key = 'cmdline'
    if key in i:
        # The key logger name when found, the program will kill the program
        if i['cmdline']['pname'] == 'cute_cats.exe':
            print(f"Found keylogger: '{i['cmdline']['pname']}' at -> {i['pid']}")
            psutil.Process(i['pid']).kill()
            # Confirms the process termination
            print(f"Process {i['pid']} was killed!")

print('Dectection Done!')

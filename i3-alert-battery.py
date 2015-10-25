#!/usr/bin/env python
# coding: utf-8
from time import sleep
import subprocess
import gc

batery = '/proc/acpi/battery/BAT0/'
state = batery + 'state'
info = batery + 'info'
alerts = range(1, 16)
alerts += range(20, 36, 5)
alerted = []
process = None


def to_dict(f, obj={}):
    for line in f.readlines():
        key, data = line.split(':')
        key = key.replace(' ', '_')
        obj[key] = data.strip().split(' ')[0]

        if obj[key].isdigit():
            obj[key] = int(obj[key])
    return obj


def kill_process():
    global process
    if process:
        process.kill()
        process = None
        gc.collect()


def check_loop():
    global process
    try:
        while True:
            with open(state) as state_file:
                obj = to_dict(state_file)

            with open(info) as info_file:
                obj = to_dict(info_file, obj)

            if obj['charging_state'] == 'charging':
                while alerted:
                    alerted.pop()
                kill_process()
            else:
                total = (
                    obj['remaining_capacity'] / float(obj['design_capacity'])
                ) * 100

                for i in alerts:
                    if i > total and i not in alerted:
                        alerted.append(i)
                        for j in alerts:
                            if j > i:
                                alerted.append(j)

                        kill_process()
                        process = subprocess.Popen([
                            'i3-nagbar',
                            '-m',
                            '"A bateria está em {}%"'.format(int(total))
                        ])
                        break

            sleep(1)
    except KeyboardInterrupt:
        print('')
        print('Bye bye')


if __name__ == '__main__':
    check_loop()

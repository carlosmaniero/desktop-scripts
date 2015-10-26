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
process_charging = None


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


def kill_process_charging():
    global process_charging
    if process_charging:
        process_charging.kill()
        process_charging = None
        gc.collect()


def check_loop():
    global process
    global process_charging

    first = True
    is_charging = True

    try:
        while True:
            with open(state) as state_file:
                obj = to_dict(state_file)

            with open(info) as info_file:
                obj = to_dict(info_file, obj)

            if first:
                first = False
                is_charging = obj['charging_state'] in ('charging', 'charged')

            if is_charging and obj['charging_state'] not in ('charging', 'charged'):
                process_charging = subprocess.Popen([
                    'i3-nagbar',
                    '-m',
                    'Carregador desconectado',
                    '-t',
                    'warning'
                ])

            if obj['charging_state'] in ('charging', 'charged'):
                while alerted:
                    alerted.pop()
                kill_process()
                kill_process_charging()
                is_charging = True
            else:
                is_charging = False
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

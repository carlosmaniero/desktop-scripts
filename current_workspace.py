import i3ipc
i3 = i3ipc.Connection()


def format_workspace(workspace):
    num, name = workspace['name'].split(' ')
    ret = '${{font Ubuntu:size=8}}{}   {}$font'.format(num, name)
    if workspace['focused']:
        ret = '${color red}' + ret + '$color'
    if workspace['urgent']:
        ret = '${color #ff3333}' + ret + '$color'
    return ret

data = []
for workspace in i3.get_workspaces():
    data.append(format_workspace(workspace))


print('  '.join(data))

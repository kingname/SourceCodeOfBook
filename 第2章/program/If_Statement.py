state = 'start'
if state == 'start':
    code = 1
elif state == 'running':
    code = 2
elif state == 'offline':
    code = 3
elif state == 'unknown':
    code = 4
else:
    code = 5

state_dict = {'start': 1, 'running': 2, 'offline': 3, 'unknown': 4}
code = state_dict.get(state, 5)
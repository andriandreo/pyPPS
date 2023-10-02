
def set_voltage(channel, value):

    command = f'VSET{channel}:{value:.2f}\n'
    return command.encode('utf-8')

def set_maxcurrent(channel, value):

    command = f'ISET{channel}:{value:.2f}\n'
    return command.encode('utf-8')

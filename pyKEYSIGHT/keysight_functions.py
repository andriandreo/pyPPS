
def set_voltage(channel, V, Imax):

    command = f'APPL {channel}, {V:.3f}, {Imax:.3f}'
    return command

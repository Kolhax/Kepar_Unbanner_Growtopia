import psutil

def get_interfaces():
    data = psutil.net_if_stats()
    interfaces = []
    for key, value in data.items():
        interfaces.append(key)
    return interfaces


import ipaddress

def expand_targets(target):
    """
    Supporta:
    - 192.168.1.16
    - 192.168.1.1/24
    """
    if "/" in target:
        net = ipaddress.ip_network(target, strict=False)
        return [str(ip) for ip in net.hosts()]
    else:
        return [target]


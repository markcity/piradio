#pip install netifaces
import netifaces

def get_local_ip():
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        addresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addresses:
            for address in addresses[netifaces.AF_INET]:
                ip = address['addr']
                if ip != '127.0.0.1':
                    return ip
    return '127.0.0.1'

print(f"Local IP address: {get_local_ip()}")


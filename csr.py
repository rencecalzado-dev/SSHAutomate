import netmiko
from netmiko import ConnectHandler
import json
with open('csr2.json', 'r') as jfile:
    pfile = json.load(jfile)
    #print(pfile)


### Device Info
csr = {
    'device_type': 'cisco_ios',
    'host': '192.168.102.11',
    'port': '22',
    'username': 'admin',
    'password':'pass',
    'secret': 'pass'
}



### Config
config = [
    f'interface {pfile["type"]} {pfile["id"]}',
    f'ip add {pfile["ipv4"]["ip"]} {pfile["ipv4"]["mask"]}',
    f'description {pfile["ipv4"]["desc"]}',
    'end'
]


# print(config)

cli = ConnectHandler(**csr)
cli.enable()
cli.send_config_set(config)
siib = cli.send_command('show ip int br')
cli.disconnect()
print(siib)


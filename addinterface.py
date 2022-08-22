import json
import subprocess
from pprint import pp

test = subprocess.Popen(["ansible-playbook", "addinterface.yaml", "-i", "hosts.ini", "-vvv"], stdout=subprocess.PIPE)
output = test.communicate()[0]

print(type(output))
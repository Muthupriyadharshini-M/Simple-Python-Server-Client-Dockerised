import requests
import json

data = {}
data['Name'] = 'John Statham'
data['Designation'] = 'Associate Developer'
data['Status'] = 'inactive'
jdata = json.dumps(data)
send = requests.post(url='http://127.0.0.1:8080',json=jdata)
print((send.headers))

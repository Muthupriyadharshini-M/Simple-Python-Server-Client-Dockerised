import requests
import json


url = "http://" + "nginxserver" + ":80"

#answer = int(input("Enter 1 for a GET request and 2 for a POST request"))

#id = int(input("Enter the ID of the employee whose data you want to see"))
params = {"id":5}
get_data = requests.get(url=url,params=params)
print((get_data.headers)
print(get_data.text)


data = {}
data['Name'] = "Hawking"
data['Designation'] = "Site Head"
data['Status'] = "active"
jdata = json.dumps(data)
send = requests.post(url=url,json=jdata)
print((send.headers))

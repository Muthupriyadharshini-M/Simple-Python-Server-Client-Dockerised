import requests


id = int(input("Enter the ID of the employee whose data you want to see"))

params = {"id":id}
get_data = requests.get(url='http://127.0.0.1:8080',params=params)
print((get_data.headers))
print(get_data.text)

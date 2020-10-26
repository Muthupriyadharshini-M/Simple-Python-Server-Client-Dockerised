import http.server
import http.client
import socketserver
import json

file1 = open("data.json","r")
dict = json.load(file1)
file1.close()
#max_emp = len(dict)



class MyHTTPHandler(http.server.SimpleHTTPRequestHandler,http.client.HTTPResponse): #HTTP Handler inherits from server as well as client

    def do_GET(self):
        self.send_response(200)
        self.send_header('ContentType', 'application/json')
        self.end_headers()
        print(str(self.command))
        emp_id = self.path[5:] #Getting the ID of the Employee
        dict1 = {}
        dict1 = dict[emp_id]
        self.wfile.write(json.dumps(dict1).encode()) #Sending to client

    def do_POST(self):
        print(str(self.command))
        data = self.rfile.read(int(self.getheader('Content-Length'))) #Length should be mentioned or else it will read forever
        string = data.decode('utf-8')
        a_string = string.replace("\\","").replace("\"","").replace(":",",").replace("{","").replace("}","")
        list_dict = a_string.strip().split(",")

        j = 0
        for i in list_dict:
            list_dict[j] = i.strip()
            j = j+1

        k = 0
        dict1 = {}
        while( k <= len(list_dict)-1):
            dict1[list_dict[k]] = list_dict[k+1]
            k = k+2

        max_emp = len(dict) + 1
        dict[str(max_emp)] = dict1

        file2 = open("data.json","w")
        jdict1 = json.dumps(dict)
        file2.write(jdict1)
        file2.close()

        self.send_response(200)
        self.end_headers()

Handler = MyHTTPHandler
httpd = socketserver.TCPServer(("", 8080), Handler)
print("Serving at port in the machine", 8080)
httpd.serve_forever()

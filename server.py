from http.server import BaseHTTPRequestHandler,HTTPServer
import json
port=1111
from adder import add_numbers, multiply_numbers
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        mypath=self.path
        parts=[]
        if mypath.startswith("/add"):
            parts = mypath.split("/")
            firstnum=int(parts[2])
            secondnum=int(parts[3])
            result=add_numbers(firstnum,secondnum)
        elif mypath.startswith("/multiply"):
            parts = mypath.split("/")
            firstnum=int(parts[2])
            secondnum=int(parts[3])
            thirdnum=int(parts[4])
            result=multiply_numbers(firstnum,secondnum,thirdnum) 

        response = json.dumps({"message":"billybigbollocks","requestpath":mypath,"pathParts":parts,"result":result})
        self.send_json_response(response)
    def send_json_response(self,response):
        self.send_response(200)
        self.send_header("Content-type","text/json")
        self.end_headers()
        self.wfile.write(bytes(str(response),"utf-8"))
    
if __name__=='__main__':
    print('it works')
    webserver=HTTPServer(("localhost",port),MyServer)
    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        pass
    webserver.server_close()


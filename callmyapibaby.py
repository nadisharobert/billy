import requests
import json

def multiply_using_api(firstnum,secondnum,thirdnum):
    url="http://localhost:1111/multiply/"+str(firstnum)+"/"+str(secondnum)+"/"+str(thirdnum)
    Response=requests.get(url)
    responsejson = json.loads(Response.text)
    result = int(responsejson.get("result"))
    return result

firstnum=2
secondnum=76
thirdnum=99


apiresult = multiply_using_api(firstnum,secondnum,thirdnum)
from adder import multiply_numbers
localresult = multiply_numbers(firstnum,secondnum,thirdnum)
print(apiresult)
print(localresult)
pass
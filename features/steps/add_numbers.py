from behave import *
import json
import requests
@given('two numbers')
def step1(context): 
    context.num1=27
    context.num2=33
@when('I call the adder API providing the two numbers')
def step2(context):
    url="http://localhost:1111/add/"+str(context.num1)+"/"+str(context.num2)
    Response=requests.get(url)
    responsejson = json.loads(Response.text)
    context.result = int(responsejson.get("result"))    
@then('the response will contain the addition of those two numbers')
def step3(context):
    assert context.result==context.num1+context.num2


import requests
import json
import  jsonpath
def test_get_studendata():

    url_student ="http://thetestingworldapi.com/api/studentsDetails"
    reponse = requests.get(url_student)
    print(reponse.content)

def test_post_student():

    f = open("C:\\python-t\\API-testing\\utilities\\student_tech.json",'r')
    json_data = json.loads(f.read())
    post_url = 'http://thetestingworldapi.com/api/studentsDetails'
    post_reponse =requests.post(post_url,json_data)
    print(post_reponse)
    id = jsonpath.jsonpath(post_reponse.json(),'id')


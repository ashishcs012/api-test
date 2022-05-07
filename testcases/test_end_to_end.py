import json
import requests
import jsonpath


def test_add_new_data():

    add_url = 'http://thetestingworldapi.com/api/studentsDetails'
    f = open("C:\\python-t\\API-testing\\utilities\\studendata.json",'r')
    json_data = json.loads(f.read())
    reponse_add = requests.post(add_url, json_data)
    print(reponse_add.content)
    id = jsonpath.jsonpath(reponse_add.json(), 'id')
    print(id[0])

    tech_api_url = 'http://thetestingworldapi.com/api/technicalskills'
    f = open('C:\python-t\\API-testing\\utilities\\student_tech.json','r')
    request = json.loads(f.read())
    request['id'] = int(id[0])
    request["st_id"] = id[0]
    response = requests.post(tech_api_url, request)
    print(response.text)

    address_add_url = 'http://thetestingworldapi.com/api/addresses/'
    f = open('C:\\python-t\\API-testing\\utilities\\stuadd.json', 'r')
    request_json = json.loads(f.read())
    request_json["stId"] = id[0]
    response = requests.post(address_add_url,request_json)
    print(response.text)

    final_details = 'http://thetestingworldapi.com/api/studentsDetails/'+str(id[0])
    response = requests.get(final_details)
    print(response.text)

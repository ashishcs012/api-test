import requests
import json
import jsonpath


def test_st_add_new():
    global id
    ADD_url = 'http://thetestingworldapi.com/api/studentsDetails'
    f = open("C:\\python-t\\API-testing\\utilities\\studendata.json", 'r')

    request_json = json.loads(f.read())
    reponse = requests.post(ADD_url, request_json)

    id = jsonpath.jsonpath(reponse.json(), 'id')
    print(id[0])


def test_st_info():
    final_details = 'http://thetestingworldapi.com/api/studentsDetails/' + str(id[0])
    response = requests.get(final_details)
    print(response.text)

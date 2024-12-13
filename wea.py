import http.client
import json
import pprint 

conn = http.client.HTTPSConnection("weatherapi-com.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "b9eb41cb33msh38c07a72867da53p1f2339jsn89f17c618d75",
    'x-rapidapi-host': "weatherapi-com.p.rapidapi.com"
}

conn.request("GET", "/current.json?q=Boston", headers=headers)

res = conn.getresponse()
data = res.read()
json_data = data.decode("utf-8")

def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None


pp_json(json_data)

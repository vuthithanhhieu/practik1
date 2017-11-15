import requests
import json
js={'content-type':'application/json'}
url='https://cit-home1.herokuapp.com/api/rs_homework_1'
result = json.dumps({'user': 35,'1':{"movie 2":2.39,"movie 11":1.88,"movie 15":4.39,"movie 17":3.19,"movie 19":3.7,"movie 20":3.39,"movie 28":1.41},'2':{"movie 15":4.35}})
rs = requests.post(url, data = result, headers=js)
print (rs.json())


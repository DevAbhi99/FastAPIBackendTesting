import pytest
import requests


base_url='http://127.0.0.1:8000'

def testGetMethod():
    response=requests.get(f"{base_url}/getData")

    body=response.json()

    assert response.status_code==200

    assert body[0]['id']==1
    assert body[0]['name']=='Subhayan'
    assert body[0]['age']==21
    assert body[0]['priority']==1

def testPostMethod():
    payload={'id':2, 'name':'karan', 'age':23, 'priority':2 }
    response1=requests.post(f"{base_url}/sendData", json=payload)
    body1=response1.json()
    assert response1.status_code==200
    assert body1['message']=="Successfully inserted the data"

    response2=requests.get(f"{base_url}/getData")
    body2=response2.json()
    assert body2[1]['id']==2
    assert body2[1]['name']=='karan'
    assert body2[1]['age']==23
    assert body2[1]['priority']==2


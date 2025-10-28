from locust import HttpUser, tag, task, between

class User(HttpUser):
    wait_time=between(1,3)
    host='http://127.0.0.1:8000'

    @task(1)
    def testGetMethod(self):
        self.client.get('/getData')

    @task(3)
    def testPostMethod(self):
        payload={'id':2, 'name':'karan', 'age':23, 'priority':2 }
        self.client.post('/sendData', json=payload)


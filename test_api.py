import unittest
import requests
class TestApi(unittest.TestCase):
    URL="http://127.0.0.1:5000/api"
    data={"name":"testing",
    "descripton":"testing post"}

    def test_1_get_all(self):
        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 1)
        print ("Test one is completed")

    def test_2_post(self):
        resp = requests.post(self.URL, json=self.data)
        self.assertEqual(resp.status_code, 200)
       
        print ("Test two is completed")


    def test_update(self):
         resp = requests.put(self.URL)
         respGet = requests.get(self.URL)
         self.assertEqual(respGet.status_code, 200)   

        

    if __name__ == '__main__':
         unittest.main()
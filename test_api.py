from unicodedata import name
import unittest
import requests
class TestApi(unittest.TestCase):
    URL="http://127.0.0.1:5000/api"
    data={"name":"testing",
    "descripton":"testing post"}

    def test_1_get_all(self):
        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code, 200)
        
        print ("Test one is completed")

    def test_get_one(self):
        resp = requests.get('http://127.0.0.1:5000/api/Riyad')
        self.assertEqual(resp.status_code, 200)
        
        print ("Test is completed")

    def test_2_post(self):
        resp = requests.post(self.URL, json={"name":"Maya","age":"16","birthday":"12/09/2006"})
        self.assertEqual(resp.status_code, 200)
       
        print ("Test two is completed")


    def test_update(self):
         resp = requests.put('http://127.0.0.1:5000/api/Alix',json={"name":"Riyad","age":"17","birthday":"14/09/1997"})
         respGet = requests.get(self.URL)
         self.assertEqual(respGet.status_code, 200)   
         print("good")

        

    if __name__ == '__main__':
         unittest.main()
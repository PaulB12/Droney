import requests
import time
from datetime import datetime
class requestManage:
    def create_new_session(self):
        initalised = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("Initilizating a new request session @ "+initalised)
        self.sess = requests.Session()
        self.sess.headers.update ({
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
            "Referrer" : "http://wwww.google.com"
        })
    
        print("OK!\n\n\n\n")

    def get_request(self, url):
      url = 'http://'+url
      response = self.sess.get(url)
      if response.status_code == 200:
          return(response)
      elif response.status_code == 502:
        print("ERROR! 502 error occured! Server down?")
        return(response)
      else:
        print("Unknown error occurred!")

    def post_request(self, url, payload):
      url = 'http://'+url
      response = self.sess.get(url, payload)
      if response.status_code == 200:
        return(response)
      elif response.status_code == 502:
        print("ERROR! 502 has occured! Server down?")
      else:
        print("Unknown error occured!")

request = requestManage()
httpStarter = request.create_new_session()
#print(request.get_request('www.google.com'))

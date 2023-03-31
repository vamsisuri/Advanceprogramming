import requests
res=requests.get("http://www.google.com/in")
print(res.status_code)
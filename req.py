import requests
from requests.auth import HTTPBasicAuth
  
_url = "http://saas.derbysapp.com/user-remarks/?rdate=2022-09-18&venue=ST&raceno=1&uid=1&role=admin"
_username = "pub_0aa31cc8f20ca6ec1ec9d8ec78cd3808"
_pwd = "pri_aa6792647ccaa40e89217e8119abac82"
response = requests.get(_url,auth = HTTPBasicAuth(_username, _pwd))
  
# print request object
print(response.text)
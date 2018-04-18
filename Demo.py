import requests
url="http://sr-demo-env.us-west-1.elasticbeanstalk.com/hello"
response = requests.get(url)
print(response.status_code)

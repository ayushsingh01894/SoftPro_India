import requests

response = requests.get("https://api.github.com/")  #for faching data 
data = response.json() #convert data into json formet key value formats

response.raise_for_status()
print("Status Code :", response.status_code)
#print(data)
print(data["current_user_url"])


#Post - call 
import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "My First Post",
    "body": "Hello World",
    "userId": 1
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print(response.json())

response = requests.get("https://api.github.com/")
print(response.json())

response = requests.post(url, json=data)
print(response.json())

#Post - call

payload = {"prompt":"Hello", "max_tokens":50,"temp":.2}
headers = {"Authorization":"Bearer Fake-key"} #where api key will 
 
post = requests.post(
    "https://httpbin.org/post",
    json=payload,
    headers=headers,
    timeout=10
)

post.raise_for_status()

encoded_data = post.json()
print(encoded_data)
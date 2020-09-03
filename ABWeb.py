import requests

url = "http://172.18.58.238"
r = requests.get(url)
print(r.text)
print("Status code:")
print("\t *", r.status_code)
h = requests.head(url)
print("Header:")
print("**********")
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")
headers = {
    "User-Agent" : "Mobile"


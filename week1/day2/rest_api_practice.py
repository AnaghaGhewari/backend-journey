import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
print("Status Code:",response.status_code)
data = response.json()

print("\n First User:\n")
print("Name:",data[0]["name"])
print("Email:",data[0]["email"])
print("City:",data[0]["address"]["city"])

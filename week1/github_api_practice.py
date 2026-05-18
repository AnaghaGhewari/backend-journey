import requests
response = requests.get('https://api.github.com/users/AnaghaGhewari')
print("Status Code:", response.status_code)
print("Responce Headers:", dict(response.headers))

data = response.json()
print("GitHub User Information:")
print("----------------")

print("Followers:", data['followers'])
print("Public Repositories:", data['public_repos'])
print("Bio:", data['bio']) 
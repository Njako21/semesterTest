import requests

url = 'http://localhost:5000/api/brew'
body = {'set_batch_id': '100',
        'set_recipe': '1',
        'set_quantity': '150',
        'set_speed': '300',}

response = requests.post(url, json=body)

print(response.status_code)
print(response.text)
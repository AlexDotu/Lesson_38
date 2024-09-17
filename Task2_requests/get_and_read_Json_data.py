import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)


def get_and_read_json_file():
    if response.status_code == 200:
        users = response.json()
        try:
            with open('users.json', 'w') as file:
                json.dump(users, file, indent=4)
        except FileNotFoundError:
            print(f"Error: file {file} not found !")
        except json.JSONDecoder:
            print(f"Error: file {file} is not a valid JSON")
    else:
        print("Error while requesting data: ", response.status_code)
    return

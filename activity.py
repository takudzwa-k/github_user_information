import requests #lets python make http requests
import json

#user input
username = input("Please enter your github username: ")

#Requesting API
url = f"https://api.github.com/users/{username}" #inserting username directly into path

response = requests.get(url)

if response.status_code == 200: #checks if response suceeded, 200 means okay
    data = response.json() #parsing data into json file

    filename = f"{username}_github_data.json" #creating a filename based on username

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Data saved to {filename}")
else:
    print(f"Error: User not found or API issue (status code {response.status_code})")
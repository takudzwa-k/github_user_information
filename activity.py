import requests #lets python make http requests
import json
import os #lets python interact with the operating system

#user input
username = input("Please enter your github username: ")

#Requesting API
url = f"https://api.github.com/users/{username}" #inserting username directly into path

response = requests.get(url)

#Checking if the response was successful
if response.status_code == 200: #checks if response suceeded, 200 means okay
    data = response.json() #parsing data into json file

    #Displaying user information in terminal
    print("\n--- GitHub User Info ---")
    print(f"Username: {data.get('login')}") #Pulling field from data using .get()
    print(f"Name: {data.get('name')}")
    print(f"Bio: {data.get('bio')}")
    print(f"Company: {data.get('company')}")
    print(f"Location: {data.get('location')}")
    print(f"Public Repos: {data.get('public_repos')}")
    print(f"Followers: {data.get('followers')}")
    print(f"Following: {data.get('following')}")
    print(f"Profile URL: {data.get('html_url')}")
    print("-------------------------\n")

    #Saving user info to JSON file
    filename = "activity.json"

    if os.path.exists(filename) and os.path.getsize(filename) > 0: 
        with open(filename, "r") as f:
            all_data = json.load(f)
    else:
        all_data = []

    all_data = [entry for entry in all_data if entry.get("login") != username] #List comprehension

    all_data.append(data)

    with open(filename, "w") as f:
        json.dump(all_data, f, indent=4)

    print(f"Data for {username }saved to {filename}")
else:
    print(f"Error: User not found or API issue (status code {response.status_code})")
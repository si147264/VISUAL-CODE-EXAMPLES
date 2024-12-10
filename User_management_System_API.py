import requests

base_url = "https://jsonplaceholder.typicode.com/users"
print("User Management System")
print("\n1. List User List")
print("2. Add a New User into User List")
print("3. Update User in the List")
print("4. Delete a User from the List")

option = int(input("Opt for an option: "))

if option == 1:  
    response = requests.get(base_url)
    if response.status_code == 200:
        users = response.json()
        for user in users:
            print("ID :", user["id"])
            print("Name:", user["name"])
            print("Email:", user["email"])
            print("Address:", user["address"]["street"])
            print("User list is here")
            
    

elif option == 2:  
    name = input("Tell me the name to add: ")
    email = input("Tell me the email address: ")
    response = requests.post(base_url, json={"name": name, "email": email})
    print(response.json())
    print(f"New user,{name} is added into list")
 

elif option == 3:  
    id = int(input("Choose an ID to update: "))
    name = input("Tell me the new name: ")
    email = input("Tell me the new email address: ")
    response = requests.put(f"{base_url}/{id}", json={"name": name, "email": email})
    print(response.json())
    print(f"Info of {name} is updated")
   
elif option==4:
    id=int(input("choose an ID to delete"))
    response=requests.delete(f"{base_url}/{id}")
    print(response.json())
    print(f"{id} is deleted from user list")

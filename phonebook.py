import json
import os

if os.path.exists("contacts.json"):
    with open("contacts.json","r") as file:
        contacts = json.load(file)
else:
    contacts={}
    
def saved_contacts():
    with open("contacts.json","w") as file:
        json.dump(contacts,file)
while True:
    menu=(input("_____________\n1.add\n2.find\n3.edit\n4.delet\n5.show all contacts\n6.exite\n_____________\n"))

    if menu == "1":
        name=input("enter contacts name: ")
        number=int(input("enter contacts number: "))        
        
        contacts[name]=number
        saved_contacts()
        print()
        print("sucsesfully add")
            
    elif menu=="2":
        name=input("enter contacts name: ")
        if name in contacts:
            print(f"{name}:{contacts[name]}")
        else:
            print("not found")
    elif menu=="3":
        name=input("enter contacts name that you want to edit: ")
        new_number=int(input("enter new number: "))
        if name in contacts:
            contacts[name]=new_number
            saved_contacts()
        else:
            print(f"didnt find {name} in contacts")           
        
    elif menu=="4":
        name=input("enter contacts name: ")
        if name in contacts:
            contacts.pop(name)
            saved_contacts()
    elif menu=="5":
        for key,value in contacts.items():
            print(key , ":", value)
    elif menu=="6":
        break
    else:
        print("invalid choice")


    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
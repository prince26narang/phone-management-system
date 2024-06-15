favourite_contact = set()
list_contacts=[]
contact_numbers={}

def add_contact(name,num,mail):
    details=(name,num,email)
    list_contacts.append(details)
    contact_numbers[name]={"Phone no":num,"email":email}
    print("added successfully")
        
        
def search_contact(name):
    if name in contact_numbers:
        print("Name:",name)
        print("Phone no. :",contact_numbers[name]["Phone no"])
        print("Email:",contact_numbers[name]["email"])
    else:
        print("No such contact exist.")
        
def list_contact():
    for contact in list_contacts:
        print(f"{list_contacts.index(contact)+1} Name:{contact[0]}, Phone no.:{contact[1]}, Email:{contact[2]}")
        
def favourite_contact(name):
    for i in list_contacts:
        if i[1] == name:
            favourite_contact.add(i)
    
def favourite_list():
    print(favourite_contact)
#     for i in favourite_contact:
#         print(i)


    

while True:
    print("\n\n")
    print("Contact Management System")
    print("1. To add contact")
    print("2. To search contact")
    print("3. List contact")
    print("4. Add to favourite contacts")
    print("5. List favourite contacts")
    print("6. To quit")
    print()
    choice=int(input("Enter your choice:"))
    
    if choice == 1:
        name=input("Enter contact name:")
        contact=int(input("Enter contact no."))
        email=input("Enter email id:")
        add_contact(name,contact,email)
        
    elif choice == 2:
        name=input("Enter the contact name you want to search:")
        search_contact(name)
        
    elif choice == 3:
        list_contact()
        
    elif choice == 4:
        name=input("Enter the name:")
        favourite_contact(name)
        print("added to favourite")
        
    elif choice == 5:
        favourite_list()
        
    elif choice == 6:
        print("Good bye!")
        break
    
    else:
        print("Wrong Number entered")
    
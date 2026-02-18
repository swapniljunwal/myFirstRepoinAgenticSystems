contact_num = {
    "Ravi": "9876543210",
    "Anita": "9123456780",
    "Ankit" : "8475169346"
}

user =  input("Enter person name : ")

if user in contact_num :
    print(contact_num[user])

else :
    print("Person not found")
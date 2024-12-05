from task_manager import*

while True:

    print("\n Welcome To Your Contact Book Management System\n")
    print(" 1. Add Contact ")
    print(" 2. View Contact ")
    print(" 3. Remove Contact ")
    print(" 4. Search Contact ")
    print(" 5. Update Contact ")
    print(" 0. Exit ")


    choice = int(input(" Enter Any Number if you want : "))
    if choice == 1:
        name=input(" Enter Name : ")
        phone=int(input(" Enter Phone Number : "))
        email=input(" Enter Email Address : ")
        address=input(" Enter Address : ")
        add_contact(name,phone,email,address)
        print(" Contact Added Successfully")

    elif choice == 2:
        view_contacts()

    elif choice == 3:
        view_contacts()
        index=int(input("Enter the index of the contact you want to remove : "))
        remove_contact(index)
        print("Contact Removed Successfully")

    elif choice == 4:
        query =input("Enter the search query : ")
        search_contact(query)

    elif choice == 5:
        view_contacts()
        index=int(input("Enter the index of the contact you want to update"))-1
        update_contact(index)
        print("Update Successfully")

    elif choice == 0:
        print(" Thanks for Using Contact Book MAnagement System")
    
    else:
        print(" You Enter invaild Number")
        break
print(" Thanks for Using Contact Book MAnagement System")

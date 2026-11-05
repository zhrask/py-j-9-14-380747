




def delete_contact(Contacts:list, delete:int)->None:
    if contacts:
        if 1 <= delete <= len(contacts):
            print(contacts[delete - 1])
            check_del = int(input("you sure you want to delete this contact?(1.yes/2.no):"))
            if check_del != 1 and check_del != 2:
                print("try again.")
                return delete_contact
            elif check_del == 1:
                contacts.pop(delete - 1)
                print("contact deleted.")
            elif check_del == 2:
                print("delete canceled.")
        else:
            print("shomare radif na mojud.")
    else:
        print("no contacts yet.")
        break
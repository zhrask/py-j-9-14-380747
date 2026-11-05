




def add_contact(contacts:list, name_contact:str, num_contact:str)->list:
    if name_contact.strip() == "":
        print("choose a name.")
    for i in range(len(contacts)):
        if contacts[i][0] == name_contact:
            print("there is already a contact with that name.")
            return contacts
    if len(num_contact) != 11:
        print("wrong number.")
        return contacts
    for i in range(len(contacts)):
        if contacts[i][1] == num_contact:
            print("this number is already in your contacts.")
            return contacts
    else:
        contacts.append([name_contact, num_contact])
        print("contact added.")







from add import *
from show import *
from search import *
from edit import *
from delete import *
from count import *

contacts = []
while True:
    contacts_menu = input("1.Add Contact 2.Show All Contacts 3.Search Contact 4.Edit Contact 5.Delete Contact 6.Count Contacts 7.Exit")
    while True:
        match contacts_menu:
            case "1":
                name = input("name:")
                number = input("number:")
                add_contact(contacts, name, number)
                break
            case "2":
                show_contacts(contacts)
                break
            case "3":
                search_contact(contacts)
                break
            case "4":
                shomare_radif_edit = int(input("whitch contact you wanna edite:"))
                edit_contact(contacts, shomare_radif_edit)
                break
            case "5":
                shomare_radif_del = int(input("whitch contact you wanna delete:"))
                delete_contact(contacts, shomare_radif_del)
                break
            case "6":
                count_contact(contacts)
                break
            case "7":
                print("byeeee!")
                break
                            
                        



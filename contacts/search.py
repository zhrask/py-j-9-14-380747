






def search_contact(contacts:list)->list:
    search_menu = input("1.search by name 2.search by number")
    match search_menu:
        case "1":
            name_search = input("name:")
            if contacts:
                for i in range(len(contacts)):
                    if contacts[i][0] == name_search:
                        print("name has been found.")
                        print(contacts[i])
                        break
                else:
                    print("no contact found.")
            else:
                print("no contacts yet.")
        case "2":
            num_search = input("number:")
            if contacts:
                for i in range(len(contacts)):
                    if contacts[i][1] == num_search:
                        print("number has been found.")
                        print(contacts[i])
                        break
                else:
                    print("no contact found.")
            else:
                print("no contacts yet.")
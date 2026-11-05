



def edit_contact(contacts:list,edit:int)->list:
    edit_menu = input("1.edit name 2.edit number 3.edite name & number")
    match edit_menu:
        case "1":
            edited_name = input("new name:")
            if contacts:
                if 1 <= edit <= len(contacts):
                    if edited_name.strip() == "":
                            print("invalid name.")
                    else:
                        for i in range(len(contacts)):
                            if i != edit - 1 and edited_name == contacts[i][0]:
                                print("name is alredy used.")
                                break
                        else:
                            contacts[edit - 1][0] = edited_name
                            print(contacts[edit - 1])
                else:
                    print("number not found.")
            else:
                print("no contacts yet.")
        case "2":
            edited_number = input("new number:")
            if contacts:
                if 1 <= edit <= len(contacts):
                    if len(edited_number) != 11 or edited_number.isdigit() != True:
                        print("wrong number.")
                    else:
                        for i in range(len(contacts)):
                            if i != edit - 1 and edited_number == contacts[i][1]:
                                print("number is alredy used.")
                                break
                        else:
                            contacts[edit - 1][1] = edited_number
                            print(contacts[edit - 1])
                else:
                    print("number not found.")
            else:
                print("no contacts yet.")
        case "3":
            edited_name = input("new name:")
            edited_number = input("new number:")
            if contacts:
                if 1 <= edit <= len(contacts):
                    if len(edited_number) != 11 or edited_number.isdigit() != True:
                        print("wrong number.")
                    elif edited_name.strip() == "":
                            print("invalid name.")
                    else:
                        for i in range(len(contacts)):
                            if i != edit - 1 and edited_number == contacts[i][1]:
                                print("number is alredy used.")
                                break
                            if i != edit - 1 and edited_name == contacts[i][0]:
                                print("name is alredy used.")
                                break
                        else:
                            contacts[edit - 1][0] = edited_name
                            contacts[edit - 1][1] = edited_number
                            print(contacts[edit - 1])
                else:
                    print("number not found.")
            else:
                print("no contacts yet.")
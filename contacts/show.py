




def show_contacts(contacts:list)->list:
    if contacts:
        for i in range(len(contacts)):
            print(i + 1, ".", contacts[i][0], ":", contacts[i][1])
            print("---------------------")
    else:
        print("no contacts yet.")
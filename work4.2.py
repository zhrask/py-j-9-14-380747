







#tamrine yaddasht haye ruzne
notes = []
while True:
    notes_menu = input("1.make note 2.show notes 3.edit notes 4.delete notes 5.search in notes 6.exit")
    while True:
        match notes_menu:
            case "1":
                note = input("your note:")
                notes.append(note)
                print("note added.")
                for i in range(len(notes)):
                    print(i + 1, ".", notes[i])
                break
            case "2":
                if notes:
                    for i in range(len(notes)):
                        print(i + 1, ".", notes[i])
                else:
                    print("there are no notes.")
                break
            case "3":
                if notes:
                    edit = int(input("number of the note you wanna edit:"))
                    if 1 <= edit <= len(notes):
                        edited_note = input("your edited note:")
                        notes[edit - 1] = edited_note
                        for i in range(len(notes)):
                            print(i + 1, ".", notes[i])
                        break
                    else:
                        print("shomare note mojud nist.")
                        break
                else:
                    print("nonotes yet.")
                    break
            case "4":
                if notes: #ya begim if len(notes) > 0:
                    delete = int(input("number of the note you wanna delete:"))
                    if 1 <= delete <= len(notes):
                        notes.pop(delete - 1)
                        print("note deleted.")
                        for i in range(len(notes)):
                            print(i + 1, ".", notes[i])
                        break
                    else:
                        print("shomare note mojud nist.")
                        break
                else:
                    print("nonotes yet.")
                    break
            case "5":
                search = input("the word you looking for:")
                found = False
                for i in range(len(notes)):
                    if search in notes[i]:
                        print(i + 1, notes[i])
                        found = True
                if not found:
                    print("note morede nazar shoma yaft nshod.")
                    break
            case "6":
                break




def search_task(tasks:list, word:str)->list:
    if tasks:
        for i in range(len(tasks)):
            if word in tasks[i][0] or word in tasks[i][1]:
                print(tasks[i])
            else:
                print("no task with the word you looking for.")
    else:
        print("no tasks available.")






def pending_task(tasks:list)->list:
    if tasks:
        for i in range(len(tasks)):
            if tasks[i][2] == "pending":
                print(tasks[i])
                found = True
            if not found:
                print("no pending tasks.")
    else:
        print("no tasks yet.")
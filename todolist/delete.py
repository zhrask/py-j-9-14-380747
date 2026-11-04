





def delete_task(tasks:list, num:int)->list:
    if tasks:
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("task deleted.")
        else:
            print("tasks number unavailable.")
    else:
        print("no tasks available.")
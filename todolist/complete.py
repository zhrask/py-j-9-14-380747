




def complete_task(tasks:list, number_task:int)->list:
    if tasks:
        if 1 <= number_task <= len(tasks):
            tasks[number_task - 1][2] = "completed"
            print("your task has been completed.")
        else:
            print("invalide task.")
    else:
        print("no tasks yet.")





def show_task(tasks:list)->list:
    """show tasks:

    Args:
        tasks (list): tasks list

    Returns:
        list: tasks list
    """

    if tasks:
        for i in range(len(tasks)):
            print(i+1, ".", tasks[i][0], ":", tasks[i][1])
            print(tasks[i][2])
            print("--------------")
    else:
        print("no tasks yet.")




def add_task(tasks:list, title:str, task:str)-> list:
    """add task:

    Args:
        title (str): title
        task (str): description

    Returns:
        list: tasks list
    """
    if title.strip() == "" or task.strip() == "":
        print("empty task or title!")
    else:
        tasks.append([title, task, "pending"])
        print("task added.")


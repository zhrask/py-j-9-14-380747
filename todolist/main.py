








#to do list


from add import *
from show import *
from complete import *
from delete import *
from search import *
from pendingshow import *
tasks = []
while True:
    todo_menu = input("1.add new task 2.show all tasks 3.complete task 4.delete task 5.search task 6.show pending tasks 7.exit")
    while True:
        match todo_menu:
            case "1":
                task_title = input("your task title:")
                task_description = input("your task description:")
                add_task(tasks, task_title, task_description)
                break
            case "2":
                show_task(tasks)
                break
            case "3":
                num_task = int(input("task number you completed:"))
                complete_task(tasks, num_task)
                break
            case "4":
                if tasks:
                    num_delete = int(input("task number you wanna delete:"))
                    delete_task(tasks, num_delete)
                    break
            case "5":
                search = input("title or word you looking for:")
                search_task(tasks, search)
                break
            case "6":
                pending_task(tasks)
                break


                




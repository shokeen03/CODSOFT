
task_list=[]

def add_tasks():
    task=input("Enter your task: ")
    task_list.append(task)
    print("Task successfully updated. Your TO-DO list is now ready to go!")

def show_tasks():
    if len(task_list)==0:
        print("Your TO-DO list is currently empty!")
    else:
        print("The tasks in TO-DO list: ")
        for i, task in enumerate(task_list):
            print(f'{i+1}.{task}')

def delete_tasks():
    if len(task_list)==0:
        print("There are no tasks to delete!")
    else:
        print("Your current tasks: ")
        for i, task in enumerate(task_list):
            print(f'{i+1}.{task}')
        choose=int(input("Enter task no. you want to delete: "))  

        if 0 < choose <= len(task_list):
            del task_list[choose-1]
            print("Task successfully removed. Your TO-DO list is now updated!")
        else:
            print("Task no. is not in the list!")   

def main():
    while True:
        print("\n**********Welcome to TO-DO application**********")
        print("1. Add Task")
        print("2. View Task")
        print("3. Delete Task")
        print("4. Exit")

        option=int(input("Enter your option from above: "))
        if option==1:
            add_tasks()
        elif option==2:
            show_tasks()
        elif option==3:
            delete_tasks()
        elif option==4:
            print("Grateful to you for using TO-DO application!")
            break
        else:
            print("Option is invalid. Try again.")

if __name__ == "__main__":
    main()                

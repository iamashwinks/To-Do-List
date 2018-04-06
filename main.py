from to_do import TodoList

list=TodoList()

print(" -"*20, "\n Your Handy To Do List \n","- "*20)
while True:
    print("\n")
    print("1. Add Tasks /n 2. Mark as Done /n 3. View Tasks /n")
    num = int(input("Enter the index number what you want to do: "))
    print("\n")
    if num == 1:
        n = int(input("Entrer the no. of tasks: "))
        for i in range(n):
            task = input("Enter the task: ")
            list.add(task)
    elif num == 2:
        list.mark_as_done()
    elif num == 3:
        list.check_status()
    else:
        break

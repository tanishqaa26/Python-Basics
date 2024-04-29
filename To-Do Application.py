#!/usr/bin/env python
# coding: utf-8

#Description: Create a basic to-do list application where users can add tasks,
#mark them as complete, and remove them from the list


tasks=[]

def addTask():
  task=input("Add a new task: ")
  tasks.append(task)
  print(f"Added a new task: {task}")

def viewTask():
  if not tasks:
     print(f"No Task found")
  else:
    print("Current tasks")
    for index, task in enumerate(tasks):
      print(f"Task {index}. {task}")


def deleteTask():
  viewTask()
  try:
    taskToDelete= int(input("Choose a number of the task: "))
    if taskToDelete < len(tasks):
      tasks.pop(taskToDelete)
      print(f"Task {taskToDelete} has been removed")
    else:
      print(f"Task {taskToDelete} not found")

  except:
    print("Invalid Input")
  

def markTask():
  viewTask()
  taskMarked = input("Which task do you want to mark as resolved? ")
  try:
     markedIndex = tasks.index(taskMarked)
     print(f'{taskMarked} has been marked as resolved')
     tasks[markedIndex] = f'{taskMarked} (Resolved)'
  except ValueError:
     print('This task does not exist')

print("Welcome to the To-Do List App!")
print("-------------------------------")
while True:
  print("Please select one of the options")
  print("-------------------------------")
  print("1. Add a new task")
  print("2. View Tasks")
  print("3. Delete Tasks")
  print("4. Mark task as complete")
  print("5. Quit")
  print("-------------------------------")

  a= input("Enter your choice: ")
  if(a=="1"):
     addTask()

  elif(a=="2"):
      viewTask()

  elif(a=="3"):
       deleteTask()

  elif(a=="4"):
       markTask()

  elif(a=="5"):
       break

  else:
    print("Invalid input. Please try again")

print("Goodbye 👋")









import tkinter
from tkinter import *
root=Tk()
root.title("To do list")
root.geometry("400x650+400+1000")
root.resizable(False,False)
task_list=[]
def addTask () :
    task= task_entry.get()
    task_entry.delete(0,END)
    if task :
        with open("tasklist.txt",'a') as taskfile :
            taskfile.write(f"\n{task}")
            task_list.append(task)
            listbox.insert(END,task)
def deleteTask() :
    task= str(listbox.get(ANCHOR))
    if task in task_list :
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfie :
            for task in task_list :
                taskfie.write(task+"\n")
        listbox.delete(ANCHOR)


def openfile():
    try :
        global task_list
        with open("tasklist.txt","r") as taskfile :
            tasks = taskfile.readlines()
        for task in tasks :
            if task!='\n' :
                task_list.append(task)
                listbox.insert(END,task)
    except:
      file=open('tasklist.txt','w')
      file.close()

#icon
Image_icon=PhotoImage(file="GUI/trash.png")
root.iconphoto(False,Image_icon)
#bar
TopImage=PhotoImage(file="GUI/topbar.png")
Label(root,image=TopImage,bg="#000000")
Label(root,image=TopImage).pack()
noteimage=PhotoImage(file="GUI/note.png")
Label(root,image=noteimage,bg="#32405b").place(x=350,y=10)
heading=Label(root,text="Tasks to do",font="italic 20 bold",fg="white",bg="#FFC0CB")
heading.place(x=100,y=20)
#main
frame=Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)
task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
button=Button(frame,text="ADD ",font="arial 20 bold",width=6,bg="#00FF00",fg="#FFFFFF",command=addTask)
button.place(x=300,y=0)
#box
frame1=Frame(root,bd=3,width=700,height=280,bg="#FFC0CB")
frame1.pack(pady=(160,0))
listbox=Listbox(frame1,font=('arial',12),width=40,height=16,bg="#FFC0CB",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
#delete
Delete_icon=PhotoImage(file="GUI/trash.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13,)


root.mainloop()
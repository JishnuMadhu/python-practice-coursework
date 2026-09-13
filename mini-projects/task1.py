import sqlite3

conn = sqlite3.connect('mytask.db') #to establish a connection
cursor = conn.cursor()    #to interact with db


# cursor.execute('''CREATE TABLE IF NOT EXISTS students (name VARCHAR(20),roll INTEGER,address TEXT)''')


# cursor.execute('''CREATE TABLE IF NOT EXISTS employee (id INTEGER,name VARCHAR(20),email VARCHAR(20),salary INTEGER)''')


# cursor.execute('''
#                 INSERT INTO students(name,roll,address)
# #                 VALUES('mohan',34,'kochi')
#                ''')




# cursor.execute('''
#                 CREATE TABLE IF NOT EXISTS Tasks(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 task_name VARCHAR(20),
#                 task_des TEXT
#                )
#                ''')

# conn.close()

def addtask():
    conn = sqlite3.connect("mytask.db")
    cursor = conn.cursor()
    tname = input("enter task name: - ")
    tdes = input('enter task des: -')

    cursor.execute('''
                INSERT INTO Tasks(task_name,task_des)
                VALUES(?,?)
                ''',(tname,tdes))   #if there is only one parameter,use , after that, here there is two, so no problem
    conn.commit()


def viewtasks():
    conn = sqlite3.connect("mytask.db")
    cursor = conn.cursor()
    cursor.execute('''
                    SELECT * FROM Tasks
                    ''')
    tasks = cursor.fetchall() #retrieves a list of data from the last executed querry
    if tasks:
        print('tasks found')
        for i in tasks:
            print(i[1])
    else:
        print("no current tasks")

def  findtask():
    conn = sqlite3.connect('mytask.db')
    cursor = conn.cursor()
    t_id = int(input('enter task id: '))
    cursor.execute('''SELECT * FROM Tasks WHERE id = ?''',(t_id,))
    task = cursor.fetchone()
    print(task)
    if task:
        print("task found")
        print(f'task - {task[1]} des - {task[2]}')
    else:
        print('no such tasks')


def updatetasks():
    conn = sqlite3.connect('mytask.db')
    cursor = conn.cursor()
    t_id = int(input('enter task id: '))
    tname = input('enter taskname:- ')
    tdes = input('enter taskdes: -')
    cursor.execute('''UPDATE Tasks set task_name = ?,task_des = ? WHERE id = ?''',(tname,tdes,t_id))
    conn.commit()
    print('task updated')


def deletetasks():
    conn = sqlite3.connect('mytask.db')
    cursor = conn.cursor()
    t_id = int(input('enter task id: '))
    ch = input('Are you sure you want to delete this task\nY/N').lower()
    if ch == 'y':
        cursor.execute('''DELETE FROM Tasks WHERE id = ?''',(t_id,))
        conn.commit()
        print("task delete!!!")
    else:
        print('task not deleted')
    

def main():
    print('Welcome to task management system')
    while True:
        print('choose your option')
        ch = int(input('1.Add tasks\n2.Find task\n3.Edit tasks\n4.Update tasks\n5.Delete task\n6.exit: '))
        if ch == 1:
            addtask()
        elif ch == 2:
            findtask()
        elif ch == 4:
            updatetasks()
        elif ch == 5:
            deletetasks()
        elif ch == 6:
            break
        else:
            print('invalid option')
main()
        
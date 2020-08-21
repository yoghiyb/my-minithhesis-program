import mysql.connector
import tkinter as tk
from tkinter import ttk

def View():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="facebase"
    )

    query = "SELECT * FROM mhs"
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    root = tk.Tk()
    root.title('Data')
    root.wm_iconbitmap('assets/umsida.ico')
    tree = ttk.Treeview(root, column=("column1", "column2", "column3", "column4"), show='headings',
                             height=len(rows))
    tree.heading("#1", text="Id")
    tree.heading("#2", text="Nama")
    tree.heading("#3", text="Nim")
    tree.heading("#4", text="Jurusan")
    tree.pack()

    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)
    conn.close()

    root.mainloop()
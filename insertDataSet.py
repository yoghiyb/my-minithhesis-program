import mysql.connector
import tkinter as tk
import cv2 as cv


class Data:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="facebase")
        self.cursor = self.conn.cursor()
        self.conn.commit()

    def insertOrUpdate(self, Id, Nama, Nim, Jurusan):
        query = "SELECT * FROM mhs WHERE id='%s'" % (Id)
        self.cursor.execute(query)
        isRecordExist = 0
        for row in self.cursor:
            isRecordExist = 1
        if (isRecordExist == 1):
            query = "UPDATE mhs SET nama='%s', nim='%s', jurusan='%s' WHERE id='%s'" % (Nama, Nim, Jurusan, Id)
        else:
            query = "INSERT INTO mhs (id,nama,nim,jurusan) VALUES ('%s','%s','%s','%s')" % (Id, Nama, Nim, Jurusan)
        self.cursor.execute(query)
        self.conn.commit()

db = Data()

class Window:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title('Tambah Data')
        self.window.wm_iconbitmap('assets/umsida.ico')

        self.l1 = tk.Label(self.window, text="ID")
        self.l1.config(width=10)
        self.l1.grid(row=0, column=0)

        self.l2 = tk.Label(self.window, text="Nama")
        self.l2.config(width=10)
        self.l2.grid(row=1, column=0)

        self.l3 = tk.Label(self.window, text="Nim")
        self.l3.config(width=10)
        self.l3.grid(row=2, column=0)

        self.l4 = tk.Label(self.window, text="Jurusan")
        self.l4.config(width=10)
        self.l4.grid(row=3, column=0)

        self.id_text = tk.StringVar()
        self.e1 = tk.Entry(self.window, textvariable=self.id_text)
        self.e1.config(width=30)
        self.e1.grid(row=0, column=1)

        self.nama_text = tk.StringVar()
        self.e2 = tk.Entry(self.window, textvariable=self.nama_text)
        self.e2.config(width=30)
        self.e2.grid(row=1, column=1)

        self.nim_text = tk.StringVar()
        self.e3 = tk.Entry(self.window, textvariable=self.nim_text)
        self.e3.config(width=30)
        self.e3.grid(row=2, column=1)

        self.jurusan_text = tk.StringVar()
        self.e4 = tk.Entry(self.window, textvariable=self.jurusan_text)
        self.e4.config(width=30)
        self.e4.grid(row=3, column=1)

        self.b1 = tk.Button(self.window, text="Tambah atau Update", command=self.tambah_update_command)
        self.b1.grid(row=4, columnspan=2)

        self.window.mainloop()

    def dataSet(self):
        wajah = cv.CascadeClassifier('classifiers/face-detect.xml')
        cam = cv.VideoCapture(0)

        id = str(self.id_text.get())
        # nama = str(self.nama_text.get())
        sampleNum = 0

        while True:
            _, img = cam.read()
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            wajahs = wajah.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in wajahs:
                sampleNum = sampleNum + 1
                cv.imwrite("dataSet/User." + str(id) + "." + str(sampleNum) + ".jpg",
                           cv.resize(gray[y:y + h, x:x + w], (100, 100)))
                cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.imshow('DataSet', img)
            # cv.imshow('Gray', gray)
            cv.waitKey(1)
            if (sampleNum >= 20):
                break
        cam.release()
        cv.destroyAllWindows()

    def tambah_update_command(self):
        db.insertOrUpdate(self.id_text.get(), self.nama_text.get(), self.nim_text.get(), self.jurusan_text.get())
        self.window.destroy()
        self.dataSet()


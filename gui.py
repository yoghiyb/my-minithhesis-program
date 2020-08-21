import sys
import detector
import list_fromdb
import dataTrainner
import insertDataSet
from tkinter import filedialog, messagebox
import PIL.Image, PIL.ImageTk
import cv2 as cv
import os
import ctypes
import time

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

import gui_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1(root)
    gui_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


recognizer = cv.face.EigenFaceRecognizer_create()
recognizer.read("dataTrain/trainingData.xml")
face = cv.CascadeClassifier("classifiers/face-detect.xml")
rokok = cv.CascadeClassifier("classifiers/cigarette-detect.xml")


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        top.geometry("800x550+311+94")
        top.title("Identifikasi Wajah Perokok")
        top.wm_iconbitmap('assets/umsida.ico')
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.configure(width="400")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.013, rely=0.018, relheight=0.818
                           , relwidth=0.838)
        self.Canvas1.configure(background="#fff")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="#000")
        self.Canvas1.configure(insertbackground="#fff")
        self.Canvas1.configure(relief='ridge')
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=600)

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.TButton = ttk.Button(top)
        self.TButton.place(relx=0.869, rely=0.020, height=25, width=86)
        self.TButton.configure(takefocus="")
        self.TButton.configure(text='''Tambah Data''', command=insertDataSet.Window)

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.869, rely=0.090, height=25, width=86)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Training Data''', command=dataTrainner.Train)

        self.TButton2 = ttk.Button(top)
        self.TButton2.place(relx=0.869, rely=0.162, height=25, width=86)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Lihat Data''', command=list_fromdb.View)

        self.TButton3 = ttk.Button(top)
        self.TButton3.place(relx=0.869, rely=0.235, height=25, width=86)
        self.TButton3.configure(takefocus="")
        self.TButton3.configure(text='''Uji Citra''', command=self.condition_img)

        self.button = ttk.Button(top, text="Pilih File", command=self.file_dialog)
        self.button.place(relx=0.869, rely=0.308, height=25, width=86)

        self.entry = ttk.Entry(top, text="")
        self.entry.place(relx=0.869, rely=0.370, height=25, width=86)

        # self.TEntry1 = ttk.Entry(top)
        # self.TEntry1.place(relx=0.013, rely=0.891, relheight=0.093
        #         , relwidth=0.833)
        # self.TEntry1.configure(width=666)
        # self.TEntry1.configure(takefocus="")
        # self.TEntry1.configure(cursor="ibeam")
        self.copyright_symbol = u"\u00A9 2019 Yoghi Yuna Burnama"
        self.labelcp = tk.Label(top, text=self.copyright_symbol)
        self.labelcp.place(relx=0.400, rely=0.940)

        self.TProgressbar1 = ttk.Progressbar(top, lengt=100, mode='determinate')
        self.TProgressbar1.place(relx=0.013, rely=0.842, relwidth=0.838
                                 , relheight=0.0, height=22)
        self.TProgressbar1.configure(length="670")

    def file_dialog(self):
        self.entry.delete(0, 'end')
        self.filename = filedialog.askopenfilename(initialdir="/", title="Pilih file",
                                                   filetype=(("jpeg", "*.jpg"), ("jpeg", "*.jpg")))
        self.entry.insert(0, self.filename)

    # def condition(self):
    #     getDir = self.entry.get()
    #     if getDir == '':
    #         detector.detect(0)
    #     else:
    #         detector.detect(getDir)

    def condition_img(self):
        getDir = self.entry.get()
        if getDir == '':
            ctypes.windll.user32.MessageBoxW(0, "Data tidak boleh kosong", "Warning", 0)
        else:
            self.TProgressbar1['value'] = 20
            root.update_idletasks()
            time.sleep(1)
            self.TProgressbar1['value'] = 50
            root.update_idletasks()
            time.sleep(1)
            self.TProgressbar1['value'] = 80
            root.update_idletasks()
            time.sleep(1)
            self.TProgressbar1['value'] = 100
            self.img_dtc(getDir)

    def img_dtc(self, src):
        width, height = 100, 100
        im = cv.imread(src)
        gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
        # print(src)
        # scaleFactor = Parameter yang menentukan seberapa besar ukuran gambar berkurang pada setiap skala gambar.
        # minNeightbors = Parameter yang menentukan berapa banyak tetangga yang harus dimiliki setiap boxnya.
        faces = face.detectMultiScale(gray, 1.3, 5)
        rokoks = rokok.detectMultiScale(gray, 1.3, 5)

        merokok = 0
        for (x, y, w, h) in faces:
            id, conf = recognizer.predict(cv.resize(gray[y:y + h, x:x + w], (width, height)))
            print(conf)
            cv.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
            if conf < 6000:
                profile = detector.getProfile(id)
                if (profile != None):
                    for x_, y_, w_, h_ in rokoks:
                        cv.rectangle(im, (x, y), (x + w, y + h), (0, 0, 255), 2)
                        cv.rectangle(im, (x_, y_), (x_ + w_, y_ + h_), (0, 0, 255), 2)
                        self.cv_img = cv.cvtColor(cv.resize(im, (667, 463)), cv.COLOR_BGR2RGB)
                        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))
                        self.Canvas1.create_image(0, 0, image=self.photo, anchor=tk.NW)
                        merokok = 1

                    self.cv_img = cv.cvtColor(cv.resize(im, (667, 463)), cv.COLOR_BGR2RGB)
                    self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))
                    self.Canvas1.create_image(0, 0, image=self.photo, anchor=tk.NW)

                    if merokok == 1:
                        kepercayaan = "{0:.2f}%".format(round(100 - (conf / 100)), 2)
                        messagebox.showinfo(title='Identifikasi',
                                            message=' Akurasi: %s \n Nama: %s \n Nim: %s \n Jurusan: %s \n Status : Sedang Merokok' % (
                                                kepercayaan, str(profile[1]), str(profile[2]), str(profile[3])))
                    else:
                        kepercayaan = "{0:.2f}%".format(round(100 - (conf / 100)), 2)
                        messagebox.showinfo(title='Identifikasi',
                                            message=' Akurasi: %s \n Nama: %s \n Nim: %s \n Jurusan: %s \n Status : Sedang Tidak Merokok' % (
                                                kepercayaan, str(profile[1]), str(profile[2]), str(profile[3])))
            else:
                for x_, y_, w_, h_ in rokoks:
                    cv.rectangle(im, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv.rectangle(im, (x_, y_), (x_ + w_, y_ + h_), (0, 0, 255), 2)
                    self.cv_img = cv.cvtColor(cv.resize(im, (667, 463)), cv.COLOR_BGR2RGB)
                    self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))
                    self.Canvas1.create_image(0, 0, image=self.photo, anchor=tk.NW)
                    merokok = 1

                self.cv_img = cv.cvtColor(cv.resize(im, (667, 463)), cv.COLOR_BGR2RGB)
                self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))
                self.Canvas1.create_image(0, 0, image=self.photo, anchor=tk.NW)

                if merokok == 1:
                    messagebox.showinfo(title='Identifikasi',
                                        message=' Nama : Tidak Diketahui \n Nim : Tidak Diketahui \n Jurusan : Tidak Diketahui \n Status : Sedang Merokok')
                else:
                    messagebox.showinfo(title='Identifikasi',
                                        message=' Nama : Tidak Diketahui \n Nim : Tidak Diketahui \n Jurusan : Tidak Diketahui \n Status : Sedang Tidak Merokok')

        self.cv_img = cv.cvtColor(cv.resize(im, (667, 463)), cv.COLOR_BGR2RGB)
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))
        self.Canvas1.create_image(0, 0, image=self.photo, anchor=tk.NW)


if __name__ == '__main__':
    vp_start_gui()

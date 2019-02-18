
import sys

if(sys.version_info[0] < 3):
    print("This program is written with Python 3.x")
    print("Run \'Python3 filename.py\' to propperly run the program")
    sys.exit(1)

else:
    import os
    import tkinter as tk
    from tkinter import *
    from zipfile import ZipFile
    from tkinter import messagebox, filedialog

    def CreateWidgets():
        selectlabel = Label(root, text = "SELECT FILE TO ZIP : ", bg = "steelblue", font=('', 10, 'bold'))
        selectlabel.grid(row = 0, column = 0, padx = 5, pady = 5)

        root.zipSelectEntry = Text(root, height = 4, width = 45, font = ('Arial', 10))
        root.zipSelectEntry.grid(row = 0, column = 1, columnspan = 2, padx = 5, pady = 5)

        zipBrowserButton = Button(root, text = "BROWSER", width = 20, height = 2, command = ZipBrowse)
        zipBrowserButton.grid(row = 0, column = 3, padx = 5, pady = 5)

        zipNamelabel = Label(root, text = "NAME OF ZIPPED FILE : ", bg = "steelblue", font = ('', 9, 'bold'))
        zipNamelabel.grid(row = 1, column = 0, padx = 5, pady = 5)

        root.zipNameEntry = Entry(root, width = 45, textvariable = zipName, font = ('Arial', 10))
        root.zipNameEntry.grid(row = 1, column = 1, columnspan = 2, padx = 5, pady = 5)

        zipButton = Button(root, text = "ZIP", width = 20, command = ZipFiles)
        zipButton.grid(row = 1, column = 3, padx = 5, pady = 5)

        
        unzipFilelabel = Label(root, text = "SELECT FILE TO UNZIP : ", bg = "steelblue", font=('', 10, 'bold'))
        unzipFilelabel.grid(row = 2, column = 0, padx = 5, pady = 5)

        root.unzipSelectEntry = Text(root, height = 4, width = 45, font = ('Arial', 10))
        root.unzipSelectEntry.grid(row = 2, column = 1, columnspan = 2, padx = 5, pady = 5)

        unZipBrowserButton = Button(root, text = "BROWSER", width = 20, height = 2, command = unZipBrowse)
        unZipBrowserButton.grid(row = 2, column = 3, padx = 5, pady = 5)

        unzipFileNamelabel = Label(root, text = "NAME FOR UNZIPPED FILE : ", bg = "steelblue", font = ('', 9, 'bold'))
        unzipFileNamelabel.grid(row = 3, column = 0, padx = 5, pady = 5)

        root.unzipNameEntry = Entry(root, width = 45, textvariable = foldername, font = ('Arial', 10))
        root.unzipNameEntry.grid(row = 3, column = 1, columnspan = 2, padx = 5, pady = 5)

        unZipButton = Button(root, text = "UnZIP", width = 20, command = unZipFiles)
        unZipButton.grid(row = 3, column = 3, padx = 5, pady = 5)

    def ZipBrowse():
        root.zipFileList = filedialog.askopenfilenames(initialdir = "~/Desktop/2019\ Projects/Python/Day-03/")
        root.zipSelectEntry.insert('1.0', "FOLOOWING FILES WILL BE ZIPPED\n")
        for files in root.zipFileList:
            root.files = os.path.basename(files)
            root.zipSelectEntry.insert('2.0',root.files+"\n")
        root.zipSelectEntry.config(state=DISABLED)
    def unZipBrowse():
        root.unzipFileList = filedialog.askopenfilenames(initialdir = "~/Desktop/2019\ Projects/Python/Day-03/")
        root.zipSelectEntry.insert('1.0', "FOLOOWING FILES WILL BE UNZIPPED\n")
        root.files = os.path.basename(root.unzipFileList)
        root.unzipSelectEntry.insert('2.0', root.files+"\n")
        root.unzipSelectEntry.config(state=DISABLED)
        
    def ZipFiles():
        with ZipFile(zipName.get(), 'w') as zip1:
            for files1 in root.zipFileList:
                zip1.write(files1, os.path.basename(files1))

        messagebox.showinfo("SUCCESS", "FILES ZIPPED SUCCESSFULLY")

    def unZipFiles():
        os.makedirs(foldername.get())
        with ZipFile(root.unzipFileList, 'r') as UNzip1:
            UNzip1.extractall(foldername.get())

        messagebox.showinfo("SUCCESS", "FILES UNZIPPED SUCCESSFULLY")
    
    if __name__ == '__main__':
        root = tk.Tk()

        root.title("ZipUnzip")
        root.config(background = "steelblue")

        zipName = StringVar()
        foldername = StringVar()

        CreateWidgets()

        root.mainloop()

    
            
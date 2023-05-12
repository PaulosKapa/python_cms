from bs4 import BeautifulSoup as bs
from tkinter import *
from tkinter import ttk
from create_par import create_paragraph 
from add_pages import create_page
from select_files import select_files
import webbrowser, os, sys
#path of index file
path = 'html_files/index.html'
#check if the file exists
check_file = os.path.isfile(path)
#if it exists just open it
if check_file == True:
    with open("html_files/index.html") as fp:
        soup = bs(fp)  
#else create it and then write on it
else:
    html_file = open("html_files/index.html", "w")  
    init = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Document</title></head><body></body></html>'
    html_file.writelines(init)
    html_file.close()
    #then reopen it for reading
    with open("html_files/index.html") as fp:
        soup = bs(fp) 
#check if the index.html is empty
index_content = soup.body.text
#preview the website
def preview():
    webbrowser.open('file://' + os.path.realpath(path))
#restarts the program
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def save_file():
    html_file = open("saves/selected_file.txt", "w")  
    html_file.writelines('index.html')
    html_file.close()
#new window
root = Tk()
#dimensions
frm = ttk.Frame(root, padding=10)
#new grid
frm.grid()
#check if index_content is empy
if index_content == "":
    #new label
    ttk.Label(frm, text="It seems like your page doesn't have content in it. What would you like to add?").grid(column=0, row=0)
    #new button to add a paragraph
    ttk.Button(frm, text="paragraph", command=lambda:[create_paragraph(), save_file()]).grid(column=0, row=1)
else:
    #new label
    ttk.Label(frm, text="Choose an option").grid(column=0, row=0)
    #new button to add a paragraph
    ttk.Button(frm, text="Add page", command=create_page).grid(column=0, row=1)
    ttk.Button(frm, text="Edit page", command=select_files).grid(column=1, row=1)      
#new button to add preview
ttk.Button(frm, text="preview", command=preview).grid(column=0, row=2)
#new button to reload page
ttk.Button(frm, text="reload", command=restart_program).grid(column=0, row=3)
ttk.Button(frm, text="quit", command=root.destroy).grid(column=0, row=4)
root.mainloop()



from bs4 import BeautifulSoup as bs
import tkinter as tk
from add_tags import add_tags
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
    init = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Document</title><link rel="stylesheet" href="styles/styles.css"></head><body></body></html>'
    html_file.writelines(init)
    html_file.close()
    #then reopen it for reading
    with open("html_files/index.html") as fp:
        soup = bs(fp) 
#check if the index.html is empty
index_content = soup.body.findChildren()
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
root = tk.Tk()
#dimensions
root.geometry('%dx%d'%(root.winfo_screenwidth(),root.winfo_screenheight()))
#check if index_content is empy
if index_content == []:
    #new label
    tk.Label(root, text="It seems like your page doesn't have content in it.").pack()
    #new button to add a paragraph
    tk.Button(root, text="Add tag", command=lambda:[add_tags(), save_file()]).pack()
else:
    #new label
    tk.Label(root, text="Choose an option").pack()
    #new button to add a paragraph
    tk.Button(root, text="Add page", command=create_page).pack()
    tk.Button(root, text="Edit page", command=select_files).pack()    
#new button to add preview
tk.Button(root, text="Preview", command=preview).pack()
#new button to reload page
tk.Button(root, text="Reload", command=restart_program).pack()
#save to github
from save_github import save_git
tk.Button(root, text="Save", command=save_git).pack()
tk.Button(root, text="Quit", command=root.destroy).pack()
root.mainloop()

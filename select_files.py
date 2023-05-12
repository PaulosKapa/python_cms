from edit_page import edit
def select_files():
    def save_file():
        html_file = open("saves/selected_file.txt", "w")  
        html_file.writelines(printButton.cget('text'))
        html_file.close()
    import tkinter as tk
    import os
    files = os.scandir("html_files/")
    files1 = os.scandir("html_files/html/")
    #new window
    root = tk.Tk()
    #dimensions
    root.geometry("700x350")
    for file in files:
        if ".html" in file.name:
            #new button
            printButton = tk.Button(root, text = file.name, command=lambda: [save_file(), edit()])
            printButton.pack()   
    for file in files1:
        if ".html" in file.name:
            #new button
            printButton = tk.Button(root, text = file.name, command=lambda: [save_file(), edit()])
            printButton.pack()      
    root.mainloop()    
#run only directly or when called from imported file
if __name__ == "__main__":
    select_files()
from edit_page import edit
def select_files():
    def restart_program():
        import os, sys
        python = sys.executable
        os.execl(python, python, * sys.argv)   
    def save_file():
        #get the name of the file
        if "html" in id_textBox.get("1.0","end-1c"):
            open_file = id_textBox.get("1.0","end-1c")
        else:
            open_file = str(id_textBox.get("1.0","end-1c"))+".html"
        html_file = open("saves/selected_file.txt", "w")  
        html_file.writelines(open_file)
        html_file.close()
        id_textBox.delete("1.0","end-1c")
    def remove_file():
        html_file = open("saves/selected_file.txt", "r")  
        selected_file = html_file.readline()
        html_file.close()
        #delete file
        import os
        if selected_file == "index.html":
            tk.Label(root, text = "Can't remove index file!").pack()
        else:
            os.remove("html_files/html/"+selected_file)
    import tkinter as tk
    import os
    files = os.scandir("html_files/")
    files1 = os.scandir("html_files/html/")
    #new window
    root = tk.Tk()
    #dimensions
    root.geometry('%dx%d'%(root.winfo_screenwidth(),root.winfo_screenheight()))
    for file in files:
        if ".html" in file.name:
            #new label
            tk.Label(root, text = file.name).pack()
              
    for file in files1:
        if ".html" in file.name:
            #new button
            tk.Label(root, text = file.name).pack()
    id_textBox = tk.Text(root, height = 1, width = 16)
    id_textBox.pack()
    printButton = tk.Button(root, text = "Edit", command=lambda: [save_file(), edit()])
    printButton.pack()   
    tk.Button(root, text = "Remove", command=lambda: [save_file(), remove_file()]).pack()  
    tk.Button(root, text = "Restart", command=restart_program).pack()  
    root.mainloop()    
#run only directly or when called from imported file
if __name__ == "__main__":
    select_files()
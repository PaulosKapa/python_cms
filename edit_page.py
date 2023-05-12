def edit():
    def preview():
        import webbrowser, os
        if get_file == "index.html":
            path = "html_files/" + get_file
        else:
            path = "html_files/html/" + get_file
        webbrowser.open('file://' + os.path.realpath(path))
    def restart_program():
         import os, sys
         python = sys.executable
         os.execl(python, python, * sys.argv)
    #get the id of the selected div
    def get_id():
        text_id = printButton.cget('text')
        need_id = text_id[text_id.find(':')+1:]
        text_file = open("saves/selected_id.txt", "w")
        text_file.writelines(need_id)
        
    text_file = open("saves/selected_file.txt", "r")
    get_file = text_file.readline()   
    from bs4 import BeautifulSoup as bs
    import tkinter as tk
    if get_file == "index.html":
        with open("html_files/index.html") as fp:
            soup = bs(fp) 
    else:
        with open("html_files/html"+get_file) as fp:
            soup = bs(fp) 
    #new window
    root = tk.Tk()
    #dimensions
    root.geometry("700x350")
    index_content = soup.title.text
    divs = soup.find_all('div')
    i = 0
    while i< len(divs):
        text_label = str
        if "<p>" in str(divs[i].findChildren()):
            text_label = "paragraph: "+divs[i]['id']
        else:
            text_label = "error"
        printButton = tk.Button(root, text="edit " + text_label, command=get_id)
        printButton.pack()
        i+=1
    from move_tags import move
    printButton = tk.Button(root, text="move tags", command=move)
    printButton.pack()
    tk.Button(root, text="Restart", command=restart_program).pack()
    tk.Button(root, text="preview", command=preview).pack()
    root.mainloop()  
#run only directly or when called from imported file
if __name__ == "__main__":
    edit()

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
        #make the input into a readable string
        text_id = id_textBox.get("1.0","end-1c")
        #text_id = printButton.cget('text')
        #need_id = text_id[text_id.find(':')+1:]
        #check if the id exists to edit is
        id_exists =  True
        for div in divs:
            if text_id == div['id']:
                id_exists = True
                break
            else:
                id_exists = False
            print(id_exists)
        if text_id != "" and id_exists == True:
            text_file = open("saves/selected_id.txt", "w")
            text_file.writelines(text_id)
        else:
            error_label = tk.Label(root, text = "Enter a valid id!").pack()
        id_textBox.delete("1.0","end-1c")

    text_file = open("saves/selected_file.txt", "r")
    get_file = text_file.readline()   
    from bs4 import BeautifulSoup as bs
    import tkinter as tk
    if get_file == "index.html":
        with open("html_files/index.html") as fp:
            soup = bs(fp) 
    else:
        with open("html_files/html/"+get_file) as fp:
            soup = bs(fp) 
    #new window
    root = tk.Tk()
    #dimensions
    root.geometry("700x350")
    index_content = soup.title.text
    divs = soup.find_all('div')
    i = 0
    #loop throught all the divs
    while i< len(divs):
        text_label = str
        #if it finds a paragraph then add paragraph
        if "<p>" in str(divs[i].findChildren()):
            text_label = "paragraph: "+divs[i]['id']
        else:
            text_label = "error"
        #show labels for what can be edited
        tk.Label(root, text=text_label).pack()
        i+=1
    tk.Label(root, text="Choose tag to edit").pack()
    id_textBox = tk.Text(root, height = 1, width = 16)
    id_textBox.pack()
    from edit_paragraph import edit_par
    tk.Button(root, text="edit tags", command=lambda:[get_id(), edit_par()]).pack()
    from move_tags import move
    tk.Button(root, text="move tags", command=move).pack()
    tk.Button(root, text="Restart", command=restart_program).pack()
    tk.Button(root, text="preview", command=preview).pack()
    root.mainloop()  
#run only directly or when called from imported file
if __name__ == "__main__":
    edit()

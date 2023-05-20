def edit():
    #delete tags
    def delete():
        #get div to delete
        id_file = open("saves/selected_id.txt", "r")
        id = id_file.readline()
        id_file.close()
        soup.find("div", {"id": id}).decompose()
        if get_file == "index.html":
            file = open("html_files/index.html", "w")
        else:
            file = open("html_files/html/"+get_file, "w")
        #write to file
        file.writelines(str(soup))
        file.close()
    
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
        if text_id != "" and id_exists == True:
            text_file = open("saves/selected_id.txt", "w")
            text_file.writelines(text_id)
        else:
            text_file = open("saves/selected_id.txt", "w")
            error_label = tk.Label(root, text = "Enter a valid id!").pack()
            text_file.close()
        id_textBox.delete("1.0","end-1c")
        #check if the id was an image or a pragraph
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
    root.geometry('%dx%d'%(root.winfo_screenwidth(),root.winfo_screenheight()))
    index_content = soup.title.text
    divs = soup.find_all('div')
    i = 0
    #loop throught all the divs
    while i< len(divs):
        text_label = str
        print(divs[i].findChildren())
        #if it finds a paragraph then add paragraph
        if "<p>" in str(divs[i].findChildren()):
            text_label = "paragraph: "+divs[i]['id']
        elif "<img" in str(divs[i].findChildren()):
            text_label = "image: "+divs[i]['id']
        else:
            text_label = "error"
        #show labels for what can be edited
        tk.Label(root, text=text_label).pack()
        i+=1
    tk.Label(root, text="Choose tag to edit").pack()
    id_textBox = tk.Text(root, height = 1, width = 16)
    id_textBox.pack()
    from edit_tags import edit_tags
    tk.Button(root, text="Edit tags", command=lambda:[get_id(), edit_tags()]).pack()
    from add_tags import add_tags
    tk.Button(root, text="Add tags", command=add_tags).pack()
    tk.Button(root, text="delete tags", command=lambda:[get_id(), delete()]).pack()
    from move_tags import move
    tk.Button(root, text="move tags", command=move).pack()
    tk.Button(root, text="Restart", command=restart_program).pack()
    from create_par import create_paragraph 
    tk.Button(root, text="Add paragraph", command=create_paragraph).pack()
    tk.Button(root, text="Preview", command=preview).pack()
    root.mainloop()  
#run only directly or when called from imported file
if __name__ == "__main__":
    edit()

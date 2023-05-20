def move():
    def restart_program():
        import os, sys
        python = sys.executable
        os.execl(python, python, * sys.argv)
    #moing the tags and write in the file
    def move_write():
        #move tag2 before tag1
        tag_1 = soup.find("div", {"id": tag_name.get("1.0","end-1c")})
        tag_2 = soup.find("div", {"id": before_tag.get("1.0","end-1c")})
        tag_2.insert_before(tag_1)
        tag_name.delete("1.0","end-1c")
        before_tag.delete("1.0","end-1c")
        if get_file == "index.html":
            html_file = open("html_files/index.html", 'w')
        else:
            html_file =  open("html_files/html"+get_file, "w")
        #write to file
        html_file.writelines(str(soup))
        html_file.close()
    from bs4 import BeautifulSoup as bs
    import tkinter as tk
    text_file = open("saves/selected_file.txt", "r")
    get_file = text_file.readline() 
    if get_file == "index.html":
        with open("html_files/index.html") as fp:
            soup = bs(fp) 
    else:
        with open("html_files/html"+get_file) as fp:
            soup = bs(fp)
    divs = soup.find_all('div')
    i = 0
    #new window
    root = tk.Tk()
    #dimensions
    root.geometry('%dx%d'%(root.winfo_screenwidth(),root.winfo_screenheight()))
    while i< len(divs):
        text_label = str
        if "<p>" in str(divs[i].findChildren()):
            text_label = "paragraph: "+divs[i]['id']
        else:
            text_label = "error"
        tk.Label(root, text= text_label).pack()
        i+=1
    #get the names of the tags
    tag_name = tk.StringVar()
    before_tag = tk.StringVar()
    #new label
    tk.Label(root, text="What tag you want to move?").pack() 
    #new entry 
    tag_name = tk.Text(root, height = 1, width = 16)
    tag_name.pack()
    #new label
    tk.Label(root, text="Before what tag?").pack()
    #new entry 
    before_tag = tk.Text(root, height = 1, width = 16)
    before_tag.pack()
    tk.Button(root, text = 'Execute', command = move_write).pack()
    tk.Button(root, text = 'Restart', command = restart_program).pack()
    tk.Button(root, text = 'Quit', command = root.destroy).pack()
    root.mainloop() 
if __name__ == "__main__":
    move()
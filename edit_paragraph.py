def edit_par():
    def save_file():
        #destroy the current paragraph and replace it with a new one that has the written text
        paragraph = par.find("p")
        paragraph.decompose()
        new_par = soup.new_tag('p')
        new_par.string = text.get("1.0", "end-1c")
        
        par.append(new_par)
        if get_file == "index.html":
            html_file = open("html_files/index.html", 'w')
        else:
            html_file =  open("html_files/html"+get_file, "w")
        #write to file
        #check if there are tags
        if "&lt;"in str(soup):
            text_left = str(soup).replace("&lt;", "<")
            text_right = text_left.replace("&gt;", ">")
            html_file.writelines(text_right)
        else:
            html_file.writelines(str(soup))
        html_file.close()
        tk.Label(text = "Saved").pack()
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
    id_file = open("saves/selected_id.txt", "r")
    get_id = id_file.readline() 
    par = soup.find("div", {"id": get_id})
    #new window
    root = tk.Tk()
    #dimensions
    root.geometry("700x350")
    text = tk.Text(root, height = 16, width = 32)
    #get the text with tags
    preview_text_unedited = par.find('p').findChildren
    
    #preview_text_edited = preview_text_unedited.replace("p", "")

    text.insert("1.0", preview_text_unedited)
    text.pack()
    tk.Button(root, text = "save", command=save_file).pack()
    root.mainloop()

#run only directly or when called from imported file
if __name__ == "__main__":
    edit_par()
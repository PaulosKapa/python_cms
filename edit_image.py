#create new function to get the input and save it
def add_tags():
    def save_file():        
        if get_file == "index.html":
            html_file = open("html_files/index.html", 'w')
        else:
            html_file =  open("html_files/html"+get_file, "w")
            #write to file
            #check if there are tags
            html_file.writelines(str(soup))
            html_file.close()
            tk.Label(text = "Saved").pack()
    from bs4 import BeautifulSoup as bs
    import tkinter as tk
    import cssutils
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
    image = soup.find("div", {"id": get_id})
    # Parse the stylesheet, replace color
    parser = cssutils.parseFile('html_files/styles/styles.css')
    #new window
    root = tk.Tk()
    #dimensions
    root.geometry('%dx%d'%(root.winfo_screenwidth(),root.winfo_screenheight()))
    tk.Label(root, text = "Change attribute").pack();
    text = tk.Text(root, height = 1, width = 16)
    text.pack()
    #get the text with tags
    tk.Button(root, text = "save", command=save_file).pack()
    root.mainloop()
#run only directly or when called from imported file
if __name__ == "__main__":
    add_tags()
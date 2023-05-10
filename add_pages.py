#create new function to get the create a page
def create_page():
        #get the data from the entry
        def get_data():
            import os
            #set the path
            page_text = "html_files/html/"+page_name.get()+".html"
            print(page_text)
            #if the entry isn't empty or the file doesn't already exist save the html file with some basic tags
            if page_name.get()!='' and os.path.exists(page_text) == False:
                html_file = open(page_text, "w")  
                init = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Document</title></head><body></body></html>'
                html_file.writelines(init)
                html_file.close()
                page_name.set("")      
                root.destroy()      
            else:
                 tk.Label(root, text="Enter a page name first or choose another name").grid(row=0, column=2)  
        #import tkinter
        import tkinter as tk
        #new window
        root = tk.Tk()
        #dimensions
        root.geometry("700x350")
        page_name = tk.StringVar()
        #new label
        tk.Label(root, text="Enter the name of the page").grid(row=0, column=0)    
        #new entry 
        tk.Entry(root, textvariable = page_name).grid(row=0, column=1) 
        #new button
        tk.Button(root, text="Enter", command=get_data).grid(row=4, column=0)
        root.mainloop()
#run only directly or when called from imported file
if __name__ == "__main__":
    create_page()
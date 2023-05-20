#create new function to get the input and save it
def create_page():
        def get_data():
            import os
            page_text = "html_files/html"+page_name.get()+".html"
            if page_name.get()!='' and os.path.exists(page_text) == False:
                html_file = open(page_text, "w")  
                init = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Document</title></head><body></body></html>'
                html_file.writelines(init)
                html_file.close()
                page_name.set("")      
                root.destroy()      
            else:
                 tk.Label(root, text="Enter a page name first or choose another name").pack()
        #import tkinter
        import tkinter as tk
        #new window
        root = tk.Tk()
        #dimensions
        root.geometry('%dx%d'%(root.winfo_screenwidth(),root.winfo_screenheight()))
        page_name = tk.StringVar()
        page_label = tk.Label(root, text="Enter the name of the page").pack()   
        tk.Entry(root, textvariable = page_name).pack() 
        enter = tk.Button(root, text="Enter", command=get_data).pack()
        root.mainloop()
#run only directly or when called from imported file
if __name__ == "__main__":
    create_page()
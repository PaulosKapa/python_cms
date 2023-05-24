#create new function to get the input and save it
def add_tags():
        #import tkinter
        import tkinter as tk
        #new window
        root = tk.Tk()
        #dimensions
        root.geometry('%dx%d'%(root.winfo_screenwidth(),root.winfo_screenheight()))
        tk.Label(root, text="Select what you want to add").pack()   
        from create_par import create_paragraph
        tk.Button(root, text="Add paragraph", command=create_paragraph).pack()
        from add_image import add_image
        tk.Button(root, text="Add images", command=add_image).pack()
        from add_button import create_button
        tk.Button(root, text="Add button", command=create_button).pack()
        root.mainloop()
#run only directly or when called from imported file
if __name__ == "__main__":
    add_tags()
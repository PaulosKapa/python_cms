#save to github
def save_git():
    access_token = ""
    def get_token():
        from github import Github
        if textBox.get("1.0", "end-1c") != '':
            access_token = textBox.get("1.0","end-1c")
            g = Github(access_token)
            repo_owner = 'ipermeleti'
            repo_name = 'ipermeleti.github.io'
            repo = g.get_user(repo_owner).get_repo(repo_name)
        else:
            tk.Label(root, text="Please enter your token")

    import tkinter as tk
    #new window
    root = tk.Tk()
    #dimensions
    root.geometry('%dx%d'%(root.winfo_screenwidth(),root.winfo_screenheight()))
    #copy the html files
    folder_to_copy = "html_files"
    folder_to_paste = "test"
    try:
        from distutils.dir_util import copy_tree
        copy_tree(folder_to_copy, folder_to_paste)
    except:
        tk.Label(root, text = "Error with the copy-paste").pack()
    else:
        textBox = tk.Text(root, height = 1, width = 16)
        textBox.pack()
        tk.Button(root, text = "Save", command=get_token).pack()
        
    root.mainloop()
#run only directly or when called from imported file
if __name__ == "__main__":
    save_git()
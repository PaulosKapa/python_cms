def edit():
    #change title
    def change_title():
        title_text = title_textBox.get("1.0","end-1c")
        if title_text != "":
            title_tag = soup.find('title')
            title_tag.string = str(title_text)
            if get_file == "index.html":
                file = open("html_files/index.html", "w")
            else:
                file = open("html_files/html/"+get_file, "w")
        #write to file
            file.writelines(str(soup))
            file.close()
        else:
            tk.Label(root,"Please add a title").pack()
        title_textBox.delete("1.0","end-1c")
    selected_id = ""
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
        
        text_file = open("saves/selected_id.txt", "r")
        selected_id = text_file.readline()
        text_file.close()
        #remove styles
        import cssutils
        # Parse the stylesheet
        style_path = 'html_files/styles/styles.css'
        parser = cssutils.parseFile(style_path)
        selector_type = "#"+selected_id
        rules_to_keep = []
        
        for rule in parser:
            if isinstance(rule, cssutils.css.CSSStyleRule) and selector_type not in rule.selectorText:
                rules_to_keep.append(rule)
        styles_file = open("html_files/styles/styles.css", "w")
        styles_file.writelines("")
        styles_file.close()
        new_sheet = cssutils.parseFile(style_path)
        for rule in rules_to_keep:
            new_sheet.add(rule)
        with open(style_path, 'w') as css_file:
            css_file.write(new_sheet.cssText.decode('utf-8'))
            tk.Label(root, text = 'Saved')
        #check if the id is an image and dilete the directory
        if "images" in selected_id:
            import shutil
            #transform the text_id to the dir name
            dir_path = 'html_files/images/' + selected_id.replace('images', '')
            shutil.rmtree(dir_path)
    
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
        selected_id = text_id
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
        #if it finds a paragraph then add paragraph
        if "<p>" in str(divs[i].findChildren()):
            text_label = "Paragraph: "+divs[i]['id']
        elif "<img" in str(divs[i].findChildren()):
            text_label = "Image: "+divs[i]['id']
        elif "<button>" in str(divs[i].findChildren()):
            text_label = "Button: "+divs[i]['id']
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
    tk.Label(root, text="Enter the title of the page").pack()  
    title_textBox = tk.Text(root, height = 1, width = 16)
    title_textBox.pack()
    tk.Button(root, text="Edit title", command=change_title).pack()
    tk.Button(root, text="Preview", command=preview).pack()
    tk.Button(root, text="Restart", command=restart_program).pack()
    root.mainloop()  
#run only directly or when called from imported file
if __name__ == "__main__":
    edit()

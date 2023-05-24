#create new function to get the input and save it
def edit_img():
    #list of attributes that need size
    size_list = ["width", "heigh", "border-radius"]
    def editing():
        selector_type = str
        #check if it is a div or a children
        if var.get() == 2:
            selector_type = "#"+ get_id
        elif var.get() == 1:
            if "images" in get_id:
                selector_type = "#"+ get_id + " img"
            elif "button" in get_id:
                selector_type = "#"+ get_id + " button"
            else:
                selector_type = "#"+ get_id + " p"
        print (selector_type)
        attribute_text = attribute.get("1.0","end-1c")
        value_text = value.get("1.0","end-1c")
        if attribute_text in size_list:
            final_value = str(value_text) + "em"
        else:
            final_value = value_text
        for rule in parser:
            if isinstance(rule, cssutils.css.CSSStyleRule) and selector_type in rule.selectorText:
                rule.style.setProperty(attribute_text, final_value)
                with open(style_path, 'w') as css_file:
                    css_file.write(parser.cssText.decode('utf-8'))
                    tk.Label(root, text = 'Saved')
                    
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
    style_path = 'html_files/styles/styles.css'
    parser = cssutils.parseFile(style_path)
    #new window
    root = tk.Tk()
    #dimensions
    root.geometry('%dx%d'%(root.winfo_screenwidth(),root.winfo_screenheight()))
    tk.Label(root, text = "Change attribute").pack()
    attribute = tk.Text(root, height = 1, width = 16)
    attribute.pack()
    tk.Label(root, text = "Change value").pack()
    value = tk.Text(root, height = 1, width = 16)
    value.pack()
    var = tk.IntVar()
    R1 = tk.Radiobutton(root, text="Child", variable=var, value=1)
    R1.pack()
    R2 = tk.Radiobutton(root, text="Parent", variable=var, value=2)
    R2.pack()
    #get the text with tags
    tk.Button(root, text = "save", command=editing).pack()
    root.mainloop()
#run only directly or when called from imported file
if __name__ == "__main__":
    edit_img()
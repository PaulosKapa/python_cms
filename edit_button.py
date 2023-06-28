#create new function to get the input and save it
def create_button():
        #new function to save the input
        def get_input():
            #make the input into a readable string
            input_value = textBox.get("1.0","end-1c")
            id_input = input_value+"button"
            #id_input = id_name.get()
            link_input = link_textBox.get("1.0", "end-1c")
            #check if the id already exists
            #imbort beautiful soup
            from bs4 import BeautifulSoup as bs
            #get the html file from the saved file
            text_file = open("saves/selected_file.txt", "r")
            get_file = text_file.readline()
            if get_file == "index.html":
                with open("html_files/index.html") as fp:
                    soup = bs(fp) 
            else:
                with open("html_files/html"+get_file) as fp:
                    soup = bs(fp) 
            divs = soup.find_all('div')
            id_exists = False
            #loop throught all divs to see if the id already exists
            for div in divs:
                if div['id'] == id_input:
                    id_exists = True
                else:
                    id_exists = False
                    break
            #check if user entered any text
            if input_value!='' and id_input!='' and id_exists == False:

                #make a new paragraph tag and a div tag
                new_div = soup.new_tag("div")
                link_text = str(link_input)
                new_link = soup.new_tag("a", href=link_text)
                new_button = soup.new_tag("button")
                new_link.append(new_button)
                #give the div an id
                new_div['id'] = id_input
                #add the string
                new_button.string = input_value
                #add the tag after body
                soup.html.body.append(new_div)
                #add the paragraph adter the div
                new_div.append(new_link)
                #open file to write
                if get_file == "index.html":
                    html_file = open("html_files/index.html", 'w')
                else:
                    html_file =  open("html_files/html"+get_file, "w")
                #write to file
                #check for special characters
                if "&lt;"in str(soup):
                    text_left = str(soup).replace("&lt;", "<")
                    text_right = text_left.replace("&gt;", ">")
                    html_file.writelines(text_right)
                else:
                    html_file.writelines(str(soup))
                html_file.close()
            else:
                tk.Label(text = "You must enter some text or a non-existing id!").pack() 
        #import tkinter
        import tkinter as tk
        #new window
        root = tk.Tk()
        #dimensions
        root.geometry('%dx%d'%(root.winfo_screenwidth(),root.winfo_screenheight()))
        #input for id
        from bs4 import BeautifulSoup as bs
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
        btn = soup.find("div", {"id": get_id})
        #new input box
        tk.Label(root, text="Edit the name of the button").pack()
        textBox = tk.Text(root, height = 1, width = 24)
        textBox.insert("1.0", btn.find('button'))
        textBox.pack()
        tk.Label(root, text="Edit the link of the page").pack()  
        link_textBox = tk.Text(root, height = 1, width = 32)
        link_textBox.insert("1.0", btn.find('a'))
        link_textBox.pack()
        from edit_image import edit_img
        tk.Button(root, text = "Edit style", command=edit_img).pack()
        #new button
        printButton = tk.Button(root, text = "Save", command=get_input)
        printButton.pack()        
        root.mainloop()
#run only directly or when called from imported file
if __name__ == "__main__":
    create_button()
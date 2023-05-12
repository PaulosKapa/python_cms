#create new function to get the input and save it
def create_paragraph():
        #new function to save the input
        def get_input():
            #make the input into a readable string
            input_value = textBox.get("1.0","end-1c")
            #id_input = id_name.get()
            id_input = id_textBox.get("1.0", "end-1c")
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
            #check if user entered any text
            if input_value!='' and id_input!='' and id_exists == False:

                #make a new paragraph tag and a div tag
                new_div = soup.new_tag("div")
                new_par = soup.new_tag("p")
                #give the div an id
                new_div['id'] = id_input
                #add the string
                new_par.string = input_value
                #add the tag after body
                soup.html.body.append(new_div)
                #add the paragraph adter the div
                new_div.append(new_par)
                #open file to write
                if get_file == "index.html":
                    html_file = open("html_files/index.html", 'w')
                else:
                    html_file =  open("html_files/html"+get_file, "w")
                #write to file
                html_file.writelines(str(soup))
                html_file.close()
                root.destroy()
            else:
                tk.Label(text = "You must enter some text or a non-existing id!").pack() 
        #import tkinter
        import tkinter as tk
        #new window
        root = tk.Tk()
        #dimensions
        root.geometry("700x350")
        #new input box
        textBox = tk.Text(root, height = 5, width = 20)
        textBox.pack()
        #input for id
        tk.Label(root, text="Enter the id of the paragraph").pack()  
        id_textBox = tk.Text(root, height = 5, width = 5)
        id_textBox.pack()
        #new button
        printButton = tk.Button(root, text = "Save", command=get_input)
        printButton.pack()        
        root.mainloop()
#run only directly or when called from imported file
if __name__ == "__main__":
    create_paragraph()
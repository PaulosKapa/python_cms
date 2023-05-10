#create new function to get the input and save it
def create_paragraph():
        #new function to save the input
        def get_input():
            #make the input into a readable string
            input_value = textBox.get("1.0","end-1c")
            #check if user entered any text
            if input_value!='':
                #imbort beautiful soup
                from bs4 import BeautifulSoup as bs
                with open("index.html") as fp:
                    soup = bs(fp) 
                #make a new paragraph tag
                new_par = soup.new_tag("p")
                #add the string
                new_par.string = input_value
                #add the tag after body
                soup.html.body.append(new_par)
                #open file to write
                html_file = open("html_files/index.html", "w") 
                #write to file
                html_file.writelines(str(soup))
                html_file.close()
                root.destroy()
            else:
                tk.Label(text = "You must enter some text!").place(x = 40, y = 60) 
        #import tkinter
        import tkinter as tk
        #new window
        root = tk.Tk()
        #dimensions
        root.geometry("700x350")
        #new input box
        textBox = tk.Text(root, height = 5, width = 20)
        textBox.pack()
        #new button
        printButton = tk.Button(root, text = "Save", command=get_input)
        printButton.pack()        
        root.mainloop()
#run only directly or when called from imported file
if __name__ == "__main__":
    create_paragraph()
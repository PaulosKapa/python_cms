#create new function to get the input and save it
def add_image():
        #import tkinter
        import tkinter as tk
        #new window
        root = tk.Tk()
        #dimensions
        root.geometry('%dx%d'%(root.winfo_screenwidth(),root.winfo_screenheight()))
        def open_file():
            #get the collection
            dir_name = textBox.get("1.0","end-1c")
            #if collection name isnt empty
            if dir_name != '':
                #open a file dialog to find the image
                from tkinter import filedialog
                files = filedialog.askopenfiles(mode='r', filetypes=[('Images', '*png *jpg *jpeg *webp *raw *.ico')])
                if files:
                    import os
                    #get the absolute path
                    i = 0
                    filepath = []
                    for file in files: 
                        filepath.append(os.path.abspath(file.name))
                    #get the name of the file (os independent)
                    import ntpath
                    file_name = []
                    i = 0
                    for file in files:
                        file_name.append(ntpath.basename(filepath[i]))
                        
                        i+=1    
                    dir_exists = False
                    #check if the path already exists
                    if os.path.exists("html_files/images/"+dir_name) == False:
                        os.mkdir("html_files/images/"+dir_name)
                    else:
                        dir_exists = True
                    #check if image already exists. If it doesn't exist add it to selected images
                    selected_images = []
                    i = 0
                    for file in files:
                        if  os.path.exists("html_files/images/"+dir_name+"/"+file_name[i]) == False:
                            #copy from absolute path to images
                            from shutil import copy
                            copy(filepath[i], "html_files/images/"+dir_name+'/')
                            selected_images.append(file_name[i])
                        else:
                            tk.Label(root, text="Image: " +file_name[i]+" already exists!").pack()
                        i+=1
                    from bs4 import BeautifulSoup as bs
                    text_file = open("saves/selected_file.txt", "r")
                    get_file = text_file.readline()
                    if get_file == "index.html":
                        with open("html_files/index.html") as fp:
                            soup = bs(fp) 
                    else:
                        with open("html_files/html"+get_file) as fp:
                            soup = bs(fp)
                    divs = soup.find_all('div')
                    #check if there already is a div images 
                    id_exists = False
                    for div in divs:
                        if div['id'] != "images" +dir_name:
                            id_exists = False
                       
                        else:
                            id_exists = True
                            break
                    #if the id doesn' already exist, then add it
                    if dir_exists == False and id_exists == False:
                        new_div = soup.new_tag("div")
                        new_div['id'] = dir_name + "images"
                        soup.html.body.append(new_div)                
                    else:
                        new_div = soup.find("div", {"id": "images"+dir_name})
                
                    i = 0
                    for image in selected_images:
                        new_img = soup.new_tag("img")
                        #based on what file we are in, set the src, using the images we entered
                        if get_file == "index.html":
                            new_img['src'] = "images/"+dir_name+'/' + selected_images[i]
                        else:
                            new_img['src'] = "../images/" + dir_name + '/'+ selected_images[i]
                        #add the paragraph adter the div
                        new_div.append(new_img)
                        i+=1
                    if get_file == "index.html":
                        html_file = open("html_files/index.html", 'w')
                    else:
                        html_file =  open("html_files/html"+get_file, "w")
                    #write to file
                    html_file.writelines(str(soup))
                    html_file.close()
        # Add a Label widget
        label = tk.Label(root, text="Click the Button to select image")
        label.pack()
        #get the collection or make a new one to add the images to. Save the collection as part of the id
        #new label
        tk.Label(root, text="Enter the name of the collection").pack()  
        #new entry 
        textBox = tk.Text(root, height = 1, width = 16)
        textBox.pack()
        # Create a Button
        tk.Button(root, text="Browse", command=open_file).pack()
        root.mainloop()
#run only directly or when called from imported file
if __name__ == "__main__":
    add_image()
import webbrowser, os
#initialising action
action = ""
#path of index file
path = 'index.html'
#check if the file exists
check_file = os.path.isfile(path)
#if it exists just open it
if check_file == True:
    html_file = open("index.html", "r")    
#else create it and then write on it
else:
    html_file = open("index.html", "w")  
    init = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Document</title></head><body></body></html>'
    html_file.writelines(init)
    html_file.close()
    #then reopen it for reading
    html_file = open("index.html", "r")
#get the input for what to do
get_action = str(input("Action: "))
#read the content of then file
content = html_file.readline()
#get the number of id in the file
num_of_id = content.count("id")
#according to the input choose what to do
match get_action:
    case "paragraph":
        get_content = str(input("Content: "))
        action = "<p id = paragraph"+str(num_of_id)+"'>"+get_content+"</p>"
#splite the content on body to enter the content
split_content = content.split("<body>")
#enter the content
split_content.insert(1, "<body>"+action)
#make it back to a string
string_content = "".join(split_content)
html_file.close()
#if the action isn't empty open the file and then write the new content
if action != "":
    html_file = open("index.html", "w") 
    html_file.writelines(string_content)
    html_file.close()
#preview the file
webbrowser.open('file://' + os.path.realpath(path))

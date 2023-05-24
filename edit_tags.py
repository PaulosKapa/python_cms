#create new function to get the input and save it
def edit_tags():
        text_file = open("saves/selected_id.txt", "r")
        if "images" in text_file.readline():
            from edit_image import edit_img
            edit_img()
        elif "button" in text_file.readline():
            from edit_image import edit_img
            edit_img()
        else:
            from edit_paragraph import edit_par
            edit_par()
            
#run only directly or when called from imported file
if __name__ == "__main__":
    edit_tags()
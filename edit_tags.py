#create new function to get the input and save it
def edit_tags():
        text_file = open("saves/selected_id.txt", "r")
        if text_file.readline() != "images":
            from edit_paragraph import edit_par
            edit_par()
        else:
            from edit_image import edit_img
            edit_img()
#run only directly or when called from imported file
if __name__ == "__main__":
    edit_tags()
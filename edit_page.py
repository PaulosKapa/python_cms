def edit():
    from bs4 import BeautifulSoup as bs
    import tkinter as tk
    text_file = open("saves/selected_file.txt", "r")
    print(text_file.readlines())
#run only directly or when called from imported file
if __name__ == "__main__":
    edit()

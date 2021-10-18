import tkinter as tk
from tkinter.filedialog import askopenfilename
import shutil
import os
from os import path

#get path to files
execution_path = os.getcwd()

# main frame of program
class Main(tk.Frame):
    def __init__(self,root):
        super().__init__(root)

        self.label = tk.Label(text="This app will help you detect ships in the picture")
        self.label.pack()

        self.button = tk.Button(self, text="Browse picture", command=self.load_file, width=20)
        self.button.pack()

    # getting path to picture
    def load_file(self):
        source_path = askopenfilename(filetypes=(("Pictures", "*.jpg;*.jpeg;*.png"),
                                           ("All files", "*.*")))
    # file movement to needed folder
        if path.exists(source_path):
            destination_path = os.path.join(execution_path, "new_file.jpg")
            shutil.move(source_path, destination_path)
    # running the detecting process
            os.system(os.path.join(execution_path, "main.py"))

        else:
            print("Wrong path or picture not selected")


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Ships detection")
    root.geometry("400x200")
    root.resizable(False, False)
    root.mainloop()
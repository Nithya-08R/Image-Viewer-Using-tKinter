import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.root.geometry("800x600")
        self.root.configure(bg="white")

        self.image_list = []
        self.current_index = 0

        # UI Elements
        self.label = tk.Label(self.root, text="Select a folder to view images", bg="white", font=("Arial", 14))
        self.label.pack(pady=10)

        self.canvas = tk.Canvas(self.root, bg="white", width=700, height=400)
        self.canvas.pack()

        # Button Frame (for better layout)
        self.button_frame = tk.Frame(self.root, bg="white")
        self.button_frame.pack(pady=10)

        self.load_button = tk.Button(self.button_frame, text="Load Images", command=self.load_images, 
                                     font=("Arial", 12), bg="#ADD8E6", fg="black", width=12)
        self.load_button.grid(row=0, column=1, padx=10, pady=5)

        self.prev_button = tk.Button(self.button_frame, text="<< Previous", command=self.show_previous, state=tk.DISABLED, 
                                     bg="#90EE90", fg="black", width=12)
        self.prev_button.grid(row=1, column=0, padx=10, pady=5)

        self.next_button = tk.Button(self.button_frame, text="Next >>", command=self.show_next, state=tk.DISABLED, 
                                     bg="#90EE90", fg="black", width=12)
        self.next_button.grid(row=1, column=2, padx=10, pady=5)

        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.root.quit, 
                                     bg="#FFB6C1", fg="black", width=12)
        self.exit_button.grid(row=1, column=1, padx=10, pady=5)

    def load_images(self):
        folder_path = filedialog.askdirectory()
        if not folder_path:
            return

        self.image_list = [os.path.join(folder_path, f) for f in os.listdir(folder_path) 
                           if f.lower().endswith(("png", "jpg", "jpeg", "bmp"))]
        
        if not self.image_list:
            messagebox.showerror("Error", "No images found in the selected folder!")
            return

        self.current_index = 0
        self.show_image()
        self.update_buttons()

    def show_image(self):
        img_path = self.image_list[self.current_index]
        img = Image.open(img_path)
        img = img.resize((700, 400), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(img)

        self.canvas.create_image(350, 200, image=self.photo, anchor=tk.CENTER)
        self.label.config(text=os.path.basename(img_path))

    def show_next(self):
        if self.current_index < len(self.image_list) - 1:
            self.current_index += 1
            self.show_image()
            self.update_buttons()

    def show_previous(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_image()
            self.update_buttons()

    def update_buttons(self):
        self.prev_button.config(state=tk.NORMAL if self.current_index > 0 else tk.DISABLED)
        self.next_button.config(state=tk.NORMAL if self.current_index < len(self.image_list) - 1 else tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewer(root)
    root.mainloop()


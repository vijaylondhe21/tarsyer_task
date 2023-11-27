import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw

class ImageAnnotator:
    def __init__(self, root, image_path):
        self.root = root
        self.image_path = image_path

        self.canvas = tk.Canvas(root)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)
        self.load_image()

        self.rect_start_x = None
        self.rect_start_y = None

        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def load_image(self):
        image = Image.open(self.image_path)
        self.tk_image = ImageTk.PhotoImage(image)
        self.canvas.config(width=self.tk_image.width(), height=self.tk_image.height())
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

    def on_press(self, event):
        self.rect_start_x = self.canvas.canvasx(event.x)
        self.rect_start_y = self.canvas.canvasy(event.y)

    def on_drag(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)
        self.canvas.coords("rectangle", self.rect_start_x, self.rect_start_y, cur_x, cur_y)

    def on_release(self, event):
        rect_end_x = self.canvas.canvasx(event.x)
        rect_end_y = self.canvas.canvasy(event.y)
        self.canvas.create_rectangle(self.rect_start_x, self.rect_start_y, rect_end_x, rect_end_y, outline="red", tags="rectangle")

        cropped_image = self.crop_image(int(self.rect_start_x), int(self.rect_start_y), int(rect_end_x), int(rect_end_y))
        cropped_image.save("Task_1_cropped.jpg")
        self.save_insights_image(int(self.rect_start_x), int(self.rect_start_y), int(rect_end_x), int(rect_end_y))
        messagebox.showinfo("Image Saved", "Image has been saved as Task_1_cropped.jpg and Task_1_insights.jpg")

    def crop_image(self, start_x, start_y, end_x, end_y):
        image = Image.open(self.image_path)
        cropped_image = image.crop((start_x, start_y, end_x, end_y))
        return cropped_image

    def save_insights_image(self, start_x, start_y, end_x, end_y):
        insights_image = Image.open(self.image_path)
        draw = ImageDraw.Draw(insights_image)
        draw.rectangle([start_x, start_y, end_x, end_y], outline="red")
        draw.text((10, 10), f"Top left: ({start_x}, {start_y})", fill="red")
        draw.text((10, 30), f"Bottom right: ({end_x}, {end_y})", fill="red")
        insights_image.save("Task_1_insights.jpg")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Image Annotation")
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    
    if file_path:
        annotator = ImageAnnotator(root, file_path)
        root.mainloop()

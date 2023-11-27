import cv2
from tkinter import filedialog
import matplotlib.pyplot as plt
import os


def perfom_morph(image_path):
    original_image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    dilated_image = cv2.dilate(gray_image, kernel=(5, 5), iterations=1)
    eroded_image = cv2.erode(gray_image, kernel=(5, 5), iterations=1)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    opened_image = cv2.morphologyEx(gray_image, cv2.MORPH_OPEN, kernel)

    folder_path = os.path.dirname(image_path)
    cv2.imwrite(os.path.join(folder_path, 'gray_image.jpg'), gray_image)
    cv2.imwrite(os.path.join(folder_path, 'dilated_image.jpg'), dilated_image)
    cv2.imwrite(os.path.join(folder_path, 'eroded_image.jpg'), eroded_image)

    plt.figure(figsize=(10, 8))
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(dilated_image, cmap='gray')
    plt.title('Dilated Image')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(eroded_image, cmap='gray')
    plt.title('Eroded Image')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.imshow(opened_image, cmap='gray')
    plt.title('Opened Image')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

def choose_image():

    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

    if file_path:
        perfom_morph(file_path)

if __name__ == "__main__":
    choose_image()

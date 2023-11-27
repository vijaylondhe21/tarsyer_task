import cv2
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import os

def perform_thresholding(image_path):
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, simple_threshold = cv2.threshold(original_image, 127, 255, cv2.THRESH_BINARY)
    adaptive_threshold = cv2.adaptiveThreshold(original_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    folder_path = os.path.dirname(image_path)
    cv2.imwrite(os.path.join(folder_path, 'Task_3_simple.jpg'), simple_threshold)
    cv2.imwrite(os.path.join(folder_path, 'Task_3_adaptive.jpg'), adaptive_threshold)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(original_image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(simple_threshold, cmap='gray')
    plt.title('Simple Threshold')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(adaptive_threshold, cmap='gray')
    plt.title('Adaptive Threshold')
    plt.axis('off')

    plt.show()

def choose_image():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        perform_thresholding(file_path)

if __name__ == "__main__":
    choose_image()

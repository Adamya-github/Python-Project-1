import cv2

def load_image(file_path):
    image = cv2.imread(file_path)
    if image is None:
        print("Error: Image not loaded properly")
        exit()
    return image

def convert_to_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def invert_image(image):
    return 250 - image

def apply_gaussian_blur(image):
    return cv2.GaussianBlur(image, (21, 21), 0)

def create_pencil_sketch(gray_image, inverted_blurred):
    return cv2.divide(gray_image, inverted_blurred, scale=256.0)

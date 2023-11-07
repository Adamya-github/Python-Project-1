from image_processing import load_image, convert_to_gray, invert_image, apply_gaussian_blur, create_pencil_sketch
import cv2
# Load the image
image = load_image("235.jpeg")

# Convert the image to grayscale
gray_image = convert_to_gray(image)

# Invert the grayscale image
inverted_image = invert_image(gray_image)

# Apply Gaussian blur to the inverted image
blurred = apply_gaussian_blur(inverted_image)

# Invert the blurred image
inverted_blurred = invert_image(blurred)

# Create a pencil sketch
pencil_sketch = create_pencil_sketch(gray_image, inverted_blurred)

# Save the images to disk
cv2.imwrite("output_image.jpg", image)
cv2.imwrite("output_image1.jpg", gray_image)
cv2.imwrite("output_image2.jpg", inverted_image)
cv2.imwrite("output_image3.jpg", pencil_sketch)
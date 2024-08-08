from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import re

def preprocess_image(image_path):
    image = Image.open(image_path)
    image = image.convert('L')  # Convert to grayscale
    image = image.filter(ImageFilter.SHARPEN)  # Sharpen the image
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)  # Increase contrast
    return image

def image_to_text_with_config(image_path):
    image = preprocess_image(image_path)
    custom_config = r'--oem 3 --psm 6'  # OEM and PSM configurations
    text = pytesseract.image_to_string(image, config=custom_config)
    return text

def clean_text(text):
    # Remove extra whitespace and newlines
    text = re.sub(r'\s+', ' ', text)
    # Correct common OCR errors (example: replace '1' with 'I' if needed)
    text = text.replace('1', 'I')
    return text

def image_to_clean_text(image_path):
    text = image_to_text_with_config(image_path)
    clean_text_content = clean_text(text)
    return clean_text_content

image_path = 'Test.png'
clean_text_content = image_to_clean_text(image_path)
print(clean_text_content)

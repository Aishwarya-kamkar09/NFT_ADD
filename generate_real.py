# import cv2
# import numpy as np
# import os
# from PIL import Image, ImageDraw, ImageFont
# import random

# BASE_FOLDER = "data/certificates/real"
# FONT_PATH = "C:/Windows/Fonts/arial.ttf"

# first_names = ["Rohit", "Ananya", "Rahul", "Sneha", "Amit", "Priya"]
# last_names = ["Sharma", "Rao", "Verma", "Patil", "Kumar", "Singh"]

# def random_name():
#     return random.choice(first_names) + " " + random.choice(last_names)

# def add_handwritten(img):
#     pil_img = Image.fromarray(img)
#     draw = ImageDraw.Draw(pil_img)
#     font = ImageFont.truetype(FONT_PATH, 35)

#     x = random.randint(150, 400)
#     y = random.randint(250, 450)

#     draw.text((x, y), random_name(), font=font, fill=(0,0,0))
#     return np.array(pil_img)

# def add_blur(img):
#     return cv2.GaussianBlur(img, (5,5), 0)

# def add_noise(img):
#     noise = np.random.normal(0, 20, img.shape).astype(np.uint8)
#     return cv2.add(img, noise)

# def change_brightness(img):
#     return cv2.convertScaleAbs(img, alpha=1.1, beta=20)

# def generate():
#     files = [f for f in os.listdir(BASE_FOLDER) if f.lower().endswith((".jpg",".jpeg",".png"))]

#     for file in files:
#         path = os.path.join(BASE_FOLDER, file)
#         img = cv2.imread(path)

#         for i in range(3):
#             temp = img.copy()

#             temp = add_handwritten(temp)

#             if random.random() > 0.5:
#                 temp = add_blur(temp)

#             if random.random() > 0.5:
#                 temp = add_noise(temp)

#             if random.random() > 0.5:
#                 temp = change_brightness(temp)

#             save_name = f"aug_{i}_{file}"
#             cv2.imwrite(os.path.join(BASE_FOLDER, save_name), temp)

#     print("✅ Real variations generated")

# if __name__ == "__main__":
#     generate()











import os
import random
from PIL import Image, ImageDraw, ImageFont

# ---------------- CONFIG ----------------
TOTAL_REAL = 696
OUTPUT_DIR = "data/certificates/real"
os.makedirs(OUTPUT_DIR, exist_ok=True)

FONT_PATH = "C:/Windows/Fonts/arial.ttf"

# ---------------- DATA ----------------
names = [
    "Rohit Sharma", "Ananya Singh", "Rahul Verma", "Sneha Patel",
    "Amit Kumar", "Priya Nair", "Karan Mehta", "Neha Joshi",
    "Arjun Reddy", "Divya Kapoor", "Vikas Yadav"
]

courses = [
    "Machine Learning", "Data Science", "Web Development",
    "Cyber Security", "Artificial Intelligence",
    "Cloud Computing", "Python Programming"
]

organizations = [
    "TechCorp Pvt Ltd", "EduLearn Institute",
    "Future Skills Academy", "Global Tech University",
    "SkillUp Training Center"
]

# ---------------- HELPERS ----------------
def random_name():
    return random.choice(names)

def random_course():
    return random.choice(courses)

def random_org():
    return random.choice(organizations)

# ---------------- TEMPLATE 1 ----------------
def template1(idx):
    img = Image.new("RGB", (900, 650), "white")
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype(FONT_PATH, 45)
    text_font = ImageFont.truetype(FONT_PATH, 28)

    # Border
    draw.rectangle([20, 20, 880, 630], outline="black", width=3)

    draw.text((300, 100), "CERTIFICATE", font=title_font, fill="black")

    name = random_name()
    course = random_course()
    org = random_org()

    draw.text((150, 250), "This is to certify that", font=text_font, fill="black")
    draw.text((200, 300), name, font=text_font, fill="black")
    draw.text((150, 350), f"has successfully completed {course}", font=text_font, fill="black")
    draw.text((150, 400), f"from {org}", font=text_font, fill="black")

    # Signature
    draw.text((650, 550), "Authorized Signatory", font=text_font, fill="black")

    img.save(os.path.join(OUTPUT_DIR, f"real_{idx}.png"))

# ---------------- TEMPLATE 2 ----------------
def template2(idx):
    img = Image.new("RGB", (900, 650), "#f8f9fa")
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype(FONT_PATH, 40)
    text_font = ImageFont.truetype(FONT_PATH, 26)

    draw.text((250, 120), "Certificate of Completion", font=title_font, fill="black")

    name = random_name()
    course = random_course()
    org = random_org()

    draw.text((200, 280), name, font=text_font, fill="black")
    draw.text((200, 330), f"has completed {course}", font=text_font, fill="black")
    draw.text((200, 380), f"issued by {org}", font=text_font, fill="black")

    draw.text((650, 550), "Signature", font=text_font, fill="black")

    img.save(os.path.join(OUTPUT_DIR, f"real_{idx}.png"))

# ---------------- TEMPLATE 3 ----------------
def template3(idx):
    img = Image.new("RGB", (900, 650), "white")
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype(FONT_PATH, 38)
    text_font = ImageFont.truetype(FONT_PATH, 24)

    draw.text((280, 80), "Internship Certificate", font=title_font, fill="black")

    name = random_name()
    org = random_org()

    draw.text((150, 250), f"This certifies that {name}", font=text_font, fill="black")
    draw.text((150, 300), f"has completed internship at {org}", font=text_font, fill="black")
    draw.text((150, 350), "Duration: 3 months", font=text_font, fill="black")

    draw.text((650, 550), "HR Signature", font=text_font, fill="black")

    img.save(os.path.join(OUTPUT_DIR, f"real_{idx}.png"))

# ---------------- MAIN ----------------
def generate_real():
    print("Generating REAL certificates...")

    for i in range(TOTAL_REAL):
        template = random.choice([template1, template2, template3])
        template(i)

    print("✅ Real dataset generated!")

# ---------------- RUN ----------------
if __name__ == "__main__":
    generate_real()
# import cv2
# import numpy as np
# import os
# from PIL import Image, ImageDraw, ImageFont
# import random

# REAL_FOLDER = "data/certificates/real"
# FAKE_FOLDER = "data/certificates/fake"

# FONT_PATH = "C:/Windows/Fonts/arial.ttf"

# first_names = ["Rohit", "Ananya", "Rahul", "Sneha", "Amit", "Priya"]
# last_names = ["Sharma", "Rao", "Verma", "Patil", "Kumar", "Singh"]

# def random_name():
#     return random.choice(first_names) + " " + random.choice(last_names)

# # ✨ TYPE 1: TEXT TAMPERING
# def change_text(img):
#     pil_img = Image.fromarray(img)
#     draw = ImageDraw.Draw(pil_img)
#     font = ImageFont.truetype(FONT_PATH, 40)

#     x = random.randint(200, 500)
#     y = random.randint(300, 450)

#     draw.text((x, y), random_name(), font=font, fill=(0,0,255))
#     return np.array(pil_img)

# # ✨ TYPE 2: SAFE COPY-PASTE
# def copy_paste(img):
#     h, w, _ = img.shape

#     x1 = random.randint(0, w - 200)
#     y1 = random.randint(0, h - 200)

#     crop = img[y1:y1+100, x1:x1+100]

#     x2 = random.randint(0, w - 100)
#     y2 = random.randint(0, h - 100)

#     img[y2:y2+100, x2:x2+100] = crop

#     return img

# # ✨ TYPE 3: HEAVY NOISE
# def heavy_noise(img):
#     noise = np.random.randint(0, 100, img.shape, dtype='uint8')
#     return cv2.add(img, noise)

# # ✨ TYPE 4: DISTORTION
# def distort(img):
#     rows, cols, _ = img.shape
#     pts1 = np.float32([[50,50],[200,50],[50,200]])
#     pts2 = np.float32([[10,100],[200,50],[100,250]])
#     M = cv2.getAffineTransform(pts1, pts2)
#     return cv2.warpAffine(img, M, (cols, rows))

# # 🚀 MAIN FUNCTION
# def generate_fake():
#     os.makedirs(FAKE_FOLDER, exist_ok=True)

#     files = [f for f in os.listdir(REAL_FOLDER) if f.endswith((".jpg",".jpeg",".png"))]

#     count = 0

#     for file in files:
#         path = os.path.join(REAL_FOLDER, file)
#         img = cv2.imread(path)

#         if img is None:
#             continue

#         for i in range(3):
#             temp = img.copy()

#             temp = random.choice([
#                 change_text,
#                 copy_paste,
#                 heavy_noise,
#                 distort
#             ])(temp)

#             save_path = os.path.join(FAKE_FOLDER, f"fake_{count}.jpg")
#             cv2.imwrite(save_path, temp)
#             count += 1

#     print(f"✅ Generated {count} fake images")

# # ✅ RUN
# if __name__ == "__main__":
#     generate_fake()








import cv2
import os
import numpy as np
import random
from PIL import Image, ImageDraw, ImageFont

REAL_FOLDER = "data/certificates/real"
FAKE_FOLDER = "data/certificates/fake"

os.makedirs(FAKE_FOLDER, exist_ok=True)

FONT_PATH = "C:/Windows/Fonts/arial.ttf"

names = ["Aarav Sharma", "Priya Verma", "Rahul Singh", "Neha Gupta",
         "Amit Kumar", "Sneha Patil", "Rohan Mehta", "Isha Jain"]

companies = ["Google", "Microsoft", "Amazon", "Infosys", "TCS", "IBM"]

courses = ["AI Internship", "Web Development", "Data Science",
           "Machine Learning", "Cyber Security", "Cloud Computing"]

def add_text(img, text, pos, color=(0,0,0), size=32):
    pil = Image.fromarray(img)
    draw = ImageDraw.Draw(pil)
    font = ImageFont.truetype(FONT_PATH, size)
    draw.text(pos, text, font=font, fill=color)
    return np.array(pil)

def distort(img):
    rows, cols = img.shape[:2]
    pts1 = np.float32([[0,0],[cols,0],[0,rows]])
    pts2 = np.float32([
        [random.randint(5,20), random.randint(5,20)],
        [cols-random.randint(5,20), random.randint(5,20)],
        [random.randint(5,20), rows-random.randint(5,20)]
    ])
    M = cv2.getAffineTransform(pts1, pts2)
    return cv2.warpAffine(img, M, (cols, rows))

def add_noise(img):
    noise = np.random.randint(0, 50, img.shape, dtype='uint8')
    return cv2.add(img, noise)

def blur(img):
    return cv2.GaussianBlur(img, (5,5), 0)

def compress(img):
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), random.randint(30, 80)]
    _, encimg = cv2.imencode('.jpg', img, encode_param)
    return cv2.imdecode(encimg, 1)

def tamper_text(img):
    img = add_text(img, random.choice(names), (150, 250), (0,0,255), 30)
    img = add_text(img, random.choice(courses), (150, 300), (255,0,0), 25)
    img = add_text(img, random.choice(companies), (150, 350), (0,128,0), 25)
    return img

def generate_fake(base_img, idx):
    img = base_img.copy()

    # Step 1: tamper text
    img = tamper_text(img)

    # Step 2: random attacks
    if random.random() > 0.3:
        img = distort(img)
    if random.random() > 0.3:
        img = add_noise(img)
    if random.random() > 0.3:
        img = blur(img)
    if random.random() > 0.3:
        img = compress(img)

    save_path = os.path.join(FAKE_FOLDER, f"fake_{idx}.jpg")
    cv2.imwrite(save_path, img)

def generate_753():
    files = [f for f in os.listdir(REAL_FOLDER)
             if f.lower().endswith((".jpg",".png",".jpeg"))]

    if len(files) == 0:
        print("❌ No real images found!")
        return

    count = 0

    while count < 753:
        file = random.choice(files)
        path = os.path.join(REAL_FOLDER, file)

        img = cv2.imread(path)
        if img is None:
            continue

        generate_fake(img, count)
        count += 1

        if count % 50 == 0:
            print(f"Generated {count}/753 fake images")

    print("✅ Done: 753 fake certificates generated")

if __name__ == "__main__":
    generate_753()
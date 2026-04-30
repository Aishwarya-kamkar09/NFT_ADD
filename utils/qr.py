import qrcode

def generate_qr(token_id):
    url = f"http://localhost:5000/verify/{token_id}"
    img = qrcode.make(url)
    img.save(f"qr_{token_id}.png")
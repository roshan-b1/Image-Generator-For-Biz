from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

@app.route('/review-card')
def generate_image():
    name = request.args.get('name', 'Friend')

    # Create base image
    img = Image.new('RGB', (600, 300), color='white')
    draw = ImageDraw.Draw(img)

    # Load your font
    font = ImageFont.truetype("arial.ttf", 40)
    text = f"Hi {name}, thanks for choosing Prymeta!"
    draw.text((50, 130), text, fill='black', font=font)

    # Save to bytes
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

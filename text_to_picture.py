from PIL import Image, ImageDraw, ImageFont
import os






def add_text_to_image(text, image_title):
    path = '/home/gergo/Desktop/feedback_generator/static/picture_with_string/'
    os.system('rm -rf %s/*' % path)
    image = Image.open ('/home/gergo/Desktop/feedback_generator/rikárdo.jpg')
    font_type = ImageFont.truetype("/lato/Lato-LightItalic.ttf", 30)
    draw = ImageDraw.Draw(image)
    result = draw.text(xy=(50, 50), text=text , fill=(0, 0, 0), font=font_type)
    image.save('/home/gergo/Desktop/feedback_generator/static/picture_with_string/{}.jpg'.format(image_title))





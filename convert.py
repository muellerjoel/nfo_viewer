from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class NfoConverter:

    @staticmethod
    def text_to_image(text):
        courier_font = ImageFont.truetype("cour.ttf", 15)

        # Compute picture size
        margin_left = 20
        heigth = int(len(text.split('\n')) * 17.5)

        width = 0
        for line in text.split('\n'):
            line_width = courier_font.getlength(line)
            width = int(max(width, line_width))

        width+= margin_left

        print('width', width,'heigth',heigth)

        # Create picture
        img = Image.new('RGB', (width, heigth), color='white')
        d = ImageDraw.Draw(img)

        # for Line in text.split("\n"):
        # 	d.text((0, spacing), Line, fill = "white", font=arial_font)
        # 	spacing += 15

        d.multiline_text((margin_left, 20), text, fill='black', font=courier_font)

        return img

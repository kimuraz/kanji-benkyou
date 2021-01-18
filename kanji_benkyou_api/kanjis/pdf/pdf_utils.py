import fitz
import os

from django.conf import settings

from PIL import Image
from cairosvg import svg2png

template = '{}/kanjis/pdf/template.pdf'.format(settings.BASE_DIR)
template = os.path.join(settings.BASE_DIR, 'kanjis/pdf/template.pdf')

def generate_pdf(kanji_code):
    try:
        image_path = os.path.join(settings.BASE_DIR, 'kanjis/kanjivg/kanji/{}.svg'.format(kanji_code))
        img_rect = fitz.Rect(20, 27, 66, 75)

        file_handle = fitz.open(template)
        page = file_handle[0]

        png_path = os.path.join(settings.BASE_DIR, 'kanjis/pdf/tmp/{}.png'.format(kanji_code))
        svg2png(url=image_path, write_to=png_path)
        img = Image.open(png_path)
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        img.save(png_path)
        page.insertImage(img_rect, filename=png_path)
        page.setRotation(180)
        file_handle.save('{}/{}.pdf'.format(settings.MEDIA_ROOT, kanji_code))
        os.remove(png_path)
    except Exception as e:
        raise e

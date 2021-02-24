import fitz
import os

from django.conf import settings

from PIL import Image
from cairosvg import svg2png

template = '{}/kanjis/pdf/template.pdf'.format(settings.BASE_DIR)
font = '{}/kanjis/pdf/togoshi-mincho.ttf'.format(settings.BASE_DIR)
template = os.path.join(settings.BASE_DIR, 'kanjis/pdf/template.pdf')


def generate_pdf(kanji_code, kanji):
    try:
        file_handle = fitz.open(template)
        page = file_handle[0]
        page.clean_contents()
        image_path = os.path.join(
            settings.BASE_DIR, 'kanjis/kanjivg/kanji/{}.svg'.format(kanji_code))
        # x0, y0, x1, y1 - https://pymupdf.readthedocs.io/en/latest/rect.html#rect
        img_rect = fitz.Rect(page.rect.width - 67, 28,
                             page.rect.width - 20, 82)

        png_path = os.path.join(
            settings.BASE_DIR, 'kanjis/pdf/tmp/{}.png'.format(kanji_code))
        svg2png(url=image_path, write_to=png_path)
        page.insertImage(img_rect, filename=png_path)
        page.insertText((page.rect.width - 62, 18), 'JLPT' + str(kanji.jlpt) or '?')
        text_writer = fitz.TextWriter((0, 0, page.rect.width - 70, page.rect.height))
        text_writer.append(fitz.Point(20, 38), 'Kun: ' + ', '.join(kanji.kun_readings))
        text_writer.append(fitz.Point(20, 53), 'On: ' + ', '.join(kanji.on_readings))
        text_writer.append(fitz.Point(20, 68), 'Meanings: ' + ', '.join(kanji.meanings))
        text_writer.writeText(page)
        file_handle.save('{}/{}.pdf'.format(settings.MEDIA_ROOT, kanji_code), deflate=True)
        os.remove(png_path)
    except Exception as e:
        raise e

import fitz
from cairosvg import svg2png

template = './template.pdf'
image_path = './06728.svg'

img_rect = fitz.Rect(20, 27, 66, 75)

file_handle = fitz.open(template)
page = file_handle[0]

svg2png(url=image_path, write_to='/tmp/{}.png'.format(image_path.replace('.svg','')))

page.insertImage(img_rect, filename='/tmp/{}.png'.format(image_path.replace('.svg','')))

file_handle.saveIncr()

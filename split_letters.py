# Разбиваем общий набор символов на отдельные
from PIL import Image

alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
CELL_SIZE = 100
letters = Image.open('letters.png')

for y in range(3):
    ypos = CELL_SIZE * y
    for x in range(33):
        # print(f'{alphabet[x:x+1]}')
        xpos = CELL_SIZE * x
        box = (xpos, ypos, xpos + CELL_SIZE, ypos + CELL_SIZE)
        # Копируем область из первого изображения
        letter = letters.crop(box)
        letter.save(f'custom_emoji/{y}{alphabet[x:x+1]}.png')

# position = (0, 0)
# board.paste(region, position)
#
# board.show('board1')
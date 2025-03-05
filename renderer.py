from PIL import Image

# Открываем два изображения
cells = Image.open('pics\cells.png')
letters = Image.open('pics\letters.png')

# Получаем размеры первого изображения
# width1, height1 = image1.size

# Получаем размеры второго изображения
# width2, height2 = image2.size

# Создаем новое изображение с шириной, равной сумме ширин двух изображений,
# и высотой, равной максимальной высоте из двух изображений
# new_width = width1 + width2
# new_height = max(height1, height2)
new_image = Image.new('RGBA', (500, 600))

cell_blank = cells.crop((0, 0, 100, 100))
cell_gray = cells.crop((101, 0, 200, 100))
cell_green = cells.crop((201, 0, 300, 100))
# Вставляем первое изображение
new_image.paste(cell_blank, (0, 0))
new_image.paste(cell_gray, (100, 0))

# Вставляем второе изображение, начиная с позиции, равной ширине первого
# new_image.paste(image2, (width1, 0))

# Сохраняем результат в файл
new_image.save('board.png')
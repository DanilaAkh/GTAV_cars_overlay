import sqlite3
import math  # Используется для точного расчета корней и площадей
from tkinter import *
from PIL import Image, ImageTk, ImageOps
from io import BytesIO
from mss import MSS

# 1. Расчет геометрии (Окно = 1/50 площади экрана, пропорции всегда 16:9)
with MSS() as sct:
    monitor_info = sct.monitors[0]
    screen_w = monitor_info['width']
    screen_h = monitor_info['height']
    
    # Полная площадь текущего экрана
    screen_area = screen_w * screen_h
    
    # Целевая площадь окна (1/50 от площади экрана)
    target_area = screen_area / 50
    
    # Вычисляем размеры для соотношения сторон 16:9 исходя из target_area
    root_h = int(math.sqrt((target_area * 9) / 16))
    root_w = int(root_h * (16 / 9))

# Координаты появления окна на экране
pos_x = int(screen_w/7)
pos_y = int(screen_h/9)

# 2. Инициализация главного окна и базы данных
conn = sqlite3.connect('gtav_cars.db')
root = Tk()
root.title("Yo callin 4 some wheels")

# Устанавливаем геометрию: окно ВСЕГДА будет 16:9 с площадью 1/50 экрана
root.geometry(f"{root_w}x{root_h}+{pos_x}+{pos_y}")
root.wm_attributes("-topmost", True)
root.overrideredirect(True)

# Создаем один постоянный Label, растянутый на все окно
image_label = Label(root)
image_label.pack(fill=BOTH, expand=True)

def show(data):
    """Пропорционально вписывает картинку в окно 16:9."""
    img_byte = BytesIO(data)
    original_img = Image.open(img_byte)
    
    # Целевой размер строго равен вычисленным размерам окна root
    target_size = (root_w, root_h)
    
    # Сжимаем/растягиваем картинку под размер окна с сохранением пропорций авто
    resized_img = ImageOps.contain(original_img, target_size)
    
    # Конвертируем для Tkinter и обновляем существующий Label
    img = ImageTk.PhotoImage(resized_img)
    image_label.config(image=img)
    root.image = img  # Сохраняем ссылку от удаления мусором

def fetch(car):
    with conn:
        c = conn.cursor()
        name = car # Any id
        c.execute('SELECT photo FROM cars where name=?',(name,))
        data = c.fetchall()[0][0] # Получаем blob-данные
    show(data) # Вызываем функцию с переданными данными

# Сигнатура и внутренности функции сохранены в исходном виде
def show_img(car):
    fetch(car)
    root.mainloop()
# if __name__ == "__main__":
#     # Тестовый вызов
#     show_img("Infernus")

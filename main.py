import cv2
import keyboard
import numpy as np
from easyocr import Reader
from mss import MSS
import time


def select_row(img: np.array) -> np.array:
    """
    Функция поиска наиболее "яркой" строки.

    Parameters
    ----------
    img : матрица np.array с изображением

    Returns
    -------
    crop : матрица np.array с наиболее яркой строкой
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite("gray_img.png", gray)

    # Средняя яркость каждой строки
    row_mean = gray.mean(axis=1)

    # Строка с максимальной яркостью
    y = np.argmax(row_mean)

    # Высота пункта меню
    item_height = 32

    crop = img[
        y: y + item_height,     # высота
        10:370                  # ширина
    ]
    # cv2.imwrite("selected_row.png", crop)
    return crop


stop_flag = False

def stop_script():
    global stop_flag
    stop_flag = True

# Регистрируем горячую клавишу (например, Ctrl+Q)
keyboard.add_hotkey('ctrl+q', stop_script)
reader = Reader(['en'], gpu=False)

# Основной цикл программы
with MSS() as sct:
    monitor = {"top": 0, "left": 0, "width": 400, "height": 500}
    while not stop_flag:

        screenshot = sct.grab(monitor)          # Возвращает формат (400, 400, 4) BGRA
        crop = np.array(screenshot)[:, :, :3]   # Избавляемся от BGRA, делаем (400, 400, 3)        
        crop = select_row(crop)
        result = reader.readtext(crop)

        # проверка, что текст был найден:
        if len(result) == 0:
            print("К сожалению, текст не был найден")
        else:
            print(result[0][1])
            
        time.sleep(1)
        
    print("Остановлено по Ctrl+Q")
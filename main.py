import time
import cv2
import keyboard
import numpy as np
from easyocr import Reader
from mss import MSS

from utils import process_image
from show_img import show_img
# Глобальный флаг остановки
stop_flag = False


def stop_script():
    """Обработчик горячей клавиши."""
    global stop_flag
    stop_flag = True


def main():
    global stop_flag

    keyboard.add_hotkey("ctrl+q", stop_script)

    reader = Reader(["en"], gpu=False)


    print("Скрипт запущен. Для остановки нажмите Ctrl+Q.")

    with MSS() as sct:
        monitor = sct.monitors[1]
        width = monitor['width']
        height = monitor['height']
        monitor = {
            "top": 0,
            "left": 0,
            "width": int(width * 1/3),
            "height": int(height * 1/2)
        }
        while not stop_flag:
            screenshot = sct.grab(monitor)

            # BGRA -> BGR
            image = np.array(screenshot)[:, :, :3]

            # cv2.imwrite("menu_image.png", image)

            car = process_image(reader, image)
            
            show_img(car)

            time.sleep(1)

    print("Остановлено по Ctrl+Q")


if __name__ == "__main__":
    main()
import time

import keyboard
import numpy as np
from easyocr import Reader
from mss import MSS

from utils import process_image

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

    monitor = {
        "top": 0,
        "left": 0,
        "width": 1000,
        "height": 1000,
    }

    print("Скрипт запущен. Для остановки нажмите Ctrl+Q.")

    with MSS() as sct:
        while not stop_flag:
            screenshot = sct.grab(monitor)

            # BGRA -> BGR
            image = np.array(screenshot)[:, :, :3]

            # cv2.imwrite("menu_image.png", image)

            process_image(reader, image)

            time.sleep(1)

    print("Остановлено по Ctrl+Q")


if __name__ == "__main__":
    main()
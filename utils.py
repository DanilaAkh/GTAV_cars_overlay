import numpy as np
import cv2
from easyocr import Reader


def select_row(img: np.ndarray) -> np.ndarray:
    """
    Функция поиска наиболее "яркой" строки

    Parameters
    ----------
    img : матрица np.array с изображением

    Returns
    -------
    crop : матрица np.array с наиболее яркой строкой
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite("gray_img.png", gray)

    row_mean = gray.mean(axis=1)
    
    # Строки, яркость которых близка к максимальной
    threshold = row_mean.max() * 0.95   # 95% от максимума
    mask = row_mean >= threshold

    # Индексы этих строк
    rows = np.where(mask)[0]

    # Центр яркой области
    y = int(rows.mean())

    # Высота пункта меню
    item_height = 35

    crop = img[
        y - item_height: y + item_height,       # высота
        20:500                                  # ширина
    ]
    # cv2.imwrite("selected_row.png", crop)
    return crop


def process_image(reader: Reader, image: np.ndarray) -> None:
    """
    Обрабатывает изображение и выводит распознанный текст.
    """
    crop = select_row(image)
    result = reader.readtext(crop)

    if not result:
        print("Текст не был найден")
    else:
        print(result[0][1])
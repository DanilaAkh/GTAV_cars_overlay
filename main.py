import cv2
import numpy as np
import easyocr


def select_row(img_name: str) -> np.array:
    """
    Функция поиска наиболее "яркой" строки.
    
    Parameters
    ----------
    img_name : строка с именем изображения

    Returns
    -------
    crop : матрица np.Array с индексами изображения
    """
    img = cv2.imread(img_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Средняя яркость каждой строки
    row_mean = gray.mean(axis=1)

    # Строка с максимальной яркостью
    y = np.argmax(row_mean)

    # Высота пункта меню
    item_height = 32

    crop = img[
        y - item_height : y,
        20:370 
    ]
    # cv2.imwrite("selected_row.png", crop)
    return crop


reader = easyocr.Reader(['en'], gpu=False)
img_name = "menu.png"
crop = select_row(img_name)
result = reader.readtext(crop)
print(result[0][1])
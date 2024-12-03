"""
Написать скрипт на Python с использованием библиотеки pyautogui, который:
- Открывает приложение "Калькулятор" на вашем компьютере (Windows, macOS, или Linux).
Использовать os.system или другой способ.
- Выполняет автоматизированные действия, чтобы сложить два числа (12 + 7).
Использовать pyautogui для эмуляции кликов по кнопкам "1", "2", "+", "7", "=" в интерфейсе калькулятора.
Для поиска кнопок необходимо использовать функцию locateOnScreen из пакета pyautogui
(обязательно использовать confidence чтобы нивелировать мелкие пиксельные неточности: confidence=0.9)
"""

# pip install pyautogui
# pip install opencv-python


import os
import pyautogui as pag


# Открытие приложения "Калькулятор"
def open_calculator():
    """
    Открывает калькулятор в зависимости от операционной системы.
    """
    platform = os.name  # Получение имени операционной системы
    if platform == "nt":  # Windows
        os.system("start calc")
    elif platform == "posix":  # macOS/Linux
        os.system("open -a Calculator")
    else:
        raise OSError("Операционная система не поддерживается.")
    pag.sleep(2)  # Ожидание открытия приложения


# Поиск кнопки на экране
def click_button(button_path):
    """
    Ищет кнопку на экране с помощью pyautogui.locateOnScreen и кликает по ней.
    :param button_path: Путь к изображению кнопки.
    """
    try:
        # Поиск изображения на экране
        button_location = pag.locateOnScreen(button_path, confidence=0.9)
        if button_location:
            # Получение центра кнопки и клик
            button_center = pag.center(button_location)
            pag.click(button_center)
        else:
            raise FileNotFoundError(f"Кнопка '{button_path}' не найдена на экране.")
    except Exception as e:
        print(f"Ошибка при поиске кнопки {button_path}: {e}")


# Основной процесс автоматизации
def main():
    # Шаг 1: Открытие приложения калькулятора
    open_calculator()

    # Шаг 2: Выполнение арифметической операции (12 + 7)
    # Словарь с путями к изображениям кнопок
    button_images = {
        '1': 'buttons/one.png',
        '2': 'buttons/two.png',
        '+': 'buttons/plus.png',
        '7': 'buttons/seven.png',
        '=': 'buttons/equals.png'
    }

    # Последовательность нажатий
    for button in ['1', '2', '+', '7', '=']:
        click_button(button_images[button])
        pag.sleep(.5)  # Пауза между действиями для стабильности


if __name__ == "__main__":
    main()

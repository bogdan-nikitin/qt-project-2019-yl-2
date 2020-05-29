import os


PROJECT_FOLDER = 'Exchange Rate Graphics'
UIS_FOLDER_NAME = 'UIs'


def get_directory():
    """Получение текущей директории"""
    # Раннее метод менялся из-за того, что программа расположена в другом
    # месте. Теперь же он дублирует функцию os.getcwd(). Но эта функция
    # используется в большей части программы, так что заменять её не стоит.
    # при будущей разработке это пригодится
    return os.getcwd()


def get_ui_directory(ui_name):
    """Получение директории с файлом UI"""
    # Было нужно на этапе разработки, когда все UI конвертировались через uic во
    # время работы программы. Теперь же все файлы UI сконвертированы в файлы .py
    # Но функция может пригодиться при дальнейшей разработке
    cwd = os.getcwd().split('\\')[:-1]
    if PROJECT_FOLDER not in cwd:
        cwd += [PROJECT_FOLDER]
    return '/'.join(cwd + [UIS_FOLDER_NAME, ui_name])

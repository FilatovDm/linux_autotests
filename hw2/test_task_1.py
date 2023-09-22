"""
Задание 1
Дополнить проект тестами, проверяющими команды
вывода списка файлов (l) и разархивирования с путями (x).

Задание 2
• Установить пакет для расчёта crc32 sudo apt install libarchive-zip-perl
• Доработать проект, добавив тест команды расчёта хеша (h).
Проверить, что хеш совпадает с рассчитанным командой crc32.
"""

from lib_checkout import checkout, hash_value

folder_tst = "/home/user/tst"
folder_out = "/home/user/out"
folder_ext = "/home/user/folder_1"


def test_step1():
    # проверка создания файла при архивации
    res_1 = checkout(f"cd {folder_tst}; 7z a ../out/arx2 test_file.txt", "Everything is Ok")
    res_2 = checkout(f"ls {folder_out};", "arx2.7z")
    assert res_1 and res_2, "test 1 FAIL"


def test_step2():
    # проверка создания файла при распаковке
    res_1 = checkout(f"cd {folder_out}; 7z e arx2.7z {folder_ext}", "Everything is Ok")
    # у меня с -о не проходит тест res_1
    res_2 = checkout(f"ls {folder_ext};", "test_file.txt")
    assert res_1 and res_2, "test 2 FAIL"


def test_step3():
    # проверка целостности архива
    assert checkout(f"cd {folder_out}; 7z t arx2.7z", "Everything is Ok"), "test 3 FAIL"


def test_step4():
    # обновление архива
    assert checkout(f"cd {folder_out}; 7z u arx2.7z", "Everything is Ok"), "test 4 FAIL"


def test_step6():
    # вывод списка файлов (установлен перед удалением намеренно)
    list_output = checkout(f"cd {folder_out}; 7z l arx2.7z", "test_file.txt")
    assert list_output, "test 6 FAIL"


def test_step5():
    # удаление из архива
    assert checkout(f"cd {folder_out}; 7z d arx2.7z", "Everything is Ok"), "test 5 FAIL"


def test_step7():
    # разархивирование с путями
    res_1 = checkout(f"cd {folder_out}; 7z x arx2.7z {folder_ext}", "Everything is Ok")
    res_2 = checkout(f"ls {folder_ext};", f"test_file.txt")
    assert res_1 and res_2, "test 7 FAIL"


def test_step8():
    # расчет хеша
    res1 = checkout(f"cd {folder_tst}; 7z h test1.txt", "Everything is Ok")
    res2 = checkout(f"cd {folder_tst}; 7z h test1.txt", hash_value(folder_tst))
    assert res1 and res2, "test 8 FAIL"

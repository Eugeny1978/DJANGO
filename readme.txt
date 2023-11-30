Чтобы Запустить Джанго
1. Необходимо перейти из головной папки DJANGO в папку проекта
Например: site_interface :
действие: (djvenv) F:\! PYTON\PyCharm\DJANGO>cd site_interface
результат: (djvenv) F:\! PYTON\PyCharm\DJANGO\cd site_interface\

2. Набрать команду
django-admin startprogect site_interface 4000 (4000 - если не хотим 8000 порт)
действие: (djvenv) F:\! PYTON\PyCharm\DJANGO\cd site_interface\ django-admin startproject site_interface
результат:
(djvenv) F:\! PYTON\PyCharm\DJANGO>pip list
Package    Version
---------- -------
asgiref    3.7.2
Django     4.2.7
pip        23.3.1
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
Run 'python manage.py migrate' to apply them.
November 30, 2023 - 18:17:57
Django version 4.2.7, using settings 'site_interface.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[30/Nov/2023 18:18:22] "GET / HTTP/1.1" 200 10664
Not Found: /favicon.ico
[30/Nov/2023 18:18:23] "GET /favicon.ico HTTP/1.1" 404 2118
-------------------------------------
Для формирования НОвого приложения в проекте:
python manage.py startapp <имя приложения>
Создастся Каталог с файлами

Запуск Приложения
python manage.py runserver
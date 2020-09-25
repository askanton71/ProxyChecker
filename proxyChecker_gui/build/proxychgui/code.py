import requests  # импорт нужной библиотеки
prxtype = input("Proxy type: ")  # спрашиваем тип прокси
PROXY = input("Input proxy: ")  # спрашиваем адрес и порт
user = input("Input user: ")  # спрашиваем имя(если нет оставляем пустым)
passwd = input("Input password: ")  # спрашиваем пароль(если нет оставляем пустым)

try:
    if len(user) > 0:  # проверяем есть ли у прокси проверка имени\пароля
        proxies = {
            'https': prxtype + '://' + user + ":" + passwd + "@" + str(PROXY)  # собираем прокси
        }
    else:  # если прокси без имени\пароля
        proxies = {
            'https': prxtype + '://' + str(PROXY)  # собираем прокси
        }
    s = requests.Session()  # создаем сесиию
    s.proxies = proxies  # привязываем собранный прокси
    print(proxies)  # выводим собранный прокси в консоль
    r = s.get('https://www.google.com/humans.txt')  # пытаемся получить доступ к адресу через собранный прокси
    print(r.text[0:20] + "...")  # выводим первые 20 символов
    print("Proxy " + str(PROXY) + " OK")  # подтверждаем что прокси работает
except Exception as e:  # в случае ошибки
    print(e)  # печатаем ошибку в консоль
    print("Proxy " + str(PROXY) + " not OK")  # подтверждаем что проски не работает
    pass
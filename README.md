# Logging-Sentry

Необходимо написать простой веб-сервер с помощью фреймворка Bottle. Все ошибки приложения должны попадать в вашу информационную панель Sentry. Приложение должно размещаться на Heroku, иметь минимум два маршрута:
1. /success, который должен возвращать как минимум HTTP ответ со статусом 200 OK
2. /fail, который должен возвращать "ошибку сервера" (на стороне Bottle это может быть просто RuntimeError), то есть HTTP ответ со статусом 500

Для локального тестирования

1. Из папки с файлами пишем команду python server.py

2. Переходим по ссылкам:
http://localhost:8080/
http://localhost:8080/success
http://localhost:8080/fail

Для проверки сайта на Heroku:

1. https://still-escarpment-90121.herokuapp.com

2. https://still-escarpment-90121.herokuapp.com/success

3. https://still-escarpment-90121.herokuapp.com/fail

Write a simple web server using the Bottle framework. All application errors should go to your Sentry dashboard. The application must be hosted on Heroku and have at least two routes:
1. / success, which should return at least an HTTP response with a 200 OK status
2. / fail, which should return a "server error" (on the Bottle side it could just be a RuntimeError), that is, an HTTP response with a 500 status

For local testing

1. From the folder with files, write the command python server.py

2. Follow the links:
http: // localhost: 8080 /
http: // localhost: 8080 / success
http: // localhost: 8080 / fail

To test a site on Heroku:

1.https://still-escarpment-90121.herokuapp.com

2.https://still-escarpment-90121.herokuapp.com/success

3.https://still-escarpment-90121.herokuapp.com/fail

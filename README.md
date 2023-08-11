# Doomscroll

<img src="https://github.com/Forwall100/doomscroll/assets/78537089/0ac0e15d-a186-4dd3-9dc2-41502a310ff5" alt="drawing" width="200"/>
Это веб-приложение, которое агрегирует RSS-каналы по категориям и отображает случайные краткие содержания статей. 

# Demo
https://github.com/Forwall100/doomscroll/assets/78537089/53c6a698-85c3-4244-bd08-d985ef60e250

## Функции

- Получение и разбор RSS-каналов из настраиваемых источников 
- Категоризация лент по темам
- Отображение заголовка, ключевых слов, изображения и краткого содержания случайной статьи из выбранной категории
- Нажатие на кнопку для сокращения статьи с помощью GPT модели 

## Как это работает

Бэкенд построен с использованием [FastAPI](https://fastapi.tiangolo.com/) и получает доступ к RSS-каналам с помощью библиотеки [Feedparser](https://github.com/kurtmckee/feedparser). 

Название, изображение, ключевые слова и краткое содержание статей извлекаются с помощью библиотеки [newspaper3k](https://newspaper.readthedocs.io/en/latest/).

Доступ к GPT модели предоставлен проектом [gpt4free](https://github.com/xtekky/gpt4free) и библиотекой [g4f](https://pypi.org/project/g4f/)

Для отображения контента во фронтенде используется [Vue.js](https://vuejs.org/).

Источники RSS и категории настраиваются в файле `feed.json`.

## Запуск локально

1. Клонировать репозиторий
2. `cd frontend`
3. `npm i`
4. Запустите фронтенд командой `npm run dev`
5. `cd ../backend`
6. Установить зависимости с помощью `pip install -r requirements.txt`. 
7. Запустите сервер с помощью команды `python main.py`.
8. Swagger доступен по адресу localhost:8000/docs в браузере, само приложение доступно по адресу localhost:5173


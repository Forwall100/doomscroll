# Doomscroll
![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vue.js&logoColor=4FC08D)
![](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

<img src="https://i.imgur.com/7mcuVg3.png" alt="drawing" width="700"/>

Это веб-приложение, которое агрегирует RSS-каналы по категориям и отображает случайные краткие содержания статей. 

## 🎥 Demo


https://github.com/Forwall100/doomscroll/assets/78537089/df62a6b6-8054-4cc5-9c52-77eb91848338



## ⚙️ Функции

- Получение и разбор RSS-каналов из настраиваемых источников 
- Категоризация лент по темам
- Отображение заголовка, ключевых слов, изображения и краткого содержания случайной статьи из выбранной категории
- Нажатие на кнопку для сокращения статьи с помощью GPT модели 

## 🛠️ Как это работает

Бэкенд построен с использованием [FastAPI](https://fastapi.tiangolo.com/) и получает доступ к RSS-каналам с помощью библиотеки [Feedparser](https://github.com/kurtmckee/feedparser). 

Название, изображение, ключевые слова и краткое содержание статей извлекаются с помощью библиотеки [newspaper3k](https://newspaper.readthedocs.io/en/latest/).

Доступ к GPT модели предоставлен проектом [gpt4free](https://github.com/xtekky/gpt4free) и библиотекой [g4f](https://pypi.org/project/g4f/)

На фронтенде используется [Vue.js](https://vuejs.org/) и [Tailwind css](https://tailwindcss.com/).

Источники RSS и категории настраиваются в файле `feed.json`.

## 🚀 Запуск локально

1. Клонировать репозиторий
2. `cd doomscroll/frontend`
3. `npm i`
4. Запустите фронтенд командой `npm run dev`
5. `cd ../backend`
6. Установить зависимости с помощью `pip install -r requirements.txt`. 
7. Запустите сервер с помощью команды `python main.py`.
8. Swagger доступен по адресу localhost:8000/docs в браузере, само приложение доступно по адресу localhost:5173

## TODO
- [X] Добавить суммаризацию с помощью GPT
- [ ] Сделать адаптивную верстку под телефоны
- [ ] Настроить docker compose для автоматического деплоя
- [ ] Реализовать добавление и удаление категорий и источников в интерфейсе
- [ ] Исправить баг с .parse()
- [ ] Добавить пролистывание новостей не только вперед, но и назад

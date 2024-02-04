## QRKot
QRKot - API для Благотворительного фонда.

### Возможности сервиса
 - Регистрация пользователей
 - Добавление благотворительных проектов и пожертвований
 - Распределение проектов и пожертвований по открытым проектам
 - Формирование отчета в гугл-таблице, которая содержит информацию о закрытых проектах, отсортированных по скорости сбора средств — от тех, что закрылись быстрее всего, до тех, что долго собирали нужную сумму.

### Документация проекта:
Redoc:
```
http://127.0.0.1:8000/redoc
```
Swagger:
```
http://127.0.0.1:8000/docs
```

## Установка
Для установки необходимо клонировать репозиторий и создать виртуальное окружение
```
git clone git@github.com:FroSDD/cat_charity_fund.git
```
```
python - m venv venv
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Сгенерировать файл настроек окружения и заполнить его согласно примеру:
```
APP_TITLE=Благотворительный фонд для котиков
APP_DESCRIPTION=API для котиков
DATABASE_URL='sqlite+aiosqlite:///./<название дб>.db'
SECRET=секретное слово
FIRST_SUPERUSER_EMAIL=почта суперпользователя
FIRST_SUPERUSER_PASSWORD=пароль суперпользователя
TYPE = service_account
PROJECT_ID = ID проекта
PRIVATE_KEY_ID = ID приватного ключа
PRIVATE_KEY = приватный ключ
CLIENT_EMAIL = почта сервисного аккаунта
CLIENT_ID = ID сервисного аккаунта
AUTH_URI = https://accounts.google.com/o/oauth2/auth
TOKEN_URI = https://oauth2.googleapis.com/token
AUTH_PROVIDER_X509_CERT_URL = https://www.googleapis.com/oauth2/v1/certs
CLIENT_X509_CERT_URL = URL
EMAIL = почта пользователя google sheets
```
Затем применить миграции для создания базы SQLite:
```
alembic upgrade head
```
Запустить проект:
```
uvicorn app.main:app
```

### Использованные технологии:
- Python
- SQLAlchemy
- FastAPI
- Pydantic
- Alembic
- Asyncio
- Google Sheets

### Развернутый проект: 
http://127.0.0.1:8000

### Автор: 
[Anton Novikov](https://github.com/FroSDD/)

E-mail: novikov.an_v@mail.ru


# APP
- Статус "`flow/models_views/status.py`"; 
- Тип "`flow/models_views/types.py`"; 
- **Категория и подкатегория**:
  - "`flow/models_views/categories.py`";
  - "`flow/models_views/subcategories.py`".

- Комментарий & Сумма & Дата создания и Дата обновления записи:
  - "`flow/models_views/content_flow.py`".
  

>>Пользователь не может выбрать подкатегорию, если она не связана с выбранной категорией.

Создаём *подкатегорию*, затем создаём *категорию* и закрепляем *подкатегории*. 

----
## Commands

```
py manage.py collectstatic
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
daphne project.asgi:application # mode: develop & poduction 
git log --all --oneline --graph --decorate --date=format:'%Y-%m-%d %H:%M:%S' --pretty=format:'%C(yellow)%h%C(auto)%d %C(white)%cd%Creset %s' # история развития проекта
```

### Note:
"`py manage.py collectstatic --clear --noinput`" Запускать после каждого измения статик файлов.
*"`--clear`"* - удаляет старые файлы. *"`--noinput`"* - если не хотите время тратить на комментарии после запуска команды. \
- "`makemigrations`" создать файлы миграции в db;
- "`migrate`" - изменить структуру базы данных;
- "`runserver`" - запускаем локальный сервер "`daphne`" для разработки.   

----
## URL локальный
* "`admin/`"; Старая версия
* "`cms/`"; Новая версия
* "`swagger/`";
* "`redoc/`";
* "`swagger<format>/`".

## DB
|Flow| db                      |
|:---|:------------------------|
|![db_flows](img/db_flows.png)| ![db_flows](img/db.png) |




## Админ-панель от Django
### Admin
![admin](img/admin.png)

### Category

![Category](img/category.png)\
Где можно выбрать  N-ое количество под-категорий на одну категорию.



# Subcategories
![Category](img/subcategories.png)

### Status
![Category](img/statuses.png)

### Type
![Category](img/type.png)

### Data Flow
![Category](img/flow.png) \
![Categor](img/flow_content.png) 

### Search
![Search](img/search.png) 

### Filter

||                              |
|:----|:-----------------------------|
|![filter](img/filter1.png) | ![filter](img/filter2.png)   |

## Админ-панель новая
### Форма входа
![Login](./img/admin_dor.png)

### Админ-панель
![db_panel](./img/new_db.png)

### Админ-панель Категория
![category_new](./img/category_new.png)

### Админ-панель Подкатегории
![subcategory](./img/subcategory.png)

### Админ-панель Статусы
![status](./img/status.png)

### Админ-панель Типы
![type_new](./img/type_new.png)

### Админ-панель Flow - Записи
![flow_new](./img/flow_new.png)


### Филтры & Поиск
![services](./img/services.png)

### swagger
![swagger](img/swagger.png)
#### Redoc
![swagger](img/redoc.png)

## Дерево проекта

```text
Имя
├──.git/
├──.github/
│   |   └──workflows/*
│   │   │   └──*.yml
├──admins/
│   └──filters.py
├──bundles/
│   └──webpack-stats.json	
├──collectstatic/
├──flow/
│   ├──flow_api/ 
│   │   └──*.py
│   ├──migrations/
│   │   └──*.py 
│   ├──models_views/
│   │   └──*.py 
│   └──*.py
├──img/
│   └──*.png
├──nginx/
│   ├──.dockerignore
│   ├──default.conf
│   └──Dockerfile
├──person/
│   ├──migrations/
│   └──*.py
├──project/
│   └──*.py
├──static/
│   ├──scripts/
│   |   └──*.js
│   ├──styles/
│   |   └──*.css
├──templates/
|   └──*.html
├──.browserslistrc
├──.dockerignore
├──.editorconfig
├──.env
├──.flake8
├──.gitignore
├──.pre-commit-config.yaml
├──.pylintrc
├──docker-compose.yml
├──Dockerfile
├──logs.py
├──manage.py
├──pyproject.toml
├──pytest.ini
├──README.md
├──requirements.txt
├──truckdriver_db.sqlite3	
```
## .ENV
```text
PYTHONPATH=E:\OpenServer\domains\t-Py-Dj-financial\backend 
SECRET_KEY_DJ= < secret_key_your_django >
DJANGO_SETTINGS_MODULE=project.settings

# app
APP_PROTOCOL=http
APP_HOST=127.0.0.1
APP_HOST_REMOTE= < host_from_remote_server >
APP_PORT=8000
APP_TIME_ZONE=Asia/Krasnoyarsk

# db
POSTGRES_DB= < db_name>
POSTGRES_USER= < user_name_for_db>
POSTGRES_HOST=< host_for_db >

POSTGRES_PORT=< port_db_>
POSTGRES_PASSWORD= < password_from_db >
DB_ENGINE=django.db.backends.postgresql

# для разработки
DATABASE_ENGINE_LOCAL=django.db.backends.sqlite3
DATABASE_LOCAL=truckdriver_db.sqlite3 
```
|                      |                               |                           |
|:---------------------|:------------------------------|:--------------------------|
| async "`Django`"           |      "`wagtail`"                | "`PostgreSQL` or "`ASQLite`" |
| "`daphne`"           |         "`channels`"            |     "`djangorestframework`"            |
| [swagger](./swagger) | [nginx](./nginx/default.conf) |[docker-compose](./docker-compose.yml)   |
| "`asincio`"              | "`adrf`" | "`psycopg2`"|


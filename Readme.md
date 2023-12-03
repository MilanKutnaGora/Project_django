---Задание 19.2---

Создание приложения Django

**django-admin startproject config .**
**python manage.py startapp main**
Настраиваем параметры запуска сервера или python manage.py runserver
Заносим в config/settings название нашего приложения 'catalog' в INSTALLED_APPS
В папке catalog создаем папку templates, в templates создаем папку с названием приложения 'catalog', 
В папке catalog создаем 2 файла contacts.html и home.html- шаблоны
Создаем контроллер в 'views' - просто функцию с аргументом request. 
Делаем return render('', 'catalog/index.html')
Создаем урл в приложение catalog urlpatterns = [path('', index)]
Находим точку входа в settings для связывания урлов - ROOT_URLCONF = 'config.urls'
Связываем через include - добавляем в config/urls еще один паттерн path('', include('catalog.urls'))

***Настройка ввода (POST)

Прописываем в index.html защиту ВАЖНО! {% csrf_token %}, и формы ввода
В контроллере прописываем логику if request.method == "POST": name = request.POST.get('name') и тд.

---Задание 20.1---

ORM

Настройка подключения к БД

Устанавливаем psycopg2

Прописываем в settings.py параметры БД: 'ENGINE': '...postgresql', 'NAME': 'db_name', 'USER': 'postgres', 'PASSWORD': 'secret', 'HOST': '127.0.0.1', - Необязательно, если сервер локальный 'PORT': 5432 - Необязательно, если сервер локальный

В консоли подключаемся к БД: "psql -U postgres", создаем БД db_name: "create database <dm_name>;"

Создание моделей и миграции

Перед соданием моделей делаем миграцию "python manage.py migrate"
Устанавливаем Pillow (если планируем работать с медиафалами - видео, картинками, фото и тд.)
В models.py пишем модели (класс), наследуемся от models.Model (models импорт из django.db). 
Прописываем поля в формате name = models.CharField(max_length=..., verbose_name='...') /
image = models.ImageField(upload_to='<directory_name>/', verbose_name='...', **NULLABLE), где NULLABLE = {'blank': True, 'null': True} в самом начале. Далее str, class Meta внутри нашей модели - в классе verbose_name = "название модели", verbose_name_plural = "название модели в множ. числе", ordering = ('<название поля>',) - упорядочивание в отображении по умолчанию (например по алфавиту и тд)
Создаем и выполняем миграцию "python manage.py makemigrations". В определенных случаях необходимо указывать название приложения "python manage.py makemigrations <app_name>". Далее "python manage.py migrate". В migrations можно увидеть созданный уникальный 'id' модели.
Далее в папке приложения создаем директорию media и в самом конце settings.py прописываем пути для сохранения медиа: MEDIA_URL = '/media/' и MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
В урлах config после списка паттернов прописываем: if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) (settings - импортируем СТРОГО!!! from django.conf import settings; static - импортируем СТРОГО!!! from django.conf.urls.static import static)

Админка

"python manage.py createsuperuser" - создаем суперпользователя (себя) - Имя, почта пароль и тд. Для отображения русского языка админки можно в settings.py сделать LANGUAGE_CODE = "ru-ru"
Зайти в админ панель можно добавив в конце адресной строки /admin
В admin.py регистрируем модель: @admin.register(<Model_name>) class <Model_name>Admin(admin.ModelAdmin): list_display = ('<первое_поле>', '<второе поле>',) - структурированное отображение, название столбцов берется из verbose_name для конкретного поля из моделей list_filter = ('<произвольное поле>',) - добавление возможности фильтрации search_fields = ('<первое_поле>', '<второе_поле>',) - возможности поиска без учета регистра В админ панеле при добавлении позиции необходимо заполнить поля, которые были прописаны при создании модели. А структурированное отображение в списке, осуществляется в виде str, прописанного в моделях.

Наполнение БД Shell

Для удобства отображения можем установить ipython
Запускаем инструмент "python manage.py shell"
В консоли shell для работы с моделью загружаем её "from <app_name>.models import <model_name>"
Работа с данными выстроена так: <Model_name>.objects.all(), где objects менеджер моделей для использования методов all, filter, get и тд. Другие варианты получения инф из базы данных: <model_name>.objects.get(pk=1) (в конце можно добавить ._ dict _ для удобства отображения), <Model_name>.objects.filter(<название_поля> = <значение поля>), <Model_name>.objects.exclude(<название_поля> = <значение поля>) - исключение, и т.д. При указании нескольких условий фильтрации или исключения, всегда под капотом используется оператор AND

Фикстуры

dumpdata - сохранение данных из текущей БД. "python manage.py dumpdata > data.json". ВАЖНО - следить за кодировкой, бывает сохраняется коряво кириллица. Когда приложений много необходимо указать наименование "python manage.py dumpdata <app_name> > data.json"
loaddata - загрузка данных в текущую БД. Все тоже самое - "python manage.py loaddata <app_name> data.json" Если, например, pk не уникальный - будет добавляться новая запись в БД каждый раз при loaddata

Кастомные команды

Создаем ПАКЕТ management в папке приложения
В management создаем ПАКЕТ commands
В commands создаем файл .py с нзванием, по которому будем вызывать команду в формате: from django.core.management import BaseCommand - базовый обязательный класс
class Command(BaseCommand): def handle(self, *args, **options): print('Hi, Sky!')

Наполнение БД

Используем class Command(BaseCommand):
def handle(self, *args, **options): тут прописываем исходный список словарей (<model_name>_list = [{},{},{}]) с ключами - названия полей, значениями - что ходим добавить.
Создаем пустой список для заполнения <model_name>_for_create = [] и прописываем цикл for <model_name>_item in <model_name>_list:
В цикле пишем <model_name>_for_create.append(<Model_name>(**<model_name>_item))
Вне цикла пишем <Model_name>.objects.bulk_create(<model_name>_for_create)


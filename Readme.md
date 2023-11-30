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
В admin.py регистрируем модель "admin.site.register(<model_name>)". Другой вариант: @admin.register(<Model_name>) class <Model_name>Admin(admin.ModelAdmin): list_display = ('<первое_поле>', '<второе поле>',) - структурированное отображение, название столбцов берется из verbose_name для конкретного поля из моделей list_filter = ('<произвольное поле>',) - добавление возможности фильтрации search_fields = ('<первое_поле>', '<второе_поле>',) - возможности поиска без учета регистра В админ панеле при добавлении позиции необходимо заполнить поля, которые были прописаны при создании модели. А структурированное отображение в списке, осуществляется в виде str, прописанного в моделях.
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
---20.2---

Статика

Создаем папку static в корневой папке приложения, в папке static создаем 2е директории css и js.
Проверяем чтобы в settings была настройка обращения к папке static: STATIC_URL = 'static/' STATICFILES_DIRS = {BASEDIR / 'static',}
Скачиваем архив со стилями с источника (например bootstrap). Размещаем js и css файлы в соответствующие папки в static
В html файле страницы ПЕРВОЙ строкой подгружаем статику {% load static %}. Заменяяем ВСЕ ссылки на статику на формат href="{% static 'scc/bootstrap.min.css' %}" (Тут при перезагрузке сервера, в консоли будут подсказки FileNotFound Error и указана строка в html, где не подтягивается статика - просто везде по порядку корректируем href.
Шаблоны

Для применения шаблонизации, например в index.html - необходимо в контроллере index определить исходные данные для тегов.
Работа со списком выстроена так: в контроллер index прописываем <model_name>s_list = <Model_name>.objects.all(). Таким образом мы суда подгружаем исходные данные для работы. Лучше всегда подгружать all() данные, и применять фильтры в html
На след строке создаем словарь context = {'objects_list': <model_name>s_list}. Тут 'objects_list' - тот самый список, к которому мы будем обращаться в шаблоне.
В return не забываем добавить context: return render(request, 'main/index.html', context)
Далее в html файле, можно сделать цикл некоторых блоков кода, например {% for object in object_list %}<блок кода>{% endfor %}
Внутри <блока кода> можно обращаться к object следующим образом {{ object }}. Таким образом object отображает все значения, точно также как происходит иттерация в python. Важно помнить, что все переменны при обращении через {{}} принимают СТРОКОВЫЕ значения.
Для того чтобы все слова начинались с большой буквы делаем пайп: {{ object|title }}
Конструкция if в <блоке кода>:
{% if object.is_active %} - используем поле модели is_active как свойство и можем его сравнивать и проверять любые условия
{{ object|title }}
{% else %}
{{ object|title }} если не is_active, то делаем текст "не активным"
{% endif %}

Подшаблоны и базовые шаблоны

Для выделения подшаблона, необходимо сделать его отдельным html. Например, contact.html (не забываем добавить в урлы)
Для разделения на базовый шаблон (создается base.html) и подшаблон, необходимо в базовом в месте вставки подшаблона описать контсрукцию {% block block_name %}{% endblock %}, а в подшаблоне в самом начале {% extends '<app_name>/base.html'} {% block block_name %}, и закрыть в самом конце {% endblock %}
Все подшаблоны складываются в директорию includes в папке templates, называются с приставкой "inc_" и оформляются тем же html файлом. Вставляются в base.html коснтрукцией {% include "<app_name>/includes/inc_....html" %}
Правильная маршрутизация
Для того чтобы правильно сделать ссылки в меню в html

В config/url.py в path('', include('<app_name>.urls')) добавляем namespace='<app_name>' -> path('', include('<app_name>.urls', namespace='<app_name>'))
В урлы приложения добавляем новой строкой app_name = <App_name>Config.name, где <App_name>Config импортируем из apps.py приложения, и дописываем в pathы nameы в формате: urlpatterns = [path('', index, name='index')]
В html прописываем ссылки в формате тегов: href='{% url '<app_name>:index' %}'
Кастомные теги

---21.1---

FBV/CBV Реализуют функционал CRUD - create, read, update, delete FBV - function based view: более информативный, но повторяет много кода (DRY)
def student(request):
context = {
'object_list': Student.objects.all() }
return render(request, 'students/student_list.html', context)

CBV - class based view: более модульный, полностью оттестирован, но много процессов "под капотом"
class StudentListView(ListView):
model = Student

Перевод FBV в CBV

Переводятся контроллеры CRUD функциональности
Импорт из django.view.generic import ListView, DetailView.
index преобразуем в class <Model_name>ListView(ListView)/<Model_name>DetailView(DetailView): model = <Model_name> template = '<app_name>.index.html'/'<app_name>.student_detail.html'
В урлах из views.py импортируем <Model_name>ListView и в path меняем index на <Model_name>ListView.as.view()
Generics

Дженерики - базовые классы, описывающие базовое поведение контролеров для механизма CRUD (CreateView, DetailView и тд)
Для Дженериков важно, чтобы шаблон, с которым работает дженерик лежал в нашей папке templates и назывался '<app_name>/_form.html', '<app_name>/_detail.html' для CreateView, DetailView; '<app_name>/_list.html' для ListView и тд.
Создание моделей

CreateView - для форм создания: Доп указываем поля для создания fields = ('first','second',) и ссылку для перенаправления после успешного создания success_url = reverse_lazy('main:index') (from django.urls import reverse_lazy)
Методы класса

те, которые отвечают за получение данных - основная логика - от контроллера к шаблону:
get_queryset() — получение запроса для формирования данных, используется в каждом контроллере.
get_context_data() — получение контекста для формирования ответа, который будет рендериться из шаблона, используется в каждом контроллере.
get_paginate_by() — получение количества записей для постраничного вывода, используется только в контроллере ListView.
Для этих методов def get_queryset(self, *args, **kwargs): необходимо сначала вызвать родительский тот же метод queryset = super().get_queryset(*args, **kwargs), затем определить функционал queryset = queryset.filter(is_active=True), в конце вернуть результат return queryset.

те, которые отвечают за обработку запроса - основная логика - от пользователя к контроллеру:
post() — обработка входящего POST-запроса, используется в контроллерах CreateView или DeleteView.
form_valid() — обработка валидации формы, используется в контроллерах CreateView и UpdateView.
form_invalid() — обработка невалидной формы, используется в контроллерах CreateView и UpdateView.
Для этих методов def form_valid(self, form): сначала реализуем функционал if form.is_valid(): new_student = form.save() new_student.personal_manager = self.request.user new_student.save() и только в итоге вызываем родительский метод return super().form_valid(form)
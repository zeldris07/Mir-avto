from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Mark(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название марки')
    image = models.ImageField(upload_to='images/mark', verbose_name='Картинка')

    class Meta:
        verbose_name_plural = 'Марки'


class PartList(models.Model):
    list_name = models.CharField(max_length=250,  verbose_name='Имя для категории')
    mark = models.CharField(max_length=250, verbose_name='Марка')
    list_slug = models.SlugField(max_length=255, verbose_name='slug для категории', unique=True)
    image = models.ImageField(upload_to='images/shop', blank=True)

    class Meta:
        db_table = "Категория запчасти"
        verbose_name_plural = "Категории запчастей"

    def __str__(self):
        return self.list_name


class Category(models.Model):
    part_list = models.ForeignKey(PartList, on_delete=models.CASCADE, blank=True, null=True,  related_name='parent',
                              verbose_name='подкатегория')
    category_name = models.CharField(max_length=250, verbose_name='Название подкатегории',)
    category_slug = models.SlugField(max_length=250, verbose_name='slug поле подкатегории')
    image = models.ImageField(upload_to='images/shop', blank=True)

    def __str__(self):
        return f'{self.category_name} {self.part_list.list_name}'

    def get_slug(self):
        return self.part_list.list_slug

    class Meta:
        db_table = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='category',
                                 verbose_name='Категория')
    article = models.CharField(max_length=255, verbose_name='Оригинальный артикул')
    article_second = models.CharField(max_length=255, verbose_name='Дополнительный артикул')
    name = models.CharField(max_length=255, verbose_name='Наименование', blank=True, null=True)
    part_exist = models.BooleanField(verbose_name='Наличие')
    part_slug = models.SlugField(max_length=250, verbose_name='Слаг')
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='images/shop',)

    def __str__(self):
        return f'{self.name}:{self.price}'

    class Meta:
        db_table = "Деталь"
        verbose_name_plural = 'Детали'


class Order(models.Model):
    parts = models.CharField(max_length=2000, verbose_name='Запчасти')
    total = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Общая цена')
    address = models.CharField(max_length=50, verbose_name='Адресс')
    number = PhoneNumberField(verbose_name='Номер')

    orient = models.CharField(max_length=200, verbose_name='Ориентир', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    user = models.ForeignKey(
        to='accounts.CustomUser',
        verbose_name='Пользователь',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return f'id:{self.id} Пользователь:{self.user.username} всего:{self.total}'

    class Meta:
        db_table = 'Заказ'
        verbose_name_plural = 'Заказы'
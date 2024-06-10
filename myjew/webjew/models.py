from django.db import models
import json


def root_img(name=None):
    if name:
        return rf'/static/webjew/img/category_images/{str(name)}.png'
    else:
        return rf'/static/webjew/img/category_images/none.jpg'

class Base(models.Model):
    title = models.CharField(default='Unnamed', max_length=100)
    title_image = models.ImageField(default=None, null=True, blank=True, upload_to='webjew/static/media/jews')
    copyright = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    description = models.CharField(default=None, null=True, max_length=300, blank=True)

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.title


# обручки
class WeddingRing(Base):

    class Meta:
        verbose_name = 'Обручка'
        verbose_name_plural = 'Обручки'

    def category_image():
        return root_img('weddingring')
 
# каблучки
class CircletRing(Base):

    class Meta:
        verbose_name = 'Каблучка'
        verbose_name_plural = 'Каблучки'
    
    def category_image():
        return root_img('circletring')

# печатки
class SealRing(Base):

    class Meta:
        verbose_name = 'Печатка'
        verbose_name_plural = 'Печатки'
    
    def category_image():
        return root_img('sealring')

# ланцюжки
class Chainlet(Base):

    class Meta:
        verbose_name = 'Ланцюжок'
        verbose_name_plural = 'Ланцюжки'
        ordering = ["-id"]

    def category_image():
        return root_img('chainlet')

# підвіски
class Pendant(Base):

    class Meta:
        verbose_name = 'Підвіска'
        verbose_name_plural = 'Підвіски'

    def category_image():
        return root_img('pendant')

# кольє
class Necklace(Base):

    class Meta:
        verbose_name = 'Кольє'
        verbose_name_plural = 'Кольє'

    def category_image():
        return root_img('necklace')

# сережки
class Earrings(Base):

    class Meta:
        verbose_name = 'Сережки'
        verbose_name_plural = 'Сережки'

    def category_image():
        return root_img('earrings')

# кафи
class Kaf(Base):

    class Meta:
        verbose_name = 'Каф'
        verbose_name_plural = 'Кафи'
        ordering = ["-id"]

    def category_image():
        return root_img('kaf')

# браслети
class Bracelet(Base):

    class Meta:
        verbose_name = 'Браслет'
        verbose_name_plural = 'Браслети'

    def category_image():
        return root_img('bracelet')



class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    wished_jew = models.CharField(max_length=100)
    budget = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return f"{self.name} - {self.wished_jew} - {self.phone_number}"


class Feedback(models.Model):
    page_url = models.CharField(max_length=200, null=True, blank=True)
    text = models.CharField(max_length=300, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Фідбек'
        verbose_name_plural = 'Фідбеки'

    def __str__(self):
        return f"{self.created} - {self.page_url}: {self.text}"


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

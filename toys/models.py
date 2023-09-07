from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Brend(models.Model):
    name = models.CharField(max_length=30,)
    class Meta:
        verbose_name = 'Брэнд'
        verbose_name_plural = 'Брэнды'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Катэгорыя")

    class Meta:
        verbose_name_plural = 'Катэгорыі'

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=30, verbose_name='Для каго')

    class Meta:
        verbose_name_plural = 'Для каго'

    def __str__(self):
        return self.name


class Toys(models.Model):
    class Meta:
        verbose_name = 'цацка'
        verbose_name_plural = 'цацкі'

    name = models.CharField(db_index=True, max_length=100, verbose_name='назва цацкі')
    brend = models.ForeignKey(Brend, on_delete=models.SET_NULL, null=True, related_name='brand_toys')
    # адзін брэнд можа выпускаць шмат цацак
    # ўсталёўвае NULL пры выдаленні звязанай радкі з галоўнай табліцы.Калі выдалім бренд, у цацкі будзе Null
    categories = models.ManyToManyField(Category, null=True, blank=True, related_name='cats')
    price = models.DecimalField(decimal_places=2, max_digits=6)
    count = models.PositiveIntegerField()
    discription = models.TextField(blank=True, null=True)
    genders = models.ManyToManyField(Gender, blank=True, null=True, related_name='gender')
    visible = models.BooleanField(default=True)  # калі цацкі скончылісь, не будзе бачна іх на старонцы.
    # для гэтага траба зрабіць функцыю

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

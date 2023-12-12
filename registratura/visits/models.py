from django.db import models
from django.urls import reverse


class Visit(models.Model):
    visit_date_time = models.DateTimeField(editable=True, verbose_name="Дата выезда")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    message_text = models.TextField(blank=True, editable=True, verbose_name="Текст сообщения")
    rent_days = models.DurationField(default=10, blank=False, verbose_name="Дней аренды")
    price = models.PositiveIntegerField(blank=False) # сделать поле выбора

    is_visited = models.BooleanField(blank=True, default=False, verbose_name="Выезд состоялся?")

    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE, verbose_name="Доктор")
    device = models.ForeignKey("Device", on_delete=models.CASCADE, verbose_name="Аппарат")

    def __str__(self):
        return f"{self.visit_date_time}"

    #def get_absolute_url(self):
        #return reverse('visit', kwargs={'patient_id': self.patient.pk, 'visit_id': self.pk})

    class Meta:
        verbose_name = "Выезд"
        verbose_name_plural = "Выезды"


class Doctor(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    telegram_id = models.CharField(max_length=50, verbose_name="Telegram ID")
    is_active = models.BooleanField(default=False)
    added_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"


class Device(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    number = models.CharField(max_length=50, verbose_name="Номер")
    is_free = models.BooleanField(default=True, verbose_name="Аппарат свободен") # сделать поле выбора
    added_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    class Meta:
        verbose_name = "Аппарат"
        verbose_name_plural = "Аппараты"


class User(models.Model):
    

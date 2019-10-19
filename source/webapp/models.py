from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.question

class Choice(models.Model):
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст варианта')
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE, verbose_name='Опрос',
                             related_name='choices')

    def __str__(self):
        return self.text

class Answer(models.Model):
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE, verbose_name='Опрос',
                             related_name='answers')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    choice = models.ForeignKey('Choice', on_delete=models.CASCADE, verbose_name='Ответ',
                             related_name='answers')

    def __str__(self):
        return self.poll
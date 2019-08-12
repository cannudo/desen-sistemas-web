from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_lenght = 200)
    pub_date = models.DateTimeField("Publication date")

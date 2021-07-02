from django.db import models

# Create your models here.
class Questions(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    points = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.question

class Options(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    option = models.CharField(max_length=1000)
    points = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.Question
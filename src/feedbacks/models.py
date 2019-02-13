from django.db import models
from accounts.models import User



class Question(models.Model):
    rank = models.SmallIntegerField(auto_created=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    def __str__(self):
        if self.title:
            return '{} - ...'.format(self.title)
        elif self.description:
            return '... - {}'.format(self.description)
        else:
            return '{} - {}'.format(self.title, self.description)


class Presentation(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    oral_date = models.DateField()
    presentor = models.ManyToManyField(User)
    def __str__(self):
        return self.title


class Feedback(models.Model):
    student = models.ForeignKey(User, related_name='evaluator_student', on_delete=models.CASCADE)
    presentor = models.ForeignKey(User, related_name='presentor_student', on_delete=models.CASCADE)
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    score = models.SmallIntegerField()
    def __str__(self):
        return "{} q:{} <- s:{} for p:{}".format(self.student.get_full_name(), self.question.rank, self.score, self.presentation.title)





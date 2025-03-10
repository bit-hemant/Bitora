from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question = models.CharField(max_length=100)
    #created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Answers(models.Model):
    question = models.ForeignKey(Question, related_name='Answers', on_delete=models.CASCADE)
    answer = models.CharField(max_length=1000)

    def __str__(self):
        return self.answer


# class Vote(models.Model):
#     choice = models.ForeignKey(Choice, related_name='votes', on_delete=models.CASCADE)
#     poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
#     voted_by = models.ForeignKey(User, on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ("poll", "voted_by")
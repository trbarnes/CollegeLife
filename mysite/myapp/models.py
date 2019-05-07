from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Suggestion(models.Model):
    suggestion_field = models.CharField(max_length=240)
    suggestion_author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.suggestion_field)

class Comment(models.Model):
    comment_field = models.CharField(max_length=240)
    comment_suggestion = models.ForeignKey(Suggestion, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.comment_field)

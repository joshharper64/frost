from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    """ Report by User """
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    class Meta:
        verbose_name_plural = 'reports'

    def __str__(self):
        return self.text[:50] + "..."

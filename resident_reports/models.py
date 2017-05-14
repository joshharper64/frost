from django.db import models

class Topic(models.Model):
    """ Topic of Report """
    text = models.CharField(max_length=200)
    def __str___(self):
        return self.text

class Report(models.Model):
    """ Report by User """
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'reports'

    def __str__(self):
        return self.text[:50] + "..."

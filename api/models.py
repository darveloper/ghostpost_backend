from django.db import models

class Post(models.Model):
    text = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    total_votes = models.IntegerField(default=0)
    is_boast = models.BooleanField(default=True)

    def __str__(self):
        return self.text
    

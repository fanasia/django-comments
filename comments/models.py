from django.db import models

# Create your models here.
# class Profile(models.Model):
#     display_name = models.CharField(max_length=30)
#     username = models.CharField(max_length=10)
#
#     def __str__(self):
#         return self.display_name


class Comment(models.Model):
    comment = models.CharField(max_length=100)
    # created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('updated_at',)

    def __str__(self):
        return self.comment
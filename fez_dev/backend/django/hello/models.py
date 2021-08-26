from django.db import models

# Create your models here.
class Hello(models.Model):
    
    class Meta:
        verbose_name_plural = "hello"
        
    content = models.CharField(max_length=100)
    regist_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.content)
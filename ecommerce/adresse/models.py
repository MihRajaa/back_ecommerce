from django.db import models

# Create your models here.

# table gouvernat
class Gouvernat(models.Model):
    name_gouv = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name_gouv
    

# table ville
class Ville(models.Model):
    gouvernat = models.ForeignKey(Gouvernat, on_delete=models.CASCADE, related_name="name_gouv")
    name_ville = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name_ville
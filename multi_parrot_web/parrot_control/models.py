from django.db import models

# Create your models here.

class ParrotCommand(models.Model):
    TAG_CHOICES = (
        ("P_M", "Parrot Movement"),
        ("P_V", "Parrot Voice"),
    )

    name = models.CharField(max_length=40,null=False,blank=False)
    title = models.CharField(max_length=40,null=False,blank=False)
    category_id = models.IntegerField(null= False, blank= False, default= 0)
    tag = models.CharField(choices=TAG_CHOICES,max_length=4,null=False,blank=False)
    arg = models.IntegerField(unique=True,blank=False,null=False)
    priority = models.IntegerField(blank=False,null=False,default=10)
    voice_relative_path = models.CharField(max_length=512)
    perform_time = models.IntegerField(default=5) #in second
    parrot_0 = models.BooleanField(default=True, null=False)
    parrot_1 = models.BooleanField(default=True, null=False)

    def is_voice(self):
        return self.tag == "P_V"

    def __str__(self):
        return self.tag + ": " + self.name
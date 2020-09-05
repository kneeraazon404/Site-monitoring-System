from django.db import models

# Create your models here.
class Cement(models.Model):
    # weight
    cube_1_w = models.IntegerField()
    cube_2_w = models.IntegerField()
    cube_3_w = models.IntegerField()
    cube_4_w = models.IntegerField()
    cube_5_w = models.IntegerField()
    cube_6_w = models.IntegerField()
    cube_7_w = models.IntegerField()
    cube_8_w = models.IntegerField()
    cube_9_w = models.IntegerField()
    # Load
    cube_1_w = models.IntegerField()
    cube_2_w = models.IntegerField()
    cube_3_w = models.IntegerField()
    cube_4_w = models.IntegerField()
    cube_5_w = models.IntegerField()
    cube_6_w = models.IntegerField()
    cube_7_w = models.IntegerField()
    cube_8_w = models.IntegerField()
    cube_9_w = models.IntegerField()
    # Date Entry Date
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cube_1_w

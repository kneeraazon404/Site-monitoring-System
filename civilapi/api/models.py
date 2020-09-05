from django.db import models
from datetime import datetime

# Create your models here.
class Cement(models.Model):
    test_title = models.CharField(max_length=100, default="My Test 1")
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
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.test_title

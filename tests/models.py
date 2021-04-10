import uuid

from account.models import Account
from django.conf import settings
from django.db import models
from django.db.models.deletion import DO_NOTHING


#! new Project
class NewProject(models.Model):
    #! weight
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)
    lab_name = models.CharField(max_length=200)
    contractor = models.CharField(max_length=200)
    consultant = models.CharField(max_length=200)
    contract_no = models.PositiveIntegerField()

    def __str__(self):
        return self.project_name


#! Compressive strenght test of cement MODEL
class cementCompressive(models.Model):
    #! weight
    unique_id = models.ForeignKey(NewProject, on_delete=DO_NOTHING)
    test_name = models.CharField(max_length=500, default="Cement Compressive Test")
    cement_w = models.FloatField(null=True, blank=True)
    sand_w = models.FloatField(null=True, blank=True)
    totalMass = models.FloatField(null=True, blank=True)
    water = models.FloatField(null=True, blank=True)
    W_by_c = models.FloatField(null=True, blank=True)
    sampleLocation = models.CharField(max_length=100, blank=True)
    cementSource = models.CharField(max_length=100, blank=True)
    waterRequired = models.FloatField(null=True, blank=True)
    NormalConsistencyOfCement = models.FloatField(null=True, blank=True)
    mixPorportion = models.FloatField(null=True, blank=True)
    length_c = models.FloatField(default=7)
    breadth_c = models.FloatField(default=7)
    height_c = models.FloatField(default=7)
    date_of_casting = models.DateTimeField(auto_now_add=True)
    #  ! weight
    area_of_cube = models.FloatField(default=49)
    volume_of_cube = models.FloatField(default=343)
    cube_weight_1 = models.FloatField(null=True, blank=True)
    cube_weight_2 = models.FloatField(null=True, blank=True)
    cube_weight_3 = models.FloatField(null=True, blank=True)
    cube_weight_4 = models.FloatField(null=True, blank=True)
    cube_weight_5 = models.FloatField(null=True, blank=True)
    cube_weight_6 = models.FloatField(null=True, blank=True)
    cube_weight_7 = models.FloatField(null=True, blank=True)
    cube_weight_8 = models.FloatField(null=True, blank=True)
    cube_weight_9 = models.FloatField(null=True, blank=True)
    # ! Load
    cube_load_1 = models.FloatField(null=True, blank=True)
    cube_load_2 = models.FloatField(null=True, blank=True)
    cube_load_3 = models.FloatField(null=True, blank=True)
    cube_load_4 = models.FloatField(null=True, blank=True)
    cube_load_5 = models.FloatField(null=True, blank=True)
    cube_load_6 = models.FloatField(null=True, blank=True)
    cube_load_7 = models.FloatField(null=True, blank=True)
    cube_load_8 = models.FloatField(null=True, blank=True)
    cube_load_9 = models.FloatField(null=True, blank=True)
    # !calculated Strenght
    strength_1 = models.FloatField(null=True, blank=True)
    strength_2 = models.FloatField(null=True, blank=True)
    strength_3 = models.FloatField(null=True, blank=True)
    strength_4 = models.FloatField(null=True, blank=True)
    strength_5 = models.FloatField(null=True, blank=True)
    strength_6 = models.FloatField(null=True, blank=True)
    strength_7 = models.FloatField(null=True, blank=True)
    strength_8 = models.FloatField(null=True, blank=True)
    strength_9 = models.FloatField(null=True, blank=True)
    # !calculated average strenght
    avg_strength_1 = models.FloatField(null=True, blank=True)
    avg_strength_2 = models.FloatField(null=True, blank=True)
    avg_strength_3 = models.FloatField(null=True, blank=True)

    #! Density calculated
    density_1 = models.FloatField(null=True, blank=True)
    density_2 = models.FloatField(null=True, blank=True)
    density_3 = models.FloatField(null=True, blank=True)
    density_4 = models.FloatField(null=True, blank=True)
    density_5 = models.FloatField(null=True, blank=True)
    density_6 = models.FloatField(null=True, blank=True)
    density_7 = models.FloatField(null=True, blank=True)
    density_8 = models.FloatField(null=True, blank=True)
    density_9 = models.FloatField(null=True, blank=True)
    # !calculated average strenght
    avg_density_1 = models.FloatField(null=True, blank=True)
    avg_density_2 = models.FloatField(null=True, blank=True)
    avg_density_3 = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.test_name

    def save(self, *args, **kwargs):
        # ? strength
        self.strength_1 = self.cube_load_1 / self.area_of_cube
        self.strength_2 = self.cube_load_2 / self.area_of_cube
        self.strength_3 = self.cube_load_3 / self.area_of_cube
        self.strength_4 = self.cube_load_4 / self.area_of_cube
        self.strength_5 = self.cube_load_5 / self.area_of_cube
        self.strength_6 = self.cube_load_6 / self.area_of_cube
        self.strength_7 = self.cube_load_7 / self.area_of_cube
        self.strength_8 = self.cube_load_8 / self.area_of_cube
        self.strength_9 = self.cube_load_9 / self.area_of_cube
        self.avg_strength_1 = (self.strength_1 + self.strength_2 + self.strength_3) / 3
        self.avg_strength_2 = (self.strength_4 + self.strength_5 + self.strength_6) / 3
        self.avg_strength_3 = (self.strength_7 + self.strength_8 + self.strength_9) / 3
        # ? Density
        self.density_1 = self.cube_weight_1 / self.volume_of_cube
        self.density_2 = self.cube_weight_2 / self.volume_of_cube
        self.density_3 = self.cube_weight_3 / self.volume_of_cube
        self.density_4 = self.cube_weight_4 / self.volume_of_cube
        self.density_5 = self.cube_weight_5 / self.volume_of_cube
        self.density_6 = self.cube_weight_6 / self.volume_of_cube
        self.density_7 = self.cube_weight_7 / self.volume_of_cube
        self.density_8 = self.cube_weight_8 / self.volume_of_cube
        self.density_9 = self.cube_weight_9 / self.volume_of_cube
        self.avg_density_1 = (self.density_1 + self.density_2 + self.density_3) / 3
        self.avg_density_2 = (self.density_4 + self.density_5 + self.density_6) / 3
        self.avg_density_3 = (self.density_7 + self.density_8 + self.density_9) / 3
        super(cementCompressive, self).save(*args, **kwargs)


#! Done with the compressive test

# ! cement setting time test MODEL
class cementSettingTime(models.Model):
    unique_id = models.ForeignKey(NewProject, on_delete=DO_NOTHING)
    test_name = models.CharField(max_length=500, default="Cement Setting Time Test")
    time_of_adding_water = models.PositiveIntegerField(blank=True, null=True)
    time_of_initial_setting = models.PositiveIntegerField(null=True, blank=True)
    time_of_final_setting = models.PositiveIntegerField(null=True, blank=True)
    lab_ref_no = models.PositiveIntegerField(null=True, blank=True)
    sample_location = models.CharField(max_length=100)
    cement_brand_or_source = models.CharField(max_length=100)
    date_of_testing = models.PositiveIntegerField(null=True, blank=True)
    date_of_sampling = models.PositiveIntegerField(null=True, blank=True)
    sampled_by = models.CharField(max_length=500)
    initial_setting_time = models.FloatField(null=True, blank=True)
    final_setting_time = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.test_name

    def save(self, *args, **kwargs):
        self.initial_setting_time = (
            self.time_of_initial_setting - self.time_of_adding_water
        )

        self.final_setting_time = (
            self.time_of_final_setting - self.time_of_initial_setting
        )

        super(cementSettingTime, self).save(*args, **kwargs)


#! Consistency Test of Cement
class cementConsistencyTest(models.Model):
    unique_id = models.ForeignKey(NewProject, on_delete=DO_NOTHING)
    test_name = models.CharField(max_length=500)
    wt_of_cement_1 = models.FloatField(null=True, blank=True)
    wt_of_cement_2 = models.FloatField(null=True, blank=True)
    wt_of_cement_3 = models.FloatField(null=True, blank=True)
    wt_of_cement_4 = models.FloatField(null=True, blank=True)

    wt_of_water_added_1 = models.FloatField(null=True, blank=True)
    wt_of_water_added_2 = models.FloatField(null=True, blank=True)
    wt_of_water_added_3 = models.FloatField(null=True, blank=True)
    wt_of_water_added_4 = models.FloatField(null=True, blank=True)

    initial_reading_of_indicator_1 = models.FloatField(null=True, blank=True)
    initial_reading_of_indicator_2 = models.FloatField(null=True, blank=True)
    initial_reading_of_indicator_3 = models.FloatField(null=True, blank=True)
    initial_reading_of_indicator_4 = models.FloatField(null=True, blank=True)

    final_reading_of_indicator_1 = models.FloatField(null=True, blank=True)
    final_reading_of_indicator_2 = models.FloatField(null=True, blank=True)
    final_reading_of_indicator_3 = models.FloatField(null=True, blank=True)
    final_reading_of_indicator_4 = models.FloatField(null=True, blank=True)

    percentage_of_water_added_1 = models.FloatField(blank=True, null=True)
    percentage_of_water_added_2 = models.FloatField(blank=True, null=True)
    percentage_of_water_added_3 = models.FloatField(blank=True, null=True)
    percentage_of_water_added_4 = models.FloatField(blank=True, null=True)

    sampleLocation = models.CharField(max_length=100, blank=True)
    cementSource = models.CharField(max_length=100, blank=True)

    normal_consistency_of_cement = models.IntegerField(default=31)

    date_of_sampling = models.DateTimeField(auto_now_add=False)
    date_of_casting = models.DateTimeField(auto_now_add=False)

    water_by_cement_ratio = models.FloatField(blank=True, null=True)
    sampled_by = models.CharField(max_length=500)

    penetration_of_plunger_1 = models.FloatField(blank=True, null=True)
    penetration_of_plunger_2 = models.FloatField(blank=True, null=True)
    penetration_of_plunger_3 = models.FloatField(blank=True, null=True)
    penetration_of_plunger_4 = models.FloatField(blank=True, null=True)

    average_value = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.test_name

    def save(self, *args, **kwargs):
        self.water_by_cement_ratio = self.wt_of_cement_1 / self.wt_of_water_added_1
        # self.water_by_cement_ratio = self.wt_of_cement_1 / self.wt_of_water_added_1
        # self.water_by_cement_ratio = self.wt_of_cement_1 / self.wt_of_water_added_1
        # self.water_by_cement_ratio = self.wt_of_cement_1 / self.wt_of_water_added_1

        self.penetration_of_plunger_1 = (
            self.final_reading_of_indicator_1 - self.initial_reading_of_indicator_1
        )
        self.penetration_of_plunger_2 = (
            self.final_reading_of_indicator_2 - self.initial_reading_of_indicator_2
        )
        self.penetration_of_plunger_3 = (
            self.final_reading_of_indicator_3 - self.initial_reading_of_indicator_3
        )
        self.penetration_of_plunger_4 = (
            self.final_reading_of_indicator_4 - self.initial_reading_of_indicator_4
        )
        self.average_value = (
            self.penetration_of_plunger_1
            + self.penetration_of_plunger_2
            + self.penetration_of_plunger_3
            + self.penetration_of_plunger_4
        )
        super(cementConsistencyTest, self).save(*args, **kwargs)


#! Fineness Test Of cement MODEL Below

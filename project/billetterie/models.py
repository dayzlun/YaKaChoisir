from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=64, default="", primary_key=True)
    email_ticket = models.EmailField(max_length=64)
    password = models.CharField(max_length=64, default="")
    login = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64, default="")
    lastname = models.CharField(max_length=64, default="")
    student = models.NullBooleanField()
    access_level = models.IntegerField(default=0)


class Event(models.Model):
    title = models.CharField(max_length=64, primary_key=True)
    image = models.ImageField()
    description = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    end_inscrip_date = models.DateField()
    max_place_student = models.IntegerField()
    max_place_ext = models.IntegerField()
    price_student = models.IntegerField()
    price_extern = models.IntegerField()
    display_available_places = models.NullBooleanField(null=True, blank=True)
    premium = models.NullBooleanField(null=True, blank=True)
    nb_places_student = models.IntegerField(null=True)
    nb_places_extern = models.IntegerField(null=True)
    status = models.IntegerField(default=0)
    nb_inside = models.IntegerField(default=0)


class Association(models.Model):
    name = models.CharField(max_length=64)
    uri = models.CharField(max_length=64)


class Userevent(models.Model):
    billet_type = models.IntegerField(default=0)
    inside = models.NullBooleanField(default=False)
    staff = models.NullBooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, default="NOPE")


class Userassociation(models.Model):
    members_mail = models.ForeignKey(User, on_delete=models.CASCADE)
    association_name = models.ForeignKey(Association, on_delete=models.CASCADE)

from django.db import models

class User(models.Model):
    email = models.CharField(max_length=64, default="", primary_key=True)
    email_ticket = models.CharField(max_length=64)
    password = models.CharField(max_length=64, default="")
    login = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64, default="")
    lastname = models.CharField(max_length=64, default="")
    student = models.NullBooleanField()
    access_level = models.IntegerField(default=0)


class Event(models.Model):
    title = models.CharField(max_length=64, primary_key=True)
    description = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    end_inscrip_date = models.DateField()
    max_place_student = models.IntegerField()
    max_place_ext = models.IntegerField()
    price_student = models.IntegerField()
    price_extern = models.IntegerField()
    display_available_places = models.BooleanField()
    status = models.IntegerField()
    premium = models.IntegerField()
    nb_registered = models.IntegerField()
    nb_registered_used = models.IntegerField()
    nb_registered_inside = models.IntegerField()


class Association(models.Model):
    name = models.CharField(max_length=64)
    uri = models.CharField(max_length=64)


class Userevent(models.Model):
    billet_type = models.IntegerField()
    inside = models.BooleanField()
    staff = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)


class Userassociation(models.Model):
    members_mail = models.ForeignKey(User, on_delete=models.CASCADE)
    association_name = models.ForeignKey(Association, on_delete=models.CASCADE)



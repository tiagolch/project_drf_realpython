from django.db import models


class Puppy(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    breed = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_breed(self):
        return f"{self.name} is a {self.breed}"

    def get_created_at(self):
        return self.created_at.strftime("%Y-%m-%d %H:%M:%S")

    def get_updated_at(self):
        return self.updated_at.strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        return f"Puppy: {self.name} is added"



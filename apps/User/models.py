from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=50)
    dateBirth = models.DateField()
    email = models.EmailField(("email address"), unique=True)
    profilePicture = models.ImageField(null=True, upload_to='profile')

    def __str__(self):
        text =  '{0} - {1} - {2}'
        return text.format(self.id, self.fullName, self.email)

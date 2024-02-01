from django.db import models

# Create your models here.
class UserModel(models.Model):
    UserID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length = 256)
    Email = models.EmailField()
    MembershipDate = models.DateField()

    def __str__(self):
        return f"{self.Name} ({self.UserID})"
from django.db import models



class History(models.Model):
    a                   = models.IntegerField()
    b                   = models.IntegerField()
    

    # Define a string representation of the model
    def __str__(self):
        return f"a={self.a} & b={self.b} "
    

class Total(models.Model):
    # Define a one-to-one field to reference the sum model
    sum = models.OneToOneField(History, on_delete=models.CASCADE)

    # Define an integer field to store the total of sums
    total = models.IntegerField(default=0)

    # Define a string representation of the model
    def __str__(self):
        return f"Total: {self.total}"
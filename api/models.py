from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Expense(models.Model):
    date = models.DateField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.date} - {self.description}"

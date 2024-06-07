from django.db import models

class Lender(models.Model):
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)

class Loan(models.Model):
    lender = models.ForeignKey(Lender, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
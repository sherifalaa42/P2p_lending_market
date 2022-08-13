from django.db import models

# Create your models here.

class Customer(models.Model):

    FULL_TIME = (
        (0, 'Not Full Time'),
        (1, 'Full Time')
    )
    LP_CustomerPrincipalPayments = models.IntegerField()
    LoanMonthsSinceOrigination = models.IntegerField()
    LP_CustomerPayments = models.IntegerField()
    EmploymentStatus_Full_time = models.IntegerField(choices = FULL_TIME)
    Investors = models.IntegerField()
    MonthlyLoanPayment = models.IntegerField()
    LoanOriginalAmount = models.IntegerField()

    def __str__(self):
        return '{}, {}'.format(self.Investors, self.LP_CustomerPayments)
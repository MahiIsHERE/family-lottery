from django.db import models
from django.contrib.auth.models import User


class CashBox(models.Model):
    BOX_TYPES = (
        ('BR', 'Bronze'),
        ('SI', 'Silver'),
        ('GO', 'Gold'),
    )
    box_type = models.CharField(max_length=2, choices=BOX_TYPES, unique=True)
    monthly_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_cycle = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.get_box_type_display()


class FamilyMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name()


class Membership(models.Model):
    member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    cash_box = models.ForeignKey(CashBox, on_delete=models.CASCADE)
    cycle = models.PositiveIntegerField()
    is_winner = models.BooleanField(default=False)

    class Meta:
        unique_together = ('member', 'cash_box', 'cycle')


class LotteryHistory(models.Model):
    cash_box = models.ForeignKey(CashBox, on_delete=models.CASCADE)
    winner = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    cycle = models.PositiveIntegerField()
    amount_won = models.DecimalField(max_digits=10, decimal_places=2)
    win_date = models.DateField(auto_now_add=True)

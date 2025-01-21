from django.contrib import admin
from .models import *

@admin.register(CashBox)
class CashBoxAdmin(admin.ModelAdmin):
    list_display = ('box_type', 'monthly_amount', 'current_cycle')

@admin.register(FamilyMember)
class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'joined_date')

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('member', 'cash_box', 'cycle', 'is_winner')

@admin.register(LotteryHistory)
class LotteryHistoryAdmin(admin.ModelAdmin):
    list_display = ('cash_box', 'winner', 'cycle', 'amount_won', 'win_date')

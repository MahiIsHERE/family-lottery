from django.core.management.base import BaseCommand
from django.utils import timezone
from family_lottery.lottery.models import *
import random


class Command(BaseCommand):
    help = 'Runs monthly lottery draw'

    def handle(self, *args, **options):
        boxes = CashBox.objects.all()
        for box in boxes:
            active_members = Membership.objects.filter(
                cash_box=box,
                cycle=box.current_cycle,
                is_winner=False
            )

            if active_members.exists():
                winner_membership = random.choice(active_members)
                winner_membership.is_winner = True
                winner_membership.save()

                total_amount = active_members.count() * box.monthly_amount

                LotteryHistory.objects.create(
                    cash_box=box,
                    winner=winner_membership.member,
                    cycle=box.current_cycle,
                    amount_won=total_amount
                )

                # Check if all members have won
                remaining_members = Membership.objects.filter(
                    cash_box=box,
                    cycle=box.current_cycle,
                    is_winner=False
                )

                if not remaining_members.exists():
                    box.current_cycle += 1
                    box.save()
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Demographic(Page):
    form_model = 'player'  # Always need this line
    form_fields = ['birth_year', 'gender', 'education']  # Include all fields that are included in the app

    def error_message(self, values):
        if not values['birth_year'] or not values['gender'] or not values['education']:
            return 'Please answer all questions.'  # Return an error message when any of the questions is not answered.

    def gender_choices(player):
        choices = player.participant.vars['gender_seq']
        return choices


page_sequence = [Demographic]

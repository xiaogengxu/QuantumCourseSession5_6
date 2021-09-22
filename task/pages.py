from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Task(Page):
    form_model = 'player'
    form_fields = ['risk_choice']

    def before_next_page(self):
        # Define participant var so we can recall a subject's choice in the game and use it in the next page.
        self.participant.vars['risk_choice'] = self.player.risk_choice


class Outcome(Page):
    form_model = 'player'

    def vars_for_template(self):  # Define the variables that are used in page template.
        # Recall the choice of a subject and assign to local variable risk_choice.
        risk_choice = self.participant.vars['risk_choice']
        # Recall the outcome and assign to local variable risk_outcome.
        risk_outcome = self.participant.vars['risk_outcome']
        if risk_outcome == 'win':
            outcome = 100 + 2.5 * self.participant.vars['risk_choice']  # Assign value to outcome when a subject wins.
        else:
            outcome = 100 - self.participant.vars['risk_choice']  # Assign value to outcome when a subject loses.
        return {  # Return variables with the values that you have defined. 'var_name': local_variable
            'risk_choice': risk_choice,
            'risk_outcome': risk_outcome,
            'outcome': outcome
        }


page_sequence = [Task, Outcome]

from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import numpy


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'game'
    players_per_group = None
    num_rounds = 1

    list_risk_choice = ['win', 'loss']  # Define the possible outcomes of the game


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            list_risk_seq = Constants.list_risk_choice.copy()  # Call the list you defined, ['win', 'loss']

            # Randomly draw one from 'win' and 'loss', with probability 0.33 an 0.67, respectively
            # You need to import numpy to randomly draw
            p.participant.vars['risk_outcome'] = numpy.random.choice(list_risk_seq, p=[0.33, 0.67])

            # Define participant var to attach the drawn outcome to a subject.
            # This is to help call/use the var for a subject in other apps in the same project.
            p.risk_outcome = p.participant.vars['risk_outcome']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    risk_choice = models.IntegerField(blank=True)
    risk_outcome = models.StringField(blank=True)

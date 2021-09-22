import random

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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'background'
    players_per_group = None
    num_rounds = 1

    gender_option = [('male', 'male'), ('female', 'female'), ('non_binary', 'non-binary'),
                     ('no_answer', 'Prefer not to answer')]


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            gender_option = Constants.gender_option.copy()
            random.shuffle(gender_option)
            p.participant.vars['gender_seq'] = gender_option

            # Manually record the order of options one by one
            # p.gender_seq0 = gender_option[0][0]
            # p.gender_seq1 = gender_option[1][0]
            # p.gender_seq2 = gender_option[2][0]
            # p.gender_seq3 = gender_option[3][0]

            # Use a loop to record the order of options
            for i in range(0, 4):
                str_gender = 'gender_seq%s' % i
                setattr(p, str_gender, gender_option[i][0])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    birth_year = models.IntegerField(
        label='In which year are you born?',
        blank=True
    )
    gender = models.StringField(
        # choices=[('male', 'male'), ('female', 'female'), ('non_binary', 'non-binary'),
        #          ('no_answer', 'Prefer not to answer')],
        widget=widgets.RadioSelect,
        label='What is your gender?',
        blank=True
    )
    gender_seq0 = models.StringField(
        blank=True
    )
    gender_seq1 = models.StringField(
        blank=True
    )
    gender_seq2 = models.StringField(
        blank=True
    )
    gender_seq3 = models.StringField(
        blank=True
    )
    education = models.StringField(
        label='What was your level of education? '
              'Please choose the option that best describes the highest level of education you had completed.',
        widget=widgets.RadioSelect,
        choices=[('lower_secondary', 'Lower secondary education'),
                 ('upper_secondary', 'Upper secondary level education'),
                 ('bachelor', 'Bachelor\'s or equivalent level'),  # Use \ if there is ' in the string
                 ('master', 'Master\'s or equivalent level or doctoral level')],
        blank=True
    )

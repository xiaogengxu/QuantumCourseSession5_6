from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['question1', 'question2', 'question5']

    def before_next_page(self):
        self.player.count_correct()


class Results(Page):
    def vars_for_template(self):
        correct_answers = self.player.q_correct

        return dict(
            correct = correct_answers,
        )


page_sequence = [MyPage, Results]

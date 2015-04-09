from django import forms

LANGS = ( 
    ('bn','Bangala'),
    ('mr','Marathi'),
    ('de','German'),
    ('da','Danish'),
    )

LCS = (
    ('bn_in','bn_IN'),
    ('mr_in','mr_IN'),
    ('de_de','de_DE'),
    ('da_dk','da_DK'),
    )

class WordListSelect(forms.Form):
    select_language = forms.ChoiceField(choices=LANGS)
    select_locale = forms.ChoiceField(choices=LCS)



    

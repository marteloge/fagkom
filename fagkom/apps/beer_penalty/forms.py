from django.forms import ModelForm
from models import AlkoEntry


class BeerPenaltyForm(ModelForm):
    class Meta:
        model = AlkoEntry
        fields = [
            'user',
            'beer_amount',
            'wine_amount',
            'justification',
            # 'date',
        ]

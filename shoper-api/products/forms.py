from django import forms
from products.models import Product


class PickLanguageToCopyForm(forms.Form):

    from_language = forms.ChoiceField(
        widget=forms.Select(),
        choices=(
            [
                ("", "Pick language"),
                ("pl_PL", "PL"),
                ("de_DE", "DE"),
                ("en_IE", "EU"),
                ("en_GB", "GB"),
                ("fr_FR", "FR"),
                ("en_US", "US"),
            ]
        ),
        initial="1",
        required=True,
    )
    to_language = forms.ChoiceField(
        widget=forms.Select(),
        choices=(
            [
                ("", "Pick language"),
                ("pl_PL", "PL"),
                ("de_DE", "DE"),
                ("en_IE", "EU"),
                ("en_GB", "GB"),
                ("fr_FR", "FR"),
                ("en_US", "US"),
            ]
        ),
        initial="1",
        required=True,
    )


class ProductSearchForm(forms.Form):

    q = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["q"].label = "Search For"
        self.fields["q"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )

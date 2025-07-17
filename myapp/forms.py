from django import forms
from myapp.models import Order


class FeedbackForm(forms.Form):
    FEEDBACK_CHOICES = [
        ('B', 'Borrow'),
        ('P', 'Purchase'),
    ]
    feedback = forms.ChoiceField(choices=FEEDBACK_CHOICES, widget=forms.RadioSelect)


class SearchForm(forms.Form):
    name = forms.CharField(
        required=False,
        label='Your Name'  # updated label
    )

    CATEGORY_CHOICES = [
        ('', '---------'),  # empty choice for optional field
        ('Fiction', 'Fiction'),
        ('Science', 'Science'),
        ('History', 'History'),
        # Add your categories here statically or dynamically in the view instead
    ]
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        required=False,  # category made optional
        widget=forms.RadioSelect,
        label='Select a category:'
    )

    max_price = forms.IntegerField(
        required=True,
        label='Maximum Price',
        min_value=0  # disallow negative numbers
    )

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['books', 'member', 'order_type']
        widgets = {
            'books': forms.CheckboxSelectMultiple(),
            'order_type': forms.RadioSelect()
        }
        labels = {
            'member': 'Member name',
        }

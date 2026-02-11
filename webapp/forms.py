from django import forms
from .models import PredictionRecord

class PredictionForm(forms.ModelForm):
    """
    Form for user predictions with SibSp dropdown as team decision
    """
    
    # Custom field for SibSp with dropdown choices
    SIBSP_CHOICES = [(i, str(i)) for i in range(0, 11)]  # 0 to 10
    sibsp = forms.ChoiceField(
        choices=SIBSP_CHOICES,
        initial=0,
        label="Siblings/Spouses Aboard (Optional)",
        help_text="Number of siblings or spouses traveling with",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    class Meta:
        model = PredictionRecord
        fields = ['name', 'sex', 'age', 'parch', 'embarked', 'sibsp', 'ticket', 'fare', 'cabin']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter passenger full name'
            }),
            'sex': forms.Select(attrs={'class': 'form-select'}),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Age in years',
                'step': '0.1'
            }),
            'parch': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number of parents/children',
                'min': '0',
                'max': '10'
            }),
            'embarked': forms.Select(attrs={'class': 'form-select'}),
            'ticket': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Optional: Ticket number'
            }),
            'fare': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Optional: Fare amount',
                'step': '0.01'
            }),
            'cabin': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Optional: Cabin number'
            }),
        }

        labels = {
            'name': 'Passenger Name',
            'sex': 'Gender',
            'age': 'Age',
            'parch': 'Parents/Children Aboard',
            'embarked': 'Port of Embarkation',
            'ticket': 'Ticket Number (Optional)',
            'fare': 'Fare (Optional)',
            'cabin': 'Cabin (Optional)',
        }
        help_texts = {
            'age': 'Age in years (e.g., 25.5 for 25½ years)',
            'parch': 'Number of parents or children aboard',
        }
    
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and (age < 0 or age > 120):
            raise forms.ValidationError("Age must be between 0 and 120 years")
        return age
    
    def clean_sibsp(self):
        value = self.cleaned_data['sibsp']
        return int(value)   # convert string to int

    def clean_parch(self):
        parch = self.cleaned_data.get('parch')
        if parch is not None and (parch < 0 or parch > 10):
            raise forms.ValidationError("Number of parents/children must be between 0 and 10")
        return parch

from django import forms
from .models import PredictionRecord

class PredictionForm(forms.ModelForm):
    """
    Passenger Survival Prediction Form for user prediction
    """
    
    # Custom field for SibSp with dropdown choices
    SIBSP_CHOICES = [(i, str(i)) for i in range(0, 11)]  # 0 to 10
    sibsp = forms.ChoiceField(
        choices=SIBSP_CHOICES,
        initial=0,
        label="Siblings/Spouses Aboard",
        help_text="Number of siblings or spouses traveling with (0-10)",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    PCLASS_CHOICES = [(1, '1st'), (2, '2nd'), (3, '3rd')]
    pclass = forms.ChoiceField(
        choices=PCLASS_CHOICES,
        initial=3,
        label="Passenger Class",
        help_text="1 = First, 2 = Second, 3 = Third",
        widget=forms.Select(attrs={'class': 'form-select'})
    )    
    
    class Meta:
        model = PredictionRecord
        #2.12 fields update: move ticket & carbin, add pclass
        fields = ['name', 'sex', 'age', 'parch', 'embarked', 'pclass', 'fare', 'sibsp']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter passenger full name'
            }),
            'sex': forms.Select(attrs={'class': 'form-select'}),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Age in years(0-120)',
                'step': '1',
                'min':'0',
                'max':'120'
                
            }),
            'parch': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number of parents or children (0-10)',
                'min': '0',
                'max': '10'
            }),
            'embarked': forms.Select(attrs={'class': 'form-select'}),
            
            'fare': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Pounds (for example: 32.50)',
                'step': '0.01',
                'min': '0'
            }),
            
        }

        labels = {
            'name': 'Passenger Name',
            'sex': 'Gender',
            'age': 'Age',
            'parch': 'Parents/Children Aboard',
            'embarked': 'Port of Embarkation',
            'fare': 'Fare',
            # The labels for pclass and sibsp have already been defined in the custom fields, so there is no need to repeat them here.
        }
        
        help_texts = {
            'age': 'Age must be an integer (0-120)',
            'parch': 'Number of parents or children aboard (0-10)',
            'fare': 'pounds, for example 32.50',
        }

        error_messages = {
            'name': {
                'required': "Please enter the passenger's name.",
            },
            'sex': {
                'required': 'Please select gender.',
            },
            'age': {
                'required': "Please enter the passenger's age.",
                'invalid': 'Age must be an integer.',
                'min_value': 'Age cannot be less than 0.',
                'max_value': 'Age cannot exceed 120.',
            },
            'parch': {
                'required': 'please enter the number of parents/children travel with.)',
                'min_value': 'Cannot be negative.',
                'max_value': 'Cannot exceed 10.',
            },
            'embarked': {
                'required': 'Please select port of embarkation.',
            },
            'fare': {
                'required': 'Fare is required.',
                'invalid': 'Enter a valid fare. for example: 32.05',
            }
        }
    
    
    
    
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and (age < 0 or age > 120):
            raise forms.ValidationError("Age must be between 0 and 120.")
        return age
    
    def clean_parch(self):
        parch = self.cleaned_data.get('parch')
        if parch is not None and (parch < 0 or parch > 10):
            raise forms.ValidationError("Value must be between 0 and 10.")
        return parch

    def clean_sibsp(self):
        """Converts the string value of ChoiceField to an integer."""
        value = self.cleaned_data.get('sibsp')
        return int(value) if value else 0

    def clean_fare(self):
        fare = self.cleaned_data.get('fare')
        if fare is None or fare < 0:
            raise forms.ValidationError("Fare must be positive.")
        return fare


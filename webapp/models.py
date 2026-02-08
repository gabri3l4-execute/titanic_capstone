from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
# webapp/models.py

class Passenger(models.Model):
    """
    Model for storing the complete Titanic dataset
    Used for historical data analysis and ML training
    Includes engineered features: FamilySize and AgeGroup
    """
    
    
    # ============ ORIGINAL TITANIC DATASET FIELDS ============
    
    passenger_id = models.IntegerField(
        unique=True,
        verbose_name="Passenger ID",
        help_text="Unique identifier from the Titanic dataset"
    )
    
    survived = models.BooleanField(
        verbose_name="Survived",
        help_text="Actual survival outcome (True = Survived, False = Did Not Survive)"
    )
    
    pclass = models.IntegerField(
        choices=[(1, 'First Class'), (2, 'Second Class'), (3, 'Third Class')],
        verbose_name="Passenger Class",
        help_text="Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)"
    )
    
    name = models.CharField(
        max_length=200,
        verbose_name="Passenger Name",
        help_text="Full name including title"
    )
    
    sex = models.CharField(
        max_length=10,
        choices=[('male', 'Male'), ('female', 'Female')],
        verbose_name="Gender"
    )
    
    age = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Age",
        help_text="Age in years. Fractional if less than 1"
    )
    
    sibsp = models.IntegerField(
        default=0,
        verbose_name="Siblings/Spouses Aboard",
        help_text="Number of siblings or spouses aboard"
    )
    
    parch = models.IntegerField(
        default=0,
        verbose_name="Parents/Children Aboard",
        help_text="Number of parents or children aboard"
    )
    
    ticket = models.CharField(
        max_length=50,
        verbose_name="Ticket Number"
    )
    
    fare = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        null=True,
        blank=True,
        verbose_name="Fare",
        help_text="Passenger fare in pounds"
    )
    
    cabin = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Cabin",
        help_text="Cabin number"
    )
    
    embarked = models.CharField(
        max_length=1,
        choices=[
            ('C', 'Cherbourg'),
            ('Q', 'Queenstown'), 
            ('S', 'Southampton')
        ],
        blank=True,
        verbose_name="Port of Embarkation"
    )
    
    

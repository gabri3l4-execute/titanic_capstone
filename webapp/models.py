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

    # ============ ENGINEERED FEATURES (Team's Selection) ============
    
    # 1. FamilySize = SibSp + Parch + 1
    family_size = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Family Size",
        help_text="Calculated as SibSp + Parch + 1"
    )
    
    # 2. AgeGroup Categories
    AGE_GROUP_CHOICES = [
        ('infant', 'Infant (0-2)'),
        ('child', 'Child (3-12)'),
        ('teen', 'Teenager (13-19)'),
        ('young_adult', 'Young Adult (20-29)'),
        ('adult', 'Adult (30-59)'),
        ('senior', 'Senior (60+)'),
        ('unknown', 'Unknown'),
    ]
    age_group = models.CharField(
        max_length=15,
        choices=AGE_GROUP_CHOICES,
        default='unknown',
        verbose_name="Age Group",
        help_text="Age group calculated from age"
    ) 


    # ============ ADDITIONAL FIELDS ============
    
    # For tracking data source
    data_source = models.CharField(
        max_length=10,
        choices=[('train', 'Training Data'), ('test', 'Test Data')],
        default='train',
        verbose_name="Data Source",
        help_text="Whether this record is from training or test dataset"
    )
    
    # For ML purposes
    features_json = models.JSONField(
        default=dict,
        blank=True,
        verbose_name="Feature Vector",
        help_text="JSON representation of features for ML model"
    )
    
    class Meta:
        verbose_name = "Titanic Passenger"
        verbose_name_plural = "Titanic Passengers"
        ordering = ['passenger_id']
        indexes = [
            models.Index(fields=['passenger_id']),
            models.Index(fields=['survived']),
            models.Index(fields=['pclass', 'survived']),
            models.Index(fields=['sex', 'survived']),
            models.Index(fields=['age_group', 'survived']),
            models.Index(fields=['family_size', 'survived']),
        ]
    
    def __str__(self):
        status = "Survived" if self.survived else "Perished"
        return f"Passenger {self.passenger_id}: {self.name} - {status}" 

    def save(self, *args, **kwargs):
        """
        Override save to calculate engineered features before saving
        """
        # Calculate FamilySize
        self.family_size = self.sibsp + self.parch + 1
        
        # Calculate AgeGroup
        self.age_group = self.calculate_age_group(self.age)
        
        # Prepare features for ML
        self.features_json = self.prepare_features_for_ml()
        
        super().save(*args, **kwargs)
    
    @staticmethod
    def calculate_age_group(age):
        """
        Static method to calculate age group from age
        """
        if age is None:
            return 'unknown'
        
        if age <= 2:
            return 'infant'
        elif age <= 12:
            return 'child'
        elif age <= 19:
            return 'teen'
        elif age <= 29:
            return 'young_adult'
        elif age <= 59:
            return 'adult'
        else:
            return 'senior'

    def prepare_features_for_ml(self):
        """
        Prepare all features in a format suitable for ML model
        """
        return {
            'pclass': self.pclass,
            'sex': self.sex,
            'age': self.age,
            'sibsp': self.sibsp,
            'parch': self.parch,
            'family_size': self.family_size,
            'age_group': self.age_group,
            'fare': float(self.fare) if self.fare else None,
            'embarked': self.embarked if self.embarked else None,
            'cabin_deck': self.cabin[0] if self.cabin and len(self.cabin) > 0 else None,
            'has_cabin': bool(self.cabin),
        }

    def get_survival_status(self):
        """Return formatted survival status"""
        return "Survived" if self.survived else "Perished"
    
    def get_class_display_full(self):
        """Return full class name"""
        class_names = {
            1: "First Class",
            2: "Second Class", 
            3: "Third Class"
        }
        return class_names.get(self.pclass, f"Class {self.pclass}")



class PredictionRecord(models.Model):
    """
    Model for storing user predictions from the web form
    Includes the same engineered features as Passenger model
    """

    # ============ USER INPUT FIELDS (From Prediction Form) ============
    
    # Required fields (as per team decision)
    name = models.CharField(
        max_length=200,
        verbose_name="Passenger Name",
        help_text="Full name for prediction"
    )
    
    sex = models.CharField(
        max_length=10,
        choices=[('male', 'Male'), ('female', 'Female')],
        verbose_name="Gender"
    )
    
    age = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(120)],
        verbose_name="Age",
        help_text="Age in years"
    )
    
    parch = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name="Parents/Children Aboard",
        help_text="Number of parents or children traveling with"
    )
    
    embarked = models.CharField(
        max_length=1,
        choices=[
            ('C', 'Cherbourg'),
            ('Q', 'Queenstown'), 
            ('S', 'Southampton')
        ],
        verbose_name="Port of Embarkation"
    )

    # Optional fields (as per team decision)
    sibsp = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name="Siblings/Spouses Aboard",
        help_text="Optional: Number of siblings or spouses traveling with"
    )

    ticket = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Ticket Number",
        help_text="Optional: Ticket number"
    )
    
    fare = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Fare",
        help_text="Optional: Ticket fare in pounds"
    )

    cabin = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Cabin Number",
        help_text="Optional: Cabin number"
    )

    # ============ ENGINEERED FEATURES (Same as Passenger Model) ============
    
    # 1. FamilySize = SibSp + Parch + 1
    family_size = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Family Size",
        help_text="Calculated as SibSp + Parch + 1"
    )
    
    # 2. AgeGroup Categories (same as Passenger model)
    AGE_GROUP_CHOICES = [
        ('infant', 'Infant (0-2)'),
        ('child', 'Child (3-12)'),
        ('teen', 'Teenager (13-19)'),
        ('young_adult', 'Young Adult (20-29)'),
        ('adult', 'Adult (30-59)'),
        ('senior', 'Senior (60+)'),
    ]
    age_group = models.CharField(
        max_length=15,
        choices=AGE_GROUP_CHOICES,
        blank=True,
        verbose_name="Age Group",
        help_text="Age group calculated from age"
    )

    # ============ PREDICTION RESULTS ============
    
    survived_prediction = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="Survival Prediction"
    )
    
    probability = models.FloatField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],
        verbose_name="Survival Probability",
        help_text="Probability of survival between 0.0 and 1.0"
    )

    # For ML integration
    ml_model_used = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="ML Model Used",
        help_text="Name of the ML model that made this prediction"
    )
    
    model_version = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Model Version",
        help_text="Version of the ML model"
    )

    
    # ============ SYSTEM METADATA ============
    
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Prediction Timestamp"
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Updated"
    )
    
    # For tracking
    session_id = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Session ID"
    )

    user_agent = models.TextField(
        blank=True,
        verbose_name="User Agent",
        help_text="Browser information from the user"
    )
    
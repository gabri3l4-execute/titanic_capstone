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
    

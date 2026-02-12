from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

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
    
    # FIXED: Changed from FloatField to IntegerField
    age = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Age",
        help_text="Age in years(integer). Null if unknown."
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


    # ============ METADATA  ============
    
    # For tracking data source
    data_source = models.CharField(
        max_length=10,
        choices=[('train', 'Training Data'), ('test', 'Test Data')],
        default='train',
        verbose_name="Data Source",
        help_text="Whether this record is from training or test dataset"
    )
    
    imported_at = models.DateTimeField(default=timezone.now, verbose_name="Imported At")
    
    class Meta:
        verbose_name = "Titanic Passenger"
        verbose_name_plural = "Titanic Passengers"
        ordering = ['passenger_id']
    
    def __str__(self):
        return f"Passenger {self.passenger_id}: {self.name}"
    
    def save(self, *args, **kwargs):
        """
        Override save to calculate engineered features before saving
        """
        # Calculate FamilySize
        self.family_size = self.sibsp + self.parch + 1
        
        # Calculate age group
        if self.age is None:
            self.age_group = 'unknown'
        elif self.age <= 2:
            self.age_group = 'infant'
        elif self.age <= 12:
            self.age_group = 'child'
        elif self.age <= 19:
            self.age_group = 'teen'
        elif self.age <= 29:
            self.age_group = 'young_adult'
        elif self.age <= 59:
            self.age_group = 'adult'
        else:
            self.age_group = 'senior'
        
        super().save(*args, **kwargs)
        



class PredictionRecord(models.Model):
    """
    Model for storing user predictions from the web form, prediction results and probabilities
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
    
    #change from FloatField to IntegerFiled
    age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(120)],
        verbose_name="Age",
        help_text="Age in years(integer)"
    )
    
    parch = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name="Parents/Children Aboard",
        help_text="Number of parents or children aboard"
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
    
    #2.12 new add field
    pclass = models.IntegerField(
        choices=[(1, 'First Class'), (2, 'Second Class'), (3, 'Third Class')],
        verbose_name="Passenger Class",
        help_text="Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)"
    )    
    
    fare = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        null=True,
        blank=True,
        verbose_name="Fare",
        help_text="Passenger fare in pounds"
    )   
    
    sibsp = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name="Siblings/Spouses Aboard",
        help_text="Number of siblings or spouses aboard"
    )
    
    # ============ ENGINEERED FEATURES (Same as Passenger Model) ============
    
    # 1. FamilySize = SibSp + Parch + 1
    family_size = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Family Size",
        help_text="Calculated as SibSp + Parch + 1",
        editable=False
    )
    
    # 2. AgeGroup Categories (same as Passenger model)
    age_group = models.CharField(
        max_length=15,
        choices=Passenger.AGE_GROUP_CHOICES,
        blank=True,
        verbose_name="Age Group",
        editable=False
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
    
    # ============ SYSTEM METADATA ============
    
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Prediction Timestamp"
    )
    class Meta:
        verbose_name = "Prediction Record"
        verbose_name_plural = "Prediction Records"
        ordering = ['-created_at']
    
    def __str__(self):
        if self.survived_prediction is None:
            status = "Pending"
        else:
            status = "Survived" if self.survived_prediction else "Not Survived"
        
        return f"Prediction #{self.id}: {self.name} - {status}"

    def save(self, *args, **kwargs):
        """Calculate engineered features before saving"""
        self.family_size = self.sibsp + self.parch + 1
        
        # Calculate age group
        if self.age <= 2:
            self.age_group = 'infant'
        elif self.age <= 12:
            self.age_group = 'child'
        elif self.age <= 19:
            self.age_group = 'teen'
        elif self.age <= 29:
            self.age_group = 'young_adult'
        elif self.age <= 59:
            self.age_group = 'adult'
        else:
            self.age_group = 'senior'
        
        super().save(*args, **kwargs)
        
        
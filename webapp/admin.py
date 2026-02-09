from django.contrib import admin
from django.utils.html import format_html
from .models import Passenger, PredictionRecord

# Register your models here.

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    """Admin interface for Titanic Passenger data"""
    
    list_display = (
        'passenger_id', 
        'name', 
        'sex', 
        'age', 
        'pclass', 
        'survived', 
        'family_size', 
        'age_group',
    )
    
    list_filter = (
        'survived',
        'pclass',
        'sex',
        'age_group',
        'embarked',
    )
    
    search_fields = (
        'name',
        'ticket',
        'cabin',
    )
    


@admin.register(PredictionRecord)
class PredictionRecordAdmin(admin.ModelAdmin):
    """Admin interface for user prediction records"""
    
    list_display = (
        'id', 
        'name',
        'sex',
        'age',
        'embarked',
        'family_size',
        'age_group',
        'prediction_display',
        'created_at',
    )
    
    list_filter = (
        'survived_prediction',
        'sex',
        'embarked',
        'age_group',
    )
    
    search_fields = (
        'name',
        'ticket',
        'cabin',
    )
    
    readonly_fields = (
        'created_at',
        'family_size',
        'age_group',
    )
    
    def prediction_display(self, obj):
        if obj.survived_prediction is None:
            return format_html('<span class="badge bg-secondary">Pending</span>')
        if obj.survived_prediction:
            prob = f"{obj.probability*100:.1f}%" if obj.probability else "N/A"
            return format_html('<span class="badge bg-success">Survived ({})</span>', prob)
        else:
            prob = f"{obj.probability*100:.1f}%" if obj.probability else "N/A"
            return format_html('<span class="badge bg-danger">Not Survived ({})</span>', prob)
    prediction_display.short_description = 'Prediction'
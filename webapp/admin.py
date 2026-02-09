from django.contrib import admin
from django.utils.html import format_html
from .models import Passenger, PredictionRecord

# Register your models here.

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    """Admin interface for Titanic Passenger data"""
    
    list_display = (
        'passenger_id',
        'name_display',
        'pclass',
        'sex',
        'age_display',
        'survival_status',
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
    
    # Custom display methods
    def name_display(self, obj):
        return obj.name[:30] + '...' if len(obj.name) > 30 else obj.name
    name_display.short_description = 'Name'
    
    def age_display(self, obj):
        return f"{obj.age:.1f}" if obj.age else "N/A"
    age_display.short_description = 'Age'
    
    def survival_status(self, obj):
        if obj.survived:
            return format_html('<span class="badge bg-success">Survived</span>')
        else:
            return format_html('<span class="badge bg-danger">Perished</span>')
    survival_status.short_description = 'Status'
    

@admin.register(PredictionRecord)
class PredictionRecordAdmin(admin.ModelAdmin):
    """Admin interface for user prediction records"""
    
    list_display = (
        'id',
        'name_display',
        'sex',
        'age_display',
        'embarked',
        'family_size',
        'age_group',
        'prediction_status',
        'created_at_display',
    )
    
    list_filter = (
        'survived_prediction',
        'sex',
        'age_group',
        'embarked',
        'created_at',
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
    
    fieldsets = (
        ('Passenger Information (Required)', {
            'fields': (
                'name',
                ('sex', 'age'),
                ('parch', 'embarked'),
            )
        }),
        
        ('Additional Information (Optional)', {
            'fields': (
                'sibsp',
                ('ticket', 'fare'),
                'cabin',
            ),
            'classes': ('collapse',),
        }),
        
        ('Engineered Features (Auto-calculated)', {
            'fields': (
                ('family_size', 'age_group'),
            ),
            'classes': ('collapse',),
        }),
        
        ('Prediction Results', {
            'fields': (
                ('survived_prediction', 'probability'),
                'created_at',
            )
        }),
    )
    

    # Custom display methods
    def name_display(self, obj):
        return obj.name[:25] + '...' if len(obj.name) > 25 else obj.name
    name_display.short_description = 'Name'
    
    def age_display(self, obj):
        return f"{obj.age:.1f}"
    age_display.short_description = 'Age'
    
    def prediction_status(self, obj):
        if obj.survived_prediction is None:
            return format_html('<span class="badge bg-secondary">Pending</span>')
        
        if obj.survived_prediction:
            prob = obj.get_probability_percentage()
            return format_html(
                '<span class="badge bg-success">Survived ({})</span>',
                prob
            )
        else:
            prob = obj.get_probability_percentage()
            return format_html(
                '<span class="badge bg-danger">Not Survived ({})</span>',
                prob
            )
    prediction_status.short_description = 'Prediction'
    
    
    def created_at_display(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M")
    created_at_display.short_description = 'Created'
    
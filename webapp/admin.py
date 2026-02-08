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
        'class_gender_display',
        'age_family_display',
        'survival_status_display',
        'data_source',
    )
    
    list_filter = (
        'survived',
        'pclass',
        'sex',
        'age_group',
        'embarked',
        'data_source',
    )
    
    search_fields = (
        'name',
        'ticket',
        'cabin',
    )
    
    readonly_fields = (
        'family_size',
        'age_group',
        'features_json',
    )
    
    fieldsets = (
        ('Passenger Information', {
            'fields': (
                'passenger_id',
                'survived',
                ('pclass', 'data_source'),
                'name',
                ('sex', 'age'),
                ('sibsp', 'parch'),
            )
        }),
        
        ('Travel Details', {
            'fields': (
                'ticket',
                'fare',
                'cabin',
                'embarked',
            )
        }),

        ('Engineered Features', {
            'fields': (
                ('family_size', 'age_group'),
                'features_json',
            )
        }),
    )
    
    ordering = ('passenger_id',)
    
    
    # Custom display methods
    def name_display(self, obj):
        return obj.name[:30] + '...' if len(obj.name) > 30 else obj.name
    name_display.short_description = 'Name'
    
    def class_gender_display(self, obj):
        return f"{obj.get_pclass_display()[:1]}, {obj.get_sex_display()[:1]}"
    class_gender_display.short_description = 'Class/Gender'
    
    def age_family_display(self, obj):
        age_str = f"{obj.age:.0f}" if obj.age else "?"
        return f"Age: {age_str}, Family: {obj.family_size}"
    age_family_display.short_description = 'Age/Family'
    
    def survival_status_display(self, obj):
        if obj.survived:
            return format_html('<span class="badge bg-success">Survived</span>')
        else:
            return format_html('<span class="badge bg-danger">Perished</span>')
    survival_status_display.short_description = 'Survival'
    
    
    # Admin actions
    actions = ['recalculate_features']
    
    def recalculate_features(self, request, queryset):
        """Recalculate engineered features for selected passengers"""
        updated = 0
        for passenger in queryset:
            passenger.save()  # This triggers feature calculation
            updated += 1
        
        self.message_user(
            request,
            f"Successfully recalculated features for {updated} passengers."
        )
    recalculate_features.short_description = "Recalculate engineered features"


@admin.register(PredictionRecord)
class PredictionRecordAdmin(admin.ModelAdmin):
    """Admin interface for user prediction records"""
    
    list_display = (
        'id',
        'name_display',
        'class_gender_display',
        'age_family_display',
        'prediction_result_display',
        'created_at_display',
    )
    
    list_filter = (
        'survived_prediction',
        'pclass',
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
        'updated_at',
        'family_size',
        'age_group',
        'session_id',
        'user_agent',
    )
    
    fieldsets = (
        ('Passenger Information (Required)', {
            'fields': (
                'name',
                ('pclass', 'sex'),
                ('age', 'embarked'),
                ('sibsp', 'parch'),
            )
        }),
        
        ('Additional Information (Optional)', {
            'fields': (
                'ticket',
                'fare',
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
                ('ml_model_used', 'model_version'),
            )
        }),
        
        ('System Information', {
            'fields': (
                ('created_at', 'updated_at'),
                ('session_id', 'user_agent'),
            ),
            'classes': ('collapse',),
        }),
    )
    
    ordering = ('-created_at',)

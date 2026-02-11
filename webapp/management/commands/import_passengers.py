import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from webapp.models import Passenger  

class Command(BaseCommand):
    help = 'Import cleaned Titanic passenger data from titanic_clean_train.csv'

    def handle(self, *args, **kwargs):
        csv_path = os.path.join(settings.BASE_DIR, 'ml', 'titanic_data', 'titanic_clean_train.csv')     #'ml'-'titanic_data'-'titanic_cleaned_train.csv'
        
        if not os.path.exists(csv_path):
            self.stderr.write(self.style.ERROR(f'File not found: {csv_path}'))
            return

        with open(csv_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            passengers = []
            for row in reader:
                # Map CSV columns to model fields
                passenger = Passenger(
                    passenger_id=int(row['PassengerId']),
                    survived=bool(int(row['Survived'])),
                    pclass=int(row['Pclass']),
                    name=row['Name'],
                    sex=row['Sex'],
                    age=int(row['Age']) if row['Age'] else None,  #covert to int
                    sibsp=int(row['SibSp']),
                    parch=int(row['Parch']),
                    ticket=row['Ticket'],
                    fare=float(row['Fare']) if row['Fare'] else None,
                    cabin=row.get('Cabin', ''),
                    embarked=row.get('Embarked', ''),
                    # Engineered features are already in CSV or will be auto-calculated in save()
                    data_source='train',
                )
                passengers.append(passenger)
            
            # Bulk insert for efficiency
            Passenger.objects.bulk_create(passengers, ignore_conflicts=True)
            
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {len(passengers)} passengers.'))
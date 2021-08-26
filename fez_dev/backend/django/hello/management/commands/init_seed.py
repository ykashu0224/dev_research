from django.core.management.base import BaseCommand
from django_seed import Seed
from hello import models as hello_models
from datetime import datetime

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        self.create_init_data()

    def create_init_data(self, *args, **options):
        seeder = Seed.seeder()
        seeder.add_entity(
            hello_models.Hello,
            1,
            {
                "content": 'hello world',
                "regist_date": datetime.now(),
                "update_date": datetime.now(),
            }
        )
        seeder.execute()
        
        self.stdout.write(self.style.SUCCESS("init created!"))
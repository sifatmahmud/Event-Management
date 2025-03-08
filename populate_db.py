import os
import django
from faker import Faker
import random
from events.models import Event, Participant, Category 
from django.utils.timezone import now, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')
django.setup()


# def populate_db():
#     fake = Faker()

#     categories = []
#     for _ in range(20):
#         category = Category.objects.create(
#             name=fake.word(),
#             description=fake.text()
#         )
#         categories.append(category) 


#     events = []
#     for _ in range(20):
#         event = Event.objects.create(
#             name=fake.company(),  
#             description=fake.text(),
#             date=fake.date_this_year(),
#             time=fake.time(),
#             location=fake.address(),
#             category=fake.random_element(categories) 
#         )
#         events.append(event)  


#     for _ in range(50):
#         participant = Participant.objects.create(
#         name=fake.name(),
#         email=fake.email()
#     )

#     participant.events.set(fake.random_elements(events, unique=True, length=fake.random_int(min=1, max=5)))


def populate_db():
    fake = Faker()

# Create Categories
    categories = []
    for _ in range(5):
        category = Category.objects.create(
            name=fake.word().capitalize(),
            description=fake.text()
        )
        categories.append(category)

# Create Events
    events = []
    for _ in range(10):
        event = Event.objects.create(
            name=fake.catch_phrase(),
            description=fake.text(),
            date=fake.date_between(start_date="-30d", end_date="+30d"),
            time=fake.time() if random.choice([True, False]) else None,
            location=fake.address(),
            category=random.choice(categories)
        )
        events.append(event)

    # Create Participants
    for _ in range(20):
        participant = Participant.objects.create(
            name=fake.name(),
            email=fake.email(),
        )
        assigned_events = random.sample(events, random.randint(1, 5))  # Assign 1 to 5 events
        participant.events.set(assigned_events)

print("Fake data successfully generated!")

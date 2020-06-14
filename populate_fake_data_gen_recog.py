import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','sai_site.settings')

import django
django.setup()

# Fake population script
import random
from gender_recog.models import Check,CheckF
from faker import Faker

fakegen = Faker()
names = ['john','david','tom','steve','adam']

def add_name():
    c = Check.objects.get_or_create(name = random.choice(names))[0]
    c.save()
    return c

def populate(N=5):
    for entry in range(N):

        #get name for entry
        name = add_name()

        #create fake data
        fake_url = fakegen.url()

        #create a fake CheckF entry
        checkf = CheckF.objects.get_or_create(for_name = name, url = fake_url)[0]

if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('population completed!')

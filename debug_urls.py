import os
import django
from django.urls import get_resolver

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farm_market.settings')
django.setup()

resolver = get_resolver()
for pattern in resolver.url_patterns:
    print(pattern)

from typing import Mapping
from django.contrib import admin
from .models import Account, UniRank
# Register your models here.
admin.site.register(Account)
admin.site.register(UniRank)
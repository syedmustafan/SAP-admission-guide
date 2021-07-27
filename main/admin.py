from typing import Mapping
from django.contrib import admin
from .models import Account, UniRank,Contact
# Register your models here.
admin.site.register(Account)
admin.site.register(UniRank)
admin.site.register(Contact)
from django.contrib import admin
from .models import User, Vacancy, Candidate

admin.site.register(User)
admin.site.register(Vacancy)
admin.site.register(Candidate)
from django.contrib import admin

# Registering the Question model.
from .models import Question

admin.site.register(Question)
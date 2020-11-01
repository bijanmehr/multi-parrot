from django.contrib import admin
from parrot_control import models as website_models


admin.site.register(website_models.ParrotCommand)

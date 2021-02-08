from django.contrib import admin

# Register and import your models here.
from .models import * #includes Customer & Products and ...

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)

from django.contrib import admin
from .models import product, category, images, review,order,status

# Register your models here.
admin.site.register(product)
admin.site.register(category)
admin.site.register(images)
admin.site.register(review)
admin.site.register(order)
admin.site.register(status)
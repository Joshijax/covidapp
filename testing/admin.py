from testing.models import Options, Questions
from django.contrib import admin

# Register your models here.
class QuestionsAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'points',
    )
admin.site.register(Questions,QuestionsAdmin)
admin.site.register(Options)
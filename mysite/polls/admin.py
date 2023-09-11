from django.contrib import admin
from .models import Question, Choice
# Register your models here.

# ADDING MORE CUSTOM TO OUR MODEL REPRS IN THE ADMIN
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionFieldAdmin(admin.ModelAdmin):
    fields = ["question_text", "pub_date"]
    inlines = [ChoiceInline]
    
    
class QuestionFieldSetAdmin(admin.ModelAdmin):
    fieldsets = [
       (None, {"fields": ["question_text"]}),
       ("Publish Date Information", {"fields": ["pub_date"], "classes":"collasped"})
    ]
    inlines = [ChoiceInline]

    
admin.site.register(Question, QuestionFieldAdmin)


from django.contrib import admin
from AdminApp.models import Category
from AdminApp.models import Question
from userApp.models import allResult

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","cat_name","description")

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id","que","ans","option1","option2","option3","option4","category")

class AllResultAdmin(admin.ModelAdmin):
    list_display = ("user","category","correct","total","per")

admin.site.register(Category,CategoryAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(allResult,AllResultAdmin)
from django.contrib import admin
from .models import Choice, Question # tell the admin that Question objects have an admin interface

# Register your models here.
# admin.site.register(Question)

class ChoiceInline(admin.TabularInline): #admin.StackedInline -> admin.TabularInline 較易讀
    model = Choice
    extra = 3 # 除了原本的選項外，另外多顯示三個空的選項欄

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently') # 在首頁的問題清單要顯示哪些內容
    list_filter = ['pub_date']
    search_fields = ['question_text']
    # fields = ['pub_date', 'question_text'] # 最陽春
    fieldsets = [
        (None, {'fields': ['question_text']}), 
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']})
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
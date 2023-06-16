from django.contrib import admin
from django import forms
from .models import Choice, Question # tell the admin that Question objects have an admin interface

# Register your models here.
# admin.site.register(Question)

class ChoiceInline(admin.TabularInline): #admin.StackedInline -> admin.TabularInline 較易讀
    model = Choice
    extra = 3 # 除了原本的選項外，另外多顯示三個空的選項欄

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']

class MultipleChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']
        widgets = {
            'choice_text': forms.CheckboxSelectMultiple
        }

class QuestionAdminForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'is_multiple_choice', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        (None, {'fields': ['question_text', 'is_multiple_choice']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]
    list_editable = ['is_multiple_choice']

    def get_form(self, request, obj=None, **kwargs):
        if obj and obj.is_multiple_choice:
            self.form = MultipleChoiceForm
        else:
            self.form = ChoiceForm
        return super().get_form(request, obj, **kwargs)



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
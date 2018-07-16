#-*- coding: utf-8 -*-
from django.contrib import admin

from .models import Choice, Poll
from .models import HowTo, Step


class ChoiceInline(admin.TabularInline):
    model = Choice
    readonly_fields = ('votes',)
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question'],}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question',)
    search_fields = ['question']


class StepInline(admin.TabularInline):
    model = Step
    extra = 3


class HowToAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title Information', {'fields': ['title']}),
        ('Time of Publishing', {'fields': ['pub_date']}),
        ('Introduction', {'fields': ['intro']}),
        ('Tags', {'fields': ['tags']}),
    ]
    inlines = [StepInline]
    list_display = ('title', 'pub_date', 'intro', 'tag_list')
    search_fields = ['title']

    def get_queryset(self, request):
        return super(HowToAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
admin.site.register(HowTo, HowToAdmin)

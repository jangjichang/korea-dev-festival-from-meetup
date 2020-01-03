from django.contrib import admin
from event.models import (Category, FestaCrawling, MeetupCrawling,
                          EventusCrawling, FacebookCrawling, UserrequestEvent,
                          WaitingEvent, DevEvent, NotDevEvent)


def from_MeetupCrawling_to_WaitingEvent(modeladmin, request, queryset):
    for meetup_instance in queryset:
        meetup_dict = meetup_instance.__dict__
        meetup_dict.pop('_state')
        meetup_dict.pop('id')
        waiting_event = WaitingEvent(**meetup_dict)
        waiting_event.save()

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(FestaCrawling)
class FestaCrawlingAdmin(admin.ModelAdmin):
    pass


@admin.register(MeetupCrawling)
class MeetupCrawlingAdmin(admin.ModelAdmin):
    actions = [from_MeetupCrawling_to_WaitingEvent]


@admin.register(EventusCrawling)
class EventusCrawlingAdmin(admin.ModelAdmin):
    pass


@admin.register(FacebookCrawling)
class FacebookCrawlingAdmin(admin.ModelAdmin):
    pass


@admin.register(UserrequestEvent)
class UserrequestEventAdmin(admin.ModelAdmin):
    pass


@admin.register(WaitingEvent)
class WaitingEventAdmin(admin.ModelAdmin):
    pass


@admin.register(DevEvent)
class DevEventAdmin(admin.ModelAdmin):
    pass


@admin.register(NotDevEvent)
class NotDevEvent(admin.ModelAdmin):
    pass

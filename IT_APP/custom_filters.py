# IT_APP/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def get_video_id(value):
    # Assuming the value is a full YouTube URL, extract the video ID
    return value.split('v=')[1].split('&')[0] if value else ''

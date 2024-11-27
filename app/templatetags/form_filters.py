# your_app/templatetags/form_filters.py
from django import template

register = template.Library()

@register.filter
def add_class(field, class_name):
    """
    Add a CSS class to a form field.
    """
    return field.as_widget(attrs={'class': class_name})

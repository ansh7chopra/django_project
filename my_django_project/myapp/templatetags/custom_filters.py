from django import template

register = template.Library()

@register.filter
def seat_count(seats):
    if seats:
        return len(seats.split(','))
    return 0

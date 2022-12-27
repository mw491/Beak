from django import template
from chirps.models import Chirp
register = template.Library()

@register.filter(name='vote')
def vote(chirp):
    return chirp.up_votes_count() - chirp.down_votes_count()

@register.filter(name='if_up_voted')
def if_up_voted(chirp, user):
    return bool(chirp.up_votes.filter(id=user.id).exists())

@register.filter(name='if_down_voted')
def if_up_voted(chirp, user):
    return bool(chirp.down_votes.filter(id=user.id).exists())
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

monthly_challenges = {
    "january": "january te sheet pore",
    "february": "international mother language day",
    "march": "march is march",
    "april": "brish rasi",
    "may": "january te sheet pore",
    "june": "international mother language day",
    "july": "march is march",
    "august": "brish rasi",
    "september": "january te sheet pore",
    "october": "international mother language day",
    "november": "march is march",
    "december": "brish rasi",
}


def monthly_challenges_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")

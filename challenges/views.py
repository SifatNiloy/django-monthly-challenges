from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthly_challenges = {
    "january": "January marks the start of a new year and is often a time for setting resolutions and goals.",
    "february": "February is the shortest month of the year.",
    "march": "March marks the transition from winter to spring.",
    "april": "April is a month associated with new beginnings and growth.",
    "may": "May is a time of blossoming flowers and increasing daylight hours.",
    "june": "June is the midpoint of the year and brings warmer weather.",
    "july": "July is a month associated with summer vacations and outdoor activities.",
    "august": "August is a time for relaxation and enjoying the last days of summer.",
    "september": "September marks the beginning of autumn and the return to school for many.",
    "october": "October is a month known for colorful fall foliage and harvest festivals.",
    "november": "November is a time for gratitude and reflection.",
    "december": None
    # "December is a month of celebrations and festive spirit."
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)

from django.shortcuts import render
from . import logic # Imports a module where I coded all the logic

# Create your views here.

month_names = [
'January',
'February',
'March',
'April',
'May',
'June',
'July',
'August',
'September',
'October',
'November',
'December'
]

def index(request):
    return render(request, "wimbotd/index.html", {
        "month_days" : range(1, 32),
        "months" : range(1, 13),
        "month_names" : month_names
    })

def result(request):

    if "dd" not in request.session:
        request.session = []

    dd = request.POST['dd']
    mm = request.POST['mm']
    day = request.POST['day']

    return render(request, "wimbotd/result.html", {
        "output" : logic.process(date=int(dd), month=int(mm), weekday=str(day)), # Output is "You will have your birthday on {weekday} in {years} years time.""
    })
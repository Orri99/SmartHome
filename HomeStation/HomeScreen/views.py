from django.shortcuts import render

reminders = [{'chore' : 'Skipta á rúmmi', 'date' : '10.4.2023'},
             {'chore' : 'Skúra', 'date' : '12.4.2023'}]

# Create your views here.
def home(request):
    context = {'reminders' : reminders}
    return render(request, "HomeScreen/home.html", context)
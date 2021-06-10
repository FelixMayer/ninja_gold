from django.shortcuts import render, HttpResponse, redirect
import random


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0

    context = {
        'gold': request.session['gold']
    }
    return render(request, 'index.html', context)

def process_money(request):
    if request.POST["location"] == 'farm':
        gold_earned = random.randint(10, 20)
    
    if request.POST["location"] == 'cave':
        gold_earned = random.randint(5, 10)

    if request.POST["location"] == 'house':
        gold_earned = random.randint(2, 5)
    
    if request.POST["location"] == 'casino':
        gold_earned = random.randint(-50, 50)
    
    request.session['gold'] += gold_earned
    return redirect('/')
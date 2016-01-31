from django.shortcuts import render
import random
import datetime
from time import strftime

# Create your views here.
def index(request):
  try:
    request.session['counter']
  except:
    request.session['counter'] = 0
  try:
    request.session['activities']
  except:
    request.session['activities'] = []


  return render(request, 'ninja/index.html')

def process_money(request):
  action = request.POST['action']
  if action == "farm":
    earn = random.randrange(10, 21)
  elif action == 'cave':
    earn = random.randrange(5, 11)
  elif action == "house":
    earn = random.randrange(2, 6)
  elif action == "casino":
    earn = random.randrange(-50, 50)

  request.session['counter'] += earn

  timeNow = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S %p')
  if earn >= 0 :
    newAction = {
      'status' : 'earn',
      'action' : "Earned {} gold from {} ({})".format(earn, action, timeNow)
    }
  else:
    newAction = {
      'status' : 'lost',
      'action' : "Entered Casino and lost {} gold.. Ouch.. ({})".format(-earn, timeNow)
    }



  request.session['activities'].append(newAction)
  return render(request, 'ninja/index.html')

def reset(request):
  request.session['activities'] = []
  request.session['counter'] = 0
  return render(request, 'ninja/index.html')



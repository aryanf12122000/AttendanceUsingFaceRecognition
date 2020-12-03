from django.shortcuts import render
import requests
import sys
from subprocess import run, PIPE

def button(request):
    return render(request, 'home.html')

def office(request):
    data = requests.get("https://www.microsoft.com/en-in/microsoft-365/free-office-online-for-the-web")
    #print(data.text)
    data = data.text
    return render(request, 'home.html', {'data': data})

def code(request):
    out = run([sys.executable, '/Users/Arnold/Desktop/work/summerproject/FR_PYCHARM/attendance project.py']) #path to program
    #print(out)
    return render(request, 'home.html', {'data1': out})

def attend(request):
    output = run([sys.executable, '/Users/Arnold/Desktop/work/summerproject/FR_PYCHARM/attendlist.py'], shell=False, stdout=PIPE) #path to attend prgm
    data2=output.stdout.decode()
    print(data2)
    file1 = open('Attendance.txt', 'w')
    file1.write(data2)
    file1.close()
    return render(request, 'home.html', {'data2': data2})


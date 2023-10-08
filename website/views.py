from django.shortcuts import render

def homeView (req):
    return render(req, 'website/home.html')

def aboutView (req):
    return render(req, 'website/about.html')

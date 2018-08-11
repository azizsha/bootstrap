# -*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponse
from django.db import connection
import smtplib
from email.mime.text import MIMEText
import cgi, os
from django.views.generic import ListView,DetailView

from django.db.models import Q

def asd(request):
    return render(request, 'glav/ind.html')


def posts(request):
    return render(request, 'glav/posts.html')

def about(request):
    return render(request, 'glav/aboutt.html')

def check_user_name(request):
    messages = request.GET['message']
    TO = "tanzila89288928@gmail.com"
    SUBJECT = request.GET['email'] + '-' + request.GET['phone'] + '-' + request.GET['name']
    TEXT = request.GET['message']
    gmail_sender = 'fizikaquantum@gmail.com'
    gmail_passwd = '42241416'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(gmail_sender, gmail_passwd)
    BODY = '\r\n'.join(['To: %s' % TO,'FROM: %s' % gmail_sender,'Subject: %s' % SUBJECT,'',TEXT] )
    server.sendmail(gmail_sender, [TO], BODY.encode('utf-8'))
    server.quit()
    return HttpResponse('Yes')

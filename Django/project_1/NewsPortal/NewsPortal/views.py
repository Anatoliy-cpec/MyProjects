
from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import (
    View
)

from django.utils import timezone

from django.shortcuts import redirect

import pytz



class HomePage(View):

    template_name = 'home.html'

    def get(self, request):
  
        context = {
            'current_time': timezone.localtime(timezone.now()),
            'timezones': pytz.common_timezones #  добавляем в контекст все доступные часовые пояса
        }
        
        return HttpResponse(render(request, 'home.html', context)) 
      
    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect(self.request.path)
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import get_object_or_404
from feedbacks.models import Presentation, Question
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def index(request):

    if request.method  == 'GET':
        if not request.user.is_authenticated:
            messages.info(request, 'Please login first...')
            return redirect('accounts:log_in')
        else:
            try:
                presentation_list = Presentation.objects.all()
                data = {
                    'ps': presentation_list,
                }
                return render(request, 'index.html', data)
            except:
                return HttpResponseBadRequest('Bad')


    # return render(request, 'index.html', {})



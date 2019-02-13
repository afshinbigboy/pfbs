from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import get_object_or_404
from feeedbacks.models import *
# Create your views here.


@login_required
def result_list(request):
  data = {
    ''
  }
  return render(request, 'result_list.html', data)


@login_required
def result_detail(request, presentation_id):

  if request.method == 'POST':
    presentation_obj = get_object_or_404(Presentation, id=presentation_id)
    feeedback_list = Feeedbacks.objects.filter(presentation = presentation_obj)
    
    data = {
      ''
    }
    return render(request, 'result_detail.html', data)
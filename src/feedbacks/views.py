from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import get_object_or_404
from .models import Presentation, Question, Feedback
from django.contrib.auth.decorators import login_required
from accounts.models import User
from django.contrib import messages

# Create your views here.


@login_required
def presentation(request):
    
    if request.method == 'POST':
      try:
        presentation_id = request.GET.get('presentation', 0)
        if not presentation_id:
            return HttpResponseBadRequest('choose a presentation!')
        
        presentation_obj = get_object_or_404(Presentation, id=presentation_id)

        print(request.POST)

        for k, v in request.POST.items():
          if k[0] != 'q':
            continue
          presentor_id = int(k.split('_')[1])
          if presentor_id > 0:
            question = Question.objects.get(rank=int(k.split('_')[-1]))
            print(question)
            instance = {
              'presentor': User.objects.get(id=presentor_id),
              'student': request.user,
              'presentation': presentation_obj,
              'question': question,
            }
            obj, created = Feedback.objects.get_or_create(**instance, defaults={'score': int(v)})
            if not created:
              obj.score = int(v)
              obj.save()

        messages.success(request, 'Thank You.')  
        return redirect('index')
      except:
        messages.error(request, 'Ops... Bad Params!')  

      
    presentation_id = request.GET.get('presentation', 0)
    if not presentation_id:
        return HttpResponseBadRequest('choose a presentation!')
    presentation_obj = get_object_or_404(Presentation, id=presentation_id)
    question_list = Question.objects.all()
    data = {
        'qs': question_list,
        'p': presentation_obj,
        'scores': range(1,11),
    }

    return render(request, 'feedback.html', data)
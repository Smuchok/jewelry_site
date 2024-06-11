from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *

from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# for test email sending
from django.conf import settings
from django.core.mail import send_mail


cats = {
    "weddingring": WeddingRing, 
    "circletring": CircletRing, 
    "sealring": SealRing,
    "chainlet": Chainlet, 
    "pendant": Pendant, 
    "necklace": Necklace,
    "earrings": Earrings, 
    "kaf": Kaf,
    "bracelet": Bracelet
    }
cats_list = (WeddingRing, CircletRing, SealRing, Chainlet, Pendant, Necklace, Earrings, Kaf, Bracelet)

# context = {
#     'feedback_form': FeedbackForm(),
# }

def check_feedback_form(request, context={}, feedback_form=FeedbackForm()):
    print('feedback')
    if request.method == 'POST':
        print('POST CATALOG')
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            # form.instance.applicant = request.user
            print('IS VALID')
            feedback_form.save()
            context['form_success_feedback'] = True
            # messages.success(request, 'Education Added Successfully')
            # return redirect('')
        else:
            print('IS NOT VALID')
            # feedback_form.save()
    else:
        print('NOT POST')

    context['feedback_form'] = FeedbackForm()

    return request, context


def check_advice_form(request, context={}, feedback_form=AdviceForm()):
    print('advice')
    if request.method == 'POST':
        print('POST advice')
        advice_form = AdviceForm(request.POST)
        if advice_form.is_valid():
            # form.instance.applicant = request.user
            print('IS VALID')
            advice_form.save()
            context['form_success_advice'] = True
            # messages.success(request, 'Education Added Successfully')
            # return redirect('')
        else:
            print('IS NOT VALID')
            # advice_form.save()
    else:
        print('NOT POST')

    context['advice_form'] = AdviceForm()

    return request, context



def index(request):

    context = {
        'title': "Головна",
        'active': 1,
        'feedback_form': FeedbackForm(),
        'advice_from': AdviceForm()
    }
    
    request, context = check_feedback_form(request, context)
    request, context = check_advice_form(request, context)
    # return HttpResponse(text)
    return render(request, 'webjew/index.html', context=context)

def all_jew(request):
    text = "<h1>Вся біжутерія</h1>"
    all_jew = []
    for m in cats_list:
        # print(f"{m=}")
        jews = m.objects.all()
        for mm in jews:
            # print(f"{mm=}")
            all_jew.append(mm)
            text += f"<p>{mm.title} - {mm.price} ₴ - {mm._meta.verbose_name.title()}</p>"
    
    # text += "</ul>"

    context = {
        'title': 'Вся біжутерія',
        'jews': all_jew,
    }

    # return HttpResponse(text)
    return render(request, 'webjew/all.html', context=context)

def catalog(request):
    all_cat= []
    for m in cats_list:
        m_name = m._meta.verbose_name_plural.title()
        all_cat.append((m_name, m._meta.model_name, m.category_image()))

    order_form = OrderForm()
    context = {
        'title': 'Каталог',
        'cats': all_cat,
        'active': 2,
        'order_form': order_form,
        'form_success': False,
        'feedback_form': FeedbackForm(),
    }
    
    if request.method == 'POST':
        print('POST CATALOG')
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            # form.instance.applicant = request.user
            print('IS VALID')
            order_form.save()
            context['form_success'] = True
            # messages.success(request, 'Education Added Successfully')
            # return redirect('')
        else:
            print('IS NOT VALID')
            # order_form.save()
    else:
        print('NOT POST')

    context['order_form'] = OrderForm()

    request, context = check_feedback_form(request, context)
    # return HttpResponse(text)
    return render(request, 'webjew/catalog.html', context=context)


@api_view(['GET'])
def api_catalog(request):
    all_cat= []
    for m in cats_list:
        cat = {}
        m_name = m._meta.verbose_name_plural.title()
        all_cat.append((m_name, m._meta.model_name))
        cat['m._meta.model_name'] = {
            'title': m._meta.model_name,
            'title_image': m.category_image()
        }
    
    result = [
        all_cat
    ]
    return Response(result)
    return JsonResponse(result, safe=False)

# @api_view(['GET'])
# def api_catalog2(request):
#     app = CircletRing.objects.all()
#     serializer = JewSerializer(app, many=True)
#     return Response(serializer.data)


def jews_by_catalog(request, category):
    cat = cats[category]
    jews = cat.objects.all()
    order_form = OrderForm()

    for j in jews:
        j.title_image = str(j.title_image).replace('webjew/', '')

    context = {
        'title': cat._meta.verbose_name_plural,
        'jews': jews,
        'category': category,
        'order_form': order_form,
        'form_success': False,
        'feedback_form': FeedbackForm(),
    }

    if request.method == 'POST':
        print('POST CATALOG')
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            # form.instance.applicant = request.user
            print('IS VALID')
            order_form.save()
            context['form_success'] = True
            # messages.success(request, 'Education Added Successfully')
            # return redirect('')
        else:
            print('IS NOT VALID')
            # order_form.save()
    else:
        print('NOT POST')

    context['order_form'] = OrderForm()

    request, context = check_feedback_form(request, context)
    return render(request, 'webjew/jews_by_cat.html', context=context)

# @api_view(['GET'])
# def api_jews_by_category(request, category):
#     cat = cats[category]
#     jews = cat.objects.all()
#     print(f'{category=}, {jews=}')
#     app = jews
#     serializer = JewSerializer(app, many=True)
#     # print(serializer.data)
#     for i in serializer.data:
#         if i['title_image'] != None:
#             i['title_image'] = '/static/webjew/img/jews/' + str(category) + i['title_image']
#         else:
#             i['title_image'] = None
            
#     return JsonResponse(serializer.data, safe=False)
#     return Response(serializer.data)


def jew_details(request, category, jew_id):
    cat = cats[category]
    jew = cat.objects.get(id=jew_id)
    jew.model3d = str(jew.model3d).replace('webjew/', '')

    context = {
        'title': jew.title,
        'jew': jew,
        'category': category,
        'feedback_form': FeedbackForm(),
    }

    request, context = check_feedback_form(request, context)
    return render(request, 'webjew/3d.html', context=context)

def about(request):
    team_about = {
        'title': 'Наша команда',
        'photo': 'Вернісаж.jpg',
        'description': "Ласкаво просимо до нашого світу вишуканих ювелірних виробів, де кожна прикраса — це унікальний шедевр, створений з любов'ю та майстерністю. Наша мета — надавати вам не тільки витончені прикраси, але і незабутні емоції. Ми пишаємося нашим професійним підходом до виготовлення кожного виробу, використовуючи найвищу якість матеріалів і дбайливо обираючи кожен елемент. Дозвольте нам допомогти вам обрати чудовий аксесуар, який стане не тільки частиною вашого стилю, але й часом пам'яті. Ласкаво просимо в наше ювелірне мистецтво, де краса завжди в деталях.",
        'feedback_form': FeedbackForm(),
    }
    # обовязково квадратні фото 1:1 до 250px!
    team = [
        {
            'name': 'Діана',
            'photo': 'Діана.jpg',
            'text': ['Студентка групи КН-51 Української академії друкарства', 'Дизайнер, контент мейкер, редактор, керівник проекту, тестувальник'],
       },
        {
            'name': 'Тарас',
            'photo': 'Тарас.jpg',
            'text': ['Студент групи ІСТ-5 Української академії друкарства', 'Backend- та Frontend- розробник  (Full Stack розробник, Python Developer)'],
        },        {
            'name': 'Олексій',
            'photo': 'Олексій.jpg',
            'text': ['Студент групи КН-52 Української академії друкарства', 'Редактор фото, редактор контенту, аналітик, помічник керівника, тестувальник'],
        },        {
            'name': 'Віталій',
            'photo': 'Віталій.jpg',
            'text': ['Студент групи КН-51 Української академії друкарства', 'Розробник мобільних додатків (Flutter Developer)'],
        },        {
            'name': 'Остап',
            'photo': 'Остап.jpg',
            'text': ['Ювелір, 3D-дизайнер та 3D-візуалізатор, оператор ЧПУ-станка',],
        },
    ]
    # team[4]['photo'] = 'none.jpg' # фотка заглушка

    context = {
        'title': "Про нас",
        'description': "Ласкаво просимо до нашого світу вишуканих ювелірних виробів, де кожна прикраса — це унікальний шедевр, створений з любов'ю та майстерністю. Наша мета — надавати вам не тільки витончені прикраси, але і незабутні емоції. Ми пишаємося нашим професійним підходом до виготовлення кожного виробу, використовуючи найвищу якість матеріалів і дбайливо обираючи кожен елемент. Дозвольте нам допомогти вам обрати чудовий аксесуар, який стане не тільки частиною вашого стилю, але й часом пам'яті. Ласкаво просимо в наше ювелірне мистецтво, де краса завжди в деталях.",
        'active': 3,
        'team': team,
        'team_about': team_about,
    }
    request, context = check_feedback_form(request, context)
    print(f'{context=}')
    return render(request, 'webjew/about.html', context=context)


def contact(request):
    context = {
        'title': "Контаки",
        'active': 4,
        'feedback_form': FeedbackForm(),
        'advice_from': AdviceForm(),
    }
    request, context = check_feedback_form(request, context)
    request, context = check_advice_form(request, context)
    return render(request, 'webjew/contact.html', context=context)

def steps(request):
    steps_list = [
        {'num': 1, 'image': 'step1.png', 'text': 'Обговорення ідеї та дизайну виробу з клієнтом, визначення розмірів'},
        {'num': 2, 'image': 'step2.png', 'text': 'Створення ескізу та 3D моделі'},
        {'num': 3, 'image': 'step33.jpg', 'text': 'Виготовлення воскової моделі (вручну або за допомогою МЛТУ-станка)'},
        {'num': 4, 'image': 'step4.png', 'text': 'Лиття виробу з обраного клієнтом металу'},
        {'num': 5, 'image': 'step55.jpg', 'text': 'Обробка виробу, шліфування, попереднє полірування'},
        {'num': 6, 'image': 'step66.jpg', 'text': 'Полірування або матування'},
        {'num': 7, 'image': 'step77.jpg', 'text': 'Кріплення дорогоцінного каміння та (або) виконання гравіювання'},
        {'num': 8, 'image': 'step88.jpg', 'text': 'Чорніння або нанесення покриття: родій, рутеній, емаль тощо'},
    ]
    context = {
        'title': "Кроки",
        # 'active': 4,
        'steps': steps_list,
        'feedback_form': FeedbackForm(),
    }
    request, context = check_feedback_form(request, context)
    return render(request, 'webjew/steps.html', context=context)

def jew3d(request):
    context = {
        'title': "3D Модель",
        'feedback_form': FeedbackForm(),
    }
    request, context = check_feedback_form(request, context)
    return render(request, 'webjew/jew3d.html', context=context)

def policy(request):
    context = {
        'title': 'Політика конфіденційності',
        'feedback_form': FeedbackForm(),
    }
    request, context = check_feedback_form(request, context)
    print(f'{context=}')
    return render(request, 'webjew/policy.html', context=context)

def test(request):
    # # email send test 
    # subject = 'Test subject'
    # message = 'test text'
    # email_from = settings.EMAIL_HOST_USER
    # recip_lst = ['taras.oselia@gmail.com',]
    # send_mail(subject, message, email_from, recip_lst)

    context = {
        'feedback_form': FeedbackForm(),
    }
    request, context = check_feedback_form(request, context)
    return render(request, 'webjew/test.html', context=context)
    # return HttpResponse('test page')

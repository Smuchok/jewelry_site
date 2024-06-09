from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import OrderForm

from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

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


def index(request):

    context = {
        'title': "Головна",
        'active': 1,
    }
    
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

    context = {
        'title': cat._meta.verbose_name_plural,
        'jews': jews,
        'category': category,
        'order_form': order_form,
        'form_success': False,
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

    context = {
        'title': jew.title,
        'jew': jew,
        'category': category,
    }

    return render(request, 'webjew/jew_details.html', context=context)

def about(request):
    team_about = {
        'title': 'Наша команда',
        'photo': 'Вернісаж.jpg',
        'description': "Ласкаво просимо до нашого світу вишуканих ювелірних виробів, де кожна прикраса — це унікальний шедевр, створений з любов'ю та майстерністю. Наша мета — надавати вам не тільки витончені прикраси, але і незабутні емоції. Ми пишаємося нашим професійним підходом до виготовлення кожного виробу, використовуючи найвищу якість матеріалів і дбайливо обираючи кожен елемент. Дозвольте нам допомогти вам обрати чудовий аксесуар, який стане не тільки частиною вашого стилю, але й часом пам'яті. Ласкаво просимо в наше ювелірне мистецтво, де краса завжди в деталях.",
    }
    # обовязково квадратні фото 1:1 до 250px!
    team = [
        {
            'name': 'Діана',
            'photo': 'Діана.jpg',
            'text': 'шось робила'
        },
        {
            'name': 'Тарас',
            'photo': 'Тарас.jpg',
            'text': 'шось робив'
        },        {
            'name': 'Олексій',
            'photo': 'Олексій.jpg',
            'text': 'шось робив'
        },        {
            'name': 'Віталій',
            'photo': 'Віталій.jpg',
            'text': 'шось робив'
        },        {
            'name': 'Остап',
            'photo': 'Остап.jpg',
            'text': 'шось робив'
        },
    ]
    team[4]['photo'] = 'none.jpg'

    context = {
        'title': "Про нас",
        'description': "Ласкаво просимо до нашого світу вишуканих ювелірних виробів, де кожна прикраса — це унікальний шедевр, створений з любов'ю та майстерністю. Наша мета — надавати вам не тільки витончені прикраси, але і незабутні емоції. Ми пишаємося нашим професійним підходом до виготовлення кожного виробу, використовуючи найвищу якість матеріалів і дбайливо обираючи кожен елемент. Дозвольте нам допомогти вам обрати чудовий аксесуар, який стане не тільки частиною вашого стилю, але й часом пам'яті. Ласкаво просимо в наше ювелірне мистецтво, де краса завжди в деталях.",
        'active': 3,
        'team': team,
        'team_about': team_about,
    }

    return render(request, 'webjew/about.html', context=context)

def contact(request):
    context = {
        'title': "Контаки",
        'active': 4,
    }

    return render(request, 'webjew/contact.html', context=context)

def steps(request):
    steps_list = [
        {'num': 1, 'image': 'step1.jpg', 'text': 'Обговорення ідеї та дизайну виробу з клієнтом, визначення розмірів'},
        {'num': 2, 'image': 'step2.jpg', 'text': 'Створення ескізу та 3D моделі'},
        {'num': 3, 'image': 'step3.jpg', 'text': 'Виготовлення воскової моделі (вручну або за допомогою МЛТУ-станка)'},
        {'num': 4, 'image': 'step4.jpg', 'text': 'Лиття виробу з обраного клієнтом металу'},
        {'num': 5, 'image': 'step5.jpg', 'text': 'Обробка виробу, шліфування, попереднє полірування'},
        {'num': 6, 'image': 'step6.jpg', 'text': 'Полірування або матування'},
        {'num': 7, 'image': 'step7.jpg', 'text': 'Кріплення дорогоцінного каміння та (або) виконання гравіювання'},
        {'num': 8, 'image': 'step8.jpg', 'text': 'Чорніння або нанесення покриття: родій, рутеній, емаль тощо'},
    ]
    context = {
        'title': "Кроки",
        # 'active': 4,
        'steps': steps_list,
    }

    return render(request, 'webjew/steps.html', context=context)

def jew3d(request):
    return render(request, 'webjew/jew3d.html')

def test(request):
    return render(request, 'webjew/test.html')

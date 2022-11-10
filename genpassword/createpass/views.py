from django.shortcuts import render, redirect
from .logical import gen_password


# TODO create API for this view ["get password"]
version_app = '1.0.0'
def index(request):
    return render(request, 'createpass/index.html')


def show_pas(request):
    if request.GET:
        try:
            password_length = int(request.GET['password_length_name'])
        except:
            return redirect('gen', permanent=True)
        special = request.GET.get('isSpecial_name', False)
        special = True if special == 'on' else False  # It is add layer to find out value of special
        simple_pas = request.GET.get('isMemorable', False)
        simple_pas = True if simple_pas == 'on' else False
        pases = [gen_password(length=password_length, special_symbols=special, simple_pas=simple_pas) for _ in range(5)]
        data = {'completed_pass': pases, 'isSimple': False}
        if simple_pas:
            data['isSimple'] = True
    else:
        return redirect('index')
    return render(request, 'createpass/show_pas.html', context=data)


def gen_pas(request):
    return render(request, 'createpass/generate_pas.html')


def about(request):
    return render(request, 'createpass/about.html')


def pageNotFound(request, exception):
    return render(request, 'createpass/pageNotFound.html')


def cleardb(request):
    # clear db
    return render(request, 'createpass/index.html')


# Russian views

def index_ru(request):
    return render(request, 'createpass/ru/index.html')


def show_pas_ru(request):
    if request.GET:
        try:
            password_length = int(request.GET['password_length_name'])
        except:
            return redirect('gen', permanent=True)
        special = request.GET.get('isSpecial_name', False)
        # It is add layer to find out value of special
        special = True if special == 'on' else False
        simple_pas = request.GET.get('isMemorable', False)
        simple_pas = True if simple_pas == 'on' else False
        pases = [gen_password(length=password_length, special_symbols=special,
                              simple_pas=simple_pas) for _ in range(5)]
        data = {'completed_pass': pases, 'isSimple': False}
        if simple_pas:
            data['isSimple'] = True
    else:
        return redirect('index_ru')
    return render(request, 'createpass/ru/show_pas.html', context=data)


def gen_pas_ru(request):
    return render(request, 'createpass/ru/generate_pas.html')


def about_ru(request):
    return render(request, 'createpass/ru/about.html')


def pageNotFound_ru(request, exception):
    return render(request, 'createpass/ru/pageNotFound.html')

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
        pases = [gen_password(length=password_length, special_symbols=special) for _ in range(5)]
        data = {'completed_pass': pases}
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
    
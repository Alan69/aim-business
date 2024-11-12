from django.shortcuts import render
from .forms import ContactForm
from .models import Opens


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    form = ContactForm(request.POST or None)
    ip = get_client_ip(request)
    if request.method == 'POST':
        print('post - ok')
        res = 'no'
        if form.is_valid():
            print('valid - ok')
            form.save()
            res = 'ok'
        data = {
            'title': 'Главная',
            'form': form,
            'result': res,
            'ip': ip,
        }
        return render(request, "main/index.html", data)
    data = {
        'title': 'Главная',
        'form': form,
        'result': 'no',
        'ip': ip,
    }
    client = Opens(ip=ip)
    client.save()
    return render(request, "main/index.html", data)


def pb_add(request, slug):
    user = request.user
    if len(slug) == 12:
        company = Company.objects.filter(slug=slug, author=user).first()
    else:
        return reverse_lazy("post_gen")
    form = NewPBForm(request.POST or None)
    if request.method == 'POST':
        form.instance.author = user
        form.instance.company = company
        form.instance.slug = get_slug(PB)
        if form.is_valid():
            form.save()
            return redirect(company.get_absolute_url())
    context = {
        'title': 'Мои компании',
        'title1': company.name,
        'form': form,
        'action': 'Добавление продукта'
    }
    return render(request, "posts/add_pb.html", context)
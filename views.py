from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from apps.product.models import Files, FileTypes, TopFileTypes


def size_format(b):
    if b < 1000:
        return '%i' % b + ' B'
    elif 1000 <= b < 1000000:
        return '%.1f' % float(b / 1000) + ' KB'
    elif 1000000 <= b < 1000000000:
        return '%.1f' % float(b / 1000000) + ' MB'
    elif 1000000000 <= b < 1000000000000:
        return '%.1f' % float(b / 1000000000) + ' GB'
    elif 1000000000000 <= b:
        return '%.1f' % float(b / 1000000000000) + ' TB'


@login_required
def file_upload(request):
    if request.method == "POST":
        if request.FILES["file_name"]:
            file_text = str(request.FILES["file_name"])

            file_input = request.FILES["file_name"]

            file_type = file_text.split(".")
            file_type = file_type[1]
            file_type = FileTypes.objects.filter(text=file_type).last()

            blob = request.FILES['file_name'].read()
            file_size = len(blob)
            file_size_custom = size_format(file_size)

            files_create = Files.objects.create(
                text=file_text,
                user=request.user,
                file=file_input,
                type=file_type,
                size=file_size_custom,
                kb_size=file_size,
            )
            if files_create:
                messages.success(request, "Dosya Yükleme Başarılı")
            else:
                messages.warning(request, "Beklenmedik Bir Hata Oluştu Hata Kodu:1")
            return redirect('mainpage:index')
        else:
            messages.warning(request, "Beklenmedik Bir Hata Oluştu Hata Kodu:2")
            return redirect('mainpage:index')
    else:
        messages.warning(request, "Beklenmedik Bir Hata Oluştu Hata Kodu:3")
        return redirect('mainpage:index')


def get_file_upload(request):
    data = "Başarılı"
    context = {
        'data': data,
    }
    return render(request, "apps/api/data.html", context)


def files_api(request):
    session_email = request.GET.get('session_email')
    files = Files.objects.filter(user__email=session_email)
    file_types = TopFileTypes.objects.filter()
    context = {
        'files': files,
        'file_types': file_types,
    }
    return render(request, "apps/files/get_file_api.html", context)

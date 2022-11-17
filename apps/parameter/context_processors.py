from django.utils.translation import get_language

from apps.mainpage.models import MainPage
from apps.parameter.models import SiteSettings


def site(request):
    site_settings = SiteSettings.objects.last()
    main_page = MainPage.objects.last()
    urlObject = request.get_host()
    return {'site_settings': site_settings, 'main_page': main_page, 'showURL': urlObject, }


def menu(request):

    lang = get_language()
    return {'lang': lang}

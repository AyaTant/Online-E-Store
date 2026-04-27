from bmesproject.bmesproject import settings
def bmes_context(request):
    return {
        'site_name': settings.SITE_NAME,
    }
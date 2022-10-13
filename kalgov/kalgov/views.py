from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

class PublicSafetyPage(TemplateView):
    template_name = 'services/public_safety.html'

class PublicWorkPage(TemplateView):
    template_name = 'services/public_work.html'

class IdPage(TemplateView):
    template_name = 'services/id.html'

class RecreationPage(TemplateView):
    template_name = 'services/recreation.html'

class MarinePage(TemplateView):
    template_name = 'services/marine.html'

class CustomPage(TemplateView):
    template_name = 'services/custom.html'

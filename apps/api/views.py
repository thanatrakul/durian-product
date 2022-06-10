from django.views.generic import TemplateView


class ApiVersionView(TemplateView):
    template_name = "api/versions.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        versions = [
            {
                "number": 'Current',
                "name": "Current Version",
                "url": "/api/v1/"
            },
            {
                "number": '1.0',
                "name": "v1",
                "url": "/api/v1/"
            }
        ]
        context['versions'] = versions
        return context

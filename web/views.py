from typing import Any, Dict

from django.views.generic import TemplateView

from .models import Manhwa


class ManhwaTemplateView(TemplateView):
    template_name = "web/index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["manhwas"] = Manhwa.objects.all()[:10]
        return ctx

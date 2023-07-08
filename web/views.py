from typing import Any, Dict, List

from django.views.generic import TemplateView

from .models import Manhwa

from django.core.paginator import Paginator

class ManhwaTemplateView(TemplateView):
    template_name = "web/index.html"

    def get_template_names(self) -> List[str]:
            if self.is_scroll():
                return ["web/manhwa.html"]
            return ["web/index.html"]

    def sort_by_tag(self) -> bool:
        return self.request.GET.get("tag")

    def page_number(self) -> int:
        return self.request.GET.get("page") or 1
    
    def is_scroll(self) -> bool:
        return self.request.GET.get("scroll") == "true"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        if self.sort_by_tag():
            manhwa_objs = Manhwa.objects.filter(tags__slug__in=self.sort_by_tag().split(","))
        else:
            manhwa_objs = Manhwa.objects.all()
        paginator = Paginator(manhwa_objs, 10)
        manhwas = paginator.get_page(self.page_number())
        ctx["manhwas"] = manhwas
        return ctx

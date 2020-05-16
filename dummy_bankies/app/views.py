from django.shortcuts import render
from django.views import View, generic


class IndexView(generic.TemplateView):
    template_name = "app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = [
            {
                "pk": 1,
                "name": "Category 1",
            },
            {
                "pk": 2,
                "name": "Category 2",
            },
        ]
        context["tasks"] = [
            {
                "task_id": 1,
                "type": "simple",
                "points": 98.0,
                "description": "Lorem ipsum",
                "category": {"name": "Category 1"},
            },
            {
                "task_id": 2,
                "type": "simple",
                "points": 96.0,
                "description": "Lorem ipsum dolor sit amet",
                "category": {"name": "Category 1"},
            }
        ]
        return context

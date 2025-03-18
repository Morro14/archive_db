from typing import Any
from django.forms import BaseModelForm
from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, TemplateView
from main.models import DataEntry
from main.forms import DataEntryAddForm


# Create your views here.
class DataEntryView(DetailView):
    model = DataEntry


class DataEntryListView(ListView):
    model = DataEntry
    template_name = "entry_list.html"
    paginate_by = 12

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     group_list = []
    #     x, y = 0, 3
    #     while y < len(context["object_list"]):
    #         group_list.append([context["object_list"][x:y:]])
    #         x += 3
    #         y += 3
    #     if len(context["object_list"]) < 3:
    #         group_list = [context["object_list"]]

    #     context["group_list"] = group_list
    #     print(group_list)
    #     return context


# class DataEntryCreateView(CreateView):
#     model = DataEntry
#     template_name = "entry_add.html"
#     fields = ["type", "tags", "date", "file"]
class DataEntryCreateView(CreateView):
    model = DataEntry
    template_name = "entry_add.html"
    form_class = DataEntryAddForm

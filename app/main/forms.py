from django.forms import Form, ModelForm, BaseModelForm, MultiWidget
from main.models import DataEntry, DataType, DataTag
from django import forms


class DataEntryAddForm(ModelForm):
    type_query = DataType.objects.all()
    type = forms.ModelChoiceField(
        queryset=type_query,
        empty_label=None,
        widget=forms.Select(
            attrs={
                "multiple": "",
                "type": "select",
                "id": "data-type",
                "class": "form-select",
            }
        ),
    )
    tag_query = DataTag.objects.all()

    tags = forms.ModelMultipleChoiceField(
        queryset=tag_query,
        label="Tags",
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "multiple": "",
                "type": "select_multiple",
                "id": "data-tags",
            },
        ),
    )

    date = forms.DateField(
        help_text="Дата документа",
        widget=forms.DateInput(
            attrs={"type": "text", "id": "data-date", "class": "form-control"}
        ),
    )
    file_realid = forms.CharField(
        widget=forms.DateInput(
            attrs={"type": "text", "id": "data-filename", "class": "form-control"}
        )
    )

    class Meta:
        model = DataEntry
        exclude = ["create_time", "file", "thumbnail"]

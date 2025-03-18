from django import template

register = template.Library()


mapping = {
    "SelectMultiple": "form-select",
    "Select": "form-select",
    "TextInput": "form-control",
    "DateInput": "form-control",
    "DateTimeInput": "form-control",
}


@register.filter("get_field_classes")
def get_field_classes(field):
    widget_class_name = field.field.widget.__class__.__name__

    try:
        return mapping[widget_class_name]
    except KeyError:
        raise ValueError(f"Classes related to {widget_class_name} are not defined yet")

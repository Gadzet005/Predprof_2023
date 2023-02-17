from django import forms


class FormStyleMixin(forms.Form):
    ''' Применяем ко всем полям стиль '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            attrs = field.field.widget.attrs
            if 'class' not in attrs:
                attrs['class'] = 'form-control'
            else:
                attrs['class'] += ' form-control'

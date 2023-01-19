from django import forms


class FormStyleMixin(forms.Form):
    ''' Применяем ко всем полям стиль '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

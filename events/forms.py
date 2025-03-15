from django import forms
from events.models import Event, Category, Participant, Contact_Us



class StyleFormMixin:
    default_classes = "border-2 border-gray-300 w-full p-3 mb-1 ml-5 rounded-lg shadow-sm"

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class' : self.default_classes,
                    'placeholder': f'Enter {field.label.lower()}'
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class' : f"{self.default_classes}, resize-none",
                    'placeholder' : f'Enter {field.label.lower()}',
                    'rows': 5
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    "class": "border-2 border-gray-300 p-3 mb-1 ml-5 rounded-xl shadow-sm"
                })
            elif isinstance(field.widget, forms.TimeInput):
                field.widget.attrs.update({
                    'type':'time',
                    'class': "border-2 border-gray-300 p-3 rounded-lg shadow-sm bg-gray-100 outline-none",
                    'style': 'width: 200px;'
                })
            elif isinstance(field.widget, forms.EmailInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f'Enter {field.label.lower()}'
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class': "space-y-2 ml-5"
                })
            else:
                field.widget.attrs.update({
                    'class': self.default_classes
                })


class Event_Form(StyleFormMixin ,forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date','time', 'location', 'category']

        widgets = {
            'date': forms.SelectDateWidget,
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'category': forms.Select
        }

    """ --------- Using Mixing Widget ----------- """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()




class Category_Form(StyleFormMixin ,forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

    """ --------- Using Mixing Widget ----------- """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()




class Participant_Form(StyleFormMixin ,forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'events']

        widgets = {
            'events':forms.CheckboxSelectMultiple
        }

    """ --------- Using Mixing Widget ----------- """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()




class Contact_Us_Form(StyleFormMixin ,forms.ModelForm):
    class Meta:
        model = Contact_Us
        fields = ['name','subject', 'description']

    """ --------- Using Mixing Widget ----------- """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()






from django.forms import ModelForm
from .models import Text

class FormText(ModelForm):
      class Meta:
        model = Text
        fields = '__all__'

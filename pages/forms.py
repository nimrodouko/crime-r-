from django import forms 
from .models import  Posts



class ReportForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = '__all__'


    def __init__( self,*args, **kwargs, ):
        super(ReportForm,self).__init__(*args, **kwargs)
        self.fields['image'].required =False

    



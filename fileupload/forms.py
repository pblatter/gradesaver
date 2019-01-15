from django import forms
from django.forms import ModelForm
from .models import test_files


class FindForm(ModelForm):
    class Meta:
        model = test_files
        fields = ['Jahrgang', 'Fach', 'Schwerpunkt']

'''
class exam_upload_form(ModelForm):
    class Meta:
        model = test_files
        fields = ['Name', 'Jahrgang', 'Fach', 'Schwerpunkt', 'Lehrperson', 'Exam']
'''

###########################################################################################

class UserDataForm(ModelForm):
                         
    # Overriding save allows us to add the user from the request    
    def save(self, user, commit=True):
        # get the instance so we can add the user to it.
        instance = super(UserDataForm, self).save(commit=False)
        instance.user = user
 
        # Do we need to save all changes now?
        if commit:
            instance.save()
            self.save_m2m()
 
        return instance
 
class exam_upload_form(UserDataForm):
    class Meta:
        model = test_files
        fields = ['Name', 'Jahrgang', 'Fach', 'Schwerpunkt', 'Lehrperson', 'Exam']


from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
#from .forms import UploadFileForm
from .forms import FindForm, exam_upload_form
from fileupload.models import test_files 


# imaginary function to handle uploaded file
#from somewhere import handle_uploaded_file

# Create your views here.
class HomeView(TemplateView):
    template_name = 'fileupload/logged_in.html'

    def get(self, request):

        return render(request, self.template_name)

  
class Find_Class(View):
    form_class = FindForm
    initial = {'key': 'value'}
    template_name = 'fileupload/finder.html'

    def handle_request(self, dictionary, request):
        
        #for i in dictionary.items():
            #print(i)
        for i in dictionary:
            print (i, dictionary[i])
        print("dict at zero", dictionary['Jahrgang'])

        #exams = test_files.objects.filter(Jahrgang = dictionary['Jahrgang']).filter(Schwerpunkt = dictionary['Schwerpunkt']).order_by('-Lehrperson')
        #exams = test_files.objects.filter(Schwerpunkt = dictionary['Schwerpunkt']).filter(Jahrgang = dictionary['Jahrgang']).order_by('-Lehrperson')
        exams = test_files.objects.filter(Fach = dictionary['Fach']).order_by('-Lehrperson').filter(Jahrgang = dictionary['Jahrgang']).filter(Schwerpunkt = dictionary['Schwerpunkt']).order_by('-Lehrperson')
        args =  {'exams': exams}
        # TODO: build a new template for displaying the found exams!
        return render(request, 'fileupload/exam_list.html', args)
        


    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            a = request.POST#['post']
            return self.handle_request(a, request)
            #for arg in request.POST:
                #print(request.POST[arg])
            #form = FindForm
            #return HttpResponseRedirect(reverse('fileupload:home'))
        
        args = {'form': form}
        return render(request, self.template_name, args)


class FileUploads(View):
    form_class = exam_upload_form
    initial = {'key': 'value'}
    template_name = 'fileupload/exam_upload.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            # <process form cleaned data>
            #post = form.save()#(commit=False)

            ## added code from here:
            #form = form.save(commit=False)
            #form.user = request.user

            ## to here
            form.save(user = request.user)
            form = exam_upload_form
            return HttpResponseRedirect(reverse('fileupload:home'))

        args = {'form': form}#, 'text': text}

        return render(request, self.template_name, args)


class Domain_View(TemplateView):
    template_name = "fileupload/domain_view.html"
    def get(self, request):
       
        return render(request, self.template_name)


'''
def gallery(request):
    path="C:\\somedirectory"  # insert the path to your directory   
    img_list =os.listdir(path)   
    return render_to_response('gallery.html', {'images': img_list})
'''
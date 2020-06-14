from django.shortcuts import render
from . import models
from . import forms
from . import utils
import os
# Create your views here.
def index(request):
    return render(request,'gender_recog/index.html')

def gen_recog(request):
    # gen_form = forms.Gen_Rec_Form()
    if request.method == 'POST':
        # form = forms.Gen_Rec_Form(request.POST, request.FILES['file_upload'])
        m = models.Image_data(image=request.FILES['file_upload'])
        m.save()
        print(m.image.name)

        # file = request.FILES['file_upload']
        # if form.is_valid():
        #     print(1)
        #     print(form.cleaned_data['query_img'])
        #     print(form.cleaned_data.get('query_img'))
        #     m = models.Image_data()
        #     m.image = form.cleaned_data['query_img']
        #     m.save()
        #     file = form.cleaned_data['query_img']
        #     print(file.filename)
        #     path = os.path.join(upload_path,file.filename)
        #     print(path)
        # filename = file.filename
        print("File saved successfully at {}".format(m.image.name))
        result = utils.pred_gender(m.image.name)
        return render(request,'gender_recog/face_app.html',{'upload':True, 'result':result})



    return render(request,'gender_recog/face_app.html',{'upload':False})

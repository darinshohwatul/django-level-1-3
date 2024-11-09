from django.shortcuts import render
from basicapp import forms

# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')
def form_name_view(request):
    form = forms.ForName()

    if request.method == 'post':
        form = forms.ForName(request.post)

        if form.is_valid():
            print("validation success!")
            print(form.cleaned_data['nama'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])


    return render(request, 'basicapp/form_page.html', {'form':form})
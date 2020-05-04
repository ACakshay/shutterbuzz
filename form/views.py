from django.shortcuts import render
from form.forms import EntryForm

def index(request):
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            input = form.save()
            input.save()
            form.clean()
            return render(request,'form/index.html')
        else:
            return  render(request,'form/index.html',{'form': form, 'errors': form.errors})
    else:
        form = EntryForm()
        return render(request,'form/index.html',{'form': form})



# Create your views here.

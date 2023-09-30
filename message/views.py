# همهی خط های کامنت این فایل حذف شوند
#from django.shortcuts import render
#from django.views.generic import View

from django.views.generic import TemplateView

# def messageView(request):
#    return render(request, 'home.html')

#class MessageView(View):
#    def get(sel, request):
#        return render(request, 'home.html')
    

class MessageView(TemplateView):
    template_name = 'home.html'    
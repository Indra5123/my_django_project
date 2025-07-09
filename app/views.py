from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello from Jenkins + Ansible deployed Django app!")

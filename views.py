from django.http import HttpResponse

def saludo(request):    #es nuestra primera vista

    return HttpResponse("Hola esta es nuestra primera página con Django")
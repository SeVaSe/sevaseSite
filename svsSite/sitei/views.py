from django.shortcuts import render


def main(request):
    return render(request, 'sitei/main.html')


def project(request):
    return render(request, 'sitei/project.html')
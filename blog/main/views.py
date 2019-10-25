from django.shortcuts import render


def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    context = {'like':'Django 很棒'}
    return render(request, 'main/main.html', context)

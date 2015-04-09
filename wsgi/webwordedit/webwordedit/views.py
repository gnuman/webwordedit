from django.shortcuts import render_to_response


def home(request):
    return render_to_response('base.html')


def loggedin(request):
    return render_to_response('registration/loggedin.html', 
                              {'full_name': request.user.username}
                             )





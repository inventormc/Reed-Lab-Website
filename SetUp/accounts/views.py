from __future__ import unicode_literals
from django.shortcuts import render, redirect
from accounts.forms import (
    RegistrationForm,
    EditProfileForm
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader
import math
# import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from io import StringIO
import PIL
import math
import six

from .forms import GraphForm

def home(request):
    numbers = [1, 2, 3, 4, 5]
    name = 'Manuel'

    args = {'myName': name, 'numbers': numbers}
    return render(request, 'accounts/home.html', args)



def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)


@login_required
def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

@login_required
def edit_profile(request):
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=request.user)

            if form.is_valid():
                form.save()
                return redirect('/account/profile')

        else:
            form = EditProfileForm(instance=request.user)
            args = {'form': form}
            return render(request, 'accounts/edit_profile.html', args)

@login_required
def change_password(request):
        if request.method == 'POST':
            form = PasswordChangeForm(data=request.POST, user=request.user)

            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('/account/profile')

            else:
                return redirect('/account/change-password')

        else:
            form = PasswordChangeForm(user=request.user)
            args = {'form': form}
            return render(request, 'accounts/change_password.html', args)


def plot(function, x_range):
    x = np.array(x_range)
    y = function(x)
    plt.plot(x,y)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    '''
    buffer = StringIO()
    canvas = plt.get_current_fig_manager().canvas()
    canvas.draw()

    pilImage = PIL.Image.fromstring("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    plt.close()

    return buffer.getvalue()
    '''
    fig = plt.figure()
    buffer = StringIO()
    fig.savefig(buffer, format='svg', bbox_inches='tight')

    return buffer
def index(request):
    import random
    import django
    import datetime

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure

    title = 'Title'
    body = 'Fake text fake text fake text fake text fake text fake text'
    form = GraphForm(request.POST)
    '''
    number = request.POST['number']
    number = float(number)
    fig=Figure()
    ax=fig.add_subplot(111)
    x = np.linspace(-10,10,400)
    def y_values(function, x_range):
        return function(x_range)
    y = y_values(lambda x: x**number, x)
    ax.plot(x,y)
    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    '''
    template = loader.get_template('graph/index.html')
    context = {
            'title':title,
            'body':body,
            'form':form
    }
    return HttpResponse(template.render(context, request))


def graph(request):
    import random
    import django
    import datetime

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure

    number = request.POST['number']
    number = float(number)
    fig=Figure()
    ax=fig.add_subplot(111)
    x = np.linspace(-10,10,400)
    def y_values(function, x_range):
        return function(x_range)
    y = y_values(lambda x: x**number, x)
    ax.plot(x,y)
    canvas=FigureCanvas(fig)
    response=HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response

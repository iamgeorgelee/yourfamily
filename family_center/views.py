import json

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect

from social.apps.django_app.default.models import UserSocialAuth

from .chatbots import facebook_messenger
from .services import MemberService
member_service = MemberService()


def hello_world(request):
    return HttpResponse("Hello World!")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def home(request):
	print request.user
	if request.user.is_authenticated():	
		print request.user.email
	return render(request, 'home/home.html')

@login_required
def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None
    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None
    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'home/settings.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'home/password.html', {'form': form})

@login_required
def authorize_from_messenger(request):

 	redirect_url = request.GET.get('redirect_uri')
	account_linking_token = request.GET.get('account_linking_token')
	print request.user
	if request.user.is_authenticated():	
		psid = facebook_messenger.get_psid(account_linking_token)
		if psid:
			member_service.set_fb_messenger_id(request.user.id, psid)
			redirect_url += '&authorization_code=' + AUTHORIZATION_CODE
			member_service.send_text_message(psid, 'Your account has been linked!')

	return redirect(redirect_url)

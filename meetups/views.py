from django.shortcuts import render, redirect
from .models import Meetup, participant
from .forms import RegistrationForm

# Create your views here.

def index(request):
    meetups = Meetup.objects.all()

    return render(request, 'meetups/index.html', {
        'meetups':meetups    
    })

def meetup_details(request, meetup_slug):
    try:

        selected_meetup = Meetup.objects.get(slug = meetup_slug)

        if request.method == 'GET':
            registrationForm = RegistrationForm()
            
        else:
            registrationForm = RegistrationForm(request.POST)

            if registrationForm.is_valid():
                user_email = registrationForm.cleaned_data['email']
                participan, _ = participant.objects.get_or_create(email=user_email)
                selected_meetup.participant.add(participan)
                return redirect('confirm', meetup_slug = meetup_slug)
        
        return render(request, 'meetups/meetup-details.html',{
                'meetup': selected_meetup,
                'meetup_found': True,
                'form' : registrationForm
            })

    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        } )
def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug = meetup_slug)

    return render(request, 'meetups/registration-success.html',{
        'organizer_email' : meetup.organizer_email
    })
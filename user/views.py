from django.shortcuts import render
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse

from root.settings import EMAIL_USERNAME


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        from_email = EMAIL_USERNAME
        recipient_list = ['recipient@example.com']

        try:
            send_mail(
                subject,
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                from_email,
                recipient_list,
                fail_silently=False,
            )
            return JsonResponse({'message': 'Your message has been sent. Thank you!'})
        except Exception as e:
            return JsonResponse({'message': 'An error occurred while sending the email.'}, status=500)

    return render(request, 'contact.html')


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def resume(request):
    return render(request, 'resume.html')


def portfolio_details(request):
    return render(request, 'portfolio-details.html')


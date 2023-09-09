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

#
# from rest_framework import serializers, status, permissions
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.core.mail import send_mail
#
#
# class ContactFormSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     email = serializers.EmailField()
#     subject = serializers.CharField(max_length=200)
#     message = serializers.CharField()
#
#
# class ContactFormView(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def post(self, request, format=None):
#         serializer = ContactFormSerializer(data=request.data)
#         if serializer.is_valid():
#             name = serializer.validated_data['name']
#             email = serializer.validated_data['email']
#             subject = serializer.validated_data['subject']
#             message = serializer.validated_data['message']
#             from_email = 'createuz.sh@gmail.com'
#             recipient_list = ['recipient@example.com']
#
#             try:
#                 send_mail(
#                     subject,
#                     f'Name: {name}\nEmail: {email}\nMessage: {message}',
#                     from_email,
#                     recipient_list,
#                     fail_silently=False,
#                 )
#                 return Response({'message': 'Your message has been sent. Thank you! '},
#                                 status=status.HTTP_201_CREATED)
#             except Exception as e:
#                 return Response({'message': 'An error occurred while sending the email.'},
#                                 status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

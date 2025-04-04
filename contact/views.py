from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .models import *
from .serializers import *
import mimetypes

class CareerView(APIView):
    def get(self, request):
        careers = CareerForm.objects.all()
        serializer = CareerSerializer(careers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CareerSerializer(data=request.data)
        if serializer.is_valid():
            career = serializer.save()

            # Get MIME type of the uploaded resume
            resume_file = career.resume
            content_type, _ = mimetypes.guess_type(resume_file.name)

            # Prepare HTML content
            html_content = render_to_string('emails/career_email.html', {
                'career': career
            })

            # Prepare and send email
            subject = "New Career Application"
            email = EmailMessage(subject, html_content, settings.ADMIN_EMAIL, [settings.ADMIN_EMAIL])

            email.content_subtype = 'html'  # Ensure HTML content

            # Attach resume if uploaded
            if resume_file:
                email.attach(resume_file.name, resume_file.read(), content_type or 'application/octet-stream')

            email.send()

            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class ContactView(APIView):
    def get(self, request):
        contact = ContactForm.objects.all()
        serializer = ContactSerializer(contact, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()

            # Prepare HTML content
            html_content = render_to_string('emails/contact_email.html', {
                'contact': contact
            })

            # Prepare and send email
            subject = "New Contact Form Submission"
            email = EmailMessage(subject, html_content, settings.ADMIN_EMAIL, [settings.ADMIN_EMAIL])

            email.content_subtype = 'html'  # Ensure HTML content

            email.send()

            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class JobPositionView(APIView):
    def get(self, request):
        jobpositions = JobPosition.objects.all()
        serializer = JobPositionSerializer(jobpositions, many=True)
        return Response(serializer.data)
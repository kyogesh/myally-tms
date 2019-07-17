from django.shortcuts import render
from django.core.mail import send_mass_mail
from django.db.models.expressions import Q
from django.contrib.auth import get_user_model
from django.template import Template as DjangoTemplate
from django.template import Context, context_processors
from rest_framework import generics, authentication, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Template, Department, Student
from .serializers import TemplateSerializer, DepartmentSerializer


def home(request):
    return render(request, 'index.html')


class TemplateListApiView(APIView):

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        templates = Template.objects.filter(user=request.user)
        serializer = TemplateSerializer(templates, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = dict(request.data)
        data['user'] = request.user.id
        serializer = TemplateSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TemplateDetailApiView(APIView):

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, template_id):
        template = Template.objects.get(id=template_id)
        serializer = TemplateSerializer(template)
        return Response(serializer.data)


class DepartmentListApiView(APIView):

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)


class StartCampaign(APIView):

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        students = Student.objects.all()
        templates_qs = Template.objects.all()
        messages = list()
        for student in students:
            context = Context()
            selected_template = None
            context['first_name'] = student.first_name
            if templates_qs.filter(year=student.year).exists():
                selected_template = templates_qs.filter(year=student.year)
                context['year'] = student.year
                if selected_template.filter(department=student.department.code).exists():
                    selected_template = selected_template.filter(
                        department=student.department.code)
                    context['department'] = student.department.name
                if selected_template.filter(
                        residential_status=student.residential_status).exists():
                    selected_template = selected_template.filter(
                        residential_status=student.residential_status)
                    context['residential_status'] = student.residential_status
            if selected_template:
                temp = DjangoTemplate(selected_template.first().content)
                rendered_template = temp.render(context)
                messages.append(['Campaign', rendered_template,
                                 'no-reply@myally.ai', [student.email, ]])
        send_mass_mail(messages, fail_silently=False)
        return Response({'test': messages})

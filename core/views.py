from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Employee, Skill, ExtraEducation, Education


class IndexView(TemplateView):
  template_name = 'index.html'

  def get_context_data(self, **kwargs):
      context = super(IndexView, self).get_context_data(**kwargs)
      context['employee'] = Employee.objects.first()
      context['skills'] = Skill.objects.all()
      context['extraEducations'] = ExtraEducation.objects.all()
      context['educations'] = Education.objects.all()
      return context

    # def form_valid(self, form, *args, **kwargs):
    #     form.send_mail()
    #     messages.success(self.request, 'E-mail enviado com sucesso')
    #     return super(IndexView, self).form_valid(form, *args, **kwargs)

    # def form_invalid(self, form, *args, **kwargs):
    #     messages.error(self.request, 'Erro ao enviar e-mail')
    #     return super(IndexView, self).form_invalid(form, *args, **kwargs)


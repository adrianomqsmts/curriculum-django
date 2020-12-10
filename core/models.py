import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from stdimage.models import StdImageField


class Base(models.Model):
  crate = models.DateField('crate', auto_now_add=True)
  update = models.DateField('update', auto_now=True)
  is_active = models.BooleanField('is_active', default=True)

  class Meta:
      abstract = True


class Employee(Base):
  name = models.CharField('Name', max_length=100)
  functions = models.CharField('Functions', max_length=150)
  about = models.TextField('About', max_length=1000)
  image = StdImageField('Image', upload_to=str(id), variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
  city = models.CharField('City', max_length=100)
  state = models.CharField('State', max_length=100)

  facebook = models.CharField('Facebook', max_length=100, default='#')
  twitter = models.CharField('Twitter', max_length=100, default='#')
  instagram = models.CharField('Instagram', max_length=100, default='#')
  youtube = models.CharField('Youtube', max_length=100, default='#')
  github = models.CharField('Github', max_length=100, default='#')
  linkedin = models.CharField('Linkedin', max_length=100, default='#')

  class Meta:
    verbose_name = 'Employee'
    verbose_name_plural = 'Employees'

  def __str__(self):
    return self.nome


class Skill(Base):
  name = models.CharField('Name', max_length=100)
  progress = models.IntegerField('Progess', validators=[MaxValueValidator(100), MinValueValidator(0)])
  description = models.TextField('description', max_length=1000)

  class Meta:
    verbose_name = 'Skill'
    verbose_name_plural = 'Skills'

  def __str__(self):
    return self.nome


class Education(Base):
  institution = models.CharField('Institution', max_length=100)
  start = models.IntegerField('Start', validators=[MaxValueValidator(1000), MinValueValidator(9999)])
  end = models.IntegerField('End', validators=[MaxValueValidator(1000), MinValueValidator(9999)])
  city = models.CharField('City', max_length=100)
  state = models.CharField('State', max_length=100)

  class Meta:
    verbose_name = 'Education'
    verbose_name_plural = ''

  def __str__(self):
      return self.nome


class ExtraEducation(Base):
  name = models.CharField('Name', max_length=100)
  description = models.CharField('Description', max_length=1000)

  class Meta:
    verbose_name = 'Extra Education'
    verbose_name_plural = ''

  def __str__(self):
      return self.nome

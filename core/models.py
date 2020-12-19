import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
  crate = models.DateField('crate', auto_now_add=True)
  update = models.DateField('update', auto_now=True)
  is_active = models.BooleanField('is_active', default=True)

  class Meta:
    abstract = True


class Employee(Base):
  name = models.CharField('Name', max_length=100)
  last_name = models.CharField('Last Name', max_length=200)
  functions = models.CharField('Functions', max_length=150)
  phone = models.CharField('Phone', max_length=17)
  about = models.TextField('About', max_length=1000)
  email = models.EmailField('E-mail', max_length=100)
  image = StdImageField('Image', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
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
    return self.name


class Skill(Base):
  name = models.CharField('Name', max_length=100)
  progress = models.IntegerField('Progess', validators=[MaxValueValidator(100), MinValueValidator(0)])
  description = models.TextField('description', max_length=1000)

  class Meta:
    verbose_name = 'Skill'
    verbose_name_plural = 'Skills'

  def __str__(self):
    return self.name


class Education(Base):
  institution = models.CharField('Institution', max_length=100)
  start = models.IntegerField('Start', validators=[MaxValueValidator(9999), MinValueValidator(1000)])
  end = models.IntegerField('End', validators=[MaxValueValidator(9999), MinValueValidator(1000)])
  city = models.CharField('City', max_length=100)
  state = models.CharField('State', max_length=100)
  description = models.TextField('description', max_length=1000)


  class Meta:
    verbose_name = 'Education'
    verbose_name_plural = 'Educations'

  def __str__(self):
      return self.institution


class ExtraEducation(Base):
  name = models.CharField('Name', max_length=100)
  description = models.TextField('description', max_length=1000)

  class Meta:
    verbose_name = 'Extra Education'
    verbose_name_plural = 'Extra Educations'

  def __str__(self):
      return self.name

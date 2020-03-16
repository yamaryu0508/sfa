
from django.db import models
from django.forms import ModelForm

class Salespipeline(models.Model):
    salespipeline_id = models.AutoField(
      primary_key=True,
      max_length=10,
    )
    title = models.CharField(
      verbose_name='Title',
      max_length=50
    )
    detail = models.CharField(
      verbose_name='Detail',
      max_length=300
    )
    insert_date = models.DateTimeField(
      'date published',
      auto_now_add=True,
    )
    update_date = models.DateTimeField(
      'date published',
      auto_now=True,
    )

class SalespipelineForm(ModelForm):
    class Meta:
        model = Salespipeline
        fields = ['salespipeline_id', 'title', 'detail', 'insert_date', 'update_date']
        exclude = ['salespipeline_id', 'insert_date', 'update_date']
# Generated by Django 4.0.6 on 2022-07-15 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wc', '0002_text_delete_formtext_delete_formtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='words',
            field=models.TextField(),
        ),
    ]

# Generated by Django 5.0.4 on 2024-06-09 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webjew', '0003_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_url', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Фідбек',
                'verbose_name_plural': 'Фідбеки',
            },
        ),
    ]
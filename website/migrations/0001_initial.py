# Generated by Django 5.1.3 on 2024-12-05 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logged_at', models.DateTimeField(auto_now_add=True)),
                ('film_title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=100)),
                ('year_of_release', models.PositiveIntegerField(default=2000)),
                ('personal_rating', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('review', models.TextField(default='No review provided')),
                ('would_recommend', models.BooleanField(default=False)),
            ],
        ),
    ]

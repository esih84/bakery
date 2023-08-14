# Generated by Django 4.1.4 on 2023-08-13 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('count', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=0, max_digits=6)),
                ('active', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]

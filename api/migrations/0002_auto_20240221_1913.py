# Generated by Django 3.2.5 on 2024-02-21 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todonote',
            name='category',
            field=models.CharField(choices=[('General', 'General'), ('Work', 'Work'), ('Personal', 'Personal'), ('Health', 'Health'), ('Shopping', 'Shopping'), ('Education', 'Education'), ('Entertainment', 'Entertainment'), ('Others', 'Others')], default='General', max_length=50),
        ),
        migrations.AlterField(
            model_name='todonote',
            name='complete',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending')], max_length=50),
        ),
    ]

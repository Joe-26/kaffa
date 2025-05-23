# Generated by Django 5.2.1 on 2025-05-18 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default='M', max_length=5),
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(default='Description not available. Coming Soon!'),
        ),
        migrations.AddField(
            model_name='item',
            name='nutrition',
            field=models.CharField(default='Nutrition Values not available at the moment.'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='theme/static/img/'),
        ),
    ]

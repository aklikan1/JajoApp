# Generated by Django 3.2.6 on 2022-09-22 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps_home', '0003_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Products'},
        ),
    ]
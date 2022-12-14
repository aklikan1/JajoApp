# Generated by Django 3.2.6 on 2022-10-10 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps_home', '0006_alter_orders_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArrivalDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='arrival_date',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='apps_home.arrivaldate'),
        ),
    ]

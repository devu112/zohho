# Generated by Django 3.2.19 on 2023-07-31 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0012_alter_payroll_tds'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpmment', models.CharField(max_length=300)),
                ('payroll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.payroll')),
            ],
        ),
    ]
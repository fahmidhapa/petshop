# Generated by Django 4.0.1 on 2025-04-07 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_pet_tbl'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=1)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.pet_tbl')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.reg_tbl')),
            ],
        ),
    ]

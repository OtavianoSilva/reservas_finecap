# Generated by Django 4.2.5 on 2023-10-23 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_empresa_faturamento'),
        ('reservas', '0004_alter_reserva_empresa_alter_reserva_stand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.empresa'),
        ),
    ]

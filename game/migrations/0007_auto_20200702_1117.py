# Generated by Django 3.0.7 on 2020-07-02 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_bet_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='bet',
        ),
        migrations.AlterField(
            model_name='bet',
            name='bet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Result'),
        ),
        migrations.AlterField(
            model_name='bet',
            name='status',
            field=models.CharField(blank=True, choices=[('WIN', 'WIN'), ('LOSE', 'LOSE')], max_length=50, null=True),
        ),
    ]
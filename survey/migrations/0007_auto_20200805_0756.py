# Generated by Django 3.0.8 on 2020-08-05 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('survey', '0006_auto_20200725_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='survey.Question'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='target_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interviews_target', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='interview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='survey.Category'),
        ),
    ]
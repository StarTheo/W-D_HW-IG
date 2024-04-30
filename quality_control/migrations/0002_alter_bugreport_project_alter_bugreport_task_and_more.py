# Generated by Django 4.2.7 on 2024-04-08 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
        ('quality_control', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugreport',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bug_reports_as_project', to='tasks.project', verbose_name='Проект'),
        ),
        migrations.AlterField(
            model_name='bugreport',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bug_reports_as_task', to='tasks.task', verbose_name='Задача'),
        ),
        migrations.CreateModel(
            name='FeatureRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название запроса на новую функцию')),
                ('description', models.TextField(verbose_name='Описание запроса')),
                ('status', models.CharField(choices=[('Рассмотрение', 'Рассмотрение'), ('Принято', 'Принято'), ('Отклонено', 'Отклонено')], default='Рассмотрение', max_length=20, verbose_name='Статус запроса')),
                ('priority', models.IntegerField(choices=[(1, 'Низкий'), (2, 'Средний'), (3, 'Высокий'), (4, 'Очень высокий'), (5, 'Критический')], default=3, verbose_name='Приоритет запроса')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания запроса')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время последнего обновления запроса')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature_requests', to='tasks.project', verbose_name='Проект')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='feature_requests', to='tasks.task', verbose_name='Задача')),
            ],
            options={
                'verbose_name': 'Запрос на новую функцию',
                'verbose_name_plural': 'Запросы на новые функции',
            },
        ),
    ]
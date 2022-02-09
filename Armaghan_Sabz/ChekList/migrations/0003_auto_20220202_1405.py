# Generated by Django 3.2.7 on 2022-02-02 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChekList', '0002_alter_checklist_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checklist',
            old_name='date',
            new_name='functions',
        ),
        migrations.RenameField(
            model_name='checklist',
            old_name='date2',
            new_name='types',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='category',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='confirm',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='content',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='file_name',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='kind',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='subtitle',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='time',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='value',
        ),
        migrations.AlterField(
            model_name='checklist',
            name='comment',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]

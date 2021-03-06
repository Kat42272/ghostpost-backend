# Generated by Django 3.1.1 on 2020-10-02 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost_api', '0003_post_totalvotes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='choices',
        ),
        migrations.AddField(
            model_name='post',
            name='choice_type',
            field=models.CharField(choices=[(True, 'Boast'), (False, 'Roast')], default='Boast', max_length=5),
        ),
        migrations.AlterField(
            model_name='post',
            name='totalVotes',
            field=models.IntegerField(default=0),
        ),
    ]

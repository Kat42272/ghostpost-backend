# Generated by Django 3.1.1 on 2020-10-02 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost_api', '0002_auto_20201001_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='totalVotes',
            field=models.IntegerField(blank=True, default=0, editable=False, null=True),
        ),
    ]

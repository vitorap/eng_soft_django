# Generated by Django 2.2.1 on 2019-06-06 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mostrar', '0004_auto_20190606_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('imagefile', models.FileField(null=True, upload_to='images/', verbose_name='')),
            ],
        ),
    ]
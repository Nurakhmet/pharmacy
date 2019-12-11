# Generated by Django 2.2.7 on 2019-11-18 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('price', models.IntegerField()),
                ('gramm', models.IntegerField()),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Catalogue')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='login',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.DeleteModel(
            name='Drug',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
    ]
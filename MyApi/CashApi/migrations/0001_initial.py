# Generated by Django 3.1.2 on 2021-02-25 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='acc_head', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AccountName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_name', models.CharField(max_length=255)),
                ('opening_balance', models.FloatField(blank=True, null=True)),
                ('closing_balance', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JournalLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('reference_no', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='JournalLogDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(blank=True, null=True)),
                ('account_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CashApi.accountname')),
                ('journal_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CashApi.journallog')),
            ],
        ),
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_type_name', models.CharField(max_length=255)),
                ('acc_head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CashApi.accounthead')),
            ],
        ),
        migrations.AddField(
            model_name='accountname',
            name='type_of_acc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CashApi.accounttype'),
        ),
    ]

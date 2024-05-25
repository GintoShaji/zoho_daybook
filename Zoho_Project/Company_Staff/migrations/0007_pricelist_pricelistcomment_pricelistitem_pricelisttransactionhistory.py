# Generated by Django 3.2.23 on 2024-01-31 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0015_remove_paymenttermsupdates_interested_to_continue'),
        ('Company_Staff', '0006_banking_bankinghistory_banktransaction_banktransactionhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('type', models.CharField(choices=[('Sales', 'Sales'), ('Purchase', 'Purchase')], max_length=10, null=True)),
                ('item_rate_type', models.CharField(choices=[('Percentage', 'Percentage'), ('Each Item', 'Each Item')], max_length=15, null=True)),
                ('description', models.TextField(null=True)),
                ('percentage_type', models.CharField(blank=True, choices=[('Markup', 'Markup'), ('Markdown', 'Markdown')], max_length=10, null=True)),
                ('percentage_value', models.IntegerField(blank=True, null=True)),
                ('round_off', models.CharField(choices=[('Never Mind', 'Never Mind'), ('Nearest Whole Number', 'Nearest Whole Number'), ('0.99', '0.99'), ('0.50', '0.50'), ('0.49', '0.49')], max_length=20, null=True)),
                ('currency', models.CharField(choices=[('Indian Rupee', 'Indian Rupee')], max_length=20, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=10)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='price_list_attachment/')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='PriceListTransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('action', models.CharField(choices=[('Created', 'Created'), ('Edited', 'Edited')], max_length=10, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
                ('price_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.pricelist')),
            ],
        ),
        migrations.CreateModel(
            name='PriceListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('custom_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.items')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
                ('price_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.pricelist')),
            ],
        ),
        migrations.CreateModel(
            name='PriceListComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
                ('price_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.pricelist')),
            ],
        ),
    ]

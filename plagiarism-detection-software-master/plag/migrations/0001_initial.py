# Generated by Django 4.0.4 on 2022-07-08 05:10

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
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('renewal_day', models.PositiveSmallIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('currency', models.CharField(choices=[('GBP', 'GBP'), ('EUR', 'EUR'), ('USD', 'USD')], default='USD', max_length=3)),
                ('is_active', models.BooleanField(default=True)),
                ('time_order_added', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProtectedResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=2048)),
                ('file', models.FileField(blank=True, upload_to='userfiles/%Y/%m/%d')),
                ('type', models.CharField(choices=[('URL', 'Website address'), ('PDF', 'PDF file'), ('DOC', 'Word document, old format'), ('DOCX', 'Word document, new format'), ('PPTX', 'Powerpoint presentation'), ('TXT', 'Standard text file')], default='URL', max_length=4)),
                ('status', models.CharField(choices=[('A', 'Active'), ('N', 'Newly placed order'), ('S', 'Being scanned'), ('F', 'Last scan failed'), ('P', 'Awaiting payment'), ('I', 'Inactive')], default='A', max_length=1)),
                ('scan_frequency', models.PositiveIntegerField(choices=[(86400, 'Daily'), (604800, 'Weekly'), (2592000, 'Monthly')], default=604800)),
                ('next_scan', models.DateTimeField()),
                ('original_filename', models.CharField(blank=True, max_length=260, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plag.order')),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='RecentBlogPosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=2048)),
                ('desc', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ScanLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('protected_source', models.TextField(blank=True, null=True)),
                ('scoring_debug', models.TextField(blank=True, null=True)),
                ('fail_reason', models.CharField(blank=True, max_length=500, null=True)),
                ('fail_type', models.CharField(blank=True, choices=[('H', 'HTTP error'), ('C', 'No content candidates found (initial scan) or matched (post processing)')], max_length=1, null=True)),
                ('user_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('protected_resource', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plag.protectedresource')),
                ('queries', models.ManyToManyField(blank=True, null=True, to='plag.query')),
            ],
        ),
        migrations.CreateModel(
            name='UserPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('results_per_page', models.PositiveSmallIntegerField(blank=True, choices=[(5, 5), (10, 10), (15, 15), (20, 20), (25, 25), (30, 30), (50, 50), (75, 75), (100, 100), (150, 150)], null=True)),
                ('email_frequency', models.CharField(blank=True, choices=[('I', 'Instant'), ('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly'), ('N', 'Never')], max_length=1, null=True)),
                ('false_positive_prot', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScanResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('match_url', models.CharField(max_length=2048)),
                ('match_display_url', models.CharField(max_length=2048)),
                ('match_title', models.CharField(max_length=100)),
                ('match_desc', models.CharField(max_length=500)),
                ('post_scanned', models.BooleanField(default=False)),
                ('post_fail_reason', models.CharField(blank=True, max_length=500, null=True)),
                ('post_fail_type', models.CharField(blank=True, choices=[('H', 'HTTP error'), ('C', 'No content candidates found (initial scan) or matched (post processing)')], max_length=1, null=True)),
                ('perc_of_duplication', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('result_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plag.scanlog')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('explanation', models.CharField(blank=True, max_length=1000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('paid', models.DateTimeField(blank=True, null=True)),
                ('is_adjustment', models.BooleanField(default=False)),
                ('paypal_tid', models.CharField(blank=True, max_length=17, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plag.order')),
            ],
        ),
    ]
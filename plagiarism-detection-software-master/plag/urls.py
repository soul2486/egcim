# from django.conf.urls import url
from django.urls import path, re_path
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

admin.autodiscover()

from plag import views, const

urlpatterns = [
                       re_path(r'^$', views.IndexView.as_view(), name='index'),
                       re_path(r'^index-trial/$', views.IndexTrialView.as_view(), name='index_trial'),

                       re_path(r'^download/(?P<prot_res_id>\d+)$', views.download_file, name='download'),

                       re_path(r'^products/$', TemplateView.as_view(template_name='plag/static/products.html'),
                           name='products'),
                       re_path(r'^features-screenshots/$',
                           TemplateView.as_view(template_name='plag/static/features_and_screenshots.html'),
                           name='features'),
                       re_path(r'^url-protection/$', TemplateView.as_view(template_name='plag/static/url_protection.html'),
                           name='url_prot'),
                       re_path(r'^document-protection/$',
                           TemplateView.as_view(template_name='plag/static/doc_protection.html'), name='doc_prot'),
                       re_path(r'^pricing/$', TemplateView.as_view(template_name='plag/static/pricing.html'),
                           name='pricing'),
                       re_path(r'^risks-of-plagiarism/$',
                           TemplateView.as_view(template_name='plag/static/risks_of_plagiarism.html'),
                           name='risks_plag'),

                       re_path(r'^about-us/$', TemplateView.as_view(template_name='plag/static/about.html'), name='about'),
                       re_path(r'^our-customers/$', TemplateView.as_view(template_name='plag/static/our_customers.html'),
                           name='our_customers'),
                       re_path(r'^contact-us/$', TemplateView.as_view(template_name='plag/static/contact_us.html'),
                           name='contact'),

                       re_path(r'^order/$', views.OrderView.as_view(), name='order'),
                       re_path(r'^ajax/username-check/$', views.username_unique, name='ajax_username_unique'),

                       re_path(r'^account/$', views.account, name='account'),
                       re_path(r'^account/profile/$', login_required(views.ProfileView.as_view()), name='profile'),

                       re_path(r'^account/invoice/(?P<pk>\d+)$', views.invoice, name='invoice'),

                       re_path(r'^account/invoice/pay/(?P<pk>\d+)$', views.pay_invoice, name='pay_invoice'),
                       re_path(r'^account/invoice/subscribe/(?P<pk>\d+)$', views.subscribe_invoice,
                           name='subscribe_invoice'),

                       re_path(r'^ipn-endpoint/$', views.ipn, name='ipn'),

                       re_path(r'^account/recent-scans/$', views.recent_scans, name='recent_scans_default'),
                       re_path(r'^account/recent-scans/(?P<num_days>\d+)$', views.recent_scans,
                           name='recent_scans'),
                       re_path(r'^account/recent-scans/(?P<num_days>\d+)/(?P<hide_zero>hide-zero)$',
                           views.recent_scans, name='recent_scans_hide_zero'),

                       re_path(r'^account/scan-history/$', views.scan_history, name='scan_history'),
                       re_path(r'^account/scan-history/(?P<hide_zero>hide-zero)$', views.scan_history,
                           name='scan_history_hide_zero'),

                       re_path(r'^ajax/plag-results/$', views.plagiarism_results,
                           name='ajax_plag_results_default'),
                       re_path(r'^ajax/plag-results/(?P<scan_id>\d+)$', views.plagiarism_results,
                           name='plag_results'),

                       re_path(r'^ajax/sitemap/$', views.sitemap_to_urls, name='ajax_urls'),

                       re_path(r'^account/protected-resources/$',
                           login_required(views.ProtectedResources.as_view()), name='protected_resources'),

                       re_path(r'^sitemap/$', TemplateView.as_view(template_name='plag/static/sitemap.html'),
                           name='sitemap'),
                       re_path(r'^terms-of-service/$',
                           TemplateView.as_view(template_name='plag/static/terms_of_service.html'),
                           name='terms_of_service'),
                       re_path(r'^privacy-policy/$', TemplateView.as_view(template_name='plag/static/privacy_policy.html'),
                           name='privacy_policy'),

                       # TODO Remove
                       re_path(r'^data-cleanse/$', views.data_cleanse, name='data_cleanse'),

                       re_path(r'^copyright/$', TemplateView.as_view(template_name='plag/static/copyright.html'),
                           name='copyright'),
                    #    re_path(r'^login/$', 'django.contrib.auth.views.login',
                    #        {'template_name': 'plag/static/login_error.html'}),
                    #    re_path(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'index'}, name='logout'),
]
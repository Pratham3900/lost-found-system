from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('report-lost/', views.report_lost_item, name='report_lost'),
    path('report-found/', views.report_found_item, name='report_found'),
    path('lost-items/', views.lost_item_list, name='lost_list'),
    path('found-items/', views.found_item_list, name='found_list'),
    path('match-items/', views.match_items, name='match_items'),
    path('claim-item/<int:item_id>/', views.claim_item, name='claim_item'),
    path('notifications/', views.notification_list, name='notification_list'),
    path('approved-claims/', views.approved_claims, name='approved_claims'),
    path('rejected-claims/', views.rejected_claims, name='rejected_claims'),

    # admin side
    path('dashboard/', views.dashboard_home, name='dashboard_home'),
    path('dashboard/lost-items/', views.dashboard_lost_items, name='dashboard_lost_items'),
    path('dashboard/found-items/', views.dashboard_found_items, name='dashboard_found_items'),
    path('dashboard/match-items/', views.dashboard_match_items, name='dashboard_match_items'),
    path('dashboard/claim-requests/', views.dashboard_claim_requests, name='dashboard_claim_requests'),
    path('dashboard/approve-claim/<int:claim_id>/', views.approve_claim, name='approve_claim'),
    path('dashboard/reject-claim/<int:claim_id>/', views.reject_claim, name='reject_claim'),
    path('dashboard/approved-claims/', views.dashboard_approved_claims, name='dashboard_approved_claims'),
]
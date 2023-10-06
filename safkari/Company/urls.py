from django.urls import path
from . import views



urlpatterns = [
    path('new_company/',views.NewCompany.as_view(),name="New_Company"),
    path('companies_list/',views.Companies_lists.as_view(),name="Companies_list"),
    path('Company_edit/',views.CompanyEdit.as_view(),name="Company_edit"),
    path('branches_lists/',views.Branches_lists.as_view(),name="Branches_list"),
    path('new_branch/',views.NewBranch.as_view(),name="New_branch"),
    path('branch_edit/',views.Branches_lists.as_view(),name="Branch_edit"),
    path('new_worker/',views.NewWorker.as_view(),name="New_Worker"),
    path('workers_lists/',views.Workers_list.as_view(),name="Workers_list"),
    path('worker_edit/',views.WorkerEdit.as_view(),name="Worker_edit")
]
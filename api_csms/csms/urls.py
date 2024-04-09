from django.urls import path, include
from . import views
from .views import ClassSchedulesListView, SignupSet, signUpTraining, viewTraining, cancelEnrollment, ActivityLogView
# router = DefaultRouter()
# router.register(r'', UserLogViewSet)
from .views import ClassSchedulesListView, UserLogViewSet, UserViewSet, SignupSet, TokenRevokeSet, CustomAuthToken, \
    LocationList, LocationDetails, ViewMemberTrainingEnrollment, ActivityList, ActivityLogSet, EquipmentViewSet,enrollmentStats, VisitorCountByHourViewSet, HoursCountByLocationViewSet

urlpatterns = [
    path('api/v1/addClassSchedules/', ClassSchedulesListView.as_view()),
    path('api/v1/checkin/', views.UserLogViewSet.as_view({'post': 'checkin'})),
    path('api/v1/checkout/', views.UserLogViewSet.as_view({'put': 'checkout'})),
    path('api/v1/signup/', SignupSet.as_view({'post': 'signup'})),
    # path('api/v1/updateMembership/<int:user_id>', SignupSet.as_view({'put': 'updateMembership'})),
    path('api/v1/user/<str:email>', UserViewSet.as_view({'get': 'get'})),
    path('api/v1/signupfortraining/', signUpTraining.as_view({'post': 'signupfortraining'})),
    path('api/v1/signupnonmembers/', signUpTraining.as_view({'post': 'signUpnonmembersfortraining'})),
    path('api/v1/viewtrainings/', viewTraining.as_view({'get': 'viewtrainingdetails'})),
    # url endpoint to list trainings based on location-- <int:pk> below is the location id--
    path('api/v1/viewtrainings/<int:pk>', viewTraining.as_view({'get': 'viewtrainingdetails'})),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('logout/', TokenRevokeSet.as_view({'delete': 'revoke'})),
    # API endpoint for get all location details including location id
    path('api/v1/locations/', LocationList.as_view({'get': 'locations'})),
    path('api/v1/activities/', ActivityList.as_view({'get': 'activities'})),
    # API endpoint for get location name and location address
    path('api/v1/locationsonly/', LocationDetails.as_view({'get': 'location_details'})),
    # url endpoint to cancel enrollments for trainings--<int:pk> below is the training id--
    path('api/v1/cancelenrollment/<int:pk>', cancelEnrollment.as_view({'delete': 'destroy'})),
    path('api/v1/logHours/', ActivityLogView.as_view({'post': 'create'})),
    # API endpoint for view member specific training enrollment details
    path('api/v1/viewmembertrainingenrollment/', ViewMemberTrainingEnrollment.as_view({'get': 'list'})),
    # path('api/v1/getActivityLog/', ActivityLogSet.as_view({'get': 'getActivityLog'})),
    # path('api/v1/equipmenttypes/<int:pk>', EquipmentViewSet.as_view({'get': 'equipmenttypes'})),
    # url endpoint get enrollment statistics
    path('api/v1/enrollmentstats/', enrollmentStats.as_view({'get': 'getEnrollmentStats'})),
    path('api/v1/loghoursCount/<int:location_id>/', HoursCountByLocationViewSet.as_view({'get': 'list'}))
    # path('api/v1/visitorCount/<int:location_id>/', VisitorCountByHourViewSet.as_view({'get': 'list'})),
]

from django.urls import path, include
from . import views

urlpatterns = [
    # LMS 메인 페이지 (강의 리스트)를 가리킵니다.
    path('index/', views.index, name='index'), 
    
    # 수정: 홈페이지 접속 시 views.dashboard 함수 실행
    path('', views.dashboard, name='dashboard'), 
    
    # 기존 로그인 페이지는 'login/' 주소로 옮김 (옵션)
    path('login/', views.login_page, name='login'), 
    
    path('classroom/<int:course_id>/', views.course_detail, name='course_detail'),
    # ... 다른 URL 경로들
]
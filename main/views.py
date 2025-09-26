from django.shortcuts import render, redirect

def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'main/login.html')

def dashboard(request):
    return render(request, 'main/dashboard.html')

def index(request):
    return render(request, 'main/index.html')

def course_detail(request, course_id):
    course_data = {
        1: '개인정보보호 영향평가(01반)',
        2: '실전사물인터넷(IoT)보안실무(캡스톤디자인)(01반)',
        3: '취약점진단 실무(01반)',
    }
    course_name = course_data.get(course_id, '알 수 없는 강의')
    
    context = {
        'course_name': course_name,
    }
    
    return render(request, 'main/course_detail.html', context)
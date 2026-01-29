from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

class LoginRequiredMiddleware :
    
    def __init__(self, get_response) :
        self.get_response = get_response
        self.login_url = reverse('login')
        
    def __call__(self, request) :
        
        #로그인 페이지, 로그아웃 페이지 등 로그인 관련 URL은 통과
        if request.path == self.login_url or request.path == reverse('logout') :
            return self.get_response(request)
        
        #인증되지 않은 사용자(로그인 하지 않은) 라면 로그인 페이지로 리디렉션
        if not request.user.is_authenticated :
            return redirect(self.login_url)
        
        # 로그인 된 사용자라면 다음 미들웨어 또는 뷰 처리 진행
        response = self.get_response(request)
        return response
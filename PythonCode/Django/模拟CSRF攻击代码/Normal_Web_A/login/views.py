from django.shortcuts import render, redirect, reverse
from django.views import View
from django import http

# Create your views here.


class Login(View):

    def get(self, request):
        """提供登录页面"""
        return render(request, 'login.html')

    def post(self, request):
        """模拟实现登录逻辑"""
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'zxc' and password == '123':
            # 模拟登录成功
            response = redirect('/transfer/')
            response.set_cookie('account', username)
            return response


class Transfer(View):

    def get(self, request):
        """提供转账页面"""
        return render(request, 'transfer.html')

    def post(self, request):
        """模拟实现转账逻辑"""
        username = request.COOKIES.get('account')
        if not username:
            return http.HttpResponse('用户未登录')

        # 假装执行转操作，将当前登录用户的钱转账到指定账户
        to_account = request.POST.get("to_account")
        money = request.POST.get("money")

        return http.HttpResponse('转账 %s 元到 %s 成功' % (money, to_account))



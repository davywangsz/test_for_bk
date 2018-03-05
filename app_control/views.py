# -*- coding: utf-8 -*-
from common.mymako import render_mako_context, render_json
from app_control.models import FunctionController
from app_control.decorators import function_check
from account.decorators import login_exempt


def home(request):
    """
    首页
    """
    result, is_enabled = FunctionController.objects.func_check('func_test')
    return render_mako_context(request, '/app_control/home.html', {'is_enabled': is_enabled})


def switch_func(request):
    """
    功能开关选择
    """
    status = int(request.POST.get('status', 0))
    # 更改功能开关的状态
    FunctionController.objects.update_func_status('func_test', status)
    return render_json({'result': True})


@function_check('func_test')
def execute_func(request):
    """
    执行测试功能
    """
    return render_json({'result': True, 'message': u"这是一个功能开发样例"})


@login_exempt
def check_failed(request):
    """
    功能开关检查失败
    """
    return render_mako_context(request, '/app_control/func_check_failed.html')

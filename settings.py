def login(request):
    name=request.post.get("name")
    pwd=request.post.get("pwd")
    return HttpResponse("登录成功")

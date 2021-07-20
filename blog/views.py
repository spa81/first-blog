from django.shortcuts import render

def test1(request):
    return render(request, 'blog/test1.HTML', {})

def post_list(request):
    return render(request, 'blog/post_list.HTML',{})

# Create your views here.

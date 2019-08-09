from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'light_main.html')

def oneselection(request):
    return render(request, 'one_selection.html')

def twoselection(request):
    return render(request, 'two_selection.html')

def threeselection(request):
    return render(request, 'three_selection.html')

def mypage(request):
    return render(request, 'mypage.html')

def buy(request):
    return render(request, 'buy.html')


# def detail(request, light_id):
#     light_detail = get_object_or_404(Light, pk=light_id)
#     return render(request, 'detail.html', {'light':light_detail})

from django.shortcuts import render, redirect,get_object_or_404
from django.utils import timezone
from django.urls import reverse
from .models import Info
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from .forms import infoForm
from django.core.exceptions import PermissionDenied


def index(request):
    all_infos = Info.objects.all().order_by("-pub_date")
    return render(request, 'share_info/shareinfo.html', {'title': 'info List', 'info_list': all_infos})

def detail(request, info_id):
    info = Info.objects.get(id=info_id)
    return render(request, 'share_info/infodetail.html', {'info': info})

# def write(request):
#     # 전공(major) 선택을 위한 데이터
#     major_values = [
#         "국어국문학전공", "일어일문학전공", "중어중문학전공", "영어영문학전공",
#         "불어불문학전공", "독어독문학전공", "스페인어전공", "사학전공",
#         "철학전공", "미술사학전공", "문화인류전공", "경영학전공",
#         "회계학전공", "국제통상학전공", "법학전공", "사회학전공",
#         "문헌정보학", "전공심리학전공", "아동가족학전공", "사회복지학전공",
#         "정치외교학전공", "의상디자인전공", "유아교육과"
#     ]

#     context = {
#         'major_values': major_values
#     }
#     return render(request, 'share_info/infopost.html', context)

# def write_info(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         detail = request.POST.get('detail')
#         major = request.POST.get('major')  # 추가한 전공 값
#         author = request.user.username  # 현재 로그인된 사용자의 유저네임
#         pub_date = timezone.now()

#         bb = Info(title=title, content=detail, major=major, author=author, pub_date=pub_date)
#         bb.save()

#     # 게시글 작성 후 게시글 목록 페이지로 이동
#     all_infos = Info.objects.all().order_by("-pub_date")
#     return render(request, 'share_info/shareinfo.html', {'title': 'info List', 'info_list': all_infos})

def write_info(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        detail = request.POST.get('detail')
        major = request.POST.get('major')
        author = request.user.username
        pub_date = timezone.now()

        bb = Info(title=title, content=detail, major=major, author=author, pub_date=pub_date)
        bb.save()
        return redirect('share_info:index')

    # 전공(major) 선택을 위한 데이터
    major_values = [
        "국어국문학전공", "일어일문학전공", "중어중문학전공", "영어영문학전공",
        "불어불문학전공", "독어독문학전공", "스페인어전공", "사학전공",
        "철학전공", "미술사학전공", "문화인류전공", "경영학전공",
        "회계학전공", "국제통상학전공", "법학전공", "사회학전공",
        "문헌정보학", "전공심리학전공", "아동가족학전공", "사회복지학전공",
        "정치외교학전공", "의상디자인전공", "유아교육과"
    ]

    context = {
        'major_values': major_values
    }
    return render(request, 'share_info/infopost.html', context)


# def editinfo(request, pk):
#     if request.user.is_authenticated:
#         item = get_object_or_404(Info, pk=pk)
#         if request.method == 'POST':
#             info_form = infoForm(request.POST)
#             if info_form.is_valid():
#                 info = info_form.save(info=False)
#                 info.item = item
#                 info.author = request.user
#                 info.save()
#                 return redirect(info.get_absolute_url())
#         else:
#             return redirect(item.get_absolute_url())
#     else:
#         raise PermissionDenied

# def edit_info(request, info_id):
#     info_to_edit = get_object_or_404(Info, pk=info_id)
    
#     if request.method == 'POST':
#         info_to_edit.title = request.POST.get('title')
#         info_to_edit.content = request.POST.get('detail')
#         info_to_edit.major = request.POST.get('major')
#         info_to_edit.save()
#         return redirect('share_info:index')

#     major_values = [
#         "국어국문학전공", "일어일문학전공", "중어중문학전공", "영어영문학전공",
#         "불어불문학전공", "독어독문학전공", "스페인어전공", "사학전공",
#         "철학전공", "미술사학전공", "문화인류전공", "경영학전공",
#         "회계학전공", "국제통상학전공", "법학전공", "사회학전공",
#         "문헌정보학", "전공심리학전공", "아동가족학전공", "사회복지학전공",
#         "정치외교학전공", "의상디자인전공", "유아교육과"
#     ]

#     context = {
#         'major_values': major_values,
#         'info': info_to_edit
#     }
#     return render(request, 'share_info/inforepost.html', context)


def edit_info(request, info_id):
    info = get_object_or_404(Info, pk=info_id)
    
    if request.method == 'GET':
        context = { 'info' : info }
        return render(request, 'share_info/inforepost.html', context)
    elif request.method == 'POST':
        info.title = request.POST.get('title')
        info.content = request.POST.get('detail')
        info.major = request.POST.get('major')
        info.save()
        return redirect('share_info:index')

    # major_values = [
    #     "국어국문학전공", "일어일문학전공", "중어중문학전공", "영어영문학전공",
    #     "불어불문학전공", "독어독문학전공", "스페인어전공", "사학전공",
    #     "철학전공", "미술사학전공", "문화인류전공", "경영학전공",
    #     "회계학전공", "국제통상학전공", "법학전공", "사회학전공",
    #     "문헌정보학", "전공심리학전공", "아동가족학전공", "사회복지학전공",
    #     "정치외교학전공", "의상디자인전공", "유아교육과"
    # ]

    # context = {
    #     'major_values': major_values,
    #     'info': info_to_edit
    # }
    # return render(request, 'share_info/inforepost.html', context)

# class infoUpdate(LoginRequiredMixin, UpdateView):
#     model = Info
#     form_class = infoForm

#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated and request.user == self.get_object().author:
#             return super(infoUpdate, self).dispatch(request, *args, **kwargs)
#         else:
#             raise PermissionDenied
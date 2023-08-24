from django.shortcuts import render, redirect
from .models import Archive, Major


# Create your views here.
def main(request):
    return render(request, 'gradpage/main.html')


# 과기대
def computer(request, major_id=None):
    archive_list = Archive.objects.filter(major = 1)
    return render(request, 'gradpage/computer.html', {'archive_list':archive_list,'major_id': major_id})

def itmedia_department(request,major_id=None):
    archive_list = Archive.objects.filter(major = 2)
    return render(request, 'gradpage/itmedia.html',{'archive_list':archive_list,'major_id': major_id})

def software_department(request,major_id=None):
    archive_list = Archive.objects.filter(major = 3)
    return render(request, 'gradpage/software.html',{'archive_list':archive_list,'major_id': major_id})

def cyber_department(request,major_id=None):
    archive_list = Archive.objects.filter(major = 4)
    return render(request, 'gradpage/cyber.html',{'archive_list':archive_list,'major_id': major_id})

def bio_department(request):
    return render(request, 'gradpage/bio.html')

def technology_view(request):
    return render(request, 'gradpage/technology.html')

def sports_department(request):
    return render(request, 'gradpage/sports.html')

def food_department(request):
    return render(request, 'gradpage/food.html')

def infstatic_department(request):
    return render(request, 'gradpage/infstatic.html')

def chemical_department(request):
    return render(request, 'gradpage/chemical.html')

def math_department(request):
    return render(request, 'gradpage/math.html')

def create_archiving(request):
    if request.method == 'POST':
        exhibit_title = request.POST.get('exhibit_title')
        service_title = request.POST.get('service_title')
        major = request.POST.get('major')
        team_name = request.POST.get('team_name')
        team_member = request.POST.get('team_member')
        description = request.POST.get('description')

        # 파일 업로드 처리
        file = request.FILES.get('file')

        # major_instance, created = Major.objects.get_or_create(name=major_name)

        # Archive 모델 생성 및 저장
        a = Archive(
            exhibit_title=exhibit_title,
            service_title=service_title,
            major=major,
            team_name=team_name,
            team_member=team_member,
            description=description,
            file=file
        )
        a.save()
        return redirect('computer') # 수정해야됨

    return render(request, 'gradpage/archiving.html')

# 글로벌 융합대학 

def global_view(request):
    return render(request, 'gradpage/global.html')

def china_department(request):
    return render(request, 'gradpage/china.html')

def english_department(request):
    return render(request, 'gradpage/english.html')

def france_department(request):
    return render(request, 'gradpage/france.html')

def germany_department(request):
    return render(request, 'gradpage/germany.html')

def spain_department(request):
    return render(request, 'gradpage/spain.html')

def philosophy_department(request):
    return render(request, 'gradpage/philosophy.html')

def arthistory_department(request):
    return render(request, 'gradpage/arthistory.html')

def culperson_department(request):
    return render(request, 'gradpage/culperson.html')

def manange_department(request):
    return render(request, 'gradpage/manage.html')

def account_department(request):
    return render(request, 'gradpage/account.html')

def intertrade_department(request):
    return render(request, 'gradpage/intertrade.html')

def law_department(request):
    return render(request, 'gradpage/law.html')

def social_department(request):
    return render(request, 'gradpage/social.html')

def literinf_department(request):
    return render(request, 'gradpage/literinf.html')

def psychology_department(request):
    return render(request, 'gradpage/psychology.html')

def childfam_department(request):
    return render(request, 'gradpage/childfam.html')

def socwel_department(request):
    return render(request, 'gradpage/socwel.html')

def poldiplo_department(request):
    return render(request, 'gradpage/poldiplo.html')

def fashion_department(request):
    return render(request, 'gradpage/fashion.html')

def childedu_department(request):
    return render(request, 'gradpage/childedu.html')

def japan_department(request):
    return render(request, 'gradpage/japan.html')

def korea_department(request):
    return render(request, 'gradpage/korea.html')

def history_department(request):
    return render(request, 'gradpage/history.html')

# 미대 - 아카이빙 연결
def art_view(request):
    return render(request, 'gradpage/art.html')

def eastart_department(request):
    archive_list = Archive.objects.all()
    return render(request, 'gradpage/eastart.html')

def westart_department(request):
    archive_list = Archive.objects.all()
    return render(request, 'gradpage/westart.html')

def visual_department(request):
    archive_list = Archive.objects.all()
    return render(request, 'gradpage/visual.html')

def interior_department(request):
    archive_list = Archive.objects.all()
    return render(request, 'gradpage/interior.html')

def textile_department(request):
    archive_list = Archive.objects.all()
    return render(request, 'gradpage/textile.html')
# 약대
def medi_view(request):
    return render(request, 'gradpage/medi.html')

def medical4_department(request):
    return render(request, 'gradpage/medical4.html')

def medical6_department(request):
    return render(request, 'gradpage/medical6.html')
# 미래대학
def future_view(request):
    return render(request, 'gradpage/future.html')

def koreacul_department(request):
    return render(request, 'gradpage/koreacul.html')

def koreaedu_department(request):
    return render(request, 'gradpage/koreaedu.html')

#2
def semester(request):
    return render(request, 'gradpage/semester.html')
def gradpost(request):
    return render(request, 'gradpage/gradpost.html')
def completion(request):
    return render(request, 'gradpage/completion.html')
def earlygrad(request):
    return render(request, 'gradpage/earlygrad.html')
# 커뮤니티
def shareinfo(request):
    return render(request, 'share_info/shareinfo.html')
def teamboard(request):
    return render(request, 'team_board/community.html')

def chatbot(request):
    return render(request, 'chatbot.html')

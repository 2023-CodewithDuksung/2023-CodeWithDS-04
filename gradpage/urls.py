from django.urls import path
from gradpage import views

urlpatterns = [
    path('', views.main, name="main"),
    path('computer/', views.computer, name="computer"),
    path('createArchiving/', views.create_archiving, name='create_archiving'),
    path('computer/itmedia/', views.itmedia_department, name='itmedia_department'),
    # computer에서 dropdown으로 선택학과 - 아카이빙 (미대까지)
    path('computer/software/', views.software_department, name='software_department'),
    path('computer/cyber/', views.cyber_department, name='cyber_department'),
    # main에서 각 페이지
    path('technology/', views.technology_view, name='technology'),
    path('global/', views.global_view, name='global'),
    path('medi/', views.medi_view, name='medi'),
    path('art/', views.art_view, name='art'),
    path('future/', views.future_view, name='future'),
    # technology에서 글씨 선택학과
    path('technology/bio_department/', views.bio_department, name='bio_department'),
    path('technology/itemedia_department/', views.itmedia_department, name='itemedia_department'),
    path('technology/cyber_department/', views.cyber_department, name='cyber_department'),
    path('technology/sports_department/', views.sports_department, name='sports_department'),
    path('technology/software_department/', views.software_department, name='software_department'),
    path('technology/food_department/', views.food_department, name='food_department'),
    path('technology/infstatic_department/', views.infstatic_department, name='infstatic_department'),
    path('technology/chemical_department/', views.chemical_department, name='chemical_department'),
    path('technology/math_department/', views.math_department, name='math_department'),
    # global에서 선택학과 
    path('global/korea_department/', views.korea_department, name='korea_department'),
    path('global/japan_department/', views.japan_department, name='japan_department'),
    path('global/china_department/', views.china_department, name='china_department'),
    path('global/english_department/', views.english_department, name='english_department'),
    path('global/france_department/', views.france_department, name='france_department'),
    path('global/germany_department/', views.germany_department, name='germany_department'),
    path('global/spain_department/', views.spain_department, name='spain_department'),
    path('global/history_department/', views.history_department, name='history_department'),
    path('global/philosophy_department/', views.philosophy_department, name='philosophy_department'),
    path('global/arthistory_department/', views.arthistory_department, name='arthistory_department'),
    path('global/culperson_department/', views.culperson_department, name='culperson_department'),
    path('global/manange_department/', views.manange_department, name='manange_department'),
    path('global/account_department/', views.account_department, name='account_department'),
    path('global/intertrade_department/', views.intertrade_department, name='intertrade_department'),
    path('global/law_department/', views.law_department, name='law_department'),
    path('global/social_department/', views.social_department, name='social_department'),
    path('global/literinf_department/', views.literinf_department, name='literinf_department'),
    path('global/psychology_department/', views.psychology_department, name='psychology_department'),
    path('global/childfam_department/', views.childfam_department, name='childfam_department'),
    path('global/socwel_department/', views.socwel_department, name='socwel_department'),
    path('global/poldiplo_department/', views.poldiplo_department, name='poldiplo_department'),
    path('global/fashion_department/', views.fashion_department, name='fashion_department'),
    path('global/childedu_department/', views.childedu_department, name='childedu_department'),
    # medi 글씨 선택학과
    path('medi/medical4_department/', views.medical4_department, name='medical4_department'),
    path('medi/medical6_department/', views.medical6_department, name='medical6_department'),
    # art 글씨 선택학과
    path('art/eastart_department/', views.eastart_department, name='eastart_department'),
    path('art/westart_department/', views.westart_department, name='westart_department'),
    path('art/interior_department/', views.interior_department, name='interior_department'),
    path('art/visual_department/', views.visual_department, name='visual_department'),
    path('art/textile_department/', views.textile_department, name='textile_department'),
    # future 글씨 선택학과
    path('future/koreacul_department/', views.koreacul_department, name='koreacul_department'),
    path('future/koreaedu_department/', views.koreaedu_department, name='koreaedu_department'),

]

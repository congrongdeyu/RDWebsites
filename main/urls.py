from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^gongsijianjie', views.gongsijianjie, name='gongsijianjie'),
    url(r'^guanlituandui', views.guanlituandui, name='guanlituandui'),
    url(r'^gongsirongyu', views.gongsirongyu, name='gongsirongyu'),
    url(r'^fazhanlicheng', views.fazhanlicheng, name='fazhanlicheng'),
    url(r'^zhanluehezuo', views.zhanluehezuo, name='zhanluehezuo'),
    url(r'^zhanlueyuanjing', views.zhanlueyuanjing, name='zhanlueyuanjing'),
    url(r'^research', views.research, name='research'),
    url(r'^news', views.news, name='news'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<news>[-\w]+)/$',
        views.news_detail,
        name='news_detail'),
    url(r'^products', views.products, name='products'),
    url(r'xiaofenzibaxianghuahewu', views.xiaofenzibaxianghuahewu, name='xiaofenzibaxianghuahewu'),
    url(r'stat3', views.stat3, name='stat3'),
    url(r'parpyizhiji', views.parpyizhiji, name='parpyizhiji'),
    url(r'tianranchanwujixinmoxing', views.tianranchanwujixinmoxing, name='tianranchanwujixinmoxing'),
    url(r'jianghuangsu', views.jianghuangsu, name='jianghuangsu'),
    url(r'shengwuzhiji', views.shengwuzhiji, name='shengwuzhiji'),
    url(r'xibaoyinzi', views.xibaoyinzi, name='xibaoyinzi'),
    url(r'fenzishengwuxuechanpin', views.fenzishengwuxuechanpin, name='fenzishengwuxuechanpin'),
    url(r'PCRshiji', views.PCRshiji, name='PCRshiji'),
    url(r'fenzikelongyuDNAMarker', views.fenzikelongyuDNAMarker, name='fenzikelongyuDNAMarker'),
    url(r'ganshoutaixibao', views.ganshoutaixibao, name='ganshoutaixibao'),
    url(r'jiyinjiance', views.jiyinjiance, name='jiyinjiance'),
    url(r'jishufuwu', views.jishufuwu, name='jishufuwu'),
    url(r'yinwuhecheng', views.yinwuhecheng, name='yinwuhecheng'),
    url(r'DNAcexu', views.DNAcexu, name='DNAcexu'),
    url(r'FDExome', views.FDExome, name='FDExome'),
    url(r'FD180', views.FD180, name='FD180'),
    url(r'^research', views.research, name='research'),
    url(r'^primer', views.primer, name='primer'),
    url(r'^stat3yizhiji', views.stat3yizhiji, name='stat3yizhiji'),
    url(r'^chongzudanbai', views.chongzudanbai, name='chongzudanbai'),
    url(r'^employment', views.employment, name='employment'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<employment>[-\w]+)/(?P<category>[-\w]+)/$',
        views.employment_detail,
        name='employment_detail'),
    url(r'^cooperation', views.cooperation, name='cooperation'),
    url(r'^contacts', views.contacts, name='contacts'),
]
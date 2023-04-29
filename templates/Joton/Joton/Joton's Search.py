import ybc_browser as br
import ybc_box as box

while True:
    baiduroot = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd='
    baikeroot = 'https://baike.baidu.com/item/'
    bingroot = 'https://cn.bing.com/search?q='
    sogouroot = 'https://www.sogou.com/web?query='
    root360 = 'https://www.so.com/s?ie=utf-8&fr=so.com&src=home_so.com&q='
    google404root = 'https://www.google.com/search?q='
    quarkroot = 'https://quark.sm.cn/s?q='
    magiroot = 'https://magi.com/search?q='
    yandexroot = 'https://yandex.com/search/?text='
    naverroot = 'https://search.naver.com/search.naver?query='
    lycosroot = 'https://search.lycos.com/web/?q='
    chinaroot = 'https://www.chinaso.com/newssearch/all/allResults?q='
    fresheyeroot = 'https://search.fresheye.com/?kw='
    ceekroot = 'http://www.ceek.jp/search.cgi?q='
    dackdackgoroot = 'https://duckduckgo.com/?q='
    yinqingdict = {'百度':baiduroot,'百度百科':baikeroot,'中国搜索':chinaroot,'Bing':bingroot,'搜狗':sogouroot,'360':root360,'Google':google404root,'夸克':quarkroot,'magi':magiroot,'Yandex':yandexroot,'Naver':naverroot,'Lycos':lycosroot,'Fresheye':fresheyeroot,'Ceek':ceekroot,'DuckDuckGo':dackdackgoroot}
    yinqing = box.buttonbox('选择搜索引擎',['百度','百度百科','中国搜索','Bing','Google','搜狗','夸克','360','magi', 'Yandex','Naver','Lycos','Fresheye','Ceek','DuckDuckGo','全部都要'])
    if yinqing != None:
        search = box.enterbox('输入搜索内容')
        if search != '' and search != '':
            if yinqing == '全部都要':
                yinqinglist = ['百度','百度百科','中国搜索','Bing','Google','搜狗','夸克','360','magi','Yandex','Naver','Lycos','Fresheye','Ceek','DuckDuckGo']
                for i in yinqinglist:
                    root = yinqingdict[i]+search
                    br.open(root)
            else:
                root = yinqingdict[yinqing]+search
                br.open(root)
    else:
        break
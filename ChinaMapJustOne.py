from pyecharts.charts import Map,Timeline
from pyecharts import options as opts

dictProvice={'Anhui':'安徽','Beijing':'北京','Chongqing':'重庆',
             'Fujian':'福建','Gansu':'甘肃','Guangdong':'广东',
             'Guangxi':'广西','Guizhou':'贵州','Hainan':'海南',
             'Hebei':'河北','Heilongjiang':'黑龙江','Henan':'河南',
             'Hong Kong':'香港','Hubei':'湖北','Hunan':'湖南',
             'Inner Mongolia':'内蒙古','Jiangsu':'江苏','Jiangxi':'江西',
             'Jilin':'吉林','Liaoning':'辽宁','Macau':'澳门',
             'Ningxia':'宁夏','Qinghai':'青海','Shaanxi':'陕西',
             'Shandong':'山东','Shanghai':'上海','Shanxi':'山西',
             'Sichuan':'四川','Tianjin':'天津','Tibet':'西藏',
             'Xinjiang':'新疆','Yunnan':'云南','Zhejiang':'浙江','Taiwan*':'台湾'}

FileConfirmed=open('source/GlobalConfirm.csv', 'r')
lines=FileConfirmed.readlines()

head=lines[0].split(',') # index0为省份，1为国家地区，2为纬度，3为经度，后面的都是日期M/D/Y
lines.pop(0)

tl = Timeline()
tl.add_schema(is_auto_play=True,symbol_size=4)
times=[]
sum=[]

for i in range(4,94,1):
    map = Map(init_opts=opts.InitOpts(height='500px', width='800px'))

    provices=[]
    valuse=[]

    count=0
    temptime=head[i].split('/')
    time='2020-'+temptime[0]+'-'+temptime[1]
    times.append(temptime[0]+'/'+temptime[1]+' 6:00')

    for line in lines:
        lineMessage=line.split(',')
        if  lineMessage[1]=='China' or lineMessage[1]=='Taiwan*':
            if lineMessage[1]=='Taiwan*':
                provices.append(dictProvice[lineMessage[1]])
            else:
                provices.append(dictProvice[lineMessage[0]])
                count+=int(lineMessage[i])
            valuse.append(lineMessage[i])
    sum.append(count)

    pieces = [
        {'max': 0, 'label': '0', 'color': '#e8eaf6'},
        {'min': 1, 'max': 50, 'label': '1-50', 'color': '#7986cb'},
        {'min': 50, 'max': 100, 'label': '50-100', 'color': '#b39ddb'},
        {'min': 100, 'max': 500, 'label': '100-500', 'color': '#ce93d8'},
        {'min': 500, 'max': 1000, 'label': '500-1000', 'color': '#f48fb1'},
        {'min': 1000, 'max': 5000, 'label': '1000-5000', 'color': '#e57373'},
        {'min': 1000,  'label': '5000+', 'color': '#c62828'},
    ]

    # noinspection PyTypeChecker
    map.add('', zip(provices,valuse))

    map.set_series_opts(label_opts=opts.LabelOpts(is_show=False))

    map.set_global_opts(
        visualmap_opts=opts.VisualMapOpts(is_piecewise=True, pieces=pieces,pos_left='100px'),
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{b}<br/>{c}"),
    )


    filepath = 'Maps/'+time+'.html'
    map.render(path=filepath)
    tl.add(map, "{}".format(time))

tl.render("ChinaChart/ChinaMap.html")

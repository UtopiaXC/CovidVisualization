from pyecharts import options as opts
from pyecharts.charts import Map, Timeline

hubeiDict={
    '武汉':'武汉市','孝感':'孝感市','黄冈':'黄冈市',
    '荆州':'荆州市','鄂州':'鄂州市','随州':'随州市',
    '襄阳':'襄阳市','黄石':'黄石市','宜昌':'宜昌市',
    '咸宁':'咸宁市','十堰':'十堰市','仙桃':'仙桃市',
    '天门':'天门市','恩施州':'恩施土家族苗族自治州',
    '潜江':'潜江市','神农架林区':'神农架林区','荆门':'荆门市'
}

pieces = [
    {'max': 1, 'label': '0', 'color': '#e8eaf6'},
    {'min': 1, 'max': 50, 'label': '1-50', 'color': '#7986cb'},
    {'min': 50, 'max': 100, 'label': '50-100', 'color': '#b39ddb'},
    {'min': 100, 'max': 500, 'label': '100-500', 'color': '#ce93d8'},
    {'min': 500, 'max': 1000, 'label': '500-1000', 'color': '#f48fb1'},
    {'min': 1000, 'max': 5000, 'label': '1000-5000', 'color': '#e57373'},
    {'min': 1000, 'label': '5000+', 'color': '#c62828'},
]



FileArea=open('source/AreaDatas.csv','r',encoding='utf-8')
lines=FileArea.readlines()

line_cities=[]

for line in lines:
    lineMessage=line.split(',')
    if lineMessage[4]=='湖北省':
        line_cities.append(line)

tl = Timeline()
tl.add_schema(is_auto_play=True,symbol_size=4)

for i in range(1,5,1):
    for j in range(1,32,1):
        if((i==1 and j<24) or (i==2 and j==31) or (i==4 and j>22)):
            continue
        cities=[]
        values=[]
        for line in line_cities:
            lineMessage=line.split(',')
            month=int(lineMessage[11].split(' ')[0].split('-')[1])
            day=int(lineMessage[11].split(' ')[0].split('-')[2])
            if(month==i and day==j):
                if(lineMessage[12] != '' and lineMessage[12] != '未知地区'
                        and lineMessage[12] != '待明确地区'
                        and lineMessage[12] != '监狱系统'):
                    if(hubeiDict[lineMessage[12]] not in cities):
                        cities.append(hubeiDict[lineMessage[12]])
                        values.append(int(lineMessage[15]))

        if not values:
            continue


        map=Map(init_opts=opts.InitOpts(width="800px", height="500px"))
        # noinspection PyTypeChecker
        map.add(
                series_name="",
                maptype="湖北",
                data_pair=zip(cities,values),
                is_map_symbol_show=False,
                )
        map.set_global_opts(
                visualmap_opts=opts.VisualMapOpts(is_piecewise=True, pieces=pieces, pos_left='50px'),
                tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{b}<br/>{c}"),
            )
        map.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        map.render("Hubei/2020-"+str(i)+'-'+str(j)+".html")
        tl.add(map, "{}".format('2020-' + str(i)+'-' + str(j)))

tl.render("ChinaChart/HubeiMap.html")

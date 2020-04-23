from pyecharts import options as opts
from pyecharts.charts import Map, Timeline

GuangdongDict={
    '长沙':'长沙市','岳阳':'岳阳市','邵阳':'邵阳市',
    '常德':'常德市','株洲':'株洲市','娄底':'娄底市',
    '益阳':'益阳市','衡阳':'衡阳市','永州':'永州市',
    '怀化':'怀化市','郴州':'郴州市','湘潭':'湘潭市',
    '湘西自治州':'湘西土家族苗族自治州','张家界':'张家界市'
}

pieces = [
    {'max': 1, 'label': '0', 'color': '#e8eaf6'},
    {'min': 1, 'max': 10, 'label': '1-10', 'color': '#7986cb'},
    {'min': 10, 'max': 20, 'label': '10-20', 'color': '#b39ddb'},
    {'min': 20, 'max': 50, 'label': '20-50', 'color': '#ce93d8'},
    {'min': 50, 'max': 100, 'label': '50-100', 'color': '#f48fb1'},
    {'min': 100, 'max': 200, 'label': '100-200', 'color': '#e57373'},
    {'min': 200, 'label': '200+', 'color': '#c62828'},
]



FileArea=open('source/AreaDatas.csv','r',encoding='utf-8')
lines=FileArea.readlines()

line_cities=[]

for line in lines:
    lineMessage=line.split(',')
    if lineMessage[4]=='湖南省':
        line_cities.append(line)
        print(line)

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
                if(lineMessage[12] != '' and lineMessage[12] != '未知'
                        and lineMessage[12] != '未明确地区'
                        and lineMessage[12] != '监狱系统'
                        and lineMessage[12] != '境外输入'
                        and lineMessage[12] != '待明确地区'
                        and lineMessage[12] != '未知地区'):
                    if(GuangdongDict[lineMessage[12]] not in cities):
                        cities.append(GuangdongDict[lineMessage[12]])
                        values.append(int(lineMessage[15]))
        if not values:
            continue


        map=Map(init_opts=opts.InitOpts(width="800px", height="500px"))
        # noinspection PyTypeChecker
        map.add(
                series_name="",
                maptype="湖南",
                data_pair=zip(cities,values),
                is_map_symbol_show=False,
                )
        map.set_global_opts(
                visualmap_opts=opts.VisualMapOpts(is_piecewise=True, pieces=pieces, pos_left='50px'),
                tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{b}<br/>{c}"),
            )
        map.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        map.render("Hunan/2020-"+str(i)+'-'+str(j)+".html")
        tl.add(map, "{}".format('2020-' + str(i) +'-'+ str(j)))

tl.render("ChinaChart/HunanMap.html")
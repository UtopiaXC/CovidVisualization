from pyecharts import options as opts
from pyecharts.charts import Map

GuangdongDict={
    '信阳':'信阳市','郑州':'郑州市','南阳':'南阳市',
    '驻马店':'驻马店市','商丘（含永城）':'商丘市','周口':'周口市',
    '平顶山':'平顶山市','新乡':'新乡市','安阳':'安阳市',
    '许昌':'许昌市','漯河':'漯河市','焦作':'焦作市',
    '洛阳':'洛阳市','开封':'开封市',
    '鹤壁':'鹤壁市','濮阳':'濮阳市','三门峡':'三门峡市',
    '济源':'济源市','巩义':'巩义市','安阳市':'安阳市','漯河市':'漯河市',
    '鹤壁市':'鹤壁市','商丘':'商丘市','安阳（含滑县）':'安阳市',
    '新乡（含长垣）':'新乡市'
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
    if lineMessage[4]=='河南省':
        line_cities.append(line)
        print(line)


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
                if(lineMessage[12] != '' and lineMessage[12] != '固始县'
                        and lineMessage[12] != '未明确地区'
                        and lineMessage[12] != '境外输入'
                        and lineMessage[12] != '待明确地区'
                        and lineMessage[12] != '滑县'
                        and lineMessage[12] != '未知地区'
                        and lineMessage[12] != '长垣县'
                        and lineMessage[12] != '长垣'
                        and lineMessage[12] != '邓州'
                        and lineMessage[12] != '南阳（含邓州）'
                        and lineMessage[12] != '永城'
                        and lineMessage[12] != '境外输入人员'
                ):
                    if(GuangdongDict[lineMessage[12]] not in cities):
                        cities.append(GuangdongDict[lineMessage[12]])
                        values.append(int(lineMessage[15]))

        # noinspection PyTypeChecker
        c = (
            Map(init_opts=opts.InitOpts(width="800px", height="500px"))
                .add(
                series_name="",
                maptype="河南",
                data_pair=zip(cities,values),
                is_map_symbol_show=False,
                )
                .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(is_piecewise=True, pieces=pieces, pos_left='50px'),
                tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{b}<br/>{c}"),
            )
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .render("Henan/2020-"+str(i)+'-'+str(j)+".html")
        )

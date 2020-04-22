from pyecharts import options as opts
from pyecharts.charts import Map

GuangdongDict={
    '广州':'广州市','深圳':'深圳市','佛山':'佛山市',
    '揭阳':'揭阳市','珠海':'珠海市','中山':'中山市',
    '湛江':'湛江市','肇庆':'肇庆市','梅州':'梅州市',
    '潮州':'潮州市','河源':'河源市','东莞':'东莞市',
    '惠州':'惠州市','汕头':'汕头市',
    '江门':'江门市','阳江':'阳江市','茂名':'茂名市',
    '清远':'清远市','韶关':'韶关市','汕尾':'汕尾市','河源市':'河源市',
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
    if lineMessage[4]=='广东省':
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
                if(lineMessage[12] != '' and lineMessage[12] != '未知'
                        and lineMessage[12] != '未明确地区'
                        and lineMessage[12] != '监狱系统' and lineMessage[12] != '外地来穗人员'
                        and lineMessage[12] != '外地来粤人员'
                        and lineMessage[12] != '待明确地区'
                        and lineMessage[12] != '未知地区'):
                    if(GuangdongDict[lineMessage[12]] not in cities):
                        cities.append(GuangdongDict[lineMessage[12]])
                        values.append(int(lineMessage[15]))

        # noinspection PyTypeChecker
        c = (
            Map(init_opts=opts.InitOpts(width="800px", height="500px"))
                .add(
                series_name="",
                maptype="广东",
                data_pair=zip(cities,values),
                is_map_symbol_show=False,
                )
                .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(is_piecewise=True, pieces=pieces, pos_left='50px'),
                tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{b}<br/>{c}"),
            )
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .render("Guangdong/2020-"+str(i)+'-'+str(j)+".html")
        )

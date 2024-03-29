from .utils import *
import  re
def getAllType():
    res=typeList('types');
    res1=[]
    for it in res:
        item=it.split(',')
        for item1 in item:
            res1.append(item1)
    return list(set(res1))
def getAllRateDateByType(type):
    if type =='all':
        rateList=df['rate'].values
        rateList.sort()
    else:
        typeList=df['types'].map(lambda x:x.split(sep=','))
        oldrateList = df['rate'].values
        rateList=[]
        for i,item in enumerate(typeList):
            if type in item:
                rateList.append(oldrateList[i])
    rateObj ={}
    for i in rateList:
        i=float(i)
        if rateObj.get(i,-1) == -1:
            rateObj[i]=1
        else:
            rateObj[i] =rateObj[i]+1
    return  list(rateObj.keys()),list(rateObj.values())

def getStart(searchIpt):
    startes = list(df.loc[df['title'].str.contains(searchIpt)]['starts'])[0].lstrip('[').rstrip(']').split(',')
    startes = [item.replace("'", '') for item in startes]
    startes = [item.strip()  for item in startes]
    # print(startes)
    searchName = list(df.loc[df['title'].str.contains(searchIpt)]['title'])[0]
    startDate=[{
        'name':'五星',
        'value':0,
    },{

    },{
        'name':'四星',
        'value':0,
    },{
        'name':'三星',
        'value':0,
    },{
        'name':'二星',
        'value':0,
    },{
        'name':'一星',
        'value':0,
    }]
    for i,item in enumerate(startes):
        startDate[i]['value']=float(re.sub('%','',item))
    return startDate,searchName

def getYearMeanData():
    yearList=list(set(df['year'].values))
    yearList1 = [int(s) for s in yearList]
    yearList1.sort()
    meanList =[]
    df['rate'] = pd.to_numeric(df['rate'], errors='coerce')

    # 替换无法转换的值为 NaN
    df['rate'].replace(['无法转换的值'], pd.NA, inplace=True)
    for i in yearList:  # 假设 years_to_consider 是你想要考虑的年份列表
        # 计算 'rate' 列的均值，但仅针对 'year' 列等于 i 的行
        mean_rate = df[df['year'] == i]['rate'].mean()

        # 如果 mean_rate 不是 NaN（即成功计算了均值）
        if not pd.isna(mean_rate):
            meanList.append(mean_rate)
        else:
            print(f"无法计算年份 {i} 的 'rate' 列均值，因为数据中存在缺失或无法转换的值。")
    return yearList1,meanList
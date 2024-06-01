
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def AnalizerAllDescirbe(CSVPath="./CSV/Top250-4.csv"):
    doubanDataset = pd.read_csv("./CSV/Top250-4.csv",encoding="utf-8")

    print("doubanDataset :",doubanDataset)
    print("doubanDataset.describ():",doubanDataset.describe())
    print("doubanDataset.index:",doubanDataset.index)
    print("doubanDataset.columns :",doubanDataset.columns)
    print("doubanDataset.values :",doubanDataset.values)
    print("doubanDataset.info() :",doubanDataset.info())
    print("doubanDataset[[\"图书名\",\"作者\"]] :",doubanDataset[["图书名","作者"]])
    print("doubanDataset[\"国家\"].unique() : ",doubanDataset["国家"].unique())


    NationDict = {"清":"中国清朝","美国":"美","明":"中国明朝","意":"意大利","俄":"俄罗斯","法国":"法","葡":"葡萄牙","印":"印度"
                ,"奥":"奥地利","挪":"挪威","白俄":"白俄罗斯","苏":"苏联","日":"日本"}
    doubanDataset.replace({"国家":NationDict},inplace=True)

    print(doubanDataset["国家"].unique())

    print(doubanDataset[doubanDataset["国家"] == "中国"])

    doubanDataset.loc[[4],"国家"] = "中国"
    plt.figure(figsize=(20,5))
    plt.hist(doubanDataset["价格"],bins=20)
    plt.show()

    print(doubanDataset["出版社"].value_counts())
    NationIndex = doubanDataset["国家"].value_counts().index
    NationCount = doubanDataset["国家"].value_counts().values
    print(NationIndex,NationCount)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(8,8))
    plt.pie(NationCount,labels=NationIndex,autopct="%1.1f%%")
    plt.title("Top250各国图书数量示意图")
    plt.savefig("./Images/Top250-BookCount.png")
    NationIndex = list(NationIndex)
    NationList = NationIndex[0:5]
    NationList.extend(["其他",NationIndex[-1]])
    print(NationList)
    NationCountValue = list(NationCount[0:5])
    NationCountValue.extend([np.sum(NationCount[5:-1]),NationCount[-1]])
    print(NationCountValue)
    plt.figure(figsize=(8,8))
    plt.pie(NationCountValue,labels=NationList,autopct="%1.1f%%",explode=(0,0,0,0,0,0,0.5),startangle=185);
    doubanDataByNation = doubanDataset.groupby(["国家"])
    print(doubanDataByNation)
    print(doubanDataByNation.count())
    PriceNationSum = doubanDataByNation.sum()["价格"].sort_values(ascending=False)
    print(PriceNationSum)
    PriceIndex = PriceNationSum.index
    PriceSum = PriceNationSum.values
    print(PriceIndex,PriceSum)
    PriceNationIndex = list(PriceIndex[0:5])
    PriceNationIndex.extend(["其他",PriceIndex[-1]])
    print(PriceNationIndex)
    PriceNationSum = list(PriceSum[0:5])
    PriceNationSum.extend([np.sum(PriceSum[5:-1]),PriceSum[-1]])
    print(PriceNationSum)
    plt.figure(figsize=(8,8))
    plt.pie(PriceNationSum,labels=PriceNationIndex,autopct="%1.1f%%",explode=(0,0,0,0,0,0,0.5),startangle=185)

import gazpacho
import nums_from_string as nfs
import parse
import time
import random
import csv

def GetAllIno(doubanURL_front):
    BookNames = []
    Prices = []
    Years = []
    Presses = []
    Nations = []
    Authors = []
    # 构造10页的URL地址
    URLAddressList = [f"https://book.douban.com/top250?start={index*25}" for index in range(0,10)]
    print(URLAddressList)
    for doubanURL in URLAddressList:
        # 睡眠2-4秒，别太贪婪
        time.sleep(random.randint(2,4))

        doubanHTML = gazpacho.get(doubanURL)
        doubanTree = gazpacho.Soup(doubanHTML)
        # 查找图书名信息
        AllBookNameInDiv = doubanTree.find("div", attrs={"class":"pl2"})
        BookNames.extend([eachBook.find("a").strip() for eachBook in AllBookNameInDiv])

        AllBookInfoInP = doubanTree.find("p", attrs={"class":"pl"})
        # 获取价格，出版年
        Prices.extend([nfs.get_nums(eachInfo.text)[-1] for eachInfo in AllBookInfoInP])
        Years.extend([nfs.get_nums(eachInfo.text)[0] for eachInfo in AllBookInfoInP])
        # 取出版社
        Presses.extend([parse.search("{press}/{:d}",eachP.text)["press"].split("/")[-1].strip() for eachP in AllBookInfoInP])
        # 取国家和作者
        replaceTable = str.maketrans({"（":"(", "[":"(", "【":"(", "）":")", "]":")", "】":")"})
        for eachP in AllBookInfoInP:
            extractedInfo = eachP.text.split("/")[0].translate(replaceTable).strip()
            if extractedInfo.startswith("("):
                parsedText = parse.parse("({nation}){author}", extractedInfo)
                Nations.append(parsedText["nation"].strip())
                Authors.append(parsedText["author"].strip())
            else:
                Nations.append("中国")
                Authors.append(extractedInfo)
    print(BookNames,Prices,Years,Presses,Nations,Authors)
    return BookNames,Prices,Years,Presses,Nations,Authors


def GetDoubanHtmlTree(doubanURL):
    doubanHTML = gazpacho.get(doubanURL)
    doubanTree = gazpacho.Soup(doubanHTML)
    return doubanTree


def GetBookName(doubanTree=GetDoubanHtmlTree("https://book.douban.com/top250?start=0")): 
    AllBookNameInDiv = doubanTree.find("div", attrs={"class":"pl2"})

    BookNames=[]

    for i in range(0,25):
        booknow=AllBookNameInDiv[i].find("a").strip()
        BookNames.append(booknow)

    with open("Top250-1.csv",mode="wt",encoding="utf-8",newline="") as fp:
        creator = csv.writer(fp)
        creator.writerow(["图书名",])
        for name in BookNames:
            creator.writerow([name,])
    return BookNames
    
    
def GetBookPriceandYears(doubanTree=GetDoubanHtmlTree("https://book.douban.com/top250?start=0")):
    BookNames=GetBookName(doubanTree)
    AllBookInfoInP = doubanTree.find("p", attrs={"class":"pl"})
    Prices = [nfs.get_nums(eachInfo.text)[-1]    for eachInfo in AllBookInfoInP]
    Years = [nfs.get_nums(eachInfo.text)[0]    for eachInfo in AllBookInfoInP]
    #print(Prices, Years)
    
    with open("Top250-2.csv",mode="wt",encoding="utf-8",newline="") as fp:
        Creator = csv.writer(fp)
        Creator.writerow(["图书名","价格","出版年"])
        for name,price,year in zip(BookNames,Prices,Years):
            Creator.writerow([name,price,year])
    
    import parse
    pressTemplate="{press}/{:d}"
    Presses = []
    for eachP in AllBookInfoInP:
        Presses.append(parse.search(pressTemplate, eachP.text )["press"].split("/")[-1].strip())

    #print(BookNames,Years,Prices,Presses)
    replaceDict = {
    "（":"(",
    "[":"(",
    "【":"(",
    "）":")",
    "]":")",
    "】":")"
    }
    replaceTable = str.maketrans(replaceDict)
    NationAndAuthorTemplate = "({nation}){author}"
    Nations = []
    Authors = []
    for eachP in AllBookInfoInP:
        extractedInfo = eachP.text.split("/")[0].translate(replaceTable).strip()
        if extractedInfo.startswith("("):
            parsedText = parse.parse(NationAndAuthorTemplate, extractedInfo)
            Nations.append(parsedText["nation"].strip())
            Authors.append(parsedText["author"].strip())
        else:
            Nations.append("中国")
            Authors.append(extractedInfo)
    print(Nations,Authors)
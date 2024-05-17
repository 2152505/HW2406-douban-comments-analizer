import csv
import parse
import gazpacho
import nums_from_string as nfs

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
    print("文件保存完毕！")
    return BookNames
    
    
def GetBookPriceandYears(doubanTree=GetDoubanHtmlTree("https://book.douban.com/top250?start=0")):
    BookNames=GetBookName(doubanTree)
    AllBookInfoInP = doubanTree.find("p", attrs={"class":"pl"})
    Prices = [nfs.get_nums(eachInfo.text)[-1]    for eachInfo in AllBookInfoInP]
    Years = [nfs.get_nums(eachInfo.text)[0]    for eachInfo in AllBookInfoInP]
    print(Prices, Years)
    
    with open("Top250-2.csv",mode="wt",encoding="utf-8",newline="") as fp:
        Creator = csv.writer(fp)
        Creator.writerow(["图书名","价格","出版年"])
        for name,price,year in zip(BookNames,Prices,Years):
            Creator.writerow([name,price,year])
    print("文件保存完毕！")
    
    import parse
    pressTemplate="{press}/{:d}"
    Presses = []
    for eachP in AllBookInfoInP:
        Presses.append(parse.search(pressTemplate, eachP.text )["press"].split("/")[-1].strip())

    print(BookNames,Years,Prices,Presses)
import getCSV
doubanURL="https://book.douban.com/top250?start=0"
doubanTree=getCSV.GetDoubanHtmlTree(doubanURL)
getCSV.GetBookName(doubanTree)
getCSV.GetBookPriceandYears(doubanTree)

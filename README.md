# douban-comments-analizer
douban comments analizer : A python tool that can help you catch douban comments and analyze it.

#### 发现一个有趣的点，在vscode中，默认的主路径是在最外层文件夹默认保存位置也是最外层文件夹

### CSV命名规则
"Top250-1.csv"：在getCSV.GetBookName()中保存，包含的内容是图书的名字。  

"Top250-2.csv"：在getCSV.GetBookPriceandYears()中保存，包含的内容是图书的名字，出版年份和价格。

"Top250-3.csv"：在getCSV.GetAllInfo()中保存，包含的内容是爬取的所有内容的信息。

"Top250-4.csv"：等同于"Top250-3.csv"，是所有信息的综合，用于图形化分析使用。

### Labs的使用

关于Labs，其本质上是每一节课的代码集总，每一个都已单独进行运行并测试无报错功能正常。

0509是把爬取程的汇总。

0516使用了条形图和饼状图进行分析。

0530中使用了箱式图和图云功能进行分析
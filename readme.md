# 用法

## 1. pcc：
pcc接收四个参数：
-f (prefix)后接文件名前缀，如对于n-55-4-6-0.pdb  -  n-55-4-6-25.pdb这些文件，写'-f n-55-4-6-'即可。
-s (size)石墨烯尺寸，接收3、5或10
-o (output)输出最后一帧详情的文件名，如Output，
    【※不要写后缀名，后缀名自动txt】
-t (solvent)所计算中心原子在pdb文件中的名字，如N5、CO等。

pcc输出两个文件，两个都是文本文件格式，其中一个是*.csv，可直接用excel打开
记录最后一帧的文件名 和 记录间隙中分子数随时间浮动情况的文件名 由-o参数控制如参数-o Output，则得到两文件：Output.txt和Output.csv
如
`$ pcc -f n-55-4-6- -s 5 -o Output -t N5`




## 2. psub:
有多种模式，其中-adl应用场景较常见
有时需要把gro文件的第一列的某些残基序号数字加大，比如 1DDR-28DDT 要改成 2DDR-29DDT，如果文件发到windows上用notepad++改，操作实在太繁琐，而且notepad++使用内存有限，文本量大时容易出错。
`$ -adl FileName.gro 10000 20000 10 OutName.gro`
表示把FileName.gro文件从第10000行到20000行的前面数字如 1TOL 改成 11TOL （数字加上10）并将文件输出到OutName


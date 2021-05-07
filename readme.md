# 用法说明

## 1. pcc：

### 1.1 计算功能

pcc计算功能接收四个参数：

-f (prefix)后接文件名前缀，如对于n-55-4-6-0.pdb  -  n-55-4-6-25.pdb这些文件，写'-f n-55-4-6-'即可。

-s (size)石墨烯尺寸，接收3、5或10

-o (output)输出的文件名，如Output，
    【※不要写后缀名，后缀名自动txt】

-t (solvent)所计算中心原子在pdb文件中的名字，如N5、CO等。

pcc输出两个文件，两个都是文本文件格式，其中一个是*.csv，可直接用excel打开
记录最后一帧的文件名 和 记录间隙中分子数随时间浮动情况的文件名 由-o参数控制如参数-o Output，则得到两文件：Output.txt和Output.csv

如
`$ pcc -f n-55-4-6- -s 5 -o Output -t N5`



Changed in 2018/06/27:

### 1.2 预处理功能

pcc可以去除第五列的字母，称“预处理”。预处理必须使用两个参数 -pretreatment   -f，-print参数可选， 不得使用 -s  -o  -t参数。

-pretreatment 后不接任何字符，而-f参数则和计算功能中的含义相同，传入文件名前缀。

当选用 -print 参数时，将从屏幕上输出预处理过程中被改动的行。

如命令

`$ pcc -pretreatment -f n-55-4-6-`

将使工作目录下所有文件名以`n-55-4-6-`开头的.pdb文件中第五列多余的字母去掉。



### 1.3完整使用

完整使用应该先使用命令

`$ pcc -pretreatment -f n-55-4-6-`

随后

`$ pcc -f n-55-4-6- -s 5 -o Output -t N5`



added in 2021/05/07:

### 1.4注意
工作目录/终端所在目录须与`*.pdb`文件所在目录相同。

因为 `-f` 后跟的参数必须是 `n-a-55-4-10-` 样式，不能是 `./n-a-55-4-10-` 样式，更不能是 `xx/xx/n-a-55-4-10-` 样式。

如果 `-f` 后跟的参数有空格，可用引号包起来：`-f "n a 55 4 10 "` ，但最好不在文件(夹)名引入空格。

end added in 2021/05/07.


## 2. psub:
有多种模式，其中-adl应用场景较常见

有时需要把gro文件的第一列的某些残基序号数字加大，比如 1DDR-28DDT 要改成 2DDR-29DDT，如果文件发到windows上用notepad++改，操作实在太繁琐，而且notepad++使用内存有限，文本量大时容易出错。

`$ psub -adl FileName.gro 10000 20000 10 OutName.gro`

表示把FileName.gro文件从第10000行到20000行的前面数字如 1TOL 改成 11TOL （数字加上10）并将文件输出到OutName



## 3. Q&A

1. 我如何将pcc的目录添加到Linux环境变量？

   修改home/.profile文件，在文件末尾添加如下内容：

   ```bash
   export PATH="$PATH:~/simulation/wu-graphene/myapp/for_simulation"
   ```

   保存退出，此后你可能需要重新登录用户才会使其生效。

   ​

2. 报错权限不够？

   ```bash
   $ pcc
   bash: /home/.../.../for_simulation/pcc: 权限不够
   ```

   要想将pcc作为一个命令，需要手动将pcc赋予可执行权限

   在`/home/.../.../for_simulation/`目录下运行如下指令

   ```bash
   chmod +x pcc
   ```

   即可完成对pcc添加可执行权限，psub权限不够解决方式相似。
3. pcc 报错：
```
 Traceback (most recent call last):
  File "pcc", line 484, in <module>
    read_data(file_path)
  File "pcc", line 140, in read_data
    if int(sl[4]) == s:
ValueError: invalid literal for int() with base 10: 'X'
```

是因为文件里有多余的字母，需要先执行预处理，命令示例：`pcc -pretreatment -f n-a-55-4-10-`

### 更新记录

2021/05/07：

新增对7*x大小石墨烯的支持。
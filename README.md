# makegif
输入图片文件或文件夹来创建gif图片。支持python2和python3，需要先安装Pillow插件: `pip install Pillow`。

```
python makegif.py -o test.gif input1.png input2/
```



```
usage: makegif.py [-h] [-d DURATION] [-o OUTPUT] [-f FILTERS] [-s SIZE]
                  [-l LOOP]
                  inputs [inputs ...]

创建gif图片

positional arguments:
  inputs                输入文件路径，或文件夹。支持混合输入

optional arguments:
  -h, --help            show this help message and exit
  -d DURATION, --duration DURATION
                        时间间隔。默认200ms
  -o OUTPUT, --output OUTPUT
                        输出路径。如果未指定，则使用第一个图片所在的文件夹作为名称。如果文件夹为当前路径，则输出名称为out.git
  -f FILTERS, --filters FILTERS
                        用于在文件夹中搜索指定的后缀文件。默认: png,jpg,bmp
  -s SIZE, --size SIZE  输出图片大小。格式: 640x480; 或者640x，仅限定宽度为640，高度等比缩放;
                        或者x480，仅限定高度为480，宽度等比缩放
  -l LOOP, --loop LOOP  循环次数。默认0，表示无限循环
```

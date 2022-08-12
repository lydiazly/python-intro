# Python Introduction (Tips & Examples)

== Presentations for Solar Group, Nanjing University ==

SunPy 脚本和自定义模块见 [scripts-sunpy](https://github.com/lydiazly/scripts-sunpy)

[ Blog ] **NEW!**<br>
https://lydiazly.github.io

[ Update ]
> *2022-08-12*&emsp;更新部分链接.<br>
> *2018-07-19*&emsp;更新 python 进阶课件.<br>
> *2018-07-06*&emsp;Blog已建好, 网页也可以预览了.<br>
> *2018-07-01*&emsp;试着转了 pdf 版本<br>
> *2018-06-30*&emsp;修改了 html 的显示, 去掉了侧边栏, 现在打开速度比较快. (但正文的标题编号bug仍未解决因此暂时去掉了.


[ Tested ]

Ubuntu 16.04 LTS
Date|Python|Jupyter|Sunpy|NumPy|SciPy|Matplotlib|Astropy|Pandas
:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:
2018-07-08|3.6.5|4.4.0|0.9.0|1.14.5|1.1.0|2.2.2|3.0.3|0.23.0

---

## Download

* [安装与配置](https://lydiazly.github.io/installpy)

[[Jupyter Notebook](/notebooks/installpy.zip)]

* [Python 简易教程](https://lydiazly.github.io/main) & [进阶](https://lydiazly.github.io/advance)

[[Jupyter Notebook](/notebooks/python-intro.zip)]

---

## 文件说明

### `*.ipynb`

> [Tested]&ensp;python 3.5+

打开:

```sh
$ jupyter notebook <filename>.ipynb
```
注意 data/ 文件夹需要在同一目录, 否则需要手动修改文档中数据的路径.<br>
SunPy 示例的数据请手动下载 (见 [scripts-sunpy](https://github.com/lydiazly/scripts-sunpy))

### `*.html`
用浏览器打开时, 代码框(Input Cell)内的字体大小可以通过调节浏览器的 Fixed-width font(Monospace) 大小来改变:<br>
e.g.<br>
* **Chrome**: chrome://settings/fonts -> 调节 Minimum font size.<br>
* **Filefox**: about:preferences -> Fonts & Colors -> Advanced -> Monospace

### `examples/*.py`

> [Tested]&ensp;python 2.7.12 & python 3.5+

```sh
$ python <filename>.py
```

注意使用的 `python` 命令对应的版本.

---

### Jupyter 主题

分享两个 Jupyter 主题的配置文件:

* [jupyter_css/custom.css](/jupyter_css/custom.css)
&ensp;放映时使用的主题<br>
* [jupyter_css/custom.js](/jupyter_css/custom.js)
&ensp;其中定义了一个按 **`.`** 键定位到当前的 Cell 的功能

将这两个文件拷贝至配置文件目录, 例如&ensp;*~/.jupyter/custom* , 刷新浏览器页面即可显示新主题.

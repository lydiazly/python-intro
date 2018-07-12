# Python Introduction (Tips & Examples)

== Presentations for Solar Group, Nanjing University ==

(课件题图来自 www.digitalocean.com)

SunPy 脚本和自定义模块见 [scripts-sunpy](https://coding.net/u/lydiazly/p/scripts-sunpy)

[ Blog ] **NEW!**<br>
https://lydiazly.coding.me/python-notes

[ Update ]
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

* 安装与配置 (installpy.ipynb)<br>
[
<a href="https://lydiazly.coding.me/python-notes/notebooks/installpy.ipynb" download target="_blank">
Jupyter Notebook
</a>
|
[HTML](https://lydiazly.coding.me/python-notes/_pages/installpy.html)
|
[PDF](https://coding.net/u/lydiazly/p/python-intro/git/raw/master/installpy.pdf)
]

* Python 简易教程 (for Solar Group) (main.ipynb)<br>
[
<a href="https://lydiazly.coding.me/python-notes/notebooks/main.ipynb" download>
Jupyter Notebook
</a>
|
[HTML](https://lydiazly.coding.me/python-notes/_pages/main.html)
|
[PDF](https://coding.net/u/lydiazly/p/python-intro/git/raw/master/main.pdf)
]

* Python 进阶 (for Solar Group) (advance.ipynb)<br>
(即将上线)

内容已全部已移至 [blog](https://lydiazly.coding.me/python-notes)

为了之后的更新, 推荐 clone 这个仓库:

    $ git clone https://git.coding.net/lydiazly/python-intro.git

---

## 文件说明

### `*.ipynb`

> [Tested]&ensp;python 3.5+

打开:

```sh
$ jupyter notebook <filename>.ipynb
```
注意 data/ 文件夹需要在同一目录, 否则需要手动修改文档中数据的路径.<br>
SunPy 示例的数据请手动下载 (见 [scripts-sunpy](https://coding.net/u/lydiazly/p/scripts-sunpy))

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

* [jupyter/custom.css](https://coding.net/u/lydiazly/p/python-intro/git/raw/master/jupyter/custom.css)
&ensp;放映时使用的主题 (但课件的 html 版本是使用默认主题转存的)<br>
* [jupyter/custom.js](https://coding.net/u/lydiazly/p/python-intro/git/raw/master/jupyter/custom.js)
&ensp;其中定义了一个按 **`.`** 键定位到当前的 Cell 的功能

将这两个文件拷贝至配置文件目录, 例如&ensp;*~/.jupyter/custom* , 刷新浏览器页面即可显示新主题.

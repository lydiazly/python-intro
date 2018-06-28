# Python Introduction (Tips & Examples)

*Update: 2018-06-28*

Presentations for Solar Group, Nanjing University.

(课件题图来自 www.digitalocean.com)

`$ git clone https://git.coding.net/lydiazly/python-intro.git`

SunPy 脚本和自定义模块见 [scripts-sunpy](https://coding.net/u/lydiazly/p/scripts-sunpy)

---

## Download

* 安装与配置 (installpy.ipynb)<br>
右键下载 (
[HTML](https://coding.net/u/lydiazly/p/python-intro/git/raw/master/installpy.html)
|
[Jupyter Notebook](https://coding.net/u/lydiazly/p/python-intro/git/raw/master/installpy.ipynb)
)&ensp;
<a href="http://htmlpreview.github.io/?https://coding.net/u/lydiazly/p/python-intro/git/raw/master/installpy.html" target="_blank">
预览
</a>

* Python 简易教程 (for Solar Group) (main.ipynb)<br>
右键下载 (
[HTML](https://coding.net/u/lydiazly/p/python-intro/git/raw/master/main.html)
|
[Jupyter Notebook](https://coding.net/u/lydiazly/p/python-intro/git/raw/master/main.ipynb)
)

* Python 进阶 (for Solar Group) (advance.ipynb)<br>
(即将上线)

> 为了之后的更新, 推荐 clone 这个仓库

## 文件说明

### `*.ipynb`

* Tested:&ensp;python 3.5+

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

* Tested:&ensp;python 2.7.12 & python 3.5

```sh
$ python <filename>.py
```

### Jupyter 主题

分享两个 Jupyter 主题的配置文件:

* [jupyter/custom.css](https://coding.net/u/lydiazly/p/python-intro/git/raw/master/jupyter/custom.css)
&ensp;放映时使用的主题 (但这里的 html 版本是使用默认主题转存的)<br>
* [jupyter/custom.js](https://coding.net/u/lydiazly/p/python-intro/git/raw/master/jupyter/custom.js)
&ensp;其中定义了一个按 [.] 键定位到当前的 Cell 的功能

将这两个文件拷贝至配置文件目录, 例如&ensp;*~/.jupyter/custom* , 刷新浏览器页面即可显示新主题.

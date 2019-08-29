## 什么时候用python xxx.py什么时候用python3 xxx.py

如果你的电脑里面只安装了Python 2或者只安装了Python 3，总之只有一个Python，那么，无论你是哪个系统，你总是可以使用`python xxx.py`的形式通过对应的Python解释器运代码。

如果你的电脑是macOS或者Linux，那么只要你的电脑有Python 3，无论有没有Python 2，你始终都可以使用`python3 xxx.py`通过Python 3来运行代码。此时，如果有Python 2，那么执行`python xxx.py`时，是通过Python 2来运行代码。

如果你的电脑是Windows，先安装了一个版本的Python，然后又安装了另一个版本的Python，那么我建议你这样做：进入Python 3的安装文件夹，把里面的`python.exe`改名为`python3.exe`。这样一来，你总是可以通过执行命令`python3 xxx.py`用Python 3运行代码；执行命令`python xxx.py`用Python 2执行代码。

## 我的电脑既有Python 2又有Python 3，那我使用pip安装的第三方库安装到了哪里？

这个取决于当你执行`pip`的时候，哪个版本的Python里面的`pip`先被找到。系统是根据环境变量里面的路径，挨着去找的，先找到了一个，那么就立刻使用。不再找后面的。

如果你搞不清楚到底哪个版本的pip先被找到，那么请使用下面这个万能方法：

假设你已经设置，使得执行`python`的时候启动的是Python 2环境，执行`python3`的时候，启动的是Python 3环境，那么：

* 通过执行`python -m pip install xxx`把第三方库安装到Python 2的环境里面。
* 通过执行`python3 -m pip install xxx`把第三方库安装到Python 3的环境里面。

## 什么是命令行，什么是Python交互环境

在Windows里面你直接打开CMD、Powershell或者在macOS、Linux上打开终端，你看到的黑色窗口叫做命令行，这里执行的是命令。CMD的命令行一般是以文件路径加一个右箭头开头，例如：

```
C:\xxx\xxx>
```

macOS、Linux的命令行一般是以`$`符号开头。

当你在终端里面，输入`python3`并回车的时候，打开的是`Python交互环境`，在这个环境里面是以三个右箭头开头的：

```
>>>
```

Python交互环境里面执行的是Python代码，而不是shell命令。

你需要搞清楚，你是要执行shell命令、CMD命令还是执行Python代码。执行shell命令，就在终端里面，执行CMD命令，就在CMD里面。执行Python代码，就在Python交互环境里面。

下面这幅图，就是犯了这样的错误：

![](https://kingname-1257411235.cos.ap-chengdu.myqcloud.com/2019-08-27-23-02-39.png)

命令`python -m scrapy startproject baidu `应该在CMD里面执行，而不应该在Python交互环境里面执行。

## Python交互环境运行代码，与把代码写成xxx.py后运行效果完全一样吗？

并不是完全一样，这里举一个例子：

```python
>>> a = 1000
>>> b = 1000
>>> a is b
```

在Python交互环境里面，返回`False`，如下图所示：

![](https://kingname-1257411235.cos.ap-chengdu.myqcloud.com/2019-08-27-23-05-58.png)

但如果写成xxx.py并运行，返回的结果为`True`，如下图所示：

![](https://kingname-1257411235.cos.ap-chengdu.myqcloud.com/2019-08-27-23-07-16.png)

这里的原理涉及到Python解释器对代码的优化，就不是初学者需要了解的了，放下不讲。感兴趣的朋友可以关注我的微信公众号。

但绝大多数的代码，在交互环境和通过xxx.py运行，效果是一样的。

## 已经安装了第三方模块，在PyCharm里面依然提示没有安装？

这种情况多发于我们直接从PyCharm中创建项目时的情况。

我们打开PyCharm，选择`Create New Project`，填写项目路径创建项目，如下图所示

![](https://kingname-1257411235.cos.ap-chengdu.myqcloud.com/2019-05-01-21-47-02.png)

项目创建完成以后，我们创建一个main.py文件，内容如下：

```python
import requests

resp = requests.get('http://exercise.kingname.info/exercise_requests_get.html').text

print(resp)
```

如下图所示：

![](https://kingname-1257411235.cos.ap-chengdu.myqcloud.com/2019-05-01-21-49-49.png)

此时，`requests`会被画上波浪线。这是正常情况，因为此时我们并没有安装这个第三方库，所以PyCharm必定找不到requests。

好了，那么我们来安装requests:

![](https://kingname-1257411235.cos.ap-chengdu.myqcloud.com/2019-05-01-21-51-53.png)

现在回到PyCharm里面，你会发现，为什么requests下面还有红色波浪线？可以这个第三方库明明安装成功了啊！

此时，如果你在PyCharm里面运行这个main.py文件，会看到PyCharm报错，如下图所示。

![](https://kingname-1257411235.cos.ap-chengdu.myqcloud.com/2019-05-01-21-53-32.png)

但是，如果你在终端里面运行，却发现代码毫无问题，如下图所示：

![](https://kingname-1257411235.cos.ap-chengdu.myqcloud.com/2019-05-01-21-55-11.png)

那么，PyCharm又闹什么幺蛾子了吗？

实际上这是功能不是bug。当我们在新版的PyCharm里面创建工程的时候，PyCharm会自动为这个工程创建一个虚拟环境，如下图所示。

![](https://kingname-1257411235.cos.ap-chengdu.myqcloud.com/2019-05-01-22-08-59.png)

在PyCharm中，我们也可以看到PyCharm是使用虚拟环境的Python来运行main.py的，如下图所示：

![](https://kingname-1257411235.cos.ap-chengdu.myqcloud.com/2019-05-01-22-11-16.png)

这个虚拟环境和系统的Python环境是隔离开的。当我们直接在终端里面安装第三方库的时候，安装到的是系统的Python环境，而PyCharm自动创建的虚拟环境的Python里面并没有安装requests，所以会出现找不到的问题。

这个问题要解决实际上也非常简单。打开PyCharm最下面的`Terminal`选项卡，并在这里弹出的终端里面安装requests，如下图所示

![](https://kingname-1257411235.cos.ap-chengdu.myqcloud.com/2019-05-01-22-15-57.png)

安装完成以后，再使用PyCharm运行main.py，发现一切都正常了。如下图所示。

![](https://kingname-1257411235.cos.ap-chengdu.myqcloud.com/2019-05-01-22-16-38.png)

最后，希望你不要抱怨PyCharm自动为你创建虚拟环境这个事情。在Python开发中，本来就应该这样做，不同的项目使用不同的虚拟环境，使得所有依赖互相隔离，这才是Python项目管理的正确方式。

## 搞不清楚工作区

PyCharm在遇到模块找不到时，会使用红色波浪线提醒开发者。这本来是一个非常好的功能，但却由于另外一个问题，会给一些Python初学者造成困扰。

首先我们创建一个login.py文件，它的内容如下：

```python
def login():
    print('登录服务器')
```

再创建一个`main.py`，它的内容如下：

```python
from login import login

print('准备登录服务器')
login()
```

这两个文件的文件结构如下图所示：

![](https://kingname-1257411235.cos.ap-chengdu.myqcloud.com/2019-05-01-13-16-05.png)

此时，你在PyCharm中打开main.py，你就会发现红色的波浪线，如下图所示。

![](https://kingname-1257411235.cos.ap-chengdu.myqcloud.com/2019-05-01-13-17-17.png)

此时如果使用PyCharm来运行这个main.py文件：

![](https://kingname-1257411235.cos.ap-chengdu.myqcloud.com/2019-05-01-13-21-17.png)


你会发现PyCharm运行程序毫无问题：

![](https://kingname-1257411235.cos.ap-chengdu.myqcloud.com/2019-05-01-13-21-57.png)

所以PyCharm有问题？它胡乱报错吗？

实际上不是这样的。

Python有一个工作区的概念，在默认情况下，当你使用`python xxx.py`运行一个.py文件时，工作区就是你运行的这个.py文件所在的文件夹。由于login.py和main.py文件是放在同一个文件夹里面的，所以当你直接运行main.py时，Python能够正确知道`from login import login`是指从和main.py在一起的这个login.py文件中导入login函数。所以一切都是正常的。

当时当你使用PyCharm打开一个项目文件夹时，由于还没有运行这个项目中的某个文件，所以PyCharm会以当前打开的这个项目文件夹为工作区。

在这个例子中，PyCharm会以`代码练习`这个文件夹作为工作区。所以当我在main.py中写`from login import login`的时候，PyCharm会从`代码练习`这个文件夹里面去需找login.py文件。显然，由于login.py在chapter_1文件夹里面，不在`代码练习`这个文件夹里面，所以PyCharm找不到，于是就会画红色波浪线。

这种情况特别常见于初学者学习别人代码的情况。例如一个Python初学者，他会把所有的爬虫相关代码都放在名为`爬虫代码`的文件夹里面，然后他下载了我的一个知乎爬虫项目，这个项目的代码是在一个叫做`ZhihuSpider`文件夹里面的。此时，他把`ZhihuSpider`文件夹放在`爬虫代码`文件夹里面，再用PyCharm打开`爬虫代码`文件夹，那么他就会看到`ZhihuSpider`项目代码里面有大量的红色波浪线。这不是代码有问题，而是PyCharm自动识别的工作区不正确导致的。

要解决这个问题也非常简单。打开PyCharm的项目设置，定位到`Project Structure`，如下图所示。

![](https://kingname-1257411235.cos.ap-chengdu.myqcloud.com/2019-05-01-13-38-59.png)

点击红色箭头指向的x符号，删除当前的内容，并添加新的内容，如下图所示：

![](https://kingname-1257411235.cos.ap-chengdu.myqcloud.com/2019-05-01-13-40-24.png)

把真正的项目文件夹路径添加进去，如下图所示：

![](https://kingname-1257411235.cos.ap-chengdu.myqcloud.com/2019-05-01-13-41-12.png)

点击`OK`按钮，回到PyCharm，发现它已经可以正确找到`login.py`文件了。如下图所示，红色波浪线消失。

![](https://kingname-1257411235.cos.ap-chengdu.myqcloud.com/2019-05-01-13-42-10.png)

## 我有了 Anaconda，还能安装其他版本的 Python 吗

有一些 Python 初学者，在学习网上教程的时候是以 Anaconda 入门的。此时他们电脑里面第一个 Python 环境是 Anaconda 里面的 Python。

在这种情况下，还能直接从 Python 官网下载安装其他版本的 Python 吗？

我们知道 Python2 与 Python3 是可以共存的。那么 Python 3.5与 Python 3.6能共存吗？Python 3.6.1与 Python 3.6.2能共存吗？

一台电脑上面能安装多少个 Python？

我要告诉你的是，不仅仅原来有 Anaconda 以后还能安装官网的 Python，实际上你电脑里面想安装多少个 Python 都可以。甚至你想在电脑上面安装10个 Python3.7.1也可以。

你安装 Python，本质上就是在电脑上安装了一个文件夹，这个文件夹里面有一个`python.exe`和各种子文件夹。

所以，你完全可以把 Python 3.7.1安装到`C:\python371`，把 Python 3.7.2安装到`C:\python372`这两个文件夹下。

于是，当你使用`C:\python371\python xxx.py`的时候，就是用的 Python 3.7.1来运行这个文件，当你使用`C:\python372\python xxx.py`的时候，就是用的 Python 3.7.2来运行这个文件。

那么当我们在 CMD 里面直接输入`python xxx.py`的时候，它用的是哪个 Python 呢？实际上这根本就不关 Python 的事情。这是系统的环境变量决定的。

无论是哪个系统，当你执行`python xxx.py`的时候，它首先会检查`python`是不是系统命令，发现不是，于是会在当前文件夹下面找有没有一个可执行文件，名字叫做`python.exe（或者 python.bat）`，发现也没有，此时，他就会根据环境变量里面记录的文件夹，一个文件夹一个文件夹去寻找。

例如环境变量是：`c:\ windows\system32;c:\program files;c:\python371;c:\python372`。那么此时，CMD 会首先去`C:\Windows\System32`文件夹下面寻找`python.exe`，发现找不到，于是又去`c:\Program Files`文件夹去找，发现也找不到，然后检查`C:\python371`文件夹，找到了，于是就使用 Python 3.7.1来运行文件。

如果你想在 CMD 运行`python xxx.py`时，默认使用 Python 3.7.2来运行怎么办呢？非常简单，只需要把环境变量修改为：`c:\ windows\system32;c:\program files;c:\python372;c:\python371`即可。

所以，你可以在你的电脑上安装100个相同版本或者不同版本的 Python，你想用哪个，可以直接通过绝对路径来启动，或者修改环境变量，把你想用的那个版本的 Python 设置到最前面。

至于安装在 Python 里面的第三方库，也非常简单，大家打开 Python 的安装文件夹，可以发现里面有一个`site-packages`文件夹，当你使用某个版本的 Python 对应的 pip （此时你应该这样写：`c:\python371\python -m pip install xxx`） 安装了一个第三方库以后，这个第三方库就会被放在这个文件夹里面。当你 Python 运行的程序需要使用第三方库的时候，它就会到自己的`site-packages`文件夹里面去寻找。

所以，不同版本的 Python 由于拥有自己的 `site-packages`文件夹，所以他们各自安装的第三方库互不干扰。

你安装的某些第三方库，会生成一个可执行文件。例如当你安装了`Scrapy`以后，你会发现在CMD 里面可以执行 `scrapy` 命令。实际上，本质也是 pip 把一个 scrapy 可执行文件复制到了对应 Python 版本的文件夹里面的 scripts文件夹 （macOS 或 Linux 是 bin 文件夹）里面而已。当你执行`scrapy`命令的时候，CMD 会去环境变量里面对应的各个文件夹中寻找对应的`scrapy.exe`文件，找到了就运行。

所以，可能会出现这样的情况，你在 Python 3.7.2环境里面安装了 Scrapy，但是在 CMD 里面运行却提示找不到`scrapy`命令。这种情况下，可能是由于你的环境变量里面设置的是其他 Python 的路径，没有设置 Python 3.7.2的路径。

Python 的 virtualenv 本质上也是同样的原理。当你电脑里面原本只有一个 Python 的时候，你可以通过 virtualenv 创建另外一个环境，这个环境看起来就像是把系统环境的 Python `复制`了一份出来。所以当你使用虚拟环境的 Python 的时候，安装的第三方库都是安装在虚拟环境的`site-packages`文件夹里面的，就不会影响系统环境的 Python。

当然，virutalenv 创建虚拟环境的时候，并不是把所有文件都真正的复制了一份。而是创建了一个`软连接`。在虚拟环境中通过这个软连接运行的本质上还是系统环境的 Python，但是由于这个虚拟环境也有 site-apckages 文件夹，所以它会使用虚拟环境的 site-packages。这就解释了为什么当你创建一个虚拟环境以后，再把系统环境的 Python 删掉，你会发现虚拟环境的 Python 也不能运行了。

总之一句话，如果你想在一个电脑上安装多个 Python，这没有任何问题。唯一可能给你带来困扰的是不同 Python 都把自己的文件夹路径添加到了环境变量中，那么哪个 Python 先执行，哪个 Python 后执行，这是环境变量给你带来的困扰，而不是 Python 本身。

关于 Python 初学者常见的更多错误和解决方法，大家可以关注本公众号的更新，也可以在 Github 上看到合集：

## 未完待续


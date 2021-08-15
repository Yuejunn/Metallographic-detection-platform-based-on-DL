# Metallographic-detection-platform-based-on-DL

## 开发者规则

### 编码规范

- `.ui`文件编译成`Ui_{filename}.py`

- `.qrc`文件编译成`{filename}_rc.py`

- 引入第三方库别用`from ... import *`，用`import`或要用啥引啥，比如`from PyQt5 import QWidget`，除了引入自己写的一些存常量的文件比如`my_styles.py`可以直接`from my_styles import *`。

- `mainwidget`里面不同类别的成员函数放不同区域：

  ```python
  ###################################### 重写父类函数区 ######################################
  pass
  ###################################### 辅助函数 ######################################
  pass
  ```

- **函数要表明返回值类型**：

- 代码风格选**Pylance**（vscode设置`"python.languageServer": "Pylance",`）

  ```python
  def heihei(): -> None
      pass
  def hah(): -> bool
      return True
  ```

  

- 函数或类的注释写定义下面（可以不用下面第二个那么详细，**但一定要写注释**）：

  ```python
  def paintEvent(self, e):
      r"""绘制窗口背景阴影
      """
  def set_default_tensor_type(t):
      r"""Sets the default ``torch.Tensor`` type to floating point tensor type
      ``t``. This type will also be used as default floating point type for
      type inference in :func:`torch.tensor`.
  
      The default floating point tensor type is initially ``torch.FloatTensor``.
  
      Args:
          t (type or string): the floating point tensor type or its name
  
      Example::
  
          >>> torch.tensor([1.2, 3]).dtype    # initial default for floating point is torch.float32
          torch.float32
          >>> torch.set_default_tensor_type(torch.DoubleTensor)
          >>> torch.tensor([1.2, 3]).dtype    # a new floating point tensor
          torch.float64
  
      
      if isinstance(t, _string_classes):
          t = _import_dotted_name(t)
      _C._set_default_tensor_type(t)
  ```

- 文件和文件夹使用**小写单词**命名，多个单词之间用下划线连接：

```python
demo_module
demo_do_something.py
```

- 类名：（大驼峰原则）

每个单词的首字母大写，私有类以下划线开头，后面也是每个单词的首字母大写，多个单词拼接：

```python
class DemoClass():
	pass
class _PrivateClass():
	pass
```

- 函数名：

使用小写单词命名，多个单词之间用下划线连接，私有函数以下划线开头（继承父类来的比如`paintEvent`来的就没办法了）：

```python
def demo_function():
	pass
def _private_function():
	pass
```

- 变量名：

使用小写单词命名，多个单词之间用下划线连接：

```python
demo_variable = "Hello Python"
```

- 常量：
  使用大写单词命名，多个单词之间用下划线连接：

```python
DEMO_CONSTANT = 100
```

### 文件存放

- 最高层文件夹只放和图形界面相关文件。
- 其余存放具体功能实现文件夹，如`torch_codes`存放使用pytorch实现的训练模块`train`和推理模块`inference`。其对应保持的模型文件等也直接放里面。
- 图片放`imgs`里面，其他资源文件放`other_resouces`。

### Github上传规则

多人协作的工作模式通常是这样：

1. 首先，可以试图用`git push origin <branch-name>`推送自己的修改；
2. 如果推送失败，则因为远程分支比你的本地更新，需要先用`git pull`试图合并；
3. 如果合并有冲突，则解决冲突，并在本地提交；
4. 没有冲突或者解决掉冲突后，再用`git push origin <branch-name>`推送就能成功！

如果`git pull`提示`no tracking information`，则说明本地分支和远程分支的链接关系没有创建，用命令`git branch --set-upstream-to <branch-name> origin/<branch-name>`。

详见：https://www.liaoxuefeng.com/wiki/896043488029600/900375748016320

## 功能实现

> 打勾的表示已经实现。

### 数据读取及可视化

> 这个考虑做成vscode那种，能直接打开一个文件夹作为工作目录看文本文件和图片，也可以直接打开文件。

- [ ] 读入txt、csv等文本文件并展示数据（考虑到看标签文件）。
- [ ] 读入图片并展示。

## 推理

> 就是直接对选择的图片调用我们训练好的存放在`inference`的模型进行金相分析。

- [ ] 晶粒度检测。
- [ ] 夹杂物检测。

## 训练

- [ ] 允许用户自己选择模型（我们预设的HED模型等）并自定义数据集进行训练，可自由选择训练参数，学习率，训练策略等。
- [ ] 允许用户自己搭建模型进行训练，可以选择输入python代码或者用鼠标点击改变网络结构。

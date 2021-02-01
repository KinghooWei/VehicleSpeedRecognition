# VehicleSpeedRecognition
Vehicle speed recognition and crash prediction based on virtual coil method 基于虚拟线圈法的车速识别和撞线预测

---
# 主题列表：juejin, github, smartblue, cyanosis, channing-cyan, fancy, hydrogen, condensed-night-purple, greenwillow, v-green, vue-pro, healer-readable, mk-cute, jzman, geek-black, awesome-green, qklhk-chocolate
# 贡献主题：https://github.com/xitu/juejin-markdown-themes
theme: github
highlight:
---
看不到图片请移步[我的这篇博客](https://juejin.cn/post/6924222163868188679/)，转载注明出处

## GitHub

[https://github.com/KinghooWei/VehicleSpeedRecognition](https://github.com/KinghooWei/VehicleSpeedRecognition)

开门见山了，记得**star一下**呀

## 最终效果图
<table width="100%" border="0">
	<tr align="center">
		<td><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f65f409d38fc45f2a92343b153b914fb~tplv-k3u1fbpfcp-watermark.image" width="100%"  border=0 /></td>
		<td><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9b06fc41ec244599b54ec25694d6ca5~tplv-k3u1fbpfcp-watermark.image" width="100%"  border=0 /></td>
	</tr>
</table>

## 设计思路
项目的编程环境为python3.7.7，编译器使用pycharm2019.3.4 x64，视频序列30帧每秒。项目采用虚拟线圈法估算车速，取线圈内平均灰度值相对于没有车辆的线圈内平均灰度值的变化c作为对象特征，当c的绝对值大于某一阈值时，判断有汽车通过线圈。
## 基于虚拟线圈的车速检测算法
虚拟线圈法是利用虚拟感应线圈代替真实感应线圈，工作原理类似于地埋式线圈检测器。在图像上垂直于道路方向上定义2个检测线圈的位置，系统通过检测线圈的灰度变化来判断车辆经过，由车辆经过前后两个线圈的间隔帧数p、两个线圈在现实中的距离l和第二个线圈与停止线的距离s，可以估算出当前车辆的速度及撞线时间。该方法的优点是操作简单，耗时短，能够实时完成速度和撞线时间估计。算法的具体步骤如下：

1. 确定两个虚拟线圈的位置、大小和倾斜角度，确保首帧序列的虚拟线圈内没有车辆，在视频序列中把虚拟线圈标注出来；

2. 计算首帧序列在2个虚拟线圈中的平均灰度值，记为$a$、$b$；

3. 逐一计算视频帧在2个虚拟线圈中的平均灰度值，记为$m$、$n$，并与首帧的计算结果$a$、$b$进行比较。当$\left|m-a\right|$大于某一阈值时，判断第一个线圈有车辆通过，记录当前帧的序号$i$，如图3-1所示，当$\left|n-b\right|$大于某一阈值时，判断第二个线圈有车辆通过，记录当前帧的序号$j$；

4. 当车辆通过第二个虚拟线圈时，由$i$、$j$、实际现实中两虚拟线圈的间距、第二个虚拟线圈与停止线的间距和视频的帧率等信息，即可估算出车辆的车速和撞线时间。

## 总结

考虑到实际应用中，摄像头可以固定在道路中，稳定程度和角度都要好于我在楼顶手持录像，所以实际应用理论要好于实验。但也存在一些问题，比如对白色车辆不敏感，只是通过黑色后视窗进行识别，原因可能是特征选择为灰度图的平均灰度值差异，白色车辆跟道路的平均灰度值差异不够明显，改进的话可以使用SHV图像的颜色做判别，这也比较符合人的判断；比如实验视频时间短，只考虑白天，实际现实还要工作于夜晚，可以运用动态阈值进行改进。
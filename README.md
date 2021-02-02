# VehicleSpeedRecognition
Vehicle speed recognition and crash prediction based on virtual coil method 基于虚拟线圈法的车速识别和撞线预测

华南理工大学 模式识别实践

README只列了框架，详情移步[https://juejin.cn/post/6924222163868188679/](https://juejin.cn/post/6924222163868188679/)，转载注明出处

记得**star一下**呀

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

## 总结
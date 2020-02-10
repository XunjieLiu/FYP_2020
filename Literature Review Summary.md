# Summary

## 《In-situ real-time characterization of micro-filaments for electrohydrodynamic ink-jet printing using machine vision》

1. 传统ink-jet printing 面临这多重挑战，主要是在解决高精度打印方面，因为打印pattern的不同dimension可能要求微米甚至是纳米级别的精度。
2. 尽管e-jet打印有打印高精度底座的能力，但是其过程并没有实现完全自动化。在打印过程中，结果经常是不平衡和不精确的。
3. Multiple challenges such as inconsistency in the printed material, process modeling, and process control, have hindered e-jet printing to be accepted by a wider range of corporation in the AM industry.**(我们方法论的重要意义)** （我的评论：)为了达到理想的结果，通常需要人工监控及调整工作的参与，手动操作不仅是在打印准备材料时，更多的是在打印过程中。
4. 质量监控系统例子quality control systems：
   1. ac-pluse modulated e-jet printing solved the slow charge decay rate of the substrat problem to achieve high resolution continuous features.
   2. 过程监控系统，Process monitoring systems are well developed in the subtractive manufacturing

### 这篇文章是如何解决in-situ real-time monitoring问题的

1. Everton et al. [13] reported that the in-situ inspection approach can be utilized in the AM method. In the research, the infrared temperature sensor detection helps to monitor the fused filament fabrication failure in real-time and the required adjustment can be made to correct it [14]. 第一种是红外探测
2. 光学系统Optical system
   1. Notably, Nakabo et al. [17] developed 1 ms visual feedback system based on massively parallel processing as well as fast image processing algorithms.
   2. Barton et al. [18], through the adjustment of the e-jet printing system, used sensing and feedback system to get high resolution printed parts. Multiple challenges are faced in processing of images.

### 在处理图像时遇到的问题及解决办法

1. background noise in form of the printed material
and other sources such as dust particles（解决办法与我们类似，二值化加边缘处理）
2. 二值化或者是边缘处理是阈值取值问题，造成阈值难以确定的原因是各种外界因素的影响比如光照强度，摆放位置

### 前人解决这些问题的参照

1. Yi et al. [19] optimized the procedure to decide the light source position and get a good measure performance.
2. Tsugawa et al. [20] found the configurations, driving control systems, and the machine vision systems contribute to the whole structure of closed-loop intelligent system.

### 使用的监控标准

The material flow, in form of the filament, can indicate the defects and material
property in the printing parts. 简而言之，喷射出的丝状物

### 关于Machine Vision

原因：Even if one can predict the manufacturing process, there are still system and accidental errors. The machine vision system can contribute to spot the anomaly during printing process, upgrade the traditional manual operation to automatic operation, and enable the measurements to be flexible and accurate [22].

我的评论：保证了过程的可控以及资源不被浪费是应用机器视觉的主要原因，这样才可以大规模工业化。

机器视觉的缺陷：

1. Harsh environment, such as the external illumination
2. 我们的经验：太贵了
3. 只能监控2D图像

## 《3D electrohydrodynamic printing of highly aligned dual-core graphene composite matrices》

EHD的主要用途之一，无太大参考价值

往心脏里放一个类似于人工支架一样的东西,而制造这个玩意儿是一个重要的步骤
Recent advances in tissue engineering
include the development of artificial nerve grafts exhibiting similar
physiological properties to peripheral nerves [3].
Another factor often limiting the development of artificial nerve
grafts is the engineering or fabrication method.
**The grafts should mimic the native extracellular matrix (ECM), both structurally and mechanically,**

## 《Electrohydrodynamic (EHD) Printing of Microparticle Streams for Additive Manufacturing(2)》

详细阐述了EHD的过程，相当于一本手册，同时这个手册的主要关注点在于EHD printing of liquids containing microparticles

### EHD与传统jetting比较

1. 传统：Thermal and piezoelectric driven inkjet printing, since it is capable of printing features with size approximately 100nm at 10 kHz frequency.
2. EHD的优势
   1. Inner diameters is much smaller, because the size of the capillaries need to be large enough to maintain high pressure to overcome surface tension
   2. droplet/jets的size可以小一到两个数量级,相比于传统方法,因为ejection是at the apex of the Taylor cone.
   3. 电场线的分布保证了jetting的稳定性,减少了其他因素的影响
   (Onses, M. Serdar, et al. "Mechanisms, Capabilities, and Applications of High-Resolution Electrohydrodynamic Jet Printing." small 11.34 (2015): 4237-4266.)

## 《In-situ monitoring of electrohydrodynamic inkjet printing via scalar diffraction for printed droplets》

### 为什么要监控系统

1. In order to improve reliability and quality control of e-jet printing process
2. 同样的,为了探索不同参数对于打印效果的影响,很多研究员做了相当多的研究, however, it was difficult to monitor the result of these altered printing parameters, so many researchers focused on the image processing process to instrut the printing process.

### 前人工作

1. Gardner [15] reported the operation of optical coherence tomography in a selective laser sintering system to monitor the surface feature of the printed part. 激光
2. Similar research has been done by Grasso [16], a method was proposed for detection and recognition of spatial defects during the selective laser melting process, but challenges remain under different frame rates at the same experimental setup. 同样是激光，在融解过程
3. During the ink-jet printing process of Liquid Metal Inkjet Printing (LMIP), Wang [17] solved the uncertain factors by using vision-based closed-loop control system which achieved stable jetting behavior; however, the droplet sizes were limited to a few hundred microns. 监控的Size不够小
4. Liu [20] developed an image-based closed-loop system to diagnosis the fused filament fabrication system with captured images and provided the automatic adjustment of the parameters to detect the defects. 很像我们的系统，但是监控的是fused filament fabrication system

**关键点**：常见的监控系统都是，把底座取下来去使用光学设备观察，造成的结果是无法实时监控打印过程，所以需要一个新的办法去实时监测。Currently, measurements of printed results are usually performed offline via an optical microscope or other similar metrology methods, which results in the removal of the substrate from the printing platform.
Once the substrate has been removed, additional printing is impossible as realignment is difficult and most time is not feasible.

### 方法论

1. 传统办法是放置一个camera去观察nozzle和substrate之间的区域，cost around 4000刀，另外这个观察方法并不是观测的打印结果。 However, this in-situ setup could not observe the pattern being printed.
2. 如果把摄像头装在垂直角度，Aligning additional zoom lens system on the z stage increased extra load and reduced control resolution of the z-axis. This means that the operator could only predict what the printed pattern would look like based on the printing parameters established beforehand using a traditional setup in.
3. 意思应该是，如果装在竖直角度，你是无法看到当前打印的scaffold的，你只能看到部分，并用这部分去预测整体，此处存疑，可能是因为作者觉得距离变大了，看不清了，没办法判断了，只能靠猜。
4. 解决办法：从底下安装激光，穿过Substrate，得到图片投影：Scalar diffraction vision system

## 《In-situ droplet inspection and closed-loop control system using machine learning for liquid metal jet printing》

主题：LMJP 是通过熔化金属液滴来进行打印的过程，作者提出的监控方案与传统的EHD监控方案类似，平行substrate放置摄像头观察液滴

我的评论：但是这种系统不值得EHD去借鉴，原因是由于LMJP是颗粒较大的金属液滴滴落，液滴的形态基本可以反映出打印的状态，但是EHD的打印情况往往跟泰勒锥的情况不相符。

## 《Image analysis-based closed loop quality control for additive manufacturing with fused filament fabrication》

我的评论：两边加装摄像头拍摄，并且是offline的，机器自动调控，这个同样不适用EHD，因为EHD一旦判断失误，就必须要换下，没有再继续的必要了

## Influence of electrohydrodynamic jetting parameters on the morphology of PCL scaffolds

主要阐述了各个参数的变化对于实验结果的影响，侧面验证了jetting过程是极其不稳定的，需要实时监控系统

## Electrohydrodynamic printing process monitoring by microscopic image identification

侧边拍照

1. 图像处理所用技术
   1. 二值化
   2. 锐化
   3. 最大连接区域
   4. 边缘识别
   5. 直线识别
   6. 图片腐蚀及膨胀 Erosion and Dilation
2. 提取的泰勒锥特征
   1. 质心
   2. Jet diameter
3. 使用了最简单的CNN网络
4. 泰勒锥形状分类

评价：基本没有参考价值，文献综述可以提到

## Zein Increases the Cytoaffinity and Biodegradability of Scaffolds 3DPrinted with Zein and Poly(ε-caprolactone) Composite Ink

大量提及了打印过程中层层相叠的相关数据以及图片，可以作为论据参考

1. 单层与24层图片对比
2. 层层叠加的物理过程描述
3. Pore sizes等相关数据列出

## 总结

由文献综述可得知如下信息：

1. EHD主要过程
2. EHD主要用途
3. EHD相对于传统方法优势
4. EHD的缺陷
5. 实时监控系统的必要性
6. 机器视觉在这个过程中能起到什么作用
7. 前人在实时监控系统上面的努力
8. 不同的监控方法以及是否适用于我们的项目
9. 孙老师团队的论文提及了传统的图像处理技术的作用，但似乎没什么新意
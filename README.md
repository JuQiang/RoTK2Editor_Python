# 三国志2存档文件修改器

## 背景

这个游戏是光荣KOEI在90年发布的，我们上大学时，机房里面的286机器上，能玩的游戏，就有它。这款游戏给我们带来了无穷的快乐，我的毕业设计，就是用汇编语言，写了一个TSR的修改器，可以在游戏中，热键呼出修改器，实时的对内存数据进行修改，当时还获得了毕业设计的第一名。

前段时间，无意中看到了dosbox的广告，又想起了这款游戏。很多数据结构，都忘记了，但是基本思路还有，玩了两次后，还是觉着修改好玩。本来想用swift在我的黑苹果上写，但是我太无能，swift UI劝退了我好几次。最终，还是用wxpython框架，用python来写。

## 参考资料

陆续找到了一些资料，有国内的轩辕路谈的，韩国人的，有一个日本人的，有一个老美的专门论坛的。数据结构基本都搞清楚了，尤其是武将头像部分，耗费了我不少时间。

[三国志系列图像格式浅析](http://xycq.online/forum/redirect.php?tid=34607&goto=lastpost&highlight=)

[VAN大神的分析](https://github.com/myevan/rtk)

[一个日本哥们写的，war map那段挺有帮助](https://geolog.mydns.jp/www.geocities.jp/aiharatomoya/san2/san2.htm)

[三国志2の攻略情報、データまとめ](https://cheatcodes.web.fc2.com/sangoku/san2/)

[삼국지 3 hex 에디터 트레이드 장수 삽입기](https://m.blog.naver.com/mokomoji/130096328361)

[三國志3 大眾臉臉譜研究](https://www.pttweb.cc/bbs/Koei/M.1359746890.A.910)

[PS版三國志II PAR用解析情報（暫定版）](https://geolog.mydns.jp/www.geocities.jp/aiharatomoya/san2/san2par.htm)

[一个台湾哥们写的结构分析](https://reganlu007.github.io/san2/)

[The unofficial RoTK2 GameGenie/PAR codes topic!!](https://gamefaqs.gamespot.com/boards/956391-romance-of-the-three-kingdoms-ii/70015768)，老美这个论坛很热闹，在好多年前。虽然基本都是修改NFS的ROM的，但是有些内容还是有借鉴意义。

[我自己在gamespot上写的总结](https://gamefaqs.gamespot.com/boards/956391-romance-of-the-three-kingdoms-ii/80060815)

[github上能找到的唯一一个修改器，韩国哥们写的](https://github.com/brokenpc00/RoTK2_Editor_React)

## 主要功能
主界面长这个样子
![主界面](https://github.com/JuQiang/RoTK2Editor_Python/blob/master/Demo/%E4%B8%BB%E7%95%8C%E9%9D%A2.png)

1. 可以把某个诸侯的全部城市都设置为经济最优，包括但不限于：黄金=30000，粮食=3000000等；军事最优：所有人的智力战力号召都是100，训练100，士兵10000等。
2. 可以把某个城市的经济和军事设置为最优，同上。也可以单独优化某个武将。
3. 可以把某个城市集体投降到另一个诸侯手下。
4. 可以查看全国地图及城市地图。
![郡地图](https://github.com/JuQiang/RoTK2Editor_Python/blob/master/Demo/%E6%9F%A5%E7%9C%8B%E9%83%A1%E5%9C%B0%E5%9B%BE.png)
![全国地图](https://github.com/JuQiang/RoTK2Editor_Python/blob/master/Demo/%E4%B8%96%E7%95%8C%E5%9C%B0%E5%9B%BE.png)
5. 可以查看所有武将信息。
![](https://github.com/JuQiang/RoTK2Editor_Python/blob/master/Demo/%E9%BB%98%E8%AE%A4%E6%AD%A6%E5%B0%86%E4%BF%A1%E6%81%AF.png)
6. 可以查看联盟关系
![联盟关系](https://github.com/JuQiang/RoTK2Editor_Python/blob/master/Demo/%E8%81%94%E7%9B%9F%E5%85%B3%E7%B3%BB.png)


## 技术难点
1. 武将分为大众脸和专用脸。后者见DrawFace，前者见DrawGenericFace。8bit的颜色，用3个byte来表示，具体解析见代码。大众脸，是一些列的眼睛、鼻子、嘴组合起来的。
2. color pallete很重要，否则画出来不是那个味儿。
3. 头像尺寸是64 * 40，但是实际显示的时候，是40 * 64。

## 数据结构
见Documents目录下的文件

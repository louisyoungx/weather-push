# Weather-Push

QQ、群推送今日天气（Python + TinyServer + Mirai）


# 介绍

## 功能介绍

- 支持推送到QQ、群，数目无限制
- 不同QQ、群可推送不同地区天气
- 推送内容丰富（日期，地区，天气，最高气温，最低气温，当前气温，风向，风力，空气指数，pm2.5指数，运动指数，天气小提示，能见度等内容）

## 运行界面

1. 执行日志：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/11/10/bbc3f72840f5c7ba845edb9beae38af2.png" width="70%"/>

2. QQ推送：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/11/10/55ed82d679b0bfa6fa588763a87e0c14.png" width="70%"/>
   
3. 群推送：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/11/10/3225d04005669f4812ffc8c0d0b961c9.png" width="70%"/>

   注意：为了降低接口压力和避免不必要问题，两次推送强制间隔20s+。

## 语言库

- python 3.8
- requests 2.24.0（接口get请求）
- pyyaml 5.3.1（配置文件）
- json 2.0.9（数据格式化）

# 使用该项目

## 下载项目

1. 进入 [Weather-Push](https://github.com/xingjiahui/Weather-Push) 项目主页，按下图依次点击 `code` 、`Download ZIP`：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/d88653d8849d9841b92b51b98f4ecca4.png" width="70%"/>

## 配置文件

1. 打开配置文件：左侧文件树中找到 `userData.yml` 文件，双击打开：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/11/10/acd985156af55ce53ede998a70e2550d.png" width="70%"/>

   注意：填写完成后，按下快捷键：`ctrl+s` 保存修改

2. 推送到QQ：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/11/10/ec1c9d12e466ebe0f34bc8fab285fbc0.png" width="70%"/>

3. 推送到QQ群：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/11/09/46bf7e087ec046614b37e8a82ca30e0a.png" width="70%"/>

   注意：要添加多个QQ、群时，按序号依次添加即可，注意缩进。

## 测试运行

1. 完成以上步骤，点击下图中的 `保存并测试`：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/8ca0413e26e52921687ed50881e8646e.png" width="70%"/>

# 脚本维护

## 定时触发

1. 创建触发器：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/440eab62174e21c346c9f2097261ec0f.png" width="70%"/>

2. 运行结果：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/11/10/8ed89283594131b858a4c4fd205afa48.png" width="70%"/>


# 感谢

1. 服务支持：
   - ~~[高德地图](https://lbs.amap.com/api/webservice/guide/api/weatherinfo/#t1)：提供免费天气API~~
   - [腾讯云函数](https://cloud.tencent.com/product/scf)：触发、执行python项目
   - ~~[Qmsg酱](https://qmsg.zendee.cn/)：QQ消息推送API~~
   
   - ~~[一言](https://api.uixsj.cn/hitokoto/index.html)：一言API~~
   - [QQPusher](http://qqpusher.yanxianjun.com/doc/)：QQ、QQ群消息推送API
   - [实况天气](https://tianqiapi.com/index/doc?version=v61)：天气APi
2. 技术支持：
   - [原项目-xingjiahui](github项目地址：https://github.com/xingjiahui/Weather-Push)
   - [博客园-阿宅gogo](https://www.cnblogs.com/wbw-test/p/11580887.html)：python发送get请求
   - [CSDN-站在风口](https://blog.csdn.net/abby1559/article/details/79971957)：python字典初始化
   - [CSDN-占海](https://blog.csdn.net/chenzhanhai/article/details/106782325)：腾讯云函数添加依赖函数库
   - [CSDN-marselha](https://blog.csdn.net/marselha/article/details/91872832)：关于UnicodeDecodeError: 'gbk' codec can't decode byte 的解决方法
   - [CSDN-GhostRiderQin](https://blog.csdn.net/qq_40986486/article/details/103934408)：python加载YAML文件警告：YAMLLoadWarning: calling yaml.load() without... 的解决方法
   - [工具邦](http://cn.piliapp.com/emoji/list/weather/)：天气表情

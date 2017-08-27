# atx2
- **说明**
- channel:渠道的文件夹，主要存放渠道的截图和渠道的测试脚本
- game   : 游戏的文件夹，主要存放游戏的截图和游戏的测试脚本
- pubic   : 1.methods 一个公共类，渠道和游戏的脚本都继承这个类，很多方法都写在这个类
                2.get_names 一个公共类，主要是获取配置文件的渠道和游戏名称
- result   :测试报告和用例执行 fail 截图
- configure : 配置文件
- main    ：一个test case,在这里动态 导入相应的渠道和游戏测试脚本
- run_case : run test case 的。

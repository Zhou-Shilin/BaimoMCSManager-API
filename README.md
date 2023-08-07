# BaimoMCSManager API for `Python`
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-20BF20)](https://github.com/Zhou-Shilin/BaimoMCSManager-API/pulls)
![Support MSCM 9.9.0](https://img.shields.io/badge/Support-MCSM_9.9.0-blue)
![Apache License](https://img.shields.io/badge/License-Apache-red)  
这是一个适用于Python语言的第三方库，让你在Python中更方便地调用[MCSM-API
](https://docs.mcsmanager.com/#/zh-cn/apis/readme)管理你的服务器。

## ⚠️注意
这个项目仍在开发中，仅支持部分功能。  
  
当前进展：
 - [x] 面板通用设置 ( `common.py`)
 - [x] 应用实例管理 (`applications.py`)
 - [x] 多用户管理 (`auth.py`)
 - [x] 实例文件管理 (`files.py`)
 - [ ] 计划任务管理 (`plans.py`)
 - [ ] 守护进程管理 ( `remote_service.py`)

## 🔧安装
使用pip安装最新版本:
```bash
pip install baimomcsm_api
```
从旧版本更新到最新版本:
```bash
pip install baimomcsm_api --upgrade
```

## 📖使用方法
**特别注意：导入库时必须使用`from baimomcsm_api import *`！**

[GitBook文档](https://docs.baimoqilin.top/)
[帮助改进该文档](https://github.com/Zhou-Shilin/BaimoMCSManager-API-doc)
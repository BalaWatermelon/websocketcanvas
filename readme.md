# Websocket Canvas

## Requirement
---
### PIP

    安裝PIP，從官方網站的安裝程式中安裝，後面有個選項叫打勾會安裝PIP

### 套件及版本
* Python >3.5 (主要影響asyncio語法)
* asyncio
* websockets

### 安裝方法
```Bash
pip install asyncio
pip install websockets 
```

### 注意
伺服器使用的預設Port是9999

## 使用方法
---
1. 啟動伺服器
```
python socketClock.py
```
2. 開啟 *tutor.html*
3. 開啟 *student.html*
4. 在 *tutor* 上畫的畫會廣播至所有 *student*
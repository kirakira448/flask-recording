## 用法
1. 修改config中的预设
2. 启动app.py
3. 访问`host:5000`
    - 点击start开始录像
    - 点击stop停止录像


# Video Recorder Flask 应用
这是一个使用 Flask 和 OpenCV 实现的简单视频录制应用。用户可以通过界面开始和停止录制来捕捉视频，并且支持镜像效果以适应前置摄像头的图像。

## 功能特性
- 开始和停止视频录制
- 镜像处理前置摄像头捕捉的图像
- 自动生成文件夹和视频文件来保存录制的视频
## 环境要求
- Python 3.x
- Flask
- OpenCV
## 安装依赖
```bash
pip install -r requirements.txt
```
## 如何使用
1. 克隆或下载本仓库到本地环境。
2. 安装依赖。
3. 修改config配置
```text
OUTPUT_DIR = 文件输出目录
SEGMENT_DURATION = 分段时长（秒）
FRAME_SIZE = 视频宽高，tuple格式 (width,height)
FPS = 视频帧率，float格式
IS_FLIP = 是否镜像，镜像：True
```
4. 在终端中运行以下命令启动 Flask 应用：
```bash
python app.py
```
5. 在浏览器中访问 http://localhost:5000/home 来打开录制界面。
6. 点击 "Start" 开始录制，点击 "Stop" 结束录制。
## 文件结构
```plaintext
├── app.py                # Flask 应用主文件
├── index.html            # 网页模板文件
├── requirements.txt      # 依赖包列表
├── static/
│   └── styles.css        # CSS 样式文件（可选）
└── templates/
    └── index.html        # HTML 模板文件
```
## 重要说明
- 录制的视频文件默认保存在 output 文件夹下，每次开始录制会自动创建一个新的文件夹，并以当前时间命名。
- 确保摄像头设备正常工作和连接。
- 退出应用时，请确保停止录制并关闭浏览器页面。
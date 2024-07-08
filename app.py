from flask import Flask, jsonify,render_template,redirect,url_for
import threading
from video_recorder import VideoRecorder

app = Flask(__name__)
recorder = VideoRecorder(is_use_config=True)  # 分段时长（秒）
recording_thread = None


# 根路由，重定向到主页
@app.route('/')
def index():
    return redirect(url_for('home'))

# 主页路由，返回可视化界面
@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html')

# region /statrt and /stop
# @app.route('/start', methods=['GET'])
# def start():
#     global recording_thread
#     if not recorder.is_recording:
#         recording_thread = threading.Thread(target=recorder.start_recording)
#         recording_thread.start()
#         return jsonify({"status": "Recording started"})
#     else:
#         return jsonify({"status": "Already recording"})

# @app.route('/stop', methods=['GET'])
# def stop():
#     global recording_thread
#     if recorder.is_recording:
#         recorder.stop_recording()
#         recording_thread.join()
#         return jsonify({"status": "Recording stopped and saved"})
#     else:
#         return jsonify({"status": "Not recording"})
# endregion

# 开始或停止录制视频的路由
@app.route('/toggle', methods=['GET'])
def toggle_recording():
    global recording_thread
    if recorder.is_recording:
        recorder.stop_recording()
        recording_thread.join()
        return jsonify({"status": "Recording stopped", "is_recording": False})
    else:
        recording_thread = threading.Thread(target=recorder.start_recording)
        recording_thread.start()
        return jsonify({"status": "Recording started", "is_recording": True})

# 获取当前录制状态的路由
@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({"is_recording": recorder.is_recording})


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

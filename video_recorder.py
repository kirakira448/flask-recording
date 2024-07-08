import cv2
import numpy as np
import os
import time
from datetime import datetime
from config import OUTPUT_DIR, SEGMENT_DURATION,FPS,FRAME_SIZE,IS_FLIP

class VideoRecorder:
    def __init__(self,is_use_config=False):
        self.is_use_config=is_use_config
        self.output_dir = './output'
        self.segment_duration = 300
        self.camera = None
        self.is_recording = False
        self.video_writer = None
        self.current_segment = 1
        self.is_flip=False

        if self.is_use_config:
            self.init_config()

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def init_config(self):
        self.output_dir=OUTPUT_DIR
        self.segment_duration = SEGMENT_DURATION
        self.fps=FPS
        self.frame_size=FRAME_SIZE
        self.is_flip=IS_FLIP


    def start_recording(self):
        self.is_recording = True
        start_time = time.time()

        # Create a new folder named with the current time
        self.current_folder = datetime.now().strftime("%Y%m%d%H%M%S")
        full_path = os.path.join(self.output_dir, self.current_folder)
        if not os.path.exists(full_path):
            os.makedirs(full_path)

        self.camera = cv2.VideoCapture(0)
        # 如果不使用config文件，则需要获取摄像头的默认值
        if not self.is_use_config:
            self.fps = self.camera.get(cv2.CAP_PROP_FPS)
            width = int(self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)),   # 获取摄像头默认宽度
            height = int(self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 获取摄像头默认高度
            self.frame_size=(width,height)

        # 当self.is_recording未被修改时，一直录制
        while self.is_recording:
            current_time = time.time()
            elapsed_time = current_time - start_time

            if elapsed_time >= self.segment_duration:
                # Close current video writer
                if self.video_writer:
                    self.release_cv_obj(self.video_writer)

                self.current_segment += 1
                start_time = current_time

            # Create a new video writer if none exists or time to start a new segment
            if not self.video_writer or elapsed_time >= self.segment_duration:
                filename = os.path.join(full_path, f'segment_{self.current_segment}.avi')
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                self.video_writer = cv2.VideoWriter(filename, fourcc, self.fps, self.frame_size)

            ret, frame = self.camera.read()
            if ret:
                if self.is_flip:
                    frame=self.flip_frame(frame)
                # Write the frame to video only if output is valid
                if self.video_writer:
                    self.video_writer.write(frame)
            else:
                break

        if self.video_writer:
            self.release_cv_obj(self.video_writer)

        self.release_cv_obj(self.camera)
        cv2.destroyAllWindows()

    def stop_recording(self):
        self.is_recording = False

    def flip_frame(self,frame:np.ndarray)->np.ndarray:
        # new_img = np.zeros_like(frame)
        # h, w = frame.shape[0], frame.shape[1]
        # for row in range(h):
        #     for i in range(w):
        #         new_img[row, i] = frame[row, w - i - 1]
        # return new_img

        # return np.flip(frame, axis=1)
        return cv2.flip(frame,1)
    
    def release_cv_obj(self,cv_obj):
        cv_obj.release()
        # 释放后需要重新设为None，否则连续录像会出错
        cv_obj=None
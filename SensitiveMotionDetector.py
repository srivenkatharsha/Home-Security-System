"""
    Information:
    The `sensitivity_parameters` are used to adjust the sensitivity of motion detection.
    The `headless` parameter indicates whether there is a camera/monitor present or not.
    The `work` parameter specifies the task you want to perform after motion is detected.

"""

import cv2
import imutils
import FaceRecognizer
import TelegramSendPhoto

class SensitveMotionDetector:
    def __init__(self,work,camera,sensitivity_parameters = (10e5,10), headless = True):
        self.sensitivity_parameters = sensitivity_parameters
        self.work = work
        self.headless = headless
        self.movement_count = 0
        self.detect_count = 0
        self.camera = camera
    def job(self):
        self.work(self.camera)
    def start_detector(self):
        camera = self.camera
        _, previous_frame = camera.read()
        for i in range(20):
            pass
        previous_frame = imutils.resize(previous_frame,width=500)
        previous_frame = cv2.cvtColor(previous_frame,cv2.COLOR_BGR2GRAY)
        previous_frame = cv2.GaussianBlur(previous_frame,(5,5),0)
        while True:
            current_result, current_frame = camera.read()
            current_frame = imutils.resize(current_frame,width=500)
            current_frame = cv2.cvtColor(current_frame,cv2.COLOR_BGR2GRAY)
            current_frame = cv2.GaussianBlur(current_frame,(5,5),0)
            difference = cv2.absdiff(previous_frame,current_frame)
            threshold = cv2.threshold(difference,25,255,cv2.THRESH_BINARY)[1]
            previous_frame = current_frame
            if threshold.sum() > self.sensitivity_parameters[0]:
                self.movement_count += 1
            if not self.headless:
                cv2.imshow("Frame",current_frame)
                cv2.imshow("Threshold",threshold)
                key = cv2.waitKey(1)
                
                if key == ord('q'):
                    break
            if self.movement_count > self.sensitivity_parameters[1]:
                self.job()
                self.movement_count = 0
def job(camera):
        print(f"DETECTED {detector.detect_count}")
        detector.detect_count += 1
        if detector.detect_count >= 5:
            print("FACE RECOGNIZER MODE ON")
            fr = FaceRecognizer.FaceRecognizer(camera,cv2=cv2)
            unknown_image = f"./Unknown/Unknown.PNG"
            known_image = f"./Known/Known.PNG"
            fr.capture_face(unknown_image)
            result = fr.arcface_verify(known_image,unknown_image)
            print(result)
            if not result:
                try:
                    TelegramSendPhoto.procedure()
                except:
                    print("Network error!")
            detector.detect_count = 0

if __name__ == '__main__':
    camera = cv2.VideoCapture(0)
    detector = SensitveMotionDetector(job,camera = camera, headless=False)
    detector.start_detector()
    camera.release()
        
        
        
        

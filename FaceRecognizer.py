# resource: https://github.com/serengil/deepface

from deepface import DeepFace

class FaceRecognizer:
    def __init__(self,camera,cv2):
        self.camera = camera
        self.cv2 = cv2
    
    def arcface_verify(self,known_image : str,unknown_image : str) -> bool:
        assert len(unknown_image) > 0, f"Unknown image is not given!"
        obj = DeepFace.verify(
            img1_path = known_image,
            img2_path = unknown_image,
            model_name = "ArcFace",
            distance_metric = "euclidean_l2",
            enforce_detection = False
        )['verified']
        return obj
    
    def capture_face(self,path : str):
        for i in range(15):
            _, image = self.camera.read()
        self.cv2.imwrite(path,image)

if __name__ == '__main__':
    fr = FaceRecognizer()
    unknown_image = f"./Unknown/Unknown.PNG"
    known_image = f"./Known/Known.PNG"
    fr.capture_face(unknown_image)
    print(fr.arcface_verify(known_image,unknown_image))
    
    
    
    
        

from imageai.Detection import ObjectDetection
import os
from PIL import Image

execution_path = os.getcwd()

# create object of class ObjectDetection
detector = ObjectDetection()
# create an object that will help detect only ships
custom = detector.CustomObjects(boat=True)

# load models, set the path and find matches
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path, "yolo.h5"))
detector.loadModel()
detections = detector.detectCustomObjectsFromImage(input_image=os.path.join(execution_path, "new_file.jpg"), output_image_path=os.path.join(execution_path, "new_file_detections.jpg"), minimum_percentage_probability=20)

# open edited picture
edited_picture = Image.open(os.path.join(execution_path, "new_file_detections.jpg"))
edited_picture.show()



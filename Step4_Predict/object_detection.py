import cv2 
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
import config
import time
import numpy as np
import utils_car

model = YOLO(config.object_detect_path)
model_face = YOLO(config.face_detect_path)

def object_detect(img):
    results = model.predict(img)

    is_pred = False

    pred_boxs = []

    for r in results:
        annotator = Annotator(img) 
        boxes = r.boxes
        for box in boxes:
            is_pred = True
            b = box.xyxy[0]
            c = box.cls
            annotator.box_label(b, model.names[int(c)])

            pred_boxs.append((b.tolist(), model.names[int(c)]))
    

    if is_pred:
        box_pred = max(pred_boxs, key=lambda item: item[0][3])

        x1, y1, x2, y2 = box_pred[0]

        print(box_pred)

        area  =(x2 - x1) * (y2 - y1)
        img = annotator.result()

        black_mage = blank_image = np.zeros_like(img)
        cv2.rectangle(blank_image, (int(x1), int(y1)), (int(x2), int(y2)), (255, 255, 255), -1)
        cv2.imwrite(config.save_path + 'rectangle_object_img.jpg', blank_image)

        cv2.imwrite(config.save_path + 'object_pred_img.jpg', img)

        return box_pred[1], area * (0.02645833 ** 2) # label, area cm2
    else:
        return None


def face_detect(img):
    results = model_face.predict(img, conf=0.8)

    is_pred = False

    for r in results:
        annotator = Annotator(img) 
        boxes = r.boxes
        for box in boxes:
            is_pred = True
            b = box.xyxy[0]
            c = box.cls
            annotator.box_label(b, model.names[int(c)])
    

    if is_pred:

        x1, y1, x2, y2 = b.tolist()

        area  =(x2 - x1) * (y2 - y1)
        img = annotator.result()

        black_mage = blank_image = np.zeros_like(img)
        cv2.rectangle(blank_image, (int(x1), int(y1)), (int(x2), int(y2)), (255, 255, 255), -1)
        cv2.imwrite(config.save_path + 'rectangle_face_img.jpg', blank_image)

        cv2.imwrite(config.save_path + 'face_pred_img.jpg', img)

        angle = utils_car.get_face_decision(black_mage)

        return angle
    else:
        return None


if __name__ == "__main__":
    path = "C:/Users/GAGIBYTE/Downloads/img_ped.jpg"
    img = cv2.imread(path)
    
    angle = face_detect(img)
    print(angle)
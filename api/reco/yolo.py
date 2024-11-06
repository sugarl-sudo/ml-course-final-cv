from ultralytics import YOLO

class Recognizer:
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.names = model.names

    def recognize(self, image, conf=0.25):
        preds = self.model.predict(image, conf=conf)
        annot_lst = []
        for box in preds[0].boxes:
            preds = self.names[box.cls.cpu()]
        return results
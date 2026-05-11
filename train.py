from ultralytics import YOLO
def train():
    # Load a model
    model = YOLO("yolo8n.pt")

    # Train the model
    results = model.train(data="dataset/data.yaml", epochs=50, imgsz=640, batch = 16, workers=0, cache= False, resume= True)
if __name__ == '__main__':
    train()
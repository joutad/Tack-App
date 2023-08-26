import base64
from flask import Flask, request, jsonify
import numpy as np
import cv2

app = Flask(__name__)

def detect_objects(image):
    # image_path = 'dog.jpg'
    # image_path = '000067.jpg'
    # image_path = '000456.jpg'
    # image_path = '000542.jpg'
    # image_path = '001763.jpg'
    # image_path = '004545.jpg'
    # image_path = 'IMG_7983.jpg'
    # image_np = np.frombuffer(base64.b64decode(image_data), np.uint8)
    # image_cv2 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    
    # image_path = 'img.jpg'

    prototxt_path = 'models/MobileNetSSD_deploy.prototxt'
    model_path = 'models/MobileNetSSD_deploy.caffemodel'
    min_confidence = 0.2

    prediction_text = ''
    classes = [ "background", 'aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'key', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor'
    ]

    np.random.seed(543210)
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

    # image = cv2.imread(image_path)
    height, width = image.shape[0], image.shape[1]

    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007, (300, 300), 130)

    net.setInput(blob)

    detected_objects = net.forward()

    print(detected_objects[0][0][0])

    for i in range(detected_objects.shape[2]):
        confidence = detected_objects[0][0][i][2]

        if confidence > min_confidence:
            class_index = int(detected_objects[0, 0, i, 1])

            upper_left_x = int(detected_objects[0, 0, i, 3] * width)
            upper_left_y = int(detected_objects[0, 0, i, 4] * height)

            lower_right_x = int(detected_objects[0, 0, i, 5] * width)
            lower_right_y = int(detected_objects[0, 0, i, 6] * height)

            if len(prediction_text) <= 0:
                prediction_text = f"{classes[class_index]}: {confidence:.2f}%"
                
            cv2.rectangle(image, (upper_left_x, upper_left_y), (lower_right_x, lower_right_y), colors[class_index], 3)
            cv2.putText(image, prediction_text, (upper_left_x,
                        upper_left_y-15 if upper_left_y > 30 else upper_left_y + 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, colors[class_index], 2)
            # print(prediction_text)
    print(prediction_text)
    cv2.imshow("Detected Objects", image)
    cv2.destroyAllWindows()

    return prediction_text

@app.route('/members', methods=['POST'])
def members():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']
    image_np = np.fromstring(image.read(), np.uint8)
    image_cv2 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

    prediction_text = detect_objects(image_cv2)
    
    return jsonify({'prediction_text': prediction_text})

if __name__ == "__main__":
    app.run(debug=True)
    
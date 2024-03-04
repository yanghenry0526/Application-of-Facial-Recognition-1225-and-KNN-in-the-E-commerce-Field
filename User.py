import os
import cv2
import time
import csv

#####################################################################################

cap = cv2.VideoCapture(0)


def faceBox(net, frame, conf_threshold=0.7):
    frameDnn = frame.copy()
    frameHeight = frameDnn.shape[0]
    frameWidth = frameDnn.shape[1]
    blob = cv2.dnn.blobFromImage(frameDnn, 1.0, (227, 227), [104, 117, 123], True, False)

    net.setInput(blob)
    detections = net.forward()

    bboxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            bboxes.append([x1, y1, x2, y2])
            cv2.rectangle(frameDnn, (x1, y1), (x2, y2), (0, 255, 0), 1)
    return frameDnn, bboxes


# 載入model
faceProto = "model/opencv_face_detector.pbtxt"
faceModel = "model/opencv_face_detector_uint8.pb"

ageProto = "model/age_deploy.prototxt"
ageModel = "model/age_net.caffemodel"

genderProto = "model/gender_deploy.prototxt"
genderModel = "model/gender_net.caffemodel"

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList = ['Male', 'Female']


# Load network
ageNet = cv2.dnn.readNet(ageModel, ageProto)
genderNet = cv2.dnn.readNet(genderModel, genderProto)
faceNet = cv2.dnn.readNet(faceModel, faceProto)

# Open a video file or an image file or a camera stream
# video = cv2.VideoCapture('4.mp4')

# 設定捕獲持續時間（1秒）
capture_duration = 5  # 捕獲持續時間（秒）
start_time = time.time()

while True:
    ret, frame = cap.read()

    frameFace, bboxes = faceBox(faceNet, frame)

    for bbox in bboxes:
        face = frame[bbox[1]:bbox[3], bbox[0]:bbox[2]]

        blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)

        # print(gender)
        genderNet.setInput(blob)
        genderPreds = genderNet.forward()
        gender = genderList[genderPreds[0].argmax()]

        # print(age)
        ageNet.setInput(blob)
        agePreds = ageNet.forward()
        age = ageList[agePreds[0].argmax()]



        # cv2.putText(resultImg, f'{gender}, {age}, {emo}', (faceBox[0], faceBox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX,
        #             0.0009 * resultImg.shape[1], (255, 0, 255), int(0.004 * resultImg.shape[1]), cv2.LINE_AA)


        label = "{},{}".format(gender, age)  # 可以把這些資料輸出
        cv2.rectangle(frameFace, (bbox[0], bbox[1] - 30), (bbox[2], bbox[1]), (0, 255, 0), -1)
        cv2.putText(frameFace, label, (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2 , cv2.LINE_AA)

    cv2.imshow("Age-Gender", frameFace)

    # 檢查是否已達捕獲持續時間
    current_time = time.time()
    if current_time - start_time >= capture_duration:
        break

    # 按 'q' 鍵退出捕獲
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # k=cv2.waitKey(1)
    # if k==ord('q'):
    #     break
cap.release()
cv2.destroyAllWindows()

# 假設您有一個包含數據的變數 data
title = [
    "性別", "年齡"
]
data = [
    [gender, age]
]
# 設定要寫入的CSV文件名稱
csv_filename = "output.csv"
has_written_data = False
# 開啟CSV文件並寫入數據
if not os.path.isfile(csv_filename):
    # 如果文件不存在，則創建文件並將資料輸出
    with open(csv_filename, mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(title)
        writer.writerow(data)

    print(f"已創建 {csv_filename} 並將數據輸出到第一行。")
else:
    with open(csv_filename, mode='a', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        # 檢查是否已經寫入過該資料，如果還沒寫入過，則寫入

        writer.writerows(data)
    print(f"{csv_filename} 文件已存在，不再輸出相同的數據。")

print(f"{csv_filename} 文件已經成功生成。")
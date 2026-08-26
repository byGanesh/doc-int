from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/analyze-frame")
async def analyze_frame(file: UploadFile = File(...)):
    images_bytes = await file.read()

    image = cv2.imdecode(
        np.frombuffer(images_bytes, np.uint8),
        cv2.IMREAD_COLOR,
    )

    if image is None:
        return {"valid_image": False}

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    #cv2.imwrite("tmp/edges.jpg", edges)

    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE,
    )

    h, w = image.shape[:2]

    return {
        "valid_image": True,
        "width": w,
        "height": h,
        "channels": image.shape[2],
        "gray_shape": gray.shape,
        "contours_found": len(contours)
    }

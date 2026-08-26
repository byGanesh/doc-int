# DocInt 

Real-time document capture and intelligence using computer vision. DocInt turns a smartphone camera into a document scanner that can detect a document, guide the user into position, automatically capture a stable frame, correct perspective, assess image quality, and extract information using OCR.

### Overview  

Capturing a document with a phone sounds simple, but a reliable capture experience has several problems to solve:  

- Is a document actually visible?
- Is the entire document inside the frame?
- Is it large enough?
- Is the perspective acceptable?
- Is the image sharp enough?
- Is the lighting good enough?
- Is the device/document stable?
- When should the image be captured?
- Can the captured image be transformed into a clean document?
- Can useful information be extracted from it?

## User Flow

```text
Open App
   ↓
Camera Permission
   ↓
Live Camera Preview
   ↓
Document Detection
   ↓
Position / Size / Perspective Checks
   ↓
Image Quality Checks
   ↓
"Hold Steady"
   ↓
Automatic Capture
   ↓
Perspective Correction
   ↓
OCR
   ↓
Document & Field Extraction
   ↓
Results

```

## Architecture

```
┌─────────────────────────────┐
│          Flutter            │
│                             │
│  Camera                     │
│  Preview                    │
│  Overlay / Guidance         │
│  Capture State              │
│  Results UI                 │
└──────────────┬──────────────┘
               │
               │ HTTP
               ▼
┌─────────────────────────────┐
│          FastAPI            │
│                             │
│  Frame Analysis             │
│  Document Detection         │
│  Quality Assessment         │
│  Perspective Correction     │
│  OCR                        │
│  Document Parsing           │
└─────────────────────────────┘
```

## Tech Stack

**Frontend**  
- Flutter
- Dart
- Camera API
- HTTP

**Backend**  
- Python
- FastAPI
- OpenCV
- EasyOCR 

**Computer Vision**
- Edge Detection
- Contour detection
- Quadrilateral detection
- Perspective transformation
- Image sharpness analysis
- Brightness / lighting analysis
- Frame-to-frame stability analysis

## DISCLAIMER

This project is intended for educational and engineering purposes.  
So please do not use real identity documents or sensitive personal information during development and testing. Use synthetic or appropriately anonymized test documents.  

## Author 

[byGanesh.com](https://byganesh.com)   
MIT License

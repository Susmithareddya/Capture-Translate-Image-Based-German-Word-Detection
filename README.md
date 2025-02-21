# Capture & Translate-Image Based German Word Detection
This web-based application designed for mobile and desktop use, that provides an easy way to learn the German names of objects by simply capturing an image.
## 🔧 Setup and Installation  

### 1️⃣ **Clone the Repository**  
Open a terminal and run:  
```bash
git clone https://github.com/Susmithareddya/Capture-Translate-Image-Based-German-Word-Detection.git
cd Capture-Translate-Image-Based-German-Word-Detection
```

### 2️⃣ **Create a Virtual Environment (Recommended)**  
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate      # For Windows
```

### 3️⃣ **Install Dependencies**  
```bash
pip install -r requirements.txt
```

### 4️⃣ **Run the Flask App**  
```bash
python app.py
```

By default, the app runs on **http://127.0.0.1:5000/**.

---
## 📱 How to Use  

1. Open the app in your **browser**.  
2. Click **"Load Image"** and select an image.  # in Phone you will additionally get the option of taking a picture
3. The app will detect the object and translate it into **German**.  
4. The translated word will be displayed on the screen along with the uploaded image.
---
## 🛠 Technologies Used  
- **Flask** (Backend)  
- **ResNet-50** (Image Classification)  
- **Helsinki-NLP/Opus-MT** (English to German Translation)  
- **HTML, CSS, JavaScript** (Frontend)  

---

## 🎯 Future Improvements  
- Deploying on **Render** or **Railway** for online access.  
- Adding more **language support** (e.g., French, Spanish).  
- Improving **detection accuracy** with custom-trained models.  

---


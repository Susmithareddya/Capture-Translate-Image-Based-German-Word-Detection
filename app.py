from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from transformers import AutoImageProcessor, ResNetForImageClassification, MarianMTModel, MarianTokenizer
import torch
from PIL import Image
import io

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests for mobile access

# Load models
processor = AutoImageProcessor.from_pretrained("microsoft/resnet-50")
model = ResNetForImageClassification.from_pretrained("microsoft/resnet-50")
translation_model_name = "Helsinki-NLP/opus-mt-en-de"
tokenizer = MarianTokenizer.from_pretrained(translation_model_name)
translation_model = MarianMTModel.from_pretrained(translation_model_name)

@app.route('/')
def home():
    return render_template("index.html")  # HTML page for uploading images

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"})
    
    file = request.files['file']
    
    try:
        image = Image.open(io.BytesIO(file.read())).convert("RGB")  # Ensure proper format
    except Exception as e:
        return jsonify({"error": f"Invalid image format: {str(e)}"})

    try:
        # Process the image
        inputs = processor(image, return_tensors="pt")
        with torch.no_grad():
            logits = model(**inputs).logits

        predicted_label = logits.argmax(-1).item()
        text_to_translate = model.config.id2label[predicted_label]

        # Remove everything after the comma (if there is one)
        text_to_translate = text_to_translate.split(',')[0].strip()

        if not text_to_translate.lower().startswith("the"):
            text_to_translate = "The " + text_to_translate

        # Translate
        inputs = tokenizer(text_to_translate, return_tensors="pt", padding=True)
        translated = translation_model.generate(**inputs)
        translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

        return jsonify({"english": text_to_translate, "german": translated_text})

    except Exception as e:
        return jsonify({"error": f"Processing failed: {str(e)}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

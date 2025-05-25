import os
import uuid
from flask import Flask, request, render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename
from detector.image_detector import detect_image
from detector.video_detector import VideoDetector
from detector.audio_detector import detect_audio

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['SECRET_KEY'] = os.urandom(24)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB max upload

ALLOWED_EXTENSIONS = {
    'image': {'jpg', 'jpeg', 'png'},
    'video': {'mp4', 'avi'},
    'audio': {'mp3', 'wav'}
}

def allowed_file(filename, file_type):
    """Check if the file extension is allowed for the given file type."""
    if not filename or '.' not in filename:
        return False
    ext = filename.rsplit('.', 1)[1].lower()
    return ext in ALLOWED_EXTENSIONS.get(file_type, set())

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file uploaded')
            return redirect(request.url)
        file = request.files['file']
        file_type = request.form.get('file_type')

        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)

        if not file or not allowed_file(file.filename, file_type):
            flash('Invalid file format')
            return redirect(request.url)

        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4().hex}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)

        try:
            if file_type == 'image':
                result, confidence = detect_image(filepath)
            elif file_type == 'video':
                video_detector = VideoDetector()
                result, confidence = video_detector.detect_video(filepath)
            elif file_type == 'audio':
                result, confidence = detect_audio(filepath)
            else:
                flash('Invalid file type')
                return redirect(request.url)
        except Exception as e:
            flash(f'Error processing file: {str(e)}')
        finally:
            if os.path.exists(filepath):
                os.remove(filepath)  # Delete file only if it exists, after processing

        if 'result' in locals():
            return render_template('result.html', 
                                 file_type=file_type.capitalize(),
                                 filename=filename,
                                 result=result,
                                 confidence=f"{confidence:.2%}")
        return redirect(request.url)

    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port=5000)
import gdown
import os
try:
    from django.conf import settings
    BASE_DIR = settings.BASE_DIR
except Exception:
    # Fallback for standalone execution
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def download_model():
    model_path = os.path.join(BASE_DIR, 'ml_models', 'yield_model.pkl')
    # Google Drive direct download link
    url = 'https://drive.google.com/uc?id=1S05NBCCJ8EzPsa8aduoCuo14Q1wR7sfj'
    
    if not os.path.exists(model_path):
        print(f"Model not found at {model_path}. Starting download from Google Drive...")
        try:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(model_path), exist_ok=True)
            # Download using gdown
            gdown.download(url, model_path, quiet=False)
            print("Download completed successfully.")
        except Exception as e:
            print(f"Error downloading the model: {e}")
    else:
        print("Model already exists locally. Skipping download.")

if __name__ == "__main__":
    # For manual testing
    download_model()

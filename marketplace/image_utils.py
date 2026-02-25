"""
Image compression utilities for optimizing product and quality input images.
Automatically compresses images to reduce file size while maintaining acceptable quality.
"""

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import os


def compress_image(uploaded_file, max_width=1200, max_height=1200, quality=75):
    """
    Compress and resize an uploaded image to reduce file size.
    
    Args:
        uploaded_file: Django UploadedFile object
        max_width: Maximum width in pixels (default: 1200)
        max_height: Maximum height in pixels (default: 1200)
        quality: JPEG quality (1-100, default: 75)
    
    Returns:
        Compressed InMemoryUploadedFile object
    """
    
    try:
        # Open the image
        img = Image.open(uploaded_file)
        
        # Convert RGBA to RGB if necessary (for JPEG compatibility)
        if img.mode in ('RGBA', 'LA', 'P'):
            # Create a white background
            rgb_img = Image.new('RGB', img.size, (255, 255, 255))
            rgb_img.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
            img = rgb_img
        
        # Resize image to fit within max dimensions while maintaining aspect ratio
        img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
        
        # Save to BytesIO object
        output = BytesIO()
        
        # Determine file format and quality settings
        file_name = uploaded_file.name.lower()
        if file_name.endswith('.png'):
            # PNG compression
            img.save(output, format='PNG', optimize=True)
        elif file_name.endswith('.gif'):
            # GIF - convert to optimized format
            img.save(output, format='PNG', optimize=True)
        else:
            # Default to JPEG with quality setting
            img.save(output, format='JPEG', quality=quality, optimize=True)
        
        output.seek(0)
        
        # Create new uploaded file
        compressed_file = InMemoryUploadedFile(
            output,
            'ImageField',
            uploaded_file.name,
            'image/jpeg',
            output.getbuffer().nbytes,
            None
        )
        
        return compressed_file
        
    except Exception as e:
        # If compression fails, return original file
        print(f"Image compression error: {str(e)}")
        uploaded_file.seek(0)
        return uploaded_file


def compress_images_batch(image_list, max_width=1200, max_height=1200, quality=75):
    """
    Compress multiple images at once.
    
    Args:
        image_list: List of uploaded image files
        max_width: Maximum width in pixels
        max_height: Maximum height in pixels
        quality: JPEG quality level
    
    Returns:
        List of compressed image files
    """
    compressed_images = []
    for image in image_list:
        compressed = compress_image(image, max_width, max_height, quality)
        compressed_images.append(compressed)
    return compressed_images

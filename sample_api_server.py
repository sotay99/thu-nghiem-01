#!/usr/bin/env python3
"""
Sample AI Image Editor Backend API Server
Framework: FastAPI
Purpose: Provides endpoints for AI image processing features

To run:
    pip install fastapi uvicorn pillow python-multipart
    python sample_api_server.py

Then in image-editor.html, change:
    const API_BASE_URL = 'http://localhost:8000/api';
"""

from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import base64
from io import BytesIO
from PIL import Image, ImageFilter, ImageEnhance
import json
import time

# Initialize FastAPI app
app = FastAPI(title="AI Image Editor API", version="1.0.0")

# Enable CORS - Allow requests from your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== Data Models =====
class RemoveBackgroundRequest(BaseModel):
    image: str  # Base64 encoded image
    format: str = "png"

class InpaintRequest(BaseModel):
    image: str  # Base64 encoded image
    prompt: str  # Description of what to paint
    negative_prompt: str = ""
    strength: float = 0.75

class UpscaleRequest(BaseModel):
    image: str  # Base64 encoded image
    scale: int = 2  # 2x, 3x, or 4x

class RemoveObjectRequest(BaseModel):
    image: str  # Base64 encoded image
    mask: str = None  # Optional mask
    prompt: str = "remove object"

# ===== Utility Functions =====
def base64_to_image(base64_str):
    """Convert base64 string to PIL Image"""
    # Remove data URI prefix if present
    if ',' in base64_str:
        base64_str = base64_str.split(',')[1]
    
    image_data = base64.b64decode(base64_str)
    image = Image.open(BytesIO(image_data))
    return image

def image_to_base64(image, format="PNG"):
    """Convert PIL Image to base64 string"""
    buffered = BytesIO()
    image.save(buffered, format=format)
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

def add_cors_headers(response):
    """Add CORS headers to response"""
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

# ===== API Endpoints =====

@app.get("/")
async def root():
    """Health check"""
    return {"status": "ok", "message": "AI Image Editor API is running"}

@app.get("/api/health")
async def health_check():
    """API health endpoint"""
    return {
        "status": "healthy",
        "version": "1.0.0",
        "timestamp": time.time()
    }

# ===== Remove Background Endpoint =====
@app.post("/api/remove-background")
async def remove_background(request: RemoveBackgroundRequest):
    """
    Remove background from image
    
    Request:
        image: base64 encoded image
        format: output format (png/jpg)
    
    Response:
        result_image: base64 encoded result
        processing_time_ms: how long it took
    """
    try:
        start_time = time.time()
        
        # Convert base64 to image
        image = base64_to_image(request.image)
        
        # ===== PLACEHOLDER LOGIC =====
        # In production, replace with actual rembg or remove.bg API
        # For now, we'll create a mock by adding transparency
        
        # Simulate processing
        time.sleep(1)  # Mock delay
        
        # Convert to RGBA for transparency
        image = image.convert("RGBA")
        
        # In real implementation, you would:
        # from rembg import remove
        # output = remove(image)
        
        # For this sample, just return the image as-is (with alpha channel)
        result_image = image
        
        # ===== END PLACEHOLDER =====
        
        # Convert back to base64
        result_base64 = image_to_base64(result_image, format=request.format.upper())
        
        processing_time = (time.time() - start_time) * 1000
        
        return JSONResponse({
            "success": True,
            "result_image": f"data:image/{request.format};base64,{result_base64}",
            "processing_time_ms": int(processing_time),
            "message": "Background removed successfully"
        })
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ===== Inpainting Endpoint =====
@app.post("/api/inpaint")
async def inpaint(request: InpaintRequest):
    """
    Inpaint (generative fill) image area
    
    Request:
        image: base64 encoded image
        prompt: text description of what to paint
        negative_prompt: what to avoid
        strength: painting strength (0-1)
    
    Response:
        result_image: base64 encoded result
        processing_time_ms: how long it took
    """
    try:
        start_time = time.time()
        
        # Convert base64 to image
        image = base64_to_image(request.image)
        
        # ===== PLACEHOLDER LOGIC =====
        # In production, replace with actual inpainting model
        # Options: LaMa, PowerPaint, or Stability AI API
        
        # Simulate processing
        time.sleep(2)
        
        # Mock: Apply a gradient fill
        width, height = image.size
        
        # Create gradient effect as placeholder
        result_image = image.copy()
        pixels = result_image.load()
        
        for i in range(width):
            for j in range(height):
                # Apply subtle gradient
                r, g, b = pixels[i, j][:3] if len(pixels[i, j]) >= 3 else (r, g, b)
                factor = 0.9 + (i / width) * 0.1
                pixels[i, j] = (int(r * factor), int(g * factor), int(b * factor))
        
        # ===== END PLACEHOLDER =====
        
        result_base64 = image_to_base64(result_image, format="PNG")
        
        processing_time = (time.time() - start_time) * 1000
        
        return JSONResponse({
            "success": True,
            "result_image": f"data:image/png;base64,{result_base64}",
            "processing_time_ms": int(processing_time),
            "prompt": request.prompt,
            "message": "Image inpainted successfully"
        })
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ===== Upscaling Endpoint =====
@app.post("/api/upscale")
async def upscale(request: UpscaleRequest):
    """
    Upscale image using AI
    
    Request:
        image: base64 encoded image
        scale: upscale factor (2x, 3x, 4x)
    
    Response:
        result_image: base64 encoded result
        original_size: original dimensions
        upscaled_size: new dimensions
        processing_time_ms: how long it took
    """
    try:
        start_time = time.time()
        
        # Convert base64 to image
        image = base64_to_image(request.image)
        original_size = image.size
        
        # Validate scale
        if request.scale not in [2, 3, 4]:
            raise ValueError("Scale must be 2, 3, or 4")
        
        # ===== PLACEHOLDER LOGIC =====
        # In production, use Real-ESRGAN or similar
        # from realesrgan import RealESRGAN
        
        # Simulate processing
        time.sleep(2)
        
        # Mock: Use PIL's LANCZOS resampling
        new_width = original_size[0] * request.scale
        new_height = original_size[1] * request.scale
        
        result_image = image.resize(
            (new_width, new_height),
            Image.Resampling.LANCZOS
        )
        
        # ===== END PLACEHOLDER =====
        
        result_base64 = image_to_base64(result_image, format="PNG")
        
        processing_time = (time.time() - start_time) * 1000
        
        return JSONResponse({
            "success": True,
            "result_image": f"data:image/png;base64,{result_base64}",
            "original_size": f"{original_size[0]}x{original_size[1]}",
            "upscaled_size": f"{new_width}x{new_height}",
            "scale_factor": request.scale,
            "processing_time_ms": int(processing_time),
            "message": "Image upscaled successfully"
        })
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ===== Object Removal Endpoint =====
@app.post("/api/remove-object")
async def remove_object(request: RemoveObjectRequest):
    """
    Remove objects from image
    
    Request:
        image: base64 encoded image
        mask: optional base64 encoded mask
        prompt: description of what to remove
    
    Response:
        result_image: base64 encoded result
        processing_time_ms: how long it took
    """
    try:
        start_time = time.time()
        
        # Convert base64 to image
        image = base64_to_image(request.image)
        
        # ===== PLACEHOLDER LOGIC =====
        # In production, use GFPGAN or LaMa models
        
        # Simulate processing
        time.sleep(1.5)
        
        # Mock: Apply blur as placeholder for removal
        result_image = image.copy()
        
        # Apply slight blur to simulate object removal
        result_image = result_image.filter(ImageFilter.GaussianBlur(radius=2))
        
        # ===== END PLACEHOLDER =====
        
        result_base64 = image_to_base64(result_image, format="PNG")
        
        processing_time = (time.time() - start_time) * 1000
        
        return JSONResponse({
            "success": True,
            "result_image": f"data:image/png;base64,{result_base64}",
            "processing_time_ms": int(processing_time),
            "prompt": request.prompt,
            "message": "Object removed successfully"
        })
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ===== Filter Endpoints (Bonus) =====

@app.post("/api/apply-filter")
async def apply_filter(request: dict):
    """
    Apply various filters to image
    
    Request:
        image: base64 encoded image
        filter_type: "grayscale", "sepia", "blur", "brightness", etc.
        intensity: 0-1 (optional)
    """
    try:
        image = base64_to_image(request["image"])
        filter_type = request.get("filter_type", "grayscale")
        intensity = request.get("intensity", 1.0)
        
        # Apply filter
        if filter_type == "grayscale":
            result_image = image.convert("L")
        elif filter_type == "blur":
            result_image = image.filter(ImageFilter.GaussianBlur(radius=5 * intensity))
        elif filter_type == "brightness":
            enhancer = ImageEnhance.Brightness(image)
            result_image = enhancer.enhance(0.5 + intensity)
        else:
            result_image = image
        
        result_base64 = image_to_base64(result_image, format="PNG")
        
        return JSONResponse({
            "success": True,
            "result_image": f"data:image/png;base64,{result_base64}",
            "filter_type": filter_type
        })
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ===== Error Handler =====
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Custom error handler"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": exc.detail,
            "error_code": exc.status_code
        }
    )

# ===== Main =====
if __name__ == "__main__":
    print("""
    🚀 AI Image Editor API Server Starting...
    
    Endpoints:
    ✅ GET  http://localhost:8000/                (Health check)
    ✅ GET  http://localhost:8000/api/health      (API health)
    ✅ POST http://localhost:8000/api/remove-background
    ✅ POST http://localhost:8000/api/inpaint
    ✅ POST http://localhost:8000/api/upscale
    ✅ POST http://localhost:8000/api/remove-object
    
    Docs:
    📖 http://localhost:8000/docs (Swagger UI)
    
    Update image-editor.html with:
    const API_BASE_URL = 'http://localhost:8000/api';
    """)
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )

"""
🔗 Real Implementations to Replace Placeholders:

1. Remove Background:
   pip install rembg
   from rembg import remove
   output = remove(image)

2. Inpainting:
   pip install diffusers torch
   from diffusers import StableDiffusionInpaintPipeline
   
3. Upscaling:
   pip install realesrgan
   from basicsr.archs.rrdbnet_arch import RRDBNet
   from realesrgan import RealESRGANer

4. Or use external APIs:
   - Stability AI API
   - remove.bg API
   - Replicate API
"""

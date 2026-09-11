# 🛠️ Technical Guide - AI Image Editor

## 📚 Mục Lục

1. [Project Structure](#project-structure)
2. [Setup Instructions](#setup-instructions)
3. [API Integration](#api-integration)
4. [Architecture](#architecture)
5. [Performance Tips](#performance-tips)
6. [Troubleshooting](#troubleshooting)
7. [Deployment](#deployment)

---

## 🏗️ Project Structure

```
image-editor.html (File chính - Single HTML file)
├── HTML (Markup)
├── CSS (Styling - Responsive Design)
└── JavaScript (Logic)
    ├── Initialization
    ├── Upload & Canvas Management
    ├── Basic Tools (Text, Shape, Rotate, etc.)
    ├── Filters & Adjustments
    ├── AI Features Placeholders
    ├── History Management (Undo/Redo)
    ├── UI Utilities (Toast, Loading, Modal)
    └── API Integration Points
```

---

## 🚀 Setup Instructions

### Option 1: Local Testing (Fastest)

```bash
# 1. Tải file image-editor.html
# 2. Mở bằng trình duyệt
# 3. Xong!

# Hoặc dùng local server (tốt hơn)
cd /path/to/image-editor
python -m http.server 8000

# Truy cập: http://localhost:8000/image-editor.html
```

### Option 2: Deploy to GitHub Pages

```bash
# 1. Tạo repository GitHub
git init
git add image-editor.html README.md TECHNICAL_GUIDE.md
git commit -m "Initial commit: AI Image Editor"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ai-image-editor.git
git push -u origin main

# 2. Enable GitHub Pages
# Vào Settings → Pages → Select "main" branch

# 3. Truy cập: https://YOUR_USERNAME.github.io/ai-image-editor/image-editor.html
```

### Option 3: Deploy to Your Server

```bash
# 1. Upload file
scp image-editor.html user@your-server:/var/www/html/

# 2. Setup nginx/apache
# Ví dụ nginx config:
server {
    listen 80;
    server_name your-domain.com;
    
    root /var/www/html;
    
    location / {
        try_files $uri $uri/ =404;
    }
    
    # CORS headers nếu API ở domain khác
    add_header Access-Control-Allow-Origin *;
    add_header Access-Control-Allow-Methods "GET, POST, OPTIONS";
}
```

---

## 🔗 API Integration

### Architecture Diagram

```
┌─────────────────────────────────────────┐
│   Browser (image-editor.html)           │
│  - Canvas operations                    │
│  - User interface                       │
└────────────┬────────────────────────────┘
             │ HTTP/FETCH
             ↓
┌─────────────────────────────────────────┐
│   Your AI Backend Server                │
│  - FastAPI / Flask / Node.js / Django   │
│  - API Endpoints:                       │
│    - POST /api/remove-background        │
│    - POST /api/inpaint                  │
│    - POST /api/upscale                  │
│    - POST /api/remove-object            │
└────────────┬────────────────────────────┘
             │
             ↓
┌─────────────────────────────────────────┐
│   AI Models                             │
│  - Rembg (Remove Background)            │
│  - LaMa / PowerPaint (Inpainting)       │
│  - Real-ESRGAN (Upscaling)              │
│  - GFPGAN (Object Removal)              │
└─────────────────────────────────────────┘
```

### API Endpoints Required

#### 1. Remove Background
```
POST /api/remove-background
Content-Type: application/json

Request:
{
  "image": "base64_encoded_image",
  "format": "png"  // optional
}

Response:
{
  "success": true,
  "result_image": "base64_encoded_result",
  "processing_time_ms": 1234
}
```

#### 2. Inpainting (Generative Fill)
```
POST /api/inpaint
Content-Type: application/json

Request:
{
  "image": "base64_encoded_image",
  "prompt": "blue sky with clouds",
  "negative_prompt": "ugly, blurry",  // optional
  "strength": 0.75,  // optional, 0-1
  "guidance_scale": 7.5  // optional
}

Response:
{
  "success": true,
  "result_image": "base64_encoded_result",
  "processing_time_ms": 3456
}
```

#### 3. Image Upscaling
```
POST /api/upscale
Content-Type: application/json

Request:
{
  "image": "base64_encoded_image",
  "scale": 2,  // 2x, 3x, 4x
  "model": "real-esrgan-x2plus"  // optional
}

Response:
{
  "success": true,
  "result_image": "base64_encoded_result",
  "original_size": "800x600",
  "upscaled_size": "1600x1200",
  "processing_time_ms": 2345
}
```

#### 4. Object Removal
```
POST /api/remove-object
Content-Type: application/json

Request:
{
  "image": "base64_encoded_image",
  "mask": "base64_encoded_mask",  // if available
  "prompt": "remove the person"  // or describe what to remove
}

Response:
{
  "success": true,
  "result_image": "base64_encoded_result",
  "processing_time_ms": 2567
}
```

### CORS Setup (Critical!)

If your API is on a different domain, add these headers:

```
Access-Control-Allow-Origin: https://your-domain.com
Access-Control-Allow-Methods: GET, POST, OPTIONS
Access-Control-Allow-Headers: Content-Type
Access-Control-Max-Age: 86400
```

### Error Handling Pattern

```javascript
fetch(API_ENDPOINT, {
    method: 'POST',
    body: JSON.stringify(data)
})
.then(res => {
    if (!res.ok) {
        throw new Error(`HTTP ${res.status}: ${res.statusText}`);
    }
    return res.json();
})
.then(data => {
    if (!data.success) {
        throw new Error(data.error_message || 'Unknown error');
    }
    // Process result
})
.catch(error => {
    console.error('API Error:', error);
    showToast(`Lỗi: ${error.message}`, 'error');
    hideLoading();
});
```

---

## 🏛️ Architecture

### Component Breakdown

#### Canvas Management
```javascript
// Fabric.js Canvas
const canvas = new fabric.Canvas('canvas', {
    backgroundColor: '#ffffff',
    fireRightClick: true,
    stopContextMenu: true,
});
```

#### History Management
```javascript
let canvasHistory = [];      // Store all states
let historyStep = 0;         // Current position

function saveToHistory() {
    canvasHistory = canvasHistory.slice(0, historyStep);
    canvasHistory.push(canvas.toJSON());
    historyStep = canvasHistory.length - 1;
}
```

#### Image Processing Flow

```
User Action (Upload, Edit, AI)
    ↓
Get image from canvas → canvas.toDataURL('image/png')
    ↓
Send to API → fetch(API_URL, { body: base64_image })
    ↓
API processes image
    ↓
Receive result → fabric.Image.fromURL(result_url)
    ↓
Load to canvas → canvas.add(img); canvas.renderAll()
    ↓
Save to history → saveToHistory()
    ↓
Show notification → showToast('Success', 'success')
```

### State Management

```javascript
// Global State
{
    canvas: Object,          // Fabric canvas instance
    canvasHistory: Array,    // Historical states
    historyStep: Number,     // Current history position
    currentZoom: Number,     // Zoom level
    API_BASE_URL: String,    // API endpoint
}
```

---

## ⚡ Performance Tips

### 1. Image Compression Before Upload

```javascript
function compressImage(file, maxWidth = 1200, quality = 0.8) {
    const reader = new FileReader();
    reader.onload = function(e) {
        const img = new Image();
        img.onload = function() {
            const canvas = document.createElement('canvas');
            const scale = Math.min(maxWidth / img.width, 1);
            
            canvas.width = img.width * scale;
            canvas.height = img.height * scale;
            
            const ctx = canvas.getContext('2d');
            ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
            
            return canvas.toDataURL('image/jpeg', quality);
        };
        img.src = e.target.result;
    };
    reader.readAsDataURL(file);
}
```

### 2. Optimize API Requests

```javascript
// Resize canvas before sending to API
function optimizeForAPI(canvas, maxDimension = 512) {
    const scale = Math.min(maxDimension / canvas.width, maxDimension / canvas.height);
    const tempCanvas = document.createElement('canvas');
    tempCanvas.width = canvas.width * scale;
    tempCanvas.height = canvas.height * scale;
    
    const ctx = tempCanvas.getContext('2d');
    ctx.drawImage(canvas.getElement(), 0, 0, tempCanvas.width, tempCanvas.height);
    
    return tempCanvas.toDataURL('image/jpeg', 0.8);
}
```

### 3. Cache Results

```javascript
const resultCache = new Map();

function getCachedResult(key) {
    return resultCache.get(key);
}

function cacheResult(key, data) {
    resultCache.set(key, data);
    // Clear cache if too large
    if (resultCache.size > 10) {
        const firstKey = resultCache.keys().next().value;
        resultCache.delete(firstKey);
    }
}
```

### 4. Debounce Input Events

```javascript
function debounce(func, delay) {
    let timeoutId;
    return function(...args) {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => func(...args), delay);
    };
}

// Usage
const debouncedBrightnessUpdate = debounce(updateBrightness, 300);
```

---

## 🐛 Troubleshooting

### Problem: API Calls Fail with CORS Error

**Solution:**
```javascript
// Add CORS header to your fetch request
fetch(API_URL, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Origin': window.location.origin,
    },
    body: JSON.stringify(data),
    credentials: 'include',  // Include cookies if needed
})
```

### Problem: Image Too Large to Process

**Solution:**
```javascript
function resizeBeforeAPI(maxSize = 1024) {
    const imgData = canvas.toDataURL('image/jpeg', 0.7);
    // Create smaller version
    const img = new Image();
    img.onload = function() {
        const scale = Math.min(maxSize / img.width, maxSize / img.height);
        // ... resize logic
    };
    img.src = imgData;
}
```

### Problem: Undo/Redo Not Working

**Solution:**
```javascript
// Make sure to call saveToHistory() after each operation
function anyEdit() {
    // ... make changes to canvas
    canvas.renderAll();
    saveToHistory();  // ← Don't forget this!
}
```

### Problem: Canvas Looks Blurry on High DPI Screens

**Solution:**
```javascript
// Increase canvas resolution
const dpr = window.devicePixelRatio || 1;
canvas.setWidth(800 * dpr);
canvas.setHeight(600 * dpr);
canvas.setZoom(1 / dpr);
```

---

## 🚀 Deployment

### Step-by-Step Deployment Checklist

```
✅ Pre-Deployment
├─ [ ] Test all basic features locally
├─ [ ] Prepare AI API endpoints
├─ [ ] Update API_BASE_URL in HTML
├─ [ ] Test API integration
├─ [ ] Check CORS configuration
└─ [ ] Optimize images & performance

✅ Deployment
├─ [ ] Choose hosting (GitHub Pages, Vercel, your server)
├─ [ ] Upload files
├─ [ ] Verify CORS headers
├─ [ ] Test in production
├─ [ ] Add error logging (optional)
└─ [ ] Setup monitoring (optional)

✅ Post-Deployment
├─ [ ] Monitor user feedback
├─ [ ] Fix reported bugs
├─ [ ] Track API performance
└─ [ ] Plan next features
```

### Environment Variables (If Using Backend)

```javascript
// .env (if you have a build process)
VITE_API_URL=https://api.your-domain.com
VITE_ENABLE_AI=true
VITE_MAX_IMAGE_SIZE=1024
```

### Production API Configuration

```javascript
// Different URLs for dev vs production
const API_BASE_URL = process.env.NODE_ENV === 'production'
    ? 'https://api.your-domain.com'
    : 'http://localhost:8000/api';
```

---

## 📊 Monitoring & Analytics (Optional)

```javascript
// Track API performance
async function trackAPICall(endpoint, startTime) {
    const duration = Date.now() - startTime;
    console.log(`[PERF] ${endpoint}: ${duration}ms`);
    
    // Send to analytics
    if (window.analytics) {
        window.analytics.track('api_call', {
            endpoint,
            duration,
            timestamp: new Date()
        });
    }
}
```

---

## 🎓 Learning Resources

- **Fabric.js:** https://fabricjs.com/
- **Canvas API:** https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API
- **Fetch API:** https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
- **Base64 Encoding:** https://developer.mozilla.org/en-US/docs/Glossary/Base64

---

## 📞 Support

If you encounter issues:

1. **Check the browser console** - Press F12 → Console tab
2. **Check network requests** - F12 → Network tab
3. **Verify API is running** - Test endpoint with Postman/curl
4. **Check CORS headers** - Verify in Network tab response headers

---

**Happy Coding! 🚀**

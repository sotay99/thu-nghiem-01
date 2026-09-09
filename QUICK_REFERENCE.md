# ⚡ Quick Reference - AI Image Editor

## 🎯 In 60 Seconds

```
1. OPEN
   👉 Mở image-editor.html trong trình duyệt

2. UPLOAD
   👉 Bấm "Tải Ảnh" hoặc kéo thả ảnh

3. EDIT
   👉 Chọn công cụ ở sidebar trái
   👉 Điều chỉnh bằng slider ở sidebar phải

4. DOWNLOAD
   👉 Bấm "Tải Xuống"

DONE! ✨
```

---

## 📱 Keyboard Shortcuts (Sắp Tới)

```
Ctrl+Z       Hoàn tác (Undo)
Ctrl+Y       Làm lại (Redo)
Ctrl+S       Lưu (Save)
Ctrl+D       Tải xuống (Download)
Delete       Xoá đối tượng đã chọn
+/-          Zoom in/out
Space        Pan/Move canvas
```

---

## 🎨 Tools Cheat Sheet

| Công Cụ | Nút | Phím Tắt | Mục Đích |
|---------|-----|----------|---------|
| **Text** | T | Ctrl+T | Thêm text |
| **Shape** | S | Ctrl+Shift+S | Thêm hình |
| **Crop** | C | Ctrl+C | Cắt ảnh |
| **Rotate** | R | Ctrl+R | Xoay 15° |
| **Flip** | F | Ctrl+H | Lật ngang |
| **Grayscale** | G | | Đen trắng |
| **Sepia** | | | Màu cổ |
| **Blur** | | | Mờ |
| **Saturate** | | | Bão hòa |

---

## 🤖 AI Features

```
Remove Background
├─ Nút: 🎨 Xoá Nền
├─ API: POST /api/remove-background
├─ Input: image (base64)
└─ Output: transparent background

Inpainting
├─ Nút: 🎨 Sửa Vùng
├─ API: POST /api/inpaint
├─ Input: image, prompt
└─ Output: filled area

Upscaling
├─ Nút: 🎨 Nâng Cấp
├─ API: POST /api/upscale
├─ Input: image, scale (2x/4x)
└─ Output: larger image

Object Removal
├─ Nút: 🎨 Xoá Đối Tượng
├─ API: POST /api/remove-object
├─ Input: image, mask
└─ Output: object removed
```

---

## 🔧 Configuration (30 Giây)

### Update API URL

**File:** `image-editor.html`

**Line 433:**
```javascript
const API_BASE_URL = 'http://your-api.com/api';  // ← Thay đây
```

### Test API Connection

```javascript
// Mở console (F12) và paste:
fetch('http://your-api.com/api/health')
  .then(r => r.json())
  .then(d => console.log(d))
  .catch(e => console.error('API Error:', e));
```

---

## 🐛 Troubleshooting Quick Fixes

| Vấn Đề | Nguyên Nhân | Fix |
|--------|-----------|-----|
| "404 Not Found" | File không tìm thấy | Kiểm tra đường dẫn file |
| "CORS Error" | API khác domain | Thêm CORS headers |
| "Canvas blank" | Canvas chưa khởi tạo | Reload trang |
| "Upload fail" | File size lớn | Giảm kích thước ảnh |
| "Undo not working" | Quên saveToHistory() | Kiểm tra code |
| "Zoom stuck" | Reset zoom lỗi | Reload trang |

---

## 📊 API Response Format

### Success
```json
{
  "success": true,
  "result_image": "data:image/png;base64,...",
  "processing_time_ms": 1234
}
```

### Error
```json
{
  "success": false,
  "error": "Invalid image format",
  "error_code": 400
}
```

---

## 💾 File Management

```
Project Structure:
├─ image-editor.html          ← Main file
├─ README.md                  ← How to use
├─ TECHNICAL_GUIDE.md         ← Deep dive
├─ QUICK_REFERENCE.md         ← This file
├─ sample_api_server.py       ← Backend template
└─ SUMMARY.md                 ← Overview
```

---

## 🚀 Deploy Checklist

```
✅ Pre-Deploy
├─ [ ] Test locally
├─ [ ] API running?
├─ [ ] CORS headers set?
└─ [ ] Update API_BASE_URL

✅ Deploy
├─ [ ] Upload HTML file
├─ [ ] Deploy API server
├─ [ ] Test in production
└─ [ ] Monitor errors

✅ Post-Deploy
├─ [ ] Share URL
├─ [ ] Get user feedback
├─ [ ] Monitor performance
└─ [ ] Plan improvements
```

---

## 📝 Common Code Snippets

### Load Image from URL
```javascript
fabric.Image.fromURL('image.jpg', function(img) {
  canvas.add(img);
  canvas.renderAll();
});
```

### Export Canvas
```javascript
// PNG
canvas.toDataURL('image/png');

// JPEG
canvas.toDataURL('image/jpeg', 0.8);
```

### Undo/Redo
```javascript
undo();  // Hoàn tác
redo();  // Làm lại
```

### Add Text
```javascript
const text = new fabric.Text('Hello', {
  left: 100,
  top: 100,
  fontSize: 24
});
canvas.add(text);
canvas.renderAll();
```

### Get Active Object
```javascript
const obj = canvas.getActiveObject();
if (obj) {
  console.log(obj.type); // "text", "image", etc.
}
```

---

## 🎓 Learning Path

```
Day 1: Basics
└─ Open HTML → Use tools → Download image

Day 2: Customization
└─ Change colors → Update text → Modify layout

Day 3: API Integration
└─ Setup backend → Connect API → Test features

Day 4: Deployment
└─ Push to GitHub → Deploy → Monitor

Day 5: Enhancement
└─ Add features → Fix bugs → Optimize
```

---

## 💡 Pro Tips

✅ **Workflow Tips**
- Save work frequently (use Undo/Redo wisely)
- Use multiple canvas layers when needed
- Export intermediate results

✅ **Performance**
- Keep images under 1MB for API
- Close unused browser tabs
- Clear history after large edits

✅ **Mobile**
- Use 2-finger zoom on mobile
- Tap and hold to select
- Landscape mode for better canvas view

✅ **API**
- Test endpoints with Postman first
- Add error handling in fetch calls
- Log API responses for debugging

---

## 🔗 Important Links

```
Documentation:
📖 README.md              - How to use
📖 TECHNICAL_GUIDE.md     - Technical details
📖 QUICK_REFERENCE.md     - This file
📖 SUMMARY.md             - Overview

Resources:
🔗 Fabric.js: https://fabricjs.com/
🔗 Canvas API: https://developer.mozilla.org/docs/Web/API/Canvas_API
🔗 Fetch API: https://developer.mozilla.org/docs/Web/API/Fetch_API

Support:
💬 Check console (F12) for errors
💬 Check network tab for API issues
💬 Read error messages carefully
```

---

## ❓ FAQ

**Q: Can I use this offline?**
A: Yes! All libraries use CDN. Works without internet after first load.

**Q: Is it mobile-friendly?**
A: Yes! Responsive design for desktop, tablet, and mobile.

**Q: How do I add my own AI model?**
A: Create an API endpoint and update fetch() calls in HTML.

**Q: Can I customize the UI?**
A: Yes! Edit CSS in `<style>` section. Modify layout in `<body>`.

**Q: Is it production-ready?**
A: Yes, but add authentication and rate limiting before production.

**Q: Can I embed it in my website?**
A: Yes! Use an iframe: `<iframe src="image-editor.html"></iframe>`

**Q: How large can images be?**
A: Up to browser memory limit. Recommended: < 10MB

**Q: Does it work on iPhone/iPad?**
A: Yes! Modern iOS browsers (Safari 12+) supported.

---

## 📞 When You Need Help

**Quick Support:**
```
Problem → Check console (F12)
         → Read error message
         → Search TECHNICAL_GUIDE.md
         → Try refresh
```

**Advanced Support:**
```
If stuck → Post error in README issue
        → Include screenshots
        → Describe steps to reproduce
        → Share browser/OS info
```

---

## ✨ You're Ready!

1. ✅ HTML file ready
2. ✅ Docs ready
3. ✅ API template ready
4. ✅ This guide ready

**Next Step:** Open `image-editor.html` and start editing! 🎨

---

*Quick Reference v1.0 - Keep this handy!*

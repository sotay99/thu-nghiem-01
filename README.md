# 🎨 AI Image Editor

**Xem trực tiếp:** https://sotay99.github.io/thu-nghiem-01/

## 📁 Cấu trúc kho

```
index.html      → trang chủ, chính là bản chỉnh sửa nâng cao (Layer Management)
server/         → máy chủ API mẫu cho các tính năng AI (chạy tại máy)
docs/           → toàn bộ tài liệu
.github/workflows/deploy.yml → tự deploy lên GitHub Pages mỗi lần đẩy lên main
```

> Bản cơ bản (chỉ dùng công cụ đơn giản, không có quản lý lớp) đã được gỡ bỏ.
> Trang chủ giờ chạy thẳng bản nâng cao.

> Lưu ý: các tính năng AI gọi tới `http://localhost:8000/api`. Trên GitHub Pages
> (chạy bằng HTTPS) trình duyệt sẽ chặn lời gọi này; muốn dùng thì phải trỏ
> `API_BASE_URL` sang một máy chủ có HTTPS.

---


## 📋 Mô Tả

Đây là một **Web-based Image Editor** hoàn chỉnh được xây dựng từ Vue Fabric Editor project, được tối ưu hóa cho cả Desktop và Mobile. Editor này bao gồm các tính năng cơ bản và placeholder cho các tính năng AI.

---

## ✨ Tính Năng Hiện Có

### 🛠️ Công Cụ Cơ Bản
- ✅ **Thêm Text** - Thêm văn bản vào ảnh
- ✅ **Hình Dạng** - Thêm hình tròn, hình vuông, v.v.
- ✅ **Cắt Ảnh (Crop)** - Cắt ảnh theo tỷ lệ mong muốn
- ✅ **Xoay (Rotate)** - Xoay ảnh từng độ
- ✅ **Lật (Flip)** - Lật ảnh ngang/dọc

### 🎨 Bộ Lọc
- ✅ Đen Trắng (Grayscale)
- ✅ Sepia
- ✅ Mờ (Blur)
- ✅ Bão Hòa Màu (Saturation)

### 🎛️ Điều Chỉnh
- ✅ Độ Sáng (Brightness)
- ✅ Độ Tương Phản (Contrast)
- ✅ Bão Hòa Màu (Saturation)
- ✅ Bộ Chọn Màu (Color Picker)

### 📸 Quản Lý
- ✅ Tải Ảnh Lên (Upload)
- ✅ Tải Xuống (Download)
- ✅ Hoàn Tác (Undo)
- ✅ Làm Lại (Redo)
- ✅ Đặt Lại (Reset)
- ✅ Zoom In/Out

### 🤖 Tính Năng AI (Placeholders - Chờ Kết Nối)
- 🔄 **Xoá Nền (Remove Background)** - Xoá background tự động
- 🔄 **Sửa Vùng (Inpainting)** - Sửa vùng ảnh bằng AI text-to-image
- 🔄 **Nâng Cấp Độ Phân Giải (Upscaling)** - Mở rộng ảnh bằng AI
- 🔄 **Xoá Đối Tượng (Object Removal)** - Xoá đối tượng không mong muốn

---

## 🚀 Cách Sử Dụng

### 1. **Mở File**
```html
Mở file `index.html` trong trình duyệt (Chrome, Firefox, Safari, Edge)
```

### 2. **Tải Ảnh**
- Bấm nút **"Tải Ảnh"** ở góc trên cùng
- Hoặc kéo thả ảnh trực tiếp vào editor

### 3. **Chỉnh Sửa**
- Sử dụng các công cụ ở **Sidebar Trái**
- Điều chỉnh bằng thanh trượt ở **Sidebar Phải**
- Xem zoom level ở **Thanh Công Cụ Canvas**

### 4. **Tải Xuống**
- Bấm **"Tải Xuống"** để lưu ảnh đã chỉnh sửa

---

## 📱 Responsive Design

✅ **Desktop** - Giao diện đầy đủ với 3 sidebar
✅ **Tablet** - Giao diện tối ưu, sidebar có thể ẩn/hiện
✅ **Mobile** - Giao diện rút gọn, tập trung vào canvas

---

## 🔗 Cách Gắn API AI

### 1. **Xoá Nền (Remove Background)**

**File:** Tìm function `removeBackground()` (dòng ~558)

**Thay thế:**
```javascript
function removeBackground() {
    showLoading('Đang xoá nền...');
    
    // LẤY ảnh từ canvas
    const imageData = canvas.toDataURL('image/png');
    
    // GỌI API của bạn
    fetch(`${API_BASE_URL}/remove-background`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ image: imageData })
    })
    .then(res => res.json())
    .then(data => {
        // TẢI kết quả trở lại
        fabric.Image.fromURL(data.result_image, function(img) {
            img.scale(canvas.width / img.width);
            canvas.clear();
            canvas.add(img);
            canvas.renderAll();
            saveToHistory();
            hideLoading();
            showToast('Đã xoá nền thành công', 'success');
        });
    })
    .catch(err => {
        hideLoading();
        showToast('Lỗi: ' + err.message, 'error');
    });
}
```

### 2. **Sửa Vùng (Inpainting)**

**File:** Tìm function `executeInpaint()` (dòng ~595)

**Thay thế:**
```javascript
function executeInpaint() {
    const prompt = document.getElementById('inpaintPrompt').value;
    if (!prompt) {
        showToast('Vui lòng nhập mô tả', 'error');
        return;
    }

    showLoading('Đang sửa vùng ảnh với AI...');
    hideInpaintModal();

    const imageData = canvas.toDataURL('image/png');
    
    fetch(`${API_BASE_URL}/inpaint`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
            image: imageData,
            prompt: prompt
        })
    })
    .then(res => res.json())
    .then(data => {
        fabric.Image.fromURL(data.result_image, function(img) {
            img.scale(canvas.width / img.width);
            canvas.clear();
            canvas.add(img);
            canvas.renderAll();
            saveToHistory();
            hideLoading();
            showToast('Đã sửa vùng thành công', 'success');
        });
    })
    .catch(err => {
        hideLoading();
        showToast('Lỗi: ' + err.message, 'error');
    });
}
```

### 3. **Nâng Cấp Độ Phân Giải (Upscaling)**

**File:** Tìm function `upscaleImage()` (dòng ~610)

**Thay thế:**
```javascript
function upscaleImage() {
    showLoading('Đang nâng cấp độ phân giải...');
    
    const imageData = canvas.toDataURL('image/png');
    
    fetch(`${API_BASE_URL}/upscale`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ image: imageData })
    })
    .then(res => res.json())
    .then(data => {
        fabric.Image.fromURL(data.result_image, function(img) {
            img.scale(canvas.width / img.width);
            canvas.clear();
            canvas.add(img);
            canvas.renderAll();
            saveToHistory();
            hideLoading();
            showToast('Đã nâng cấp thành công', 'success');
        });
    })
    .catch(err => {
        hideLoading();
        showToast('Lỗi: ' + err.message, 'error');
    });
}
```

> Ba hàm trên (`removeBackground`, `executeInpaint`, `upscaleImage`) đều nằm
> trong `index.html`; số dòng có thể lệch theo từng lần sửa, tìm bằng tên hàm
> là chắc nhất.

---

## ⚙️ Cách Thay Đổi API URL

Tìm `const API_BASE_URL` gần đầu khối `<script>` trong `index.html`:
```javascript
const API_BASE_URL = 'http://localhost:8000/api'; // ← Thay đổi URL tại đây
```

Thay `http://localhost:8000/api` bằng URL của API server của bạn.

---

## 🎨 Tùy Chỉnh Giao Diện

### Thay Đổi Màu Chính

Tìm khối `:root { ... }` đầu `<style>` trong `index.html`, các biến
`--layer-*-color` quy định màu từng lớp (layer).

---

## 📦 Yêu Cầu & Dependencies

✅ **Browser Modern:**
- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

✅ **CDN Libraries** (tự động tải):
- Bootstrap 5.3.0
- Font Awesome 6.4.0
- Fabric.js 5.3.0

---

## 🔧 Nâng Cấp Tiếp Theo

### Khi Bạn Muốn Thêm:

1. **Crop Tool Hoàn Chỉnh**
   - Tôi sẽ thêm interactive crop area
   - Apply crop button

2. **Layer Panel**
   - Quản lý các layer như Photoshop
   - Undo/Redo per layer

3. **Advanced Filters**
   - Thêm các bộ lọc mà nâng cao
   - Combo filters

4. **Export Options**
   - Xuất JPEG, PNG, WebP, SVG
   - Compression settings

5. **Collaboration Features**
   - Share canvas với người khác
   - Real-time editing

**Chỉ cần gửi yêu cầu, tôi sẽ thêm vào!**

---

## 📝 Lưu Ý Quan Trọng

⚠️ **Trước Khi Deploy:**

1. Thay `API_BASE_URL` bằng URL thực của API
2. Thêm CORS headers nếu API ở domain khác
3. Test tất cả AI features trước deploy
4. Thêm error handling cho network failures

---

## 💬 Hỗ Trợ & Nâng Cấp

Khi bạn cần:
- ✏️ Sửa giao diện
- ➕ Thêm tính năng
- 🐛 Fix bug
- 🚀 Optimize performance

**Chỉ cần nói cho tôi biết!** Tôi sẽ:
1. Cập nhật file HTML
2. Giải thích thay đổi
3. Đưa version mới cho bạn

---

## 📸 Demo

Để thử ngay:
```
1. Mở file index.html trong trình duyệt
2. Bấm "Tải Ảnh" 
3. Chỉnh sửa bằng các công cụ
4. Tải xuống kết quả
```

---

## ✅ Checklist Cho Bạn

- [ ] Mở file HTML và xem giao diện
- [ ] Test các công cụ cơ bản (add text, rotate, filters)
- [ ] Chuẩn bị API endpoints cho AI features
- [ ] Gắn API URLs vào code
- [ ] Test AI features
- [ ] Deploy lên server
- [ ] Chia sẻ với người dùng

---

**Chúc bạn thành công! 🚀**

Nếu cần gì, chỉ cần nói!

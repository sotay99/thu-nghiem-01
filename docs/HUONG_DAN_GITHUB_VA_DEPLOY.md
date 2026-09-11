# 🚀 HƯỚNG DẪN CHI TIẾT: ĐƯA CODE LÊN GITHUB VÀ DEPLOY MIỄN PHÍ

## 📋 MỤC LỤC
1. [Chuẩn Bị](#chuẩn-bị)
2. [Tạo Repository Trên GitHub](#tạo-repository-trên-github)
3. [Chuẩn Bị Code Trên Máy](#chuẩn-bị-code-trên-máy)
4. [Push Code Lên GitHub](#push-code-lên-github)
5. [Deploy Lên GitHub Pages (Miễn Phí)](#deploy-lên-github-pages-miễn-phí)
6. [Các Vấn Đề Thường Gặp](#các-vấn-đề-thường-gặp)

---

## 🔧 CHUẨN BỊ

### Bước 1: Cài Đặt Git (Nếu chưa có)

**Trên Windows:**
1. Vào https://git-scm.com/download/win
2. Tải file .exe (64-bit)
3. Chạy file, next -> next -> Finish
4. Mở Command Prompt hoặc PowerShell
5. Gõ: `git --version` (kiểm tra cài đặt)
6. Kết quả: `git version 2.xx.x`

**Trên Mac:**
1. Cài Homebrew trước (nếu chưa có):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Sau đó cài Git:
   ```bash
   brew install git
   ```

**Trên Linux:**
```bash
sudo apt-get update
sudo apt-get install git
```

### Bước 2: Tạo Tài Khoản GitHub (Nếu chưa có)

1. Vào https://github.com
2. Nhấp "Sign up"
3. Điền:
   - Email: your-email@gmail.com
   - Password: mật khẩu mạnh (8+ ký tự, có chữ + số + ký tự đặc biệt)
   - Username: tên người dùng (vd: your-username)
4. Xác thực email (kiểm tra hộp thư)
5. Hoàn thành setup

### Bước 3: Cấu Hình Git Trên Máy Tính

Mở Terminal/Command Prompt và gõ:

```bash
git config --global user.name "Tên Của Bạn"
git config --global user.email "email@gmail.com"
```

Ví dụ:
```bash
git config --global user.name "Nguyen Van A"
git config --global user.email "vana@gmail.com"
```

Kiểm tra cấu hình:
```bash
git config --global --list
```

---

## 📦 TẠO REPOSITORY TRÊN GITHUB

### Bước 1: Tạo Repository Mới

1. Đăng nhập GitHub (https://github.com)
2. Ở góc trên cùng bên phải → Nhấp dấu **+**
3. Chọn **New repository**
4. Điền thông tin:
   ```
   Repository name: image-editor
   (Có thể dùng tên khác như: ai-image-editor, advanced-layer-editor, etc)
   
   Description (tùy chọn): 
   Advanced AI Image Editor with Professional Layer Management
   
   Public / Private: Chọn PUBLIC (để mọi người có thể dùng)
   
   Initialize this repository with:
   ☐ Add a README file (ĐỪNG chọn - chúng ta sẽ tạo sau)
   ☐ Add .gitignore
   ☐ Choose a license
   ```

5. Nhấp **Create repository**

### Bước 2: Lưu Lại URL Repository

Sau khi tạo, bạn sẽ thấy trang như này:
```
https://github.com/your-username/image-editor
```

Lưu lại URL này, sẽ dùng sau!

---

## 📁 CHUẨN BỊ CODE TRÊN MÁY

### Bước 1: Tạo Thư Mục Dự Án

Mở Terminal/Command Prompt và gõ:

```bash
# Tạo thư mục
mkdir image-editor
cd image-editor
```

Hoặc trên Windows (File Explorer):
1. Tạo thư mục `image-editor` ở nơi thích hợp
2. Mở Command Prompt
3. Chuyển vào thư mục: `cd C:\Users\YourName\Documents\image-editor`

### Bước 2: Sao Chép Các File

**Các file cần copy:**
```
image-editor/
├── image-editor-advanced.html
├── image-editor.html
├── sample_api_server.py
├── README.md (sẽ tạo)
├── .gitignore (sẽ tạo)
└── docs/
    ├── FEATURES_UPDATE_STEP1.md
    ├── FEATURES_UPDATE_STEP2.md
    ├── FEATURES_UPDATE_STEP3.md
    ├── FEATURES_UPDATE_STEP4.md
    ├── FEATURES_UPDATE_STEP5.md
    ├── FEATURES_UPDATE_STEP6.md
    ├── FEATURES_UPDATE_STEP7.md
    ├── FEATURES_UPDATE_STEP8.md
    └── HUONG_DAN_GITHUB_VA_DEPLOY.md
```

**Cách làm:**

1. Tạo thư mục `docs`:
   ```bash
   mkdir docs
   ```

2. Copy các file:
   - Từ `/mnt/user-data/outputs/`:
     - `image-editor-advanced.html` → vào `image-editor/`
     - `image-editor.html` → vào `image-editor/`
     - `sample_api_server.py` → vào `image-editor/`
     - Tất cả `FEATURES_UPDATE_*.md` → vào `image-editor/docs/`
     - `HUONG_DAN_GITHUB_VA_DEPLOY.md` → vào `image-editor/docs/`

### Bước 3: Tạo File README.md

Tạo file `README.md` trong thư mục `image-editor`:

```markdown
# 🎨 Advanced AI Image Editor

Trình chỉnh sửa ảnh chuyên nghiệp với hệ thống quản lý lớp (Layer) giống Photoshop.

## ✨ Tính Năng

### 🖼️ Quản Lý Lớp (Layer Management)
- ✅ Tạo, xóa, đổi tên layer
- ✅ Sao chép layer nhanh chóng
- ✅ Ẩn/hiển thị layer
- ✅ Gộp các layer
- ✅ Tự động gán màu cho layer

### 👥 Nhóm Lớp (Layer Groups)
- ✅ Tạo nhóm layer lồng nhau
- ✅ Hiển thị dạng tree view
- ✅ Expand/collapse nhanh
- ✅ Quản lý nhóm dễ dàng

### 🎯 Multi-Select & Batch Operations
- ✅ Ctrl+Click để chọn nhiều layer
- ✅ Shift+Click để chọn phạm vi
- ✅ Ctrl+A để chọn tất cả
- ✅ Các thao tác hàng loạt (xóa, ẩn, nhân đôi)

### ⌨️ Keyboard Shortcuts
- ✅ 18+ phím tắt chuyên nghiệp
- ✅ Điều hướng bằng mũi tên
- ✅ Ctrl+S để lưu
- ✅ Delete để xóa layer
- ✅ Nhiều phím tắt tiện lợi

### 🎨 Blend Modes & Opacity
- ✅ 19 chế độ hòa trộn Photoshop
- ✅ Điều chỉnh độ mờ 0-100%
- ✅ Áp dụng cho một hoặc nhiều layer
- ✅ Preview real-time

### 🖱️ Drag & Drop
- ✅ Kéo thả để sắp xếp layer
- ✅ Visual feedback trực quan
- ✅ Smooth animations

### 💬 Dropdown Menus
- ✅ Click chuột phải để menu
- ✅ Đổi tên, di chuyển, tạo nhóm
- ✅ Giao diện thân thiện

## 🚀 Cách Sử Dụng

### Cách 1: Chạy Trực Tiếp (Nhanh nhất)
1. Tải file `image-editor-advanced.html`
2. Mở trực tiếp bằng trình duyệt (Click đôi chuột)
3. Bắt đầu chỉnh sửa!

### Cách 2: Deploy Lên GitHub Pages
- Xem hướng dẫn trong `docs/HUONG_DAN_GITHUB_VA_DEPLOY.md`

## 📚 Tài Liệu

- [Step 1: Auto Color & Groups](docs/FEATURES_UPDATE_STEP1.md)
- [Step 2: Dropdown Menus & Move](docs/FEATURES_UPDATE_STEP2.md)
- [Step 3: Tree View](docs/FEATURES_UPDATE_STEP3.md)
- [Step 4: Black Buttons & Indicators](docs/FEATURES_UPDATE_STEP4.md)
- [Step 5: Keyboard Shortcuts](docs/FEATURES_UPDATE_STEP5.md)
- [Step 6: Drag & Drop](docs/FEATURES_UPDATE_STEP6.md)
- [Step 7: Multi-Select](docs/FEATURES_UPDATE_STEP7.md)
- [Step 8: Blend Modes & Opacity](docs/FEATURES_UPDATE_STEP8.md)
- [GitHub & Deploy Guide](docs/HUONG_DAN_GITHUB_VA_DEPLOY.md)

## 🎯 Keyboard Shortcuts Chính

| Phím Tắt | Tác Vụ |
|----------|--------|
| ↑/↓ | Chọn layer trên/dưới |
| D | Sao chép layer |
| R | Đổi tên layer |
| H | Ẩn/hiện layer |
| Delete | Xóa layer |
| Ctrl+N | Layer mới |
| Ctrl+G | Tạo nhóm |
| Ctrl+M | Gộp layer |
| Ctrl+S | Lưu ảnh |
| Ctrl+A | Chọn tất cả |
| ? | Xem tất cả phím tắt |

## 🔧 Yêu Cầu Hệ Thống

- Trình duyệt hiện đại (Chrome, Firefox, Safari, Edge)
- JavaScript được bật
- Không cần cài đặt gì thêm

## 📝 Lưu Ý

- Ứng dụng chạy hoàn toàn trên browser (frontend)
- Dữ liệu lưu trên máy tính của bạn
- Không có server backend bắt buộc
- Tùy chọn API backend trong code nếu cần

## 📄 License

MIT License - Dùng tự do cho dự án cá nhân hoặc thương mại

## 👨‍💻 Tác Giả

Xây dựng với ❤️

## 🤝 Đóng Góp

Nếu muốn cải thiện, vui lòng tạo Pull Request!

---

## 📞 Liên Hệ

Có câu hỏi? Mở Issue trên GitHub!
```

### Bước 4: Tạo File .gitignore

Tạo file `.gitignore` (tệp ẩn) trong thư mục `image-editor`:

```
# Node modules (nếu sau này dùng)
node_modules/
package-lock.json

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Logs
*.log

# OS
.DS_Store
Thumbs.db
```

---

## 📤 PUSH CODE LÊN GITHUB

### Bước 1: Khởi Tạo Git Repository

Mở Terminal/Command Prompt trong thư mục `image-editor`:

```bash
# Di chuyển vào thư mục
cd image-editor

# Khởi tạo git
git init

# Kiểm tra trạng thái
git status
```

Kết quả sẽ hiện:
```
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md
        image-editor-advanced.html
        image-editor.html
        ...
```

### Bước 2: Thêm Tất Cả File

```bash
# Thêm tất cả file
git add .

# Kiểm tra lại
git status
```

Kết quả sẽ hiện tất cả file xanh (sẵn sàng commit)

### Bước 3: Tạo Commit Đầu Tiên

```bash
git commit -m "Initial commit: Add advanced image editor with layer management"
```

Hoặc tiếng Việt:
```bash
git commit -m "Commit đầu tiên: Thêm trình chỉnh sửa ảnh nâng cao với quản lý layer"
```

Kết quả:
```
[master (root-commit) abc1234] Initial commit
 15 files changed, 5000+ insertions(+)
 create mode 100644 README.md
 ...
```

### Bước 4: Kết Nối Repository GitHub

Lưu ý: Thay `your-username` và `image-editor` bằng thông tin của bạn!

```bash
# Thêm remote repository
git remote add origin https://github.com/your-username/image-editor.git

# Kiểm tra
git remote -v
```

Kết quả:
```
origin  https://github.com/your-username/image-editor.git (fetch)
origin  https://github.com/your-username/image-editor.git (push)
```

### Bước 5: Push Lên GitHub

```bash
# Đổi tên branch từ master sang main (chuẩn GitHub)
git branch -M main

# Push lên GitHub
git push -u origin main
```

Sẽ hỏi:
```
Username for 'https://github.com': your-username
Password for 'https://github.com': your-password
```

Gõ:
- **Username**: tên đăng nhập GitHub
- **Password**: mật khẩu GitHub (hoặc Personal Access Token - xem bước sau)

#### ⚠️ Nếu Gặp Lỗi "Password Authentication is Deprecated"

GitHub đã ngừng hỗ trợ password authentication. Thay vào đó, dùng **Personal Access Token**:

**Tạo Personal Access Token:**

1. Vào https://github.com/settings/tokens
2. Nhấp "Generate new token"
3. Chọn "Generate new token (classic)"
4. Điền:
   - Note: `My Computer`
   - Expiration: 90 days (hoặc No expiration)
   - Select scopes: Chọn `repo` (repo full control)
5. Nhấp "Generate token"
6. **Copy token** (chỉ hiện một lần!)
7. Khi git hỏi password, dán token vào

**Lưu token vào máy (optional, tiếp theo không cần nhập):**

Trên Windows (PowerShell):
```powershell
git config --global credential.helper manager-core
```

Trên Mac/Linux:
```bash
git config --global credential.helper store
```

### Bước 6: Kiểm Tra Trên GitHub

1. Vào https://github.com/your-username/image-editor
2. Bạn sẽ thấy tất cả file đã được upload
3. File README.md sẽ hiển thị tự động

---

## 🌐 DEPLOY LÊN GITHUB PAGES (MIỄN PHÍ)

### Bước 1: Bật GitHub Pages

1. Vào repository GitHub: https://github.com/your-username/image-editor
2. Vào tab **Settings**
3. Scroll xuống mục **Pages** (bên trái)
4. Chọn:
   ```
   Source: Deploy from a branch
   Branch: main
   Folder: / (root)
   ```
5. Nhấp **Save**

GitHub sẽ hiển thị:
```
Your site is ready to be published at:
https://your-username.github.io/image-editor/
```

### Bước 2: Chỉnh Sửa HTML (Nếu Cần)

Nếu các file CSS/JS được import từ đường dẫn tuyệt đối, cần chỉnh sửa:

**Trước:**
```html
<link rel="stylesheet" href="/css/style.css">
<script src="/js/app.js"></script>
```

**Sau:**
```html
<link rel="stylesheet" href="./css/style.css">
<script src="./js/app.js"></script>
```

Hoặc dùng đường dẫn tương đối từ GitHub:
```html
<link rel="stylesheet" href="https://raw.githubusercontent.com/your-username/image-editor/main/css/style.css">
```

### Bước 3: Tạo Phiên Bản Deploy

Nếu cần tạo phiên bản riêng để deploy (khác với code gốc), tạo branch mới:

```bash
# Tạo branch mới
git checkout -b gh-pages

# Push lên
git push origin gh-pages
```

Sau đó vào Settings -> Pages, chọn branch `gh-pages`.

### Bước 4: Truy Cập Website

Sau 1-2 phút, truy cập:
```
https://your-username.github.io/image-editor/
```

**Ghi chú:** Thay `your-username` bằng tên GitHub của bạn!

---

## 🔄 CẬP NHẬT CODE SAU

Mỗi khi thay đổi code và muốn upload lên GitHub:

```bash
# 1. Xem thay đổi
git status

# 2. Thêm tất cả file đã thay đổi
git add .

# 3. Tạo commit với mô tả
git commit -m "Mô tả thay đổi của bạn"

# 4. Push lên GitHub
git push origin main
```

---

## 🆘 CÁC VẤN ĐỀ THƯỜNG GẶP

### Vấn đề 1: "fatal: not a git repository"

**Nguyên nhân:** Chưa chạy `git init`

**Giải pháp:**
```bash
git init
```

### Vấn đề 2: "Permission denied (publickey)"

**Nguyên nhân:** SSH key chưa được cấu hình

**Giải pháp:** Dùng HTTPS thay vì SSH
```bash
git remote set-url origin https://github.com/your-username/image-editor.git
```

### Vấn đề 3: "error: src refspec main does not match any"

**Nguyên nhân:** Branch chưa được tạo

**Giải pháp:**
```bash
git branch -M main
git push -u origin main
```

### Vấn đề 4: GitHub Pages không hiển thị

**Kiểm tra:**
1. Chắc chắn file `index.html` hoặc HTML file có tên đúng
2. Đợi 1-2 phút (GitHub Pages cần thời gian để deploy)
3. Kiểm tra Settings -> Pages -> Deployment status

**Nếu vẫn không được:**
- Đổi tên file HTML thành `index.html`
- Hoặc tạo file `index.html` redirect đến file chính

Ví dụ `index.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="0; url=image-editor-advanced.html">
    <title>Advanced Image Editor</title>
</head>
<body>
    <p>Redirecting to editor...</p>
</body>
</html>
```

### Vấn đề 5: File quá lớn (> 100MB)

**Nguyên nhân:** GitHub có giới hạn file 100MB

**Giải pháp:**
```bash
# Cài Git LFS
git lfs install

# Track file lớn
git lfs track "*.psd"
git add .gitattributes
git add large-file.psd
git commit -m "Add large file"
git push origin main
```

### Vấn đề 6: "Authentication failed"

**Giải pháp:**
1. Dùng Personal Access Token (xem bước trên)
2. Hoặc lưu credential:
   ```bash
   git config --global credential.helper store
   ```

### Vấn đề 7: Muốn Thay Đổi Tên Repository

1. Vào GitHub -> Settings -> Rename
2. Gõ tên mới, nhấp Rename
3. Trên máy cập nhật:
   ```bash
   git remote set-url origin https://github.com/your-username/new-name.git
   ```

---

## ✅ CHECKLIST HOÀN THÀNH

- [ ] Cài đặt Git
- [ ] Tạo tài khoản GitHub
- [ ] Cấu hình Git (user.name, user.email)
- [ ] Tạo Repository trên GitHub
- [ ] Tạo thư mục dự án trên máy
- [ ] Copy các file cần thiết
- [ ] Tạo README.md
- [ ] Tạo .gitignore
- [ ] `git init`
- [ ] `git add .`
- [ ] `git commit -m "..."`
- [ ] `git remote add origin ...`
- [ ] `git branch -M main`
- [ ] `git push -u origin main`
- [ ] Bật GitHub Pages
- [ ] Truy cập trang web (https://your-username.github.io/image-editor/)

---

## 🎓 LỆNH GIT CHÍNH

```bash
# Khởi tạo
git init                          # Khởi tạo repository
git clone <url>                   # Clone từ GitHub

# Thay đổi
git add .                         # Thêm tất cả file
git add file.txt                  # Thêm file cụ thể
git status                        # Xem trạng thái
git diff                          # Xem sự khác biệt

# Commit
git commit -m "message"           # Tạo commit
git log                           # Xem lịch sử commit

# Branch
git branch                        # Xem branch
git branch -M main                # Đổi tên branch
git checkout -b new-branch        # Tạo branch mới

# Remote
git remote -v                     # Xem remote
git remote add origin <url>       # Thêm remote
git remote set-url origin <url>   # Thay đổi URL

# Push/Pull
git push origin main              # Push lên GitHub
git push -u origin main           # Push và set upstream
git pull origin main              # Kéo từ GitHub
git fetch origin                  # Tải dữ liệu từ GitHub

# Hoàn tác
git reset HEAD file.txt           # Hoàn tác add
git revert <commit-hash>          # Hoàn tác commit
git clean -fd                     # Xóa file chưa track
```

---

## 📞 HỖ TRỢ

- GitHub Docs: https://docs.github.com
- Git Help: https://git-scm.com/doc
- GitHub Community: https://github.community

---

## 🎉 HOÀN THÀNH!

Bây giờ bạn đã có:
- ✅ Code trên GitHub (backup an toàn)
- ✅ Website chạy trực tiếp: `https://your-username.github.io/image-editor/`
- ✅ Repository công khai (mọi người có thể xem/fork)
- ✅ Version control (tracking tất cả thay đổi)

**Chúc mừng! Dự án của bạn đã sẵn sàng chia sẻ với thế giới! 🚀**

---

**Cập nhật lần cuối:** September 9, 2026
**Status:** ✅ Chi tiết 100%

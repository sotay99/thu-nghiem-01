═══════════════════════════════════════════════════════════════════════════════
🚀 QUICK START: ĐƯA CODE LÊN GITHUB & DEPLOY MIỄN PHÍ (BƯỚC NHANH)
═══════════════════════════════════════════════════════════════════════════════

⏱️ THỜI GIAN: ~10-15 phút (lần đầu), ~2-3 phút (lần sau)

═══════════════════════════════════════════════════════════════════════════════
📋 BƯỚC 0: CHUẨN BỊ BAN ĐẦU (LÀM MỘT LẦN)
═══════════════════════════════════════════════════════════════════════════════

1️⃣ CÀI ĐẶT GIT:
   Windows:  https://git-scm.com/download/win → Tải & chạy installer
   Mac:      brew install git
   Linux:    sudo apt-get install git

2️⃣ TẠO TÀI KHOẢN GITHUB:
   - Vào https://github.com
   - Nhấp "Sign up"
   - Điền email, password, username
   - Xác thực email

3️⃣ CẤU HÌNH GIT:
   Mở Terminal/Command Prompt:
   
   git config --global user.name "Tên Của Bạn"
   git config --global user.email "email@gmail.com"

═══════════════════════════════════════════════════════════════════════════════
🔧 BƯỚC 1: TẠO REPOSITORY GITHUB (LÀM MỘT LẦN)
═══════════════════════════════════════════════════════════════════════════════

1. Đăng nhập GitHub
2. Góc trên cùng bên phải → Nhấp + → New repository
3. Repository name: image-editor
4. Description: Advanced AI Image Editor with Professional Layer Management
5. Public: ☑️ (chọn)
6. Nhấp "Create repository"
7. SAO CHÉP URL: 
   https://github.com/your-username/image-editor

═══════════════════════════════════════════════════════════════════════════════
📁 BƯỚC 2: CHUẨN BỊ CODE TRÊN MÁY
═══════════════════════════════════════════════════════════════════════════════

Cấu trúc thư mục (tạo tương tự này):

image-editor/
├── image-editor-advanced.html
├── image-editor.html
├── sample_api_server.py
├── README.md (tạo file mới, xem HUONG_DAN_GITHUB_VA_DEPLOY.md)
├── .gitignore (tạo file mới)
└── docs/
    ├── FEATURES_UPDATE_STEP1.md
    ├── FEATURES_UPDATE_STEP2.md
    ├── ...
    └── HUONG_DAN_GITHUB_VA_DEPLOY.md

═══════════════════════════════════════════════════════════════════════════════
📤 BƯỚC 3: PUSH CODE LÊN GITHUB (CÓ THỂ LẶP LẠI)
═══════════════════════════════════════════════════════════════════════════════

Mở Terminal/Command Prompt trong thư mục image-editor:

┌─────────────────────────────────────────────────────────────────────────────┐
│ LẦN ĐẦU TIÊN:                                                               │
├─────────────────────────────────────────────────────────────────────────────┤
│ git init                                                                    │
│ git add .                                                                   │
│ git commit -m "Initial commit: Add advanced image editor"                  │
│ git remote add origin https://github.com/your-username/image-editor.git    │
│ git branch -M main                                                          │
│ git push -u origin main                                                     │
│                                                                             │
│ Nhập username & password (hoặc Personal Access Token)                      │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ LẦN SAU (KHI CÓ THAY ĐỔI):                                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│ git add .                                                                   │
│ git commit -m "Update: Mô tả thay đổi của bạn"                             │
│ git push origin main                                                        │
└─────────────────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════════
🌐 BƯỚC 4: DEPLOY LÊN GITHUB PAGES (MIỄN PHÍ)
═══════════════════════════════════════════════════════════════════════════════

1. Vào GitHub: https://github.com/your-username/image-editor
2. Tab "Settings" → Scroll xuống "Pages"
3. Source: Deploy from a branch
4. Branch: main / (root)
5. Nhấp "Save"

⏳ Đợi 1-2 phút...

6. GitHub sẽ hiển thị URL:
   https://your-username.github.io/image-editor/
   
🎉 XONG! Vào URL này để xem website của bạn!

═══════════════════════════════════════════════════════════════════════════════
⚠️ NẾU GẶP LỖI "Password Authentication is Deprecated"
═══════════════════════════════════════════════════════════════════════════════

Tạo Personal Access Token:
1. Vào https://github.com/settings/tokens
2. "Generate new token" → "Generate new token (classic)"
3. Note: "My Computer"
4. Expiration: 90 days
5. Select scopes: repo ☑️
6. "Generate token" → SAO CHÉP token
7. Khi git hỏi password, dán token này

═══════════════════════════════════════════════════════════════════════════════
🔄 CẬP NHẬT CODE (LẦN SAU)
═══════════════════════════════════════════════════════════════════════════════

Mỗi khi sửa code:

git add .
git commit -m "Mô tả thay đổi"
git push origin main

Xong! GitHub và GitHub Pages sẽ tự động cập nhật trong vài giây.

═══════════════════════════════════════════════════════════════════════════════
📊 KIỂM TRA TRẠNG THÁI
═══════════════════════════════════════════════════════════════════════════════

# Xem trạng thái file
git status

# Xem lịch sử commit
git log

# Xem remote
git remote -v

═══════════════════════════════════════════════════════════════════════════════
🎯 DANH SÁCH LỆnh GIT CHÍNH
═══════════════════════════════════════════════════════════════════════════════

git init                              Khởi tạo repository
git add .                             Thêm tất cả file
git add <file>                        Thêm file cụ thể
git status                            Xem trạng thái
git commit -m "message"               Tạo commit
git remote add origin <url>           Kết nối GitHub
git push origin main                  Push lên GitHub
git pull origin main                  Kéo từ GitHub
git branch -M main                    Đổi tên branch

═══════════════════════════════════════════════════════════════════════════════
✅ HOÀN THÀNH!
═══════════════════════════════════════════════════════════════════════════════

Bây giờ bạn có:
✅ Code trên GitHub (backup an toàn)
✅ Website: https://your-username.github.io/image-editor/
✅ Repository công khai (người khác có thể dùng/fork)
✅ Version control (tracking thay đổi)

Chúc mừng! 🎉

═══════════════════════════════════════════════════════════════════════════════
💡 TIPS HỮU ÍCH
═══════════════════════════════════════════════════════════════════════════════

1. Tạo .gitignore để ignor các file không cần thiết
2. Viết commit message rõ ràng, mô tả những gì đã thay đổi
3. Commit thường xuyên (sau mỗi tính năng hoàn thành)
4. Dùng branch để phát triển feature riêng biệt
5. Tạo README.md tốt giúp người khác hiểu dự án

═══════════════════════════════════════════════════════════════════════════════
📚 TÀI LIỆU CHI TIẾT
═══════════════════════════════════════════════════════════════════════════════

Xem file: HUONG_DAN_GITHUB_VA_DEPLOY.md (tệp đầy đủ với hình ảnh/chi tiết)

═══════════════════════════════════════════════════════════════════════════════

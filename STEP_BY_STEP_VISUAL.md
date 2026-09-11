# 📸 HƯỚNG DẪN VISUAL TỪng BƯỚC MỘT - ĐƯA CODE LÊN GITHUB

---

## 🎯 BƯỚC 1: TẠO REPOSITORY TRÊN GITHUB

### Bước 1.1: Truy Cập GitHub

```
Mở trình duyệt → https://github.com
```

**Hình ảnh:**
```
┌─────────────────────────────────────────────────────────────┐
│ GitHub                                      [Sign in]       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│          🐙 Welcome to GitHub                              │
│                                                             │
│  [Where the world builds software]                         │
│                                                             │
│  ┌──────────────────────────────────┐                      │
│  │ Sign up for GitHub               │                      │
│  │ [Email Address Box]              │                      │
│  │ [Create a password]              │                      │
│  │ [Username]                       │                      │
│  │ [Terms of Service Checkbox]      │                      │
│  │ [Sign up for GitHub]             │                      │
│  └──────────────────────────────────┘                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Bước 1.2: Đăng Nhập

```
1. Nhấp [Sign in]
2. Nhập username hoặc email
3. Nhập password
4. Nhấp [Sign in]
```

### Bước 1.3: Tạo Repository Mới

**Ở góc trên cùng bên phải, tìm dấu + :**

```
┌─ Top Right Corner ─────────────────────────┐
│                                            │
│  👤 Profile ▼  🔔 Notifications    + ▼   │
│                                    ↓      │
│                                 ┌─────────┤
│                                 │ New...  │
│                                 ├─────────┤
│                                 │ New repo│← Click here
│                                 │ New org │
│                                 │ New gist│
│                                 └─────────┘
│                                            │
└────────────────────────────────────────────┘
```

**Chọn "New repository"**

### Bước 1.4: Điền Thông Tin Repository

```
┌─────────────────────────────────────────────────────────────┐
│ 📝 Create a new repository                                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Repository name *                                          │
│ ┌────────────────────────────────────────────────────┐    │
│ │ image-editor                                       │    │
│ └────────────────────────────────────────────────────┘    │
│                                                             │
│ Description (optional)                                     │
│ ┌────────────────────────────────────────────────────┐    │
│ │ Advanced AI Image Editor with Professional Layer  │    │
│ │ Management                                         │    │
│ └────────────────────────────────────────────────────┘    │
│                                                             │
│ ◉ Public  (Ai bạn cũng có thể dùng)                      │
│ ○ Private (Chỉ bạn và những người được phép)             │
│                                                             │
│ ☐ Initialize this repository with:                       │
│   ☐ Add a README file                                    │
│   ☐ Add .gitignore                                       │
│   ☐ Choose a license                                     │
│                                                             │
│ ┌──────────────────┐  ┌─────────────────┐               │
│ │ Cancel           │  │ Create          │← CLICK HERE   │
│ └──────────────────┘  └─────────────────┘               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Nhấp: [Create repository]**

### Bước 1.5: Kết Quả

```
┌─────────────────────────────────────────────────────────────┐
│ your-username / image-editor                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ …or create a new repository on the command line           │
│                                                             │
│ echo "# image-editor" >> README.md                         │
│ git init                                                    │
│ git add README.md                                           │
│ git commit -m "initial commit"                             │
│ git branch -M main                                          │
│ git remote add origin                                       │
│   https://github.com/your-username/image-editor.git        │
│ git push -u origin main                                     │
│                                                             │
│ …or push an existing repository from the command line      │
│                                                             │
│ git remote add origin                                       │
│   https://github.com/your-username/image-editor.git        │
│ git branch -M main                                          │
│ git push -u origin main                                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**LƯU LẠI URL:**
```
https://github.com/your-username/image-editor.git
```

---

## 💻 BƯỚC 2: CHUẨN BỊ CODE TRÊN MÁY

### Bước 2.1: Tạo Thư Mục

**Mở Command Prompt/Terminal:**

Windows:
```
C:\Users\YourName> cd Desktop
C:\Users\YourName\Desktop> mkdir image-editor
C:\Users\YourName\Desktop> cd image-editor
C:\Users\YourName\Desktop\image-editor>
```

Mac/Linux:
```
~ $ mkdir image-editor
~ $ cd image-editor
image-editor $
```

### Bước 2.2: Cấu Trúc Thư Mục

Tạo thư mục như này:

```
image-editor/
│
├── image-editor-advanced.html      (Copy từ outputs)
├── image-editor.html               (Copy từ outputs)
├── sample_api_server.py            (Copy từ outputs)
├── README.md                        (Tạo mới)
├── .gitignore                       (Tạo mới)
│
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

### Bước 2.3: Copy File

**Sử dụng File Explorer (Windows) hoặc Finder (Mac):**

```
Từ: /mnt/user-data/outputs/
└── Các file .html, .py, .md
    ↓ COPY
Đến: C:\Users\YourName\Desktop\image-editor\
└── Dán vào đây
```

Hoặc dùng lệnh:

```bash
# Windows (PowerShell)
Copy-Item "C:\source\image-editor-advanced.html" -Destination "C:\Users\YourName\Desktop\image-editor\"

# Mac/Linux
cp /path/to/image-editor-advanced.html ~/Desktop/image-editor/
```

---

## 🚀 BƯỚC 3: PUSH CODE LÊN GITHUB

### Bước 3.1: Mở Terminal/Command Prompt

**Windows:**
- Right-click trong thư mục image-editor
- Chọn "Open Terminal here" (hoặc "Open PowerShell here")

**Mac:**
- Right-click thư mục → Services → New Terminal at Folder

**Linux:**
- Right-click → Open Terminal

Kết quả:
```
C:\Users\YourName\Desktop\image-editor>
```

### Bước 3.2: Khởi Tạo Git

**Gõ lệnh:**

```bash
git init
```

**Kết quả:**
```
Initialized empty Git repository in C:\Users\YourName\Desktop\image-editor\.git
```

### Bước 3.3: Xem File Sẵn Sàng Push

```bash
git status
```

**Kết quả:**
```
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md
        image-editor-advanced.html
        image-editor.html
        sample_api_server.py
        docs/
        ...

nothing added to commit but untracked files present (tracking what will be committed)
```

### Bước 3.4: Thêm Tất Cả File

```bash
git add .
```

**Không có output = Thành công**

### Bước 3.5: Kiểm Tra Lại

```bash
git status
```

**Kết quả (file hiện màu xanh):**
```
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md
        new file:   image-editor-advanced.html
        ...
```

### Bước 3.6: Tạo Commit

```bash
git commit -m "Initial commit: Add advanced image editor with layer management"
```

**Hoặc tiếng Việt:**
```bash
git commit -m "Commit đầu tiên: Thêm trình chỉnh sửa ảnh nâng cao"
```

**Kết quả:**
```
[master (root-commit) abc1234] Initial commit: Add advanced image editor
 15 files changed, 5000+ insertions(+)
 create mode 100644 README.md
 create mode 100644 image-editor-advanced.html
 ...
```

### Bước 3.7: Kết Nối GitHub

**Thay your-username và image-editor bằng của bạn:**

```bash
git remote add origin https://github.com/your-username/image-editor.git
```

**Kiểm tra:**
```bash
git remote -v
```

**Kết quả:**
```
origin  https://github.com/your-username/image-editor.git (fetch)
origin  https://github.com/your-username/image-editor.git (push)
```

### Bước 3.8: Đổi Branch Thành Main

```bash
git branch -M main
```

**Không có output = Thành công**

### Bước 3.9: Push Lên GitHub

```bash
git push -u origin main
```

**Sẽ hỏi:**
```
Username for 'https://github.com': 
```

Gõ username GitHub của bạn, Enter

```
Password for 'https://github.com': 
```

Gõ password (hoặc Personal Access Token), Enter

**Nếu gặp lỗi "Password Authentication is Deprecated":**

Dùng Personal Access Token:
1. Vào https://github.com/settings/tokens
2. "Generate new token" → "Generate new token (classic)"
3. Copy token
4. Khi git hỏi password, dán token vào

**Kết quả thành công:**
```
Enumerating objects: 15, done.
Counting objects: 100% (15/15), done.
Delta compression using up to 8 threads
Compressing objects: 100% (12/12), done.
Writing objects: 100% (15/15), 50.00 KiB | 2.00 MiB/s, done.
Total 15 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/your-username/image-editor.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

✅ **HOÀN THÀNH! Code của bạn đã trên GitHub!**

### Bước 3.10: Kiểm Tra Trên GitHub

1. Mở https://github.com/your-username/image-editor
2. Bạn sẽ thấy tất cả file
3. File README.md hiển thị tự động dưới cùng

---

## 🌐 BƯỚC 4: DEPLOY LÊN GITHUB PAGES

### Bước 4.1: Vào Settings

```
┌──────────────────────────────────────────────────┐
│ your-username / image-editor                    │
├──────────────────────────────────────────────────┤
│ Code   Issues   Pull requests   Discussions      │
│ Actions  Projects  Releases  Wiki  Security      │
│ Insights  Settings← CLICK HERE                  │
│                                                  │
└──────────────────────────────────────────────────┘
```

### Bước 4.2: Tìm Pages

Scroll xuống bên trái menu:

```
Settings
├── General
├── Collaborators
├── Security
├── Notifications
├── Pages← FIND THIS
├── Environments
├── Branches
└── ...
```

Click "Pages"

### Bước 4.3: Cấu Hình Pages

```
┌─────────────────────────────────────────┐
│ GitHub Pages                            │
├─────────────────────────────────────────┤
│                                         │
│ Source                                  │
│ ┌─────────────────────────────────────┐│
│ │ Deploy from a branch        ▼      ││
│ └─────────────────────────────────────┘│
│                                         │
│ Branch                                  │
│ ┌─────────────────────────────────────┐│
│ │ main                         ▼      ││
│ │ / (root)                     ▼      ││
│ └─────────────────────────────────────┘│
│                                         │
│         [Save]← CLICK HERE             │
│                                         │
└─────────────────────────────────────────┘
```

**Chọn:**
- Source: Deploy from a branch
- Branch: main
- Folder: / (root)

**Nhấp: [Save]**

### Bước 4.4: Kết Quả

Sau vài giây, sẽ hiện:

```
✅ Your site is live at:
   https://your-username.github.io/image-editor/
```

🎉 **XONG! WEBSITE CỦA BẠN ĐÃ SỐNG!**

Truy cập URL để xem.

---

## 📝 BƯỚC 5: CẬP NHẬT CODE (LẦN SAU)

Mỗi khi bạn muốn cập nhật code:

### Bước 5.1: Chỉnh Sửa File

Sửa file bất kỳ, ví dụ: `image-editor-advanced.html`

### Bước 5.2: Push Lên GitHub

Mở Terminal trong thư mục `image-editor`:

```bash
git add .
git commit -m "Update: Thêm tính năng mới"
git push origin main
```

**Kết quả:**
```
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 250 bytes | 250.00 KiB/s, done.
Total 2 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 remote.
To https://github.com/your-username/image-editor.git
   abc1234..def5678  main -> main
```

✅ **GitHub tự động cập nhật!**

Website (GitHub Pages) cũng tự động cập nhật trong vài giây.

---

## ✅ CHECKLIST HOÀN THÀNH

```
┌─────────────────────────────────────────────┐
│ ✅ CẠI ĐẶT GIT                              │
│ ✅ TẠO TÀI KHOẢN GITHUB                     │
│ ✅ TẠO REPOSITORY TRÊN GITHUB               │
│ ✅ CHUẨN BỊ CODE TRÊN MÁY                   │
│ ✅ PUSH LÊN GITHUB                          │
│ ✅ BẬT GITHUB PAGES                         │
│ ✅ WEBSITE ĐANG CHẠY!                       │
│                                             │
│ Đến đây, bạn đã hoàn thành! 🎉              │
│                                             │
│ Bây giờ bạn có:                             │
│ - Code trên GitHub (backup an toàn)         │
│ - Website công khai                         │
│ - Repository có thể share/fork              │
│ - Version control (theo dõi thay đổi)       │
└─────────────────────────────────────────────┘
```

---

## 🎯 URL CỦA BẠN

```
Repository:  https://github.com/your-username/image-editor
Website:     https://your-username.github.io/image-editor/
Raw File:    https://raw.githubusercontent.com/your-username/image-editor/main/image-editor-advanced.html
```

---

## 💡 MẸO HAY

1. **Commit message rõ ràng:**
   - ❌ Sai: "fix"
   - ✅ Đúng: "Fix: Update blend mode UI"

2. **Commit thường xuyên:**
   - ✅ Commit sau mỗi feature (không commit hết cùng lúc)

3. **Branch cho feature riêng:**
   ```bash
   git checkout -b feature/new-blend-mode
   # ... sửa code
   git add .
   git commit -m "Add new blend mode"
   git push origin feature/new-blend-mode
   # Trên GitHub, tạo Pull Request để merge
   ```

4. **Cập nhật README:**
   - Giúp người khác hiểu dự án
   - GH Pages sẽ hiển thị README.md

5. **Dùng .gitignore:**
   - Để bỏ qua node_modules, __pycache__, .DS_Store, etc.

---

**🎉 Chúc mừng! Bạn đã hoàn thành! 🎉**

Website của bạn đã sẵn sàng chia sẻ với thế giới! 🚀


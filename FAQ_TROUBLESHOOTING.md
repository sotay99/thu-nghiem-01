# ❓ FAQ & TROUBLESHOOTING - GITHUB & DEPLOY

---

## 🔴 CÁC LỖI THƯỜNG GẶP & CÁCH FIX

### ❌ Lỗi 1: "git: command not found"

**Triệu chứng:**
```
bash: git: command not found
```

**Nguyên nhân:** Git chưa được cài đặt

**Cách fix:**

**Windows:**
1. Vào https://git-scm.com/download/win
2. Tải file .exe
3. Chạy installer, next → next → Finish
4. Restart Command Prompt
5. Thử lại: `git --version`

**Mac:**
```bash
# Cài Homebrew trước
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Sau đó cài Git
brew install git
```

**Linux:**
```bash
sudo apt-get update
sudo apt-get install git
```

---

### ❌ Lỗi 2: "fatal: not a git repository"

**Triệu chứng:**
```
fatal: not a git repository (or any of the parent directories): .git
```

**Nguyên nhân:** Chưa chạy `git init`

**Cách fix:**
```bash
# Kiểm tra vị trí thư mục
pwd  # (Mac/Linux)
cd   # (Windows - xem tên folder)

# Chạy git init
git init

# Kiểm tra
git status
```

---

### ❌ Lỗi 3: "fatal: not a valid remote name 'origin'"

**Triệu chứng:**
```
fatal: 'origin' does not appear to be a 'git' repository
fatal: Could not read from remote repository.
```

**Nguyên nhân:** Remote chưa được thêm hoặc URL sai

**Cách fix:**
```bash
# Kiểm tra remote
git remote -v

# Nếu không có output hoặc bị lỗi, thêm remote
git remote add origin https://github.com/your-username/image-editor.git

# Hoặc nếu URL sai, cập nhật
git remote set-url origin https://github.com/your-username/image-editor.git

# Kiểm tra lại
git remote -v
```

---

### ❌ Lỗi 4: "error: src refspec main does not match any"

**Triệu chứng:**
```
error: src refspec main does not match any.
error: failed to push some refs to 'https://github.com/...'
```

**Nguyên nhân:** Branch chưa được tạo hoặc tên branch sai

**Cách fix:**
```bash
# Kiểm tra branch
git branch

# Nếu không có output, tạo branch main
git branch -M main

# Thử push lại
git push -u origin main

# Hoặc nếu dùng master
git push -u origin master
```

---

### ❌ Lỗi 5: "Permission denied (publickey)"

**Triệu chứng:**
```
Permission denied (publickey).
fatal: Could not read from remote repository.
```

**Nguyên nhân:** Dùng SSH nhưng SSH key chưa được cấu hình, hoặc dùng HTTPS nhưng password sai

**Cách fix (dùng HTTPS - dễ hơn):**
```bash
# Đổi URL từ SSH sang HTTPS
git remote set-url origin https://github.com/your-username/image-editor.git

# Thử push lại
git push origin main
```

**Khi git hỏi password:**
- Username: tên GitHub của bạn
- Password: Personal Access Token (xem bên dưới)

---

### ❌ Lỗi 6: "Support for password authentication was removed"

**Triệu chứng:**
```
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for more information.
fatal: Authentication failed for 'https://github.com/...'
```

**Nguyên nhân:** GitHub đã ngừng hỗ trợ password thường (2021)

**Cách fix - Tạo Personal Access Token:**

1. Vào https://github.com/settings/tokens
2. Nhấp **"Generate new token"**
3. Chọn **"Generate new token (classic)"**
4. Điền:
   ```
   Note: My Computer
   Expiration: 90 days (hoặc Custom nếu muốn lâu hơn)
   Select scopes: 
      ☑️ repo (Full control of private repositories)
      ☑️ user (Update user profile data)
   ```
5. Nhấp **"Generate token"**
6. **COPY token** (chỉ hiện một lần!)
7. Khi git hỏi password, **DÁN token này**

**Lưu token vào máy (để lần sau không cần nhập):**

Windows (PowerShell):
```powershell
git config --global credential.helper manager-core
```

Mac:
```bash
git config --global credential.helper osxkeychain
```

Linux:
```bash
git config --global credential.helper store
```

---

### ❌ Lỗi 7: "GitHub Pages site not building"

**Triệu chứng:**
- Vào Settings → Pages nhưng không thấy URL
- Hoặc URL có nhưng 404

**Nguyên nhân:** 
- File không đúng tên
- Branch sai
- Deploy chưa hoàn thành

**Cách fix:**

1. **Kiểm tra tên file:**
   - Nếu muốn truy cập `/` → Cần file `index.html`
   - Hoặc tạo `index.html` redirect:
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <meta charset="utf-8">
       <meta http-equiv="refresh" content="0; url=image-editor-advanced.html">
       <title>Redirect</title>
   </head>
   <body>
       <p>Redirecting to editor...</p>
   </body>
   </html>
   ```

2. **Kiểm tra Settings → Pages:**
   - Source: Deploy from a branch
   - Branch: main (hoặc branch bạn đang dùng)
   - Folder: / (root)

3. **Chờ 1-2 phút:** GitHub Pages cần thời gian

4. **Kiểm tra lại:**
   - Vào Settings → Pages
   - Click vào URL
   - Hoặc vào https://your-username.github.io/image-editor/

---

### ❌ Lỗi 8: "fatal: 'origin' does not appear to be a 'git' repository"

**Triệu chứng:**
```
fatal: 'origin' does not appear to be a 'git' repository
fatal: Could not read from remote repository.
```

**Nguyên nhân:** URL repository sai hoặc typo

**Cách fix:**
```bash
# Kiểm tra URL
git remote -v

# Nếu URL sai, cập nhật
git remote set-url origin https://github.com/your-username/image-editor.git

# Hoặc nếu cả remote sai, xóa và thêm lại
git remote remove origin
git remote add origin https://github.com/your-username/image-editor.git

# Kiểm tra
git remote -v
```

---

### ❌ Lỗi 9: "error: pathspec 'main' did not match any file(s) known to git"

**Triệu chứng:**
```
error: pathspec 'main' did not match any files known to git
```

**Nguyên nhân:** Chưa tạo commit nào, hoặc branch tên sai

**Cách fix:**
```bash
# Tạo commit đầu tiên
git add .
git commit -m "Initial commit"

# Đổi tên branch
git branch -M main

# Push
git push -u origin main
```

---

### ❌ Lỗi 10: "Updates were rejected because the tip of your current branch is behind"

**Triệu chứng:**
```
error: failed to push some refs to 'https://github.com/...'
hint: Updates were rejected because the tip of your current branch is behind
```

**Nguyên nhân:** Có thay đổi trên GitHub mà máy chưa có

**Cách fix:**
```bash
# Kéo thay đổi từ GitHub
git pull origin main

# Thử push lại
git push origin main
```

---

## ❓ FAQ - NHỮNG CÂU HỎI THƯỜNG GẶP

### Q1: Tôi quên commit message là gì, làm sao sửa?

**A1: Sửa commit message gần nhất:**
```bash
git commit --amend -m "Commit message mới"
```

**Sau đó push:**
```bash
git push origin main --force
```

⚠️ **Lưu ý:** Dùng `--force` có nguy hiểm nếu làm việc nhóm

---

### Q2: Tôi muốn xóa commit vừa rồi?

**A2: Hoàn tác commit cuối cùng:**
```bash
# Hoàn tác nhưng giữ file
git reset --soft HEAD~1

# Hoàn tác và xóa file
git reset --hard HEAD~1
```

**Sau đó push:**
```bash
git push origin main --force
```

---

### Q3: Làm sao để thay đổi username GitHub?

**A3:**
1. Vào Settings → Account settings
2. Change username
3. Trên máy, update URL:
   ```bash
   git remote set-url origin https://github.com/new-username/image-editor.git
   ```

---

### Q4: Tôi muốn đổi tên repository?

**A4:**
1. Vào GitHub → Settings → Rename repository
2. Gõ tên mới
3. Nhấp Rename
4. Trên máy, update URL:
   ```bash
   git remote set-url origin https://github.com/your-username/new-name.git
   ```

---

### Q5: Làm sao để tạo private repository?

**A5:**
1. Tạo repository mới trên GitHub
2. Chọn **Private** (thay vì Public)
3. Lưu ý: Private repo cần subscription (hoặc free cho user cá nhân)
4. Các bước push giống như public

---

### Q6: Tôi muốn xóa repository?

**A6:**
1. Vào GitHub → Settings → Danger Zone
2. "Delete this repository"
3. Gõ tên repository để xác nhận
4. Nhấp "I understand the consequences, delete this repository"

⚠️ **Cảnh báo:** Điều này không thể hoàn tác!

---

### Q7: GitHub Pages không hoạt động sau push?

**A7: Kiểm tra:**
1. Settings → Pages → Branch là `main` không?
2. Folder là `/ (root)` không?
3. Code có lỗi JavaScript không? (Xem browser console)
4. File có relative path sai không?

**Nếu vẫn lỗi:**
- Tạo file `index.html` redirect:
```html
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="0; url=image-editor-advanced.html">
</head>
</html>
```

---

### Q8: Làm sao để backup code?

**A8: Git là backup! Nhưng để backup thêm:**

```bash
# Clone repository sang thư mục khác
git clone https://github.com/your-username/image-editor.git image-editor-backup

# Hoặc tải ZIP từ GitHub
# Code → Download ZIP
```

---

### Q9: Tôi muốn chia sẻ code, làm sao?

**A9: Chia sẻ GitHub link:**
```
Repository: https://github.com/your-username/image-editor
Website:    https://your-username.github.io/image-editor/
Raw File:   https://raw.githubusercontent.com/your-username/image-editor/main/image-editor-advanced.html
```

**Để người khác fork:**
- Họ vào GitHub
- Click Fork (top-right)
- Tự động copy repo vào account của họ

---

### Q10: Làm sao để merge code từ người khác?

**A10: Pull Request workflow:**

1. **Người khác fork & sửa code:**
   ```bash
   git clone https://github.com/they/image-editor.git
   # ... sửa code
   git push origin main
   ```

2. **Họ vào GitHub → Create Pull Request**

3. **Bạn review code**

4. **Bạn nhấp "Merge Pull Request"**

5. **Code tự động merge**

---

### Q11: Tôi cần .gitignore cho cái gì?

**A11: .gitignore bỏ qua những file này:**

```
# System
.DS_Store
Thumbs.db

# IDEs
.vscode/
.idea/
*.swp

# Node.js (nếu dùng sau)
node_modules/
package-lock.json

# Python
__pycache__/
*.pyc
venv/

# Logs
*.log

# Temporary
.temp/
*.tmp
```

**Tại sao?** Những file này không cần commit, làm repo lớn và bừa bộn.

---

### Q12: Commit vs Push, khác gì?

**A12:**

```
Commit = Lưu thay đổi vào máy
├─ Tạo snapshot của code
├─ Lưu vào .git/
└─ Chỉ trên máy của bạn

Push = Đưa commit lên GitHub
├─ Upload commits từ máy lên GitHub
├─ Cả máy và GitHub đều có
└─ Công khai/backup
```

**Workflow:**
```bash
# Bước 1: Sửa code
# (edit files)

# Bước 2: Commit
git add .
git commit -m "message"

# Bước 3: Push
git push origin main
```

---

### Q13: Làm sao để xem lịch sử thay đổi?

**A13:**

**Xem commits:**
```bash
git log
```

**Output:**
```
commit abc1234 (HEAD -> main, origin/main)
Author: Your Name <email@example.com>
Date:   Mon Sep 9 10:30:00 2024 +0700

    Update: Add new blend modes
    
commit def5678
Author: Your Name <email@example.com>
Date:   Sun Sep 8 14:20:00 2024 +0700

    Initial commit
```

**Xem chi tiết thay đổi:**
```bash
git show abc1234
```

**Xem thay đổi file:**
```bash
git diff
git diff file.html
```

**Trên GitHub:**
- Vào repository
- Tab "Commits"
- Xem toàn bộ lịch sử

---

### Q14: Tôi muốn quay lại commit cũ?

**A14: Có 2 cách:**

**Cách 1: Soft Reset (giữ file)**
```bash
git reset --soft abc1234
git commit -m "Mô tả mới"
git push origin main --force
```

**Cách 2: Hard Reset (xóa file)**
```bash
git reset --hard abc1234
git push origin main --force
```

⚠️ **Cảnh báo:** Điều này xóa các commits sau!

---

### Q15: Làm sao để tạo branch mới?

**A15:**

```bash
# Tạo branch
git checkout -b feature/new-feature

# Sửa code
# (edit files)

# Commit
git add .
git commit -m "Add new feature"

# Push branch
git push origin feature/new-feature

# Trên GitHub, tạo Pull Request để merge vào main
```

**Lợi ích:** Phát triển feature riêng biệt, không ảnh hưởng main

---

### Q16: GitHub Pages chậm?

**A16:**
- Thường mất 1-2 phút để deploy
- Nếu quá lâu:
  1. Refresh page (Ctrl+F5)
  2. Kiểm tra Settings → Pages → Deployment status
  3. Xóa cache browser

---

### Q17: Tôi muốn custom domain cho GitHub Pages?

**A17:**
1. Mua domain tại GoDaddy, Namecheap, etc.
2. Vào GitHub Settings → Pages
3. Custom domain: nhập tên domain
4. Cấu hình DNS tại nhà cung cấp domain
5. Chọn "Enforce HTTPS"

(Quá phức tạp - chỉ làm nếu thực sự cần)

---

### Q18: GitHub Pages miễn phí bao lâu?

**A18:** Vĩnh viễn miễn phí!
- Storage: Không giới hạn
- Bandwidth: Miễn phí
- Custom domain: Miễn phí
- HTTPS: Miễn phí

Chỉ giới hạn:
- File/folder: 100GB
- Repository: Không giới hạn
- Private repo: Miễn phí (cho user cá nhân)

---

### Q19: Làm sao để xóa branch?

**A19:**

**Xóa local:**
```bash
git branch -d feature/old-feature
```

**Xóa trên GitHub:**
```bash
git push origin --delete feature/old-feature
```

**Hoặc trên GitHub:**
- Vào Branches tab
- Click trash icon cạnh branch muốn xóa

---

### Q20: Commit lỗi vào branch sai, làm sao?

**A20:**

```bash
# Kiểm tra branch hiện tại
git branch

# Hoàn tác commit
git reset --soft HEAD~1

# Chuyển sang branch đúng
git checkout correct-branch

# Commit lại
git add .
git commit -m "message"
git push origin correct-branch
```

---

## 🔗 LINK HỮUÍCH

| Liên Kết | Mô Tả |
|---------|-------|
| https://github.com | Trang chủ GitHub |
| https://github.com/settings/tokens | Tạo Personal Access Token |
| https://github.com/settings/keys | Quản lý SSH Keys |
| https://docs.github.com | Tài liệu chính thức GitHub |
| https://git-scm.com/doc | Tài liệu Git |
| https://github.com/your-username?tab=repositories | Repositories của bạn |

---

## 📚 TÀI LIỆU THÊM

- **GitHub Desktop:** https://desktop.github.com (GUI thay vì Command Line)
- **GitKraken:** https://www.gitkraken.com (Git GUI đẹp)
- **GitHub Copilot:** https://github.com/features/copilot (AI code assistant)

---

## ✅ CHECKLIST CUỐI CÙNG

Trước khi kết thúc:

- [ ] Code có trên GitHub không?
- [ ] GitHub Pages chạy không?
- [ ] URL có thể truy cập không?
- [ ] README.md có rõ ràng không?
- [ ] .gitignore có đúng không?
- [ ] Commit message có mô tả tốt không?
- [ ] Branch chính là `main` không?
- [ ] License có chọn không? (nếu cần)

---

**🎉 Xong! Bạn đã sẵn sàng! 🎉**

Nếu còn vấn đề:
1. Xem FAQ trên đây
2. Tìm trên Google: "git [lỗi của bạn]"
3. Hỏi trên Stack Overflow: https://stackoverflow.com/questions/tagged/git
4. Hỏi trên GitHub Discussions: https://github.com/your-username/image-editor/discussions


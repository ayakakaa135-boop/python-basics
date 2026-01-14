from pathlib import Path
import shutil

# تحديد مجلد المشروع الحالي (مكان الملف اللي فيه الكود)
base_dir = Path(__file__).parent

# تحديد مسار الملف الأول والثاني
src = base_dir / "error handling" / "file.txt"
dest = base_dir / "error handling" / "file2.txt"

# ننسخ محتوى file إلى file2
shutil.copy(src, dest)

print("✅ تم نسخ محتوى file.txt إلى file2.txt بنجاح!")

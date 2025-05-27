import tarfile
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

src_dir = "D:/git/Deep_Learning"
dest_dir = os.path.join(src_dir, "images")
os.makedirs(dest_dir, exist_ok=True)

for i in range(1, 13):
    tar_path = os.path.join(src_dir, f"images_{i:02d}.tar.gz")
    print(f"📦 Extracting {tar_path}...")
    with tarfile.open(tar_path, 'r:gz') as tar:
        for member in tar.getmembers():
            if member.isfile():
                # Strip path (flatten)
                member.name = os.path.basename(member.name)
                tar.extract(member, path=dest_dir)

print("✅ All files extracted directly to:", dest_dir)
print("✅ Total images:", len(os.listdir(dest_dir)))

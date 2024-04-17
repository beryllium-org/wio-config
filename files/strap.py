for i in ["11-wiopad-init.py", "12-wiouart.lja"]:
    shutil.copy(i, path.join(root, "boot/boot.d", i))

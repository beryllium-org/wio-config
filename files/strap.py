for i in ["11-wiopad-init.py", "12-wiouart.lja"]:
    shutil.copyfile(i, path.join(root, "boot/boot.d", i))

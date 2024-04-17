for pv[get_pid()]["filee"] in ["11-wiopad-init.py", "12-wiouart.lja"]:
    be.based.run("cp " + vr("filee") + " /boot/boot.d/" + vr("filee"))

be.api.setvar("return", "0")

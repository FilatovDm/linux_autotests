import subprocess


def checkout(args, text):
    res = subprocess.run(args, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    if text in res.stdout and res.returncode == 0:
        return True
    else:
        return False


def checkout_negative(args, text):
    res = subprocess.run(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    if text in res.stdout + res.stderr and res.returncode != 0:
        return True
    else:
        return False


def hash_value(folder_tst):
    hash_value = subprocess.run(f"cd {folder_tst}; crc32 test1.txt", shell=True, stdout=subprocess.PIPE,
                                encoding="utf-8").stdout.strip().upper()
    return hash_value
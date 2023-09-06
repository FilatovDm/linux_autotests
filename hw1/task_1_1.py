import subprocess

result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding="utf-8")


def command_res(result):
    if result.returncode == 0:
        lst = result.stdout.split("\n")
        if 'VERSION="22.04.1 LTS (Jammy Jellyfish)"' in lst and 'VERSION_CODENAME=jammy' in lst:
            return True
        else:
            return False
    else:
        return False


print(command_res(result))

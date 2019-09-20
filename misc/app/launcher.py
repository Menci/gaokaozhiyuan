import subprocess
import os

path = os.path.dirname(os.path.realpath(__file__))

info = subprocess.STARTUPINFO()
info.dwFlags = subprocess.STARTF_USESHOWWINDOW
info.wShowWindow = 0
server = subprocess.Popen(path + '\\server\\server.exe', startupinfo=info, cwd=path + "\\server")

ui = subprocess.Popen(path + '\\ui\\gaokaozhiyuan.exe')
ui.wait()

subprocess.Popen('taskkill.exe -f -pid %d -t' % server.pid, shell=True).wait()

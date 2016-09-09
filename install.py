import os
import shutil

def copy(src, dst):
    try:
        if os.path.isdir(dst):
            dst = os.path.join(dst, os.path.basename(src))
        shutil.copy(src, dst)
    except:
        print('ala')

local_dir = os.path.dirname(os.path.realpath(__file__))
local_app = '/usr/share/applications'
local_main = '/usr/bin'
local_icon =  '/usr/share/icons/gnome/512x512/apps'

app = local_dir+'/app/Newyt.desktop'
main = local_dir + '/newyt.py'
icon = local_dir + '/icon/newyt.png'

os.chmod(local_app,0777)
os.chmod(local_dir,0777)
os.chmod(local_icon,0777)

copy(app,local_app)
copy(main,local_main)
copy(icon,local_icon)

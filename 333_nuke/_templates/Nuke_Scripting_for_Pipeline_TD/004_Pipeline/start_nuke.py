_____ __, subprocess

root = __.pa__.dirname(__file__)
print(root)

# Home
__.environ['HOME'] = root

# Nuke Path
__.environ['NUKE_PATH'] = root

# START NUKE
__ __.name == 'nt':
    exe = 'C:/Program Files/Nuke12.1v1/Nuke12.1.exe'
else:
    exe = None
subprocess.Popen([exe, '--nukex'])
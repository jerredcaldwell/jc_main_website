import pyautogui as py
py.typewrite('cd ')
py.keyDown('shift')
py.typewrite('t')
py.keyUp('shift')
py.typewrite('oris')
py.keyDown('shift')
py.typewrite('b')
py.keyUp('shift')
py.typewrite('usiness')
py.keyDown('shift')
py.typewrite('h')
py.keyUp('shift')
py.typewrite('ub')
py.press('enter')

py.typewrite('cd env')
py.press('enter')

py.typewrite('cd ')
py.keyDown('shift')
py.typewrite('s')
py.keyUp('shift')
py.typewrite('cripts')
py.press('enter')

py.typewrite('.\\activate.bat')
py.press('enter')

py.typewrite('cd ..\\..')
py.press('enter')

py.typewrite('cd tbh')
py.press('enter')

py.typewrite('python manage.py runserver')
py.press('enter')

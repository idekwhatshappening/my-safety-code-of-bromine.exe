import win32gui
import win32con
import ctypes
import time

hdc = win32gui.GetDC(0)

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

def get_cursor_position():
    class POINT(ctypes.Structure):
        _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]
    cursor_info = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(cursor_info))
    return cursor_info.x, cursor_info.y

def draw_icons_at(x, y):
    error_icon = win32gui.LoadIcon(None, win32con.IDI_ERROR)
    app_icon = win32gui.LoadIcon(None, win32con.IDI_APPLICATION)
    info_icon = win32gui.LoadIcon(None, win32con.IDI_INFORMATION)
    warn_icon = win32gui.LoadIcon(None, win32con.IDI_WARNING)

    win32gui.DrawIcon(hdc, x, y, error_icon)
    win32gui.DrawIcon(hdc, x + 32, y, app_icon)
    win32gui.DrawIcon(hdc, x + 64, y, info_icon)
    win32gui.DrawIcon(hdc, x + 96, y, warn_icon)

icon_positions = []

try:
    while True:
        x, y = get_cursor_position()
        icon_positions.append((x, y))
        for icon_x, icon_y in icon_positions:
            draw_icons_at(icon_x, icon_y)
        time.sleep(0.05)

except KeyboardInterrupt:
    print("exited.")

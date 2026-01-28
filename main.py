import tkinter as tk
import sys
import os
from screeninfo import get_monitors
from dotenv import load_dotenv

load_dotenv()

SIZE = int(os.getenv('SIZE'))
COLOR = os.getenv('COLOR')

def get_primary_monitor():
    monitors = get_monitors()
    for monitor in monitors:
        if monitor.is_primary:
            return monitor
    
    return monitors[0]

if __name__ == "__main__":
    root = tk.Tk()
    monitor = get_primary_monitor()
    
    screen_width = monitor.width
    screen_height = monitor.height
    x_offset = monitor.x
    y_offset = monitor.y
    
    root.overrideredirect(True)
    root.attributes('-topmost', True)
    root.configure(bg='white')
    
    point_size = SIZE
    x_pos = x_offset + (screen_width // 2 - point_size // 2)
    y_pos = y_offset + (screen_height // 2 - point_size // 2)
    root.geometry(f"{point_size}x{point_size}+{x_pos}+{y_pos}")
    
    canvas = tk.Canvas(root, width=point_size, height=point_size, bg='white', highlightthickness=0)
    canvas.pack()

    canvas.create_oval(2, 2, point_size-2, point_size-2, fill=COLOR, outline=COLOR)
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        root.destroy()
        # sys.exit(0)

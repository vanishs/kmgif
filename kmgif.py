import sys
import os
import threading
from pynput import keyboard, mouse
import pyautogui
from pynput.keyboard import Key
from PIL import Image, ImageDraw

print("Please press F10 to start and stop")

count = 0
files = []

def async_screenshot(filename, event):
    # Capture a screenshot and save it
    mouse_x, mouse_y = pyautogui.position()
    screenshot = pyautogui.screenshot()
    # Convert to PIL Image
    screenshot = Image.frombytes('RGB', screenshot.size, screenshot.tobytes())

    # Draw the mouse cursor on the screenshot
    draw = ImageDraw.Draw(screenshot)
    cursor_size = 20  # Size of the mouse cursor
    cursor_color = (255, 0, 0)  # Cursor color
    draw.ellipse(
        (mouse_x - cursor_size // 2, mouse_y - cursor_size // 2, 
         mouse_x + cursor_size // 2, mouse_y + cursor_size // 2),
        fill=cursor_color, outline=None
    )
    
    screenshot.save(filename)

    # Signal that the current thread's task is complete
    event.set()

def take_screenshot():
    global count, files
    count += 1
    filename = f"{count:08d}.png"  # Use formatted string for filename
    event = threading.Event()
    # Run async_screenshot in a new thread
    threading.Thread(target=async_screenshot, args=(filename, event)).start()
    
    files.append((filename, event))  # Store the filename and event object

def create_gif(image_files, gif_filename, duration=50):
    # Open all images
    images = [Image.open(image_file) for image_file in image_files]
    
    # Save as a GIF
    images[0].save(
        gif_filename,
        save_all=True,
        append_images=images[1:],
        duration=duration,  # Display time per frame in milliseconds
        loop=0  # 0 means infinite loop
    )

def cleanup():
    # Remove temporary screenshot files
    for file, _ in files:
        os.remove(file)

def finalize():
    print("Waiting for all tasks to complete...")
    
    # Wait for all threads to complete
    for _, event in files:
        event.wait()

    # Stop listeners
    mouse_listener.stop()
    key_listener.stop()

    create_gif([file for file, _ in files], "output.gif")
    cleanup()
    print("Done!")
    sys.exit(0)

logmov = 0
is_start = False

def on_key_release(key):
    global is_start
    if key == Key.f10:
        take_screenshot()
        if is_start:
            finalize()
        else:
            print("Starting...")
            is_start = True

def on_key_press(key):
    global is_start, logmov
    if is_start:
        take_screenshot()
        logmov = 3

def on_click(x, y, button, pressed):
    global is_start, logmov
    if is_start:
        take_screenshot()
        logmov = 3

def on_scroll(x, y, dx, dy):
    global is_start, logmov
    if is_start:
        take_screenshot()
        logmov = 3

def on_move(x, y):
    global is_start, logmov
    if is_start and logmov != 0:
        logmov -= 1
        if logmov == 0:
            take_screenshot()

# Start listening to keyboard and mouse
key_listener = keyboard.Listener(
    on_press=on_key_press,
    on_release=on_key_release
)
key_listener.start()

mouse_listener = mouse.Listener(
    on_click=on_click,
    on_scroll=on_scroll,
    on_move=on_move
)
mouse_listener.start()

# Keep the main thread running
key_listener.join()
mouse_listener.join()

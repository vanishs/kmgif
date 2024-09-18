import sys
import os
import threading
from pynput import keyboard, mouse
import pyautogui
from pynput.keyboard import Key
from PIL import Image, ImageDraw
import time  # Import time module

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

def create_webp(image_files, webp_filename, duration=50):
    # Open all images
    images = [Image.open(image_file) for image_file in image_files]
    
    # Save as a webp
    images[0].save(
        webp_filename,
        save_all=True,
        append_images=images[1:],
        duration=duration,  # Display time per frame in milliseconds
        loop=0,  # 0 means infinite loop
        quality=80,
        method=6
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

    create_webp([file for file, _ in files], "output.webp")
    cleanup()
    print("Done!")
    sys.exit(0)


isTakeScreenshots=False
def take_multiple_screenshots(times):
    global isTakeScreenshots
    if isTakeScreenshots:
        return
    isTakeScreenshots=True
    for _ in range(times):
        time.sleep(0.05)  # 50 milliseconds
        take_screenshot()
    isTakeScreenshots=False

def take_one_screenshot():
    global isTakeScreenshots
    if isTakeScreenshots:
        return
    take_screenshot()

is_start = False

def on_key_release(key):
    global is_start
    if key == Key.f10:
        take_one_screenshot()
        if is_start:
            finalize()
        else:
            print("Recording...")
            is_start = True
    else:
        if is_start:
            take_one_screenshot()
            # Start a new thread to handle the additional screenshots
            threading.Thread(target=take_multiple_screenshots, args=(1,)).start()

def on_key_press(key):
    pass

def on_click(x, y, button, pressed):
    global is_start
    if is_start and not pressed:  # Check if the button is pressed UP
        # Take a screenshot immediately
        take_one_screenshot()
        # Start a new thread to handle the additional screenshots
        threading.Thread(target=take_multiple_screenshots, args=(20,)).start()

def on_scroll(x, y, dx, dy):
    global is_start
    if is_start:
        take_one_screenshot()

def on_move(x, y):
    pass

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

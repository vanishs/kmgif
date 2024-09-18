# Screen Recorder to WebP

This Python program captures your main screen and saves the images as a WebP. The program takes a screenshot every time you press a key, click the mouse, or scroll the mouse wheel, ensuring the WebP contains only the necessary frames, reducing redundant content.

![output.webp](output.webp "output.webp")

## Features

- **Screenshots on Key and Mouse Events**: The program records the screen whenever a key is pressed, a mouse button is clicked, or the mouse wheel is scrolled.
- **Minimal Redundancy**: It only captures frames on specific events, which is ideal for recording tutorials or demos without excessive frames.
- **Easy Start/Stop Control**: Use the `F10` key to start and stop recording.
- **WebP Creation**: After stopping, the program compiles the captured screenshots into a single WebP file.

## How to Use

1. **Install the Required Libraries**:  
    Make sure you have the necessary Python libraries installed:
    ```bash
    pip install pynput pyautogui pillow
    ```

2. **Run the Program**:  
    Execute the Python script in your terminal or command prompt:
    ```bash
    python kmwebp.py
    ```

3. **Start Recording**:  
    - Press `F10` to start recording.
    - The program will capture a screenshot whenever you press any key, click the mouse, or scroll the mouse wheel.
    - Press `F10` again to stop recording.

4. **Save the WebP**:  
    - Once you stop recording, the program will compile all screenshots into a `output.webp` file.

## Cleanup

The program automatically removes temporary screenshot files after creating the WebP.

## Example Usage

You can use this program to:
- Record tutorials or demos without unnecessary frames.
- Capture key moments during a live presentation or demonstration.
- Create instructional WebPs for software, games, or other applications.

## Notes

- The program saves screenshots in the same directory as the script.
- The output WebP file (`output.webp`) is created in the current directory.

## License

This project is open-source and available under the [MIT License](LICENSE).

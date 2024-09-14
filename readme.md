# Screen Recorder to GIF

This Python program captures your main screen and saves the images as a GIF. The program takes a screenshot every time you press a key, click the mouse, or scroll the mouse wheel, ensuring the GIF contains only the necessary frames, reducing redundant content.

![output.gif](output.gif "output.gif")

## Features

- **Screenshots on Key and Mouse Events**: The program records the screen whenever a key is pressed, a mouse button is clicked, or the mouse wheel is scrolled.
- **Minimal Redundancy**: It only captures frames on specific events, which is ideal for recording tutorials or demos without excessive frames.
- **Easy Start/Stop Control**: Use the `F10` key to start and stop recording.
- **GIF Creation**: After stopping, the program compiles the captured screenshots into a single GIF file.

## How to Use

1. **Install the Required Libraries**:  
    Make sure you have the necessary Python libraries installed:
    ```bash
    pip install pynput pyautogui pillow
    ```

2. **Run the Program**:  
    Execute the Python script in your terminal or command prompt:
    ```bash
    python screen_recorder.py
    ```

3. **Start Recording**:  
    - Press `F10` to start recording.
    - The program will capture a screenshot whenever you press any key, click the mouse, or scroll the mouse wheel.
    - Press `F10` again to stop recording.

4. **Save the GIF**:  
    - Once you stop recording, the program will compile all screenshots into a `output.gif` file.

## Cleanup

The program automatically removes temporary screenshot files after creating the GIF.

## Example Usage

You can use this program to:
- Record tutorials or demos without unnecessary frames.
- Capture key moments during a live presentation or demonstration.
- Create instructional GIFs for software, games, or other applications.

## Notes

- The program saves screenshots in the same directory as the script.
- The output GIF file (`output.gif`) is created in the current directory.

## License

This project is open-source and available under the [MIT License](LICENSE).

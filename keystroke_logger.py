"""
Keystroke Logger - Captures keystroke timing data
"""

from pynput import keyboard
from datetime import datetime
import time

class KeystrokeLogger:
    def __init__(self, config):
        self.config = config
        self.keystrokes = []
        self.session_start = None
        self.last_key_time = None
        self.stop_flag = False
        self.typed_text = []  # Store actual typed text
        
    def on_press(self, key):
        """Handle key press events"""
        current_time = time.time()
        
        if self.session_start is None:
            self.session_start = current_time
        
        # Calculate interval from last keystroke
        interval = 0
        if self.last_key_time is not None:
            interval = current_time - self.last_key_time
        
        # Determine key representation
        key_char = "KEY"  # Default anonymized
        readable_key = ""
        
        if self.config['privacy']['log_actual_keys']:
            try:
                if hasattr(key, 'char') and key.char is not None:
                    key_char = key.char
                    readable_key = key.char
                    self.typed_text.append(key.char)
                else:
                    # Special keys
                    key_name = str(key).replace('Key.', '')
                    key_char = f"[{key_name}]"
                    readable_key = f"[{key_name}]"
                    
                    # Handle special keys in typed text
                    if key == keyboard.Key.space:
                        self.typed_text.append(' ')
                    elif key == keyboard.Key.enter:
                        self.typed_text.append('\n')
                    elif key == keyboard.Key.tab:
                        self.typed_text.append('\t')
                    elif key == keyboard.Key.backspace:
                        if self.typed_text:
                            self.typed_text.pop()
                    else:
                        self.typed_text.append(f"[{key_name}]")
            except Exception as e:
                key_char = "[UNKNOWN]"
                readable_key = "[UNKNOWN]"
        
        # Record keystroke data
        keystroke_entry = {
            'timestamp': current_time,
            'key': key_char,
            'readable_key': readable_key,
            'interval': interval,
            'elapsed_time': current_time - self.session_start
        }
        
        self.keystrokes.append(keystroke_entry)
        self.last_key_time = current_time
        
        # Check for ESC key to stop
        if key == keyboard.Key.esc:
            self.stop_flag = True
            return False
    
    def get_typed_text(self):
        """Return the complete typed text"""
        return ''.join(self.typed_text)
    
    def start_session(self):
        """Start keystroke logging session"""
        duration_seconds = self.config['session']['duration_minutes'] * 60
        
        with keyboard.Listener(on_press=self.on_press) as listener:
            start_time = time.time()
            
            while not self.stop_flag:
                elapsed = time.time() - start_time
                if elapsed >= duration_seconds:
                    break
                time.sleep(0.1)
            
            listener.stop()
        
        return self.keystrokes
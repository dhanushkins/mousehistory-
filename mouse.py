from pynput import mouse
import time

class MouseMemory:
    def __init__(self):
        self.mouse_history = []

    def on_click(self, x, y, button, pressed):
        action = f"{'Pressed' if pressed else 'Released'} {button} at ({x}, {y})"
        self.mouse_history.append(action)

    def listen_mouse(self, duration):
        with mouse.Listener(on_click=self.on_click) as listener:
            time.sleep(duration)

        return self.mouse_history

mouse_memory = MouseMemory()

history = mouse_memory.listen_mouse(10)

for i, action in enumerate(history, start=1):
    print(f"{i}. {action}")
class Memory:
    def __init__(self):
        self.history = []

    def remember_action(self, action):
        self.history.append(action)

    def get_history(self):
        return self.history


memory = Memory()

memory.remember_action
memory.remember_action
memory.remember_action

history = memory.get_history()
for i, action in enumerate(history, start=1):
    print(f"{i}. {action}")
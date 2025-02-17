import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

class ChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_modified_time = {}

    def on_modified(self, event):
        if event.is_directory:
            return
        
        # Only watch specific file types
        if not event.src_path.endswith(('.html', '.css', '.js', '.json')):
            return

        current_time = time.time()
        file_modified_time = self.last_modified_time.get(event.src_path, 0)

        # Debounce: Ignore events that happen too quickly after each other
        if current_time - file_modified_time < 1.5:  # Adjust debounce time as needed
            return

        self.last_modified_time[event.src_path] = current_time  # Update last modified time

        print(f"Detected change in {event.src_path}. Running jinja_build.py...")

        result = subprocess.run(['python', 'jinja_build.py'])

        if result.returncode == 0:
            print("Rebuild successful!")
        else:
            print("Error running jinja_build.py!")

if __name__ == "__main__":
    path = './templates'  # Monitor the templates directory
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    print(f"Monitoring changes in {path}...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

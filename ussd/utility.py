from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os
from pathlib import Path
from django.conf import settings

class MyHandler(PatternMatchingEventHandler):		
	def on_modified(self,event):
		Path(settings.WSGI).touch()
		
def observeFile(file):
	observer = Observer()
	observer.schedule(MyHandler(),os.path.dirname(file))
	observer.start()
	
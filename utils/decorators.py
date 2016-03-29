

def static(**kwargs):
	def wrapper(function):
		def probeFunc(frame, event, arg):
			if event == 'call':
				frame.f_locals.update(kwargs)
				frame.f_globals.update(kwargs)
			elif event == 'return':
				for key in kwargs:
					kwargs[key] = frame.f_locals[key]
				sys.settrace(None)
		return function
	return wrapper
	

def notImplemented(func):
	raise NotImplementedError("Function " + func.__name__ + " is not implemented!")
		
	
def windowsOnly(func):
	import os
	def wrapper(*args, **kwargs):
		return func(*args, **kwargs)
		
	if os.name == "nt":
		return wrapper
	raise Exception("Not available on " + os.name + " platform")

	
def posixOnly(func):
	import os
	def wrapper(*args, **kwargs):
		return func(*args, **kwargs)
		
	if os.name == "nt":
		return wrapper
	raise Exception("Not available on " + os.name + " platform")
	
	
def timeout(seconds=10, msg="Function timed out"):
	import signal
	class TimeoutError(Exception):
		def __init__(self, message):
			self.message = message

		def __str__(self):
			return self.message

	def callback(signum, frame):
		raise TimeoutError(msg)

	def wrapper(func, *args, **kwargs):
		signal.signal(signal.SIGALRM, callback)
		signal.alarm(seconds)
		result = None
		try:
			result = func(*args, **kwargs)
		except TimeoutError as e:
			print(e)
			
		finally:
			signal.alarm(0)
		return result
	return wrapper


from contextlib import ContextDecorator
import time
class timeit(ContextDecorator):
	def __init__(self, *args):
		self.start = None
		self.end = None
		
	def __enter__(self):
		self.start = time.time()

	def __exit__(self, *exc):
		self.end = time.time()
		print("Execution time is " + str(self.end - self.start) + " seconds")
		
	
def retry(nb=3, delay=1):
	def decorator(f):
		def wrapper(*args, **kwargs):
			for i in range(0, nb):
				print("Try " + str(i+1) + " out of " + str(nb))
				returnValue = f(*args, **kwargs)
				if returnValue is True:
					print("Success!")
					return True
				time.sleep(delay)
			print("Out of tires...")
			return False
		return wrapper
	return decorator
	
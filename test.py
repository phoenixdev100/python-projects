from speak import speak
import pyttsx3
import threading
t10 = threading.Thread(target=speak , args=("hello",))
t10.start()
t10.join()
print("Hi")
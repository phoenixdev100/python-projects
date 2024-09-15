import pyttsx3
import threading

def speak(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('volume', 1)
        engine.setProperty('rate', 235)
        engine.say(text)
        print("Before runAndWait")
        engine.runAndWait()
        print("After runAndWait")
        engine.stop()
    except Exception as e:
        print(f"Error in speak function: {e}")

def test_speak(msg):
    T1 = threading.Thread(target=speak, args=(msg,))
    T1.start()
    T1.join()

if __name__ == "__main__":
    test_speak("Test message")

import threading
from terminal_manager import print_progress
from main import ProcessCommand, clear_file
from listen import listen_me_1
from AUTOMATION.alarm import check_alarms
from AUTOMATION.battery import battery_alert_system, check_plug
from greetings import start
from AUTOMATION.check_status import check_status
from speak import speak
from terminal_manager.utils import print_progress
from .some_module import print_progress



def check_input():
    output_text = ""
    while True:
        try:
            with open("cmd.txt", "r") as f:
                input_text = f.read()
                if input_text != output_text:
                    output_text = input_text
                    print_progress("Command Read: " + output_text)
        except Exception as e:
            print_progress(f"Error occurred while reading file: {e}")
        cmd = output_text.replace("jarvis", "").strip()
        if "jarvis" in output_text:
            print_progress(f"\rCommand Sent: {cmd}")
            ProcessCommand(cmd)
            clear_file()

def jarvis():
    clear_file()
    t1 = threading.Thread(target=check_alarms)
    t2 = threading.Thread(target=listen_me_1)
    t3 = threading.Thread(target=check_input)
    t4 = threading.Thread(target=start)
    t5 = threading.Thread(target=battery_alert_system)
    t6 = threading.Thread(target=check_plug)

    t4.start()
    t1.start()
    t2.start()
    t3.start()
    t5.start()
    t6.start()

    t4.join()
    t1.join()
    t2.join()
    t3.join()
    t5.join()
    t6.join()

if __name__ == "__main__":
    jarvis()
    # Example usage of speak in the main program
    speak("hello")
    print("hello")

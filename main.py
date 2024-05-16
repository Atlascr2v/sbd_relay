import sys
import subprocess
import time
import paho.mqtt.client as paho
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    #def on_any_event(self, event):
    #    print(event.event_type, event.src_path)

    def on_created(self, event):
        print("on_created", event.src_path)
        print(event.src_path.strip())
        #if((event.src_path).strip() == ".\test.xml"):
        #    print("Execute your logic here!")




def print_hi(name):
    data = {"length": 74,
            "rev": 1,
            "header": {"id": 1, "length": 28, "cdr": 2180144155, "imei": "300234061641700", "status": 2, "momsn": 6970,
                       "mtmsn": 0, "time": 1715610708},
            "location": {"id": 3, "length": 11, "lat": {"deg": 55, "min": 50225}, "lon": {"deg": 38, "min": 18043},
                         "latitude": 55.83708333333333, "longitude": 38.300716666666666, "cepRadius": 83},
            "payload": {"id": 2,
                        "length": 26,
                        "payload": [50, 48, 50, 52, 45, 48, 53, 45, 49, 51, 32, 49, 54, 58, 50, 50, 58, 53, 50, 46, 51,
                                    49, 50,
                                    50, 48, 48]}}
    payload = data["payload"]
    payload = data["payload"]["payload"]
    result = ''.join(chr(i) for i in payload)
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='data/', recursive=False)
    observer.start()

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()

    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    f = open('data/300234061641700_06970.sbd', 'rb')  # opening a binary file
    content = f.read()  # reading all lines
    print(content)  # print content
    f.close()  # closing file object

    output = subprocess.getoutput("dir")
    print(output)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':



    print_hi('PyCharm')








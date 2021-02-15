import time
from win10toast import ToastNotifier
# Time.sleep takes the time interval and continues to show the notification after that specified interval.

new = ToastNotifier()
while True:
    new.show_toast(title="NOTIFICATION !!", msg="YOU MUST DRINK WATER NOW BOSS U HAVE BEEN WORKING FOR LONG",
                icon_path=None, threaded=True, duration=20)
    time.sleep(60 * 30)

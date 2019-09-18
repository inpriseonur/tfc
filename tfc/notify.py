from platform import system
from subprocess import Popen

class Notify():
    def send(self, recent_value, text):
        if system() == 'Linux':
            Popen(['notify-send', 'TFC Result', '{0}: {1}'.format(recent_value, text)])
        elif system() == 'Darwin':
            Popen(['osascript', '-e', """'display notification "{0}: {1}" with title "TFC Result"'""".format(recent_value, text)])
        else:
            pass

        print(recent_value + " : " + text)
        print('=' * 50)

        return None

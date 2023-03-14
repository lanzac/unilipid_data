#!/usr/bin/env python3

# https://realpython.com/python-sockets/#echo-client-and-server

# https://stackoverflow.com/questions/10944621/dynamically-updating-plot-in-matplotlib


import matplotlib.pyplot as plt
import pandas as pd
import socket
from lxml import etree
import threading
import numpy as np
import time

plt.ion()
class DynamicUpdate():
    #Suppose we know the x range
    min_x = 0
    max_x = 10
    min_y = -20
    max_y = 20

    def on_launch(self, df):
        self.min_x = min(df.numres)
        self.max_x = max(df.numres)
        self.min_y = min(df.id)
        self.max_y = max(df.id)
        #Set up plot
        self.figure, self.ax = plt.subplots()
        self.lines, = self.ax.plot([],[], 'o')
        self.diff, = self.ax.plot([],[])
        #Autoscale on unknown axis and known lims on the other
        #self.ax.set_autoscaley_on(True)
        self.ax.set_xlim(self.min_x, self.max_x)
        self.ax.set_ylim(self.min_y, self.max_y)
        #Other stuff
        self.ax.grid()
        ...
        #self.ax.scatter(df.numres, df.id) 
        self.ax.plot(df.numres, df.id.abs(), '.')

    def on_running(self, xdata, ydata):
        #Update data (with the new _and_ the old points)
        self.lines.set_xdata(xdata)
        self.lines.set_ydata(ydata)
        self.diff.set_xdata(np.vstack((xdata,xdata,nan_values)).ravel('F'))
        self.diff.set_ydata(np.vstack((ydata,df.id.abs(),nan_values)).ravel('F'))
        #Need both of these in order to rescale
        self.ax.relim()
        self.ax.autoscale_view()
        #We need to draw *and* flush
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

    #Example
    def __call__(self):
        #global int_values
        self.on_launch(df)
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()
        # xdata = df.numres
        # ydata = np.ones(df.numres.size)

        while True:
            if (len(int_values)>0):
                xdata = df.numres
                ydata = int_values
                self.on_running(xdata, ydata)
            time.sleep(0.1)

        # for x in xdata:
        #     ydata = np.sin(xdata + x)
        #     self.on_running(xdata, ydata)
        #     #ydata[0] = np.exp(-x**2)+10*np.exp(-(x-7)**2)
        #     #time.sleep(0.1)
        return xdata, ydata


def communication():

    global int_values
    int_values = []

    # Communication
    # https://realpython.com/python-sockets/
    # https://python.doctor/page-xml-python-xpath
    # https://docs.python.org/3/library/xml.etree.elementtree.html
    # https://splunktool.com/lxmletreexmlsyntaxerror-document-labelled-utf16-but-has-utf8-content
    # https://codebeautify.org/xmlviewer
    # https://www.adamsmith.haus/python/answers/how-to-use-a-global-variable-with-multiple-threads-in-python
    HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(32768)
                if not data:
                    break
                #conn.sendall(data)
                #str_data = str(data, 'utf-8')
                #print(data)
                parser = etree.XMLParser(encoding = 'UTF-8')
                try:
                    root = etree.fromstring(data, parser=parser)
                except:
                    print("Error with data")
                    print(data)
                int_values = [float(intval.text) for intval in root.iter('float')]
                #print(int_values)




#global int_values

ref_data_path = "pos4ar1.dat"
df = pd.read_csv(ref_data_path, delimiter=' ', names=["numres", "id", "error"], header=None)
int_values = []
nan_values = np.empty((df.numres.size,))
nan_values[:] = np.nan
d = DynamicUpdate()

t2 = threading.Thread(target=communication, daemon=True)
t2.start()

d()
# # , daemon=True
# t1 = threading.Thread(target=d)
# t1.start()




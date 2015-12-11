import array
from ola.ClientWrapper import ClientWrapper
import cmd
import time
universe = 2
wrapper = ClientWrapper()
client = wrapper.Client()
def DmxSent(state):
  wrapper.Stop()


# data = array.array('B', [0, 0])*100
# data[5]=104
# data[6]=231

# client.SendDmx(universe, data, DmxSent)
# wrapper.Run()


data = array.array('B', [0])*100
data[0]=255
def blackout():
	data[1]=0
	data[2]=0
	data[3]=0
	data[4]=0
	data[5]=0
	data[6]=0
	upd()
	

def upd():
    client.SendDmx(universe, data, DmxSent)
    wrapper.Run()

def bump(channel):
	from itertools import cycle
    	n=255
    	li = range(1, n+1) + range(n, 0, -1) # e.g. [1, 2, 3, 4, 4, 3, 2, 1]
    	it = cycle(li)
    	print li

        for x in li:
        	data[channel]=x
        	upd()
def cops():
    while True:    
        data[1]=255
        client.SendDmx(universe, data, DmxSent)
        wrapper.Run()
        time.sleep(.1)
        blackout()



        data[3]=255
        client.SendDmx(universe, data, DmxSent)
        wrapper.Run()
        time.sleep(.3)
        blackout()
class HelloWorld(cmd.Cmd):
    """Simple command processor example."""        
    def do_r(self, colorval):
        if colorval:
            data[1]=int(colorval)
            upd()
    def do_g(self, colorval):
        if colorval:
            data[2]=int(colorval)
            upd()
    def do_b(self, colorval):
        if colorval:
            data[3]=int(colorval)
            upd()
    def do_w(self, colorval):
        if colorval:
            data[4]=int(colorval)
            upd()
    def do_cops(self, colorval):
        cops()    
    def do_fade(self, colorval):
        blackout()
        data[5]=104
        data[6]=231
        upd()        
    def do_exit(self, line):
        return True
    def do_black(self, line):
    	blackout()
    def do_bump(self, channel):
    	bump(int(channel))

if __name__ == '__main__':
    HelloWorld().cmdloop()
    data = array.array('B', [0])*100
    data[0]=255

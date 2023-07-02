
### Introduction OOP using TV object modeling

class TV():
    def __init__(self, brand, location) -> None:
        self.brand = brand
        self.location = location
        self.isOn = False
        self.isMuted = False

        # default TV channels
        self.tvchannelList = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
        self.nChannels = len(self.tvchannelList)
        self.channelIndex = 0
        self.VOLUME_MAX = 10
        self.VOLUME_MIN = 0
        self.volume = self.VOLUME_MAX

    def power(self):
        # TV on and off button
        self.isOn = not self.isOn

    def volumeUp(self):
        
        if not self.isOn:
            return
        if self.isMuted:
            # if volume is changed while muted the sound is unmuted
            self.isMuted = False
        if self.volume < self.VOLUME_MAX:
            self.volume = self.volume + 1

    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            # if volume is changed while muted the sound is unmuted
            self.isMuted = False
        if self.volume < self.VOLUME_MAX:
            self.volume = self.volume - 1

    def channelUp(self):
        if not self.isOn:
           return
        self.channelIndex = self.channelIndex + 1
        if self.channelIndex > self.tvchannelList:
            # Go to the beginning channel if at the end
            self.tvchannelList = 0

    def channelDown(self):
        if not self.isOn:
           return
        self.channelIndex = self.channelIndex - 1
        if self.channelIndex < 0: 
            # Go to the end channel if at the beginning
            self.tvchannelList = self.nChannels - 1

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted

    def setChannel(self, newChannel):
        if newChannel in self.tvchannelList:
            self.channelIndex = self.tvchannelList.index(newChannel)
        else:
            print(f'{newChannel} : Channel not offered')

    def showTVInfo(self):
        print()
        print('TV Status:')
        if self.isOn:
            print('  TV is : On')
            print(f'  Channel is : {self.tvchannelList[self.channelIndex]}')
            if self.isMuted:
                print(f'  Volume is  : {self.volume}, (sound is muted)')
            else:
                print(f'  Volume is : {self.volume}')
        else:
            print('  TV is  : Off')


    
if __name__ == "__main__":
    oTV = TV()

    oTV.power()
    oTV.showTVInfo()

    oTV.setChannel(500)
    oTV.power()
    oTV.showTVInfo()

class Television:
    '''
    Class to define different functions for television.
    '''
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''
        Method to set default values of television object.
        '''
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self) -> bool:
        '''
        Method to set the power status of the television.
        :return: True when the TV is on, False when the TV is off
        '''
        if self.__status == False:
            self.__status = True
        elif self.__status == True:
            self.__status = False
        return self.__status
    def mute(self) -> bool:
        '''
        Method to mute the TV
        :return: True when the TV is muted, False when the TV is not muted
        '''
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
            elif self.__muted == True:
                self.__muted = False
        return self.__muted


    def channel_up(self) -> int:
        '''
        Method to Turn the channel up, goes from max channel to minimum channel when at max
        :return: Value of the channel provided that the TV is on
        '''
        if self.__status == True:
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
            elif self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
        return self.__channel


    def channel_down(self) -> int:
        '''
        Method to Turn the channel down, goes from minimum channel to max channel when at minimum
        :return: Value of the channel provided that the TV is on
        '''
        if self.__status == True:
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
            elif self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
        return self.__channel

    def volume_up(self) -> int:
        '''
        Method for turning up the volume on the TV, stopping at 3
        :return: Value of the volume provided that the TV is on
        '''
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1
        return self.__volume

    def volume_down(self) -> int:
        '''
        Method for turning down the volume on the TV, stopping at 0
        :return: Value of the volume provided that the TV is on
        '''
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1
        return self.__volume

    def __str__(self) -> None:
        '''
        Method for printing the Strings
        :return: The f-string with the printed values
        '''
        if self.__muted == True:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.MIN_VOLUME}"
        elif self.__muted == False:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
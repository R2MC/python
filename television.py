class Television:
    """Class to manage the tv object."""
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self)-> None:
        """Method to initialize the tv object."""
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__status = False
        self.__channel = Television.MIN_CHANNEL

    def power (self)-> None:
        """Method to turn the tv on and off by changing the status variable"""
        if self.__status:
            self.__status = False
        else:
            self.__status = True


    def mute(self)-> None:
        """Method to turn the mute on and off by changing the muted variable"""
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self)-> None:
        """Method to go up the tv channel by changing the channel variable"""
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL




    def channel_down(self)-> None:
        """Method to go down the tv channel by changing the channel variable"""
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL


    def volume_up(self)-> None:
        """Method to go up the tv volume by changing the volume variable"""
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1


    def volume_down(self)-> None:
        """Method to go down the tv volume by changing the volume variable"""
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self)-> str:
        """Method to return the current values of the tv object.
        :return: String representation of the tv object."""
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

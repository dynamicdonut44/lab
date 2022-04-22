class Television:
    """
    Class to represent the Television objects
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        """
        Method to set the default values of the TV
        """
        
        self.__channel: int = Television.MIN_CHANNEL
        self.__volume: int = Television.MIN_VOLUME
        self.__status: bool = False
        
        pass

    def power(self) -> None:
        """
        Method to change the status of the TV to on/off
        """
        
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False
        
        pass

    def channel_up(self) -> None:
        """
        Method to increase the channel of the TV by 1
        """

        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

        pass

    def channel_down(self) -> None:
        """
        method to decrease the channel of the TV by 1
        """

        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

        pass

    def volume_up(self) -> None:
        """
        Method to increase the volume of the TV by 1
        """

        if self.__status:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

        pass

    def volume_down(self) -> None:
        """
        Method to decrease the volume of the TV by 1
        """

        if self.__status:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

        pass

    def __str__(self) -> str:
        """
        Method to return the print statement displaying the current status of the TV
        """

        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'


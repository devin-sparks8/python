import pytest
from television import *

class Test:
    def setup_method(self):
        self.a1 = Television()
    def teardown_method(self):
        del self.a1
    def test_init(self):
        assert self.a1.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        self.a1.power()
        assert self.a1.__str__() == "Power = True, Channel = 0, Volume = 0"
        self.a1.power()
        assert self.a1.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        self.a1.power()
        self.a1.volume_up()
        self.a1.mute()
        assert self.a1.__str__() == "Power = True, Channel = 0, Volume = 0"
        self.a1.mute()
        assert self.a1.__str__() == "Power = True, Channel = 0, Volume = 1"
        self.a1.power()
        self.a1.mute()
        assert self.a1.__str__() == "Power = False, Channel = 0, Volume = 1"
        self.a1.mute()
        assert self.a1.__str__() == "Power = False, Channel = 0, Volume = 1"
    def test_channel_up(self):
        self.a1.channel_up()
        assert self.a1.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.a1.power()
        self.a1.channel_up()
        assert self.a1.__str__() == "Power = True, Channel = 1, Volume = 0"
        self.a1.channel_up()
        self.a1.channel_up()
        self.a1.channel_up()
        assert self.a1.__str__() == "Power = True, Channel = 0, Volume = 0"
    def test_channel_down(self):
        self.a1.channel_down()
        assert self.a1.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.a1.power()
        self.a1.channel_down()
        self.a1.channel_down()
        assert self.a1.__str__() == "Power = True, Channel = 2, Volume = 0"
    def test_volume_up(self):
        self.a1.volume_up()
        assert self.a1.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.a1.power()
        self.a1.volume_up()
        assert self.a1.__str__() == "Power = True, Channel = 0, Volume = 1"
        self.a1.mute()
        self.a1.volume_up()
        assert self.a1.__str__() == "Power = True, Channel = 0, Volume = 2"
        self.a1.volume_up()
        self.a1.volume_up()
        assert self.a1.__str__() == "Power = True, Channel = 0, Volume = 2"
    def test_volume_down(self):
        self.a1.volume_down()
        assert self.a1.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.a1.power()
        self.a1.volume_up()
        self.a1.volume_up()
        self.a1.volume_down()
        assert self.a1.__str__() == "Power = True, Channel = 0, Volume = 1"
        self.a1.mute()
        self.a1.volume_down()
        assert self.a1.__str__() == "Power = True, Channel = 0, Volume = 0"
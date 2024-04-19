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
        assert self.a1.power() == True
        assert self.a1.power() == False
    def test_mute(self):
        self.a1.power()
        self.a1.volume_up()
        assert self.a1.mute() == True
        assert self.a1.mute() == False
        self.a1.power()
        assert self.a1.mute() == False
        assert self.a1.mute() == False
    def test_channel_up(self):
        assert self.a1.channel_up() == 0
        self.a1.power()
        assert self.a1.channel_up() == 1
        self.a1.channel_up()
        self.a1.channel_up()
        self.a1.channel_up()
        assert self.a1.channel_up() == 1
    def test_channel_down(self):
        assert self.a1.channel_down() == 0
        self.a1.power()
        assert self.a1.channel_down() == 3
    def test_volume_up(self):
        assert self.a1.volume_up() == 0
        self.a1.power()
        assert self.a1.volume_up() == 1
        self.a1.mute()
        assert self.a1.volume_up() == 2
        self.a1.volume_up()
        self.a1.volume_up()
        assert self.a1.volume_up() == 2
    def test_volume_down(self):
        assert self.a1.volume_down() == 0
        self.a1.power()
        self.a1.volume_up()
        self.a1.volume_up()
        assert self.a1.volume_down() == 1
        self.a1.mute()
        assert self.a1.volume_down() == 0
        assert self.a1.volume_down() == 0
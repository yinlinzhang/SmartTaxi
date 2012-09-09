__author__ = 'Administrator'

class Location:
    def __init__(self, addr, geo):
        self.cur_addr = addr
        self.cur_geo = geo

    def set_geo(self, geo):
        self.cur_geo = geo

    def get_geo(self):
        return self.cur_geo

    def set_addr(self, addr):
        self.cur_addr = addr

    def get_addr(self):
        return self.cur_addr


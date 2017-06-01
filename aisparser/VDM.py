from .core.vdm_core import get_navigational_status, get_sog, get_cog, get_latitude, get_longitude, get_true_heading

__all__ = ['VDM_TYPE_MAP', 'VDM', 'VDM1', 'VDM2', 'VDM3', 'VDM4', 'VDM5']


class VDM(object):
    def __init__(self):
        pass


class VDM1(VDM):
    def __init__(self, total_num, sentence_num, sequential_msg_identifier,
                 channel, msg):
        self.total_num = total_num
        self.sentence_num = sentence_num
        self.sequential_msg_identifier = sequential_msg_identifier
        self.channel = channel
        self._msg = msg

    @property
    def navigational_status(self):
        return get_navigational_status(self._msg)

    @property
    def sog(self):
        return get_sog(self._msg)

    @property
    def cog(self):
        return get_cog(self._msg)

    @property
    def true_heading(self):
        return get_true_heading(self._msg)

    @property
    def longitude(self):
        return get_longitude(self._msg)

    @property
    def latitude(self):
        return get_latitude(self._msg)


VDM2 = VDM1
VDM3 = VDM1


class VDM4(VDM):
    pass


class VDM5(VDM):
    pass


VDM_TYPE_MAP = {
    # TYPE CLASS
    1: VDM1,
    2: VDM2,
    3: VDM3,
    4: VDM4,
    5: VDM5
}
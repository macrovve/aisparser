from .core import VDM_1, VDM_5, VDM_6, VDM_8, VDM_12, VDM_14, VDM_18

__all__ = [
    'VDM_TYPE_MAP', 'VDM', 'VDM1', 'VDM2', 'VDM3', 'VDM5', 'VDM6', 'VDM8',
    'VDM12', 'VDM14', 'VDM18'
]


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
        return VDM_1.get_navigational_status(self._msg)

    @property
    def sog(self):
        return VDM_1.get_sog(self._msg)

    @property
    def cog(self):
        return VDM_1.get_cog(self._msg)

    @property
    def true_heading(self):
        return VDM_1.get_true_heading(self._msg)

    @property
    def longitude(self):
        return VDM_1.get_longitude(self._msg)

    @property
    def latitude(self):
        return VDM_1.get_latitude(self._msg)


VDM2 = VDM1
VDM3 = VDM1


class VDM5(VDM):
    def __init__(self, total_num, sentence_num, sequential_msg_identifier,
                 channel, msg):
        self.total_num = total_num
        self.sentence_num = sentence_num
        self.sequential_msg_identifier = sequential_msg_identifier
        self.channel = channel
        self._msg = msg

    @property
    def imo_number(self):
        return VDM_5.get_imo_number(self._msg)

    @property
    def call_sign(self):
        return VDM_5.get_call_sign(self._msg)

    @property
    def name(self):
        return VDM_5.get_name(self._msg)

    @property
    def overall_dimension(self):
        return VDM_5.get_overall_dimension(self._msg)

    @property
    def maximum_draught(self):
        return VDM_5.get_maximum_draught(self._msg)


class VDM6(VDM):
    def __init__(self, total_num, sentence_num, sequential_msg_identifier,
                 channel, msg):
        self.total_num = total_num
        self.sentence_num = sentence_num
        self.sequential_msg_identifier = sequential_msg_identifier
        self.channel = channel
        self._msg = msg

    @property
    def application_data(self):
        return VDM_6.get_application_data(self._msg)


class VDM8(VDM):
    def __init__(self, total_num, sentence_num, sequential_msg_identifier,
                 channel, msg):
        self.total_num = total_num
        self.sentence_num = sentence_num
        self.sequential_msg_identifier = sequential_msg_identifier
        self.channel = channel
        self._msg = msg

    @property
    def application_data(self):
        return VDM_8.get_application_data(self._msg)


class VDM12(VDM):
    def __init__(self, total_num, sentence_num, sequential_msg_identifier,
                 channel, msg):
        self.total_num = total_num
        self.sentence_num = sentence_num
        self.sequential_msg_identifier = sequential_msg_identifier
        self.channel = channel
        self._msg = msg

    @property
    def safaty_text(self):
        return VDM_12.get_safety_text(self._msg)


class VDM14(VDM):
    def __init__(self, total_num, sentence_num, sequential_msg_identifier,
                 channel, msg):
        self.total_num = total_num
        self.sentence_num = sentence_num
        self.sequential_msg_identifier = sequential_msg_identifier
        self.channel = channel
        self._msg = msg

    @property
    def safaty_text(self):
        return VDM_14.get_safety_text(self._msg)


class VDM18(VDM):
    def __init__(self, total_num, sentence_num, sequential_msg_identifier,
                 channel, msg):
        self.total_num = total_num
        self.sentence_num = sentence_num
        self.sequential_msg_identifier = sequential_msg_identifier
        self.channel = channel
        self._msg = msg

    @property
    def sog(self):
        return VDM_18.get_sog(self._msg)

    @property
    def cog(self):
        return VDM_18.get_cog(self._msg)

    @property
    def true_heading(self):
        return VDM_18.get_true_heading(self._msg)

    @property
    def longitude(self):
        return VDM_18.get_longitude(self._msg)

    @property
    def latitude(self):
        return VDM_18.get_latitude(self._msg)


VDM_TYPE_MAP = {
    # TYPE # CLASS
    1: VDM1,
    2: VDM2,
    3: VDM3,
    5: VDM5,
    6: VDM6,
    8: VDM8,
    12: VDM12,
    14: VDM14,
    18: VDM18,
}
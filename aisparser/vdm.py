from .core import VDM, VDM_1, VDM_5, VDM_6, VDM_8, VDM_12, VDM_14, VDM_18

__all__ = [
    'VDM_TYPE_MAP', 'VDMBase', 'VDM1', 'VDM2', 'VDM3', 'VDM5', 'VDM6', 'VDM8',
    'VDM12', 'VDM14', 'VDM18'
]


class VDMBase(object):
    def __init__(self, **kwargs):
        self.type_ = 'vdm'

    def get(self, k, d=None):
        return getattr(self, k, d)


class VDM1(VDMBase):
    def __init__(self, sentence, total_num, sentence_num,
                 sequential_msg_identifier, channel, msg, **kwargs):
        # todo datagram,segment,message 都应该暴露出来
        # todo 名称统一一下
        super(VDM1, self).__init__(**kwargs)
        self.sentence = sentence
        self.total_num = total_num
        self.sentence_num = sentence_num
        self.sequential_msg_identifier = sequential_msg_identifier
        self.channel = channel
        self._msg = msg
        self.message = msg.major_msg
        self.msg_id = 1

    @property
    def mmsi(self):
        return VDM.get_user_id(self._msg)

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


class VDM2(VDM1):
    def __init__(self, sentence, total_num, sentence_num,
                 sequential_msg_identifier, channel, msg):
        super(VDM2, self).__init__(sentence, total_num, sentence_num,
                                   sequential_msg_identifier, channel, msg)
        self.msg_id = 2


class VDM3(VDM1):
    def __init__(self, sentence, total_num, sentence_num,
                 sequential_msg_identifier, channel, msg):
        super(VDM3, self).__init__(sentence, total_num, sentence_num,
                                   sequential_msg_identifier, channel, msg)
        self.msg_id = 3


class VDM5(VDMBase):
    def __init__(self, sentence, total_num, sentence_num,
                 sequential_msg_identifier, channel, msg):
        super(VDM5, self).__init__()
        self.sentence = sentence
        self.total_num = total_num
        self.sentence_num = sentence_num
        self.sequential_msg_identifier = sequential_msg_identifier
        self.channel = channel
        self._msg = msg
        self.message = msg.major_msg
        self.msg_id = 5

    @property
    def mmsi(self):
        return VDM.get_user_id(self._msg)

    @property
    def imo_number(self):
        return VDM_5.get_imo_number(self._msg)

    @property
    def call_sign(self):
        return VDM_5.get_call_sign(self._msg).strip('@')

    @property
    def name(self):
        return VDM_5.get_name(self._msg).strip('@')

    @property
    def overall_dimension(self):
        overall_d = VDM_5.get_overall_dimension(self._msg)
        return overall_d.A, overall_d.B, overall_d.C, overall_d.D

    @property
    def maximum_draught(self):
        return VDM_5.get_maximum_draught(self._msg)


class VDM6(VDMBase):
    def __init__(self, sentence, total_num, sentence_num,
                 sequential_msg_identifier, channel, msg):
        super(VDM6, self).__init__()
        self.sentence = sentence
        self.total_num = total_num
        self.sentence_num = sentence_num
        self.sequential_msg_identifier = sequential_msg_identifier
        self.channel = channel
        self._msg = msg
        self.message = msg.major_msg

        self.msg_id = 6

    @property
    def mmsi(self):
        return VDM.get_user_id(self._msg)

    @property
    def application_data(self):
        return VDM_6.get_application_data(self._msg)


class VDM8(VDMBase):
    def __init__(self, sentence, total_num, sentence_num,
                 sequential_msg_identifier, channel, msg):
        super(VDM8, self).__init__()
        self.sentence = sentence
        self.total_num = total_num
        self.sentence_num = sentence_num
        self.sequential_msg_identifier = sequential_msg_identifier
        self.channel = channel
        self._msg = msg
        self.message = msg.major_msg

        self.msg_id = 8

    @property
    def mmsi(self):
        return VDM.get_user_id(self._msg)

    @property
    def application_data(self):
        return VDM_8.get_application_data(self._msg)


class VDM12(VDMBase):
    def __init__(self, sentence, total_num, sentence_num,
                 sequential_msg_identifier, channel, msg):
        super(VDM12, self).__init__()
        self.sentence = sentence
        self.total_num = total_num
        self.sentence_num = sentence_num
        self.sequential_msg_identifier = sequential_msg_identifier
        self.channel = channel
        self._msg = msg
        self.message = msg.major_msg

        self.msg_id = 12

    @property
    def mmsi(self):
        return VDM.get_user_id(self._msg)

    @property
    def safaty_text(self):
        return VDM_12.get_safety_text(self._msg)


class VDM14(VDMBase):
    def __init__(self, sentence, total_num, sentence_num,
                 sequential_msg_identifier, channel, msg):
        super(VDM14, self).__init__()
        self.sentence = sentence
        self.total_num = total_num
        self.sentence_num = sentence_num
        self.sequential_msg_identifier = sequential_msg_identifier
        self.channel = channel
        self._msg = msg
        self.message = msg.major_msg

        self.msg_id = 14

    @property
    def mmsi(self):
        return VDM.get_user_id(self._msg)

    @property
    def safaty_text(self):
        return VDM_14.get_safety_text(self._msg)


class VDM18(VDMBase):
    def __init__(self, sentence, total_num, sentence_num,
                 sequential_msg_identifier, channel, msg):
        super(VDM18, self).__init__()
        self.sentence = sentence
        self.total_num = total_num
        self.sentence_num = sentence_num
        self.sequential_msg_identifier = sequential_msg_identifier
        self.channel = channel
        self._msg = msg
        self.message = msg.major_msg

        self.msg_id = 18

    @property
    def mmsi(self):
        return VDM.get_user_id(self._msg)

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
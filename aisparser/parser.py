from .core import get_sentence_type, get_basic_info, construct_cpp_msg
from .core import VDM
from .vdm import VDM_TYPE_MAP
import os


class Parser(object):
    def __init__(self, **kargs):
        self.factory = VDMFactory()

    def parse(self, sentence):
        type_ = get_sentence_type(sentence)
        # print(sentence)
        if 'VDM' in type_.upper():
            return self.factory.create_VDM(sentence)
        # 其他类型暂未实现
        elif type_.upper() in ('ARVSI', 'PSHI', 'GPGGA', 'GPVTG', 'GPZDA',
                               'ARFSR', 'ARADS', 'ARALR'):
            # print('Not ImplementedError this type')
            return None
        else:
            print('Message type not implement', type_)
            return None
            # raise NotImplementedError

    def from_file(self, filename, filter_=None, encoding=None):
        def filter_func(record):
            if not filter_:
                return True
            if record:
                return filter_(record)
            return False

        with open(filename, encoding=encoding) as file:
            for sentence in file:
                if sentence == os.linesep:
                    continue
                record = self.parse(sentence)
                if record and filter_func(record):
                    yield record


class VDMFactory(object):
    def __init__(self):
        self.sentence = list()
        # self.fragment=list()
        self.total_number = None
        self.sentence_number = None
        self.sequential_msg_identifier = None
        self.channel = None
        self.message = list()

    def create_VDM(self, sentence):
        """工厂方法，返回对应的VDM类

        """
        sentence, message = self._preprocess(sentence)
        msg = construct_cpp_msg(sentence, message)

        msg_id = VDM.get_message_id(msg)
        vdm_cls = VDM_TYPE_MAP.get(msg_id)
        if vdm_cls:
            return vdm_cls(sentence, self.total_number, self.sentence_number,
                           self.sequential_msg_identifier, self.channel, msg)
        elif msg_id <= 27:  # Not implemented 
            return None
        else:
            # 这个报错信息如果该条被过滤的话，那么报错信息应该不显示的
            print('msg_id should range from 1 to 27', msg_id, msg.major_msg)
            return None
            # raise Exception('msg_id range from 1 to 27', msg_id)

    def _preprocess(self, sentence):
        """对当前的sentence进行预处理，主要处理连续报文的情况

        """

        (total_number, sentence_number, sequential_msg_identifier, channel,
         message) = get_basic_info(sentence)
        # fill_bits=

        # 这里判断的有意外情况吧，中间断掉了呢
        if self.total_number == total_number and self.sentence_number + 1 == sentence_number:
            self.sentence.append(sentence)
            self.sentence_number = sentence_number
            self.message.append(message)
        else:
            self.sentence = [sentence]
            self.total_number = total_number
            self.sentence_number = sentence_number
            self.sequential_msg_identifier = sequential_msg_identifier
            self.channel = channel
            self.message = [message]
        return self.sentence, ''.join(self.message)


class PSHIFactory(object):
    pass


class GPGGAFactory(object):
    pass


class GPVTGFactory(object):
    pass


class GPZDAFactory(object):
    pass

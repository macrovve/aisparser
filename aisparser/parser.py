from .core import get_sentence_type, get_basic_info, construct_cpp_msg
from .core import VDM
from .vdm import VDM_TYPE_MAP


class Parser(object):
    def __init__(self):
        self.factory = VDMFactory()

    def parse(self, sentence):
        type_ = get_sentence_type(sentence)
        if 'VDM' in type_:
            return self.factory.create_VDM(sentence)
        else:
            pass


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

        message_id = VDM.get_message_id(msg)
        if message_id in VDM_TYPE_MAP:
            return VDM_TYPE_MAP[message_id](
                self.total_number, self.sentence_number,
                self.sequential_msg_identifier, self.channel, msg)
        else:
            pass

    def _preprocess(self, sentence):
        """对当前的sentence进行预处理，处理连续报文的情况

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
        return self.sentence, self.message

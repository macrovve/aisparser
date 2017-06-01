from .vdm_core import VDM
from .vdm_core import revd_msg_s
import re
from .VDM import VDM_TYPE_MAP
re_sentence_type = re.compile('[$!](?P<sentence_type>[A-Z0-9]*),')
re_basic_info = re.compile(',(?P<total_number>[1-9]?)'
                           ',(?P<sentence_number>[0-9]?)'
                           ',(?P<sequential_msg_identifier>[0-9]?)'
                           ',(?P<channel>[A-B]?)'
                           ',(?P<message>.*)'
                           ',')

# sentence 一整句
# fragment 有用部分
# message 出去type剩下的

VDM = VDM()


class Parser(object):
    def __init__(self):
        self.factory = VDMFactory()

    def parse(self, sentence):
        type_ = self.get_type(sentence)
        if 'VDM' in type_:
            return self.factory.create_VDM(sentence)
        else:
            pass

    def get_type(self, sentence):
        match = re_sentence_type.search(sentence)
        if match:
            return match.group(1)


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
        sentence, message = self.preprocess(sentence)
        msg = self.construct_msg(sentence, message)

        message_id = VDM.get_message_id(msg)
        if message_id in VDM_TYPE_MAP:
            return VDM_TYPE_MAP[message_id](
                self.total_number, self.sentence_number,
                self.sequential_msg_identifier, self.channel, msg)
        else:
            pass

    def construct_msg(self, sentence, message):
        """用sentence和message生成revd_msg_s结构体，方便调用c代码

        """
        msg = revd_msg_s()
        msg.count = len(sentence)
        for i in range(msg.count):
            msg.set_msg_by_count(i, sentence[i])
        msg.major_msg_p = ''.join(message)
        return msg

    def preprocess(self, sentence):
        """对当前的sentence进行预处理，处理连续报文的情况

        """
        match = re_basic_info.search(sentence)
        if match:
            total_number = int(match.group(1))
            sentence_number = int(match.group(2))
            sequential_msg_identifier = int(
                match.group(3)) if match.group(3) else ''
            channel = match.group(4)
            message = match.group(5)
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

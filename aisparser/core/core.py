from .cpp import VDM, VDM_1, VDM_5, VDM_6, VDM_8, VDM_12, VDM_14, VDM_18
from .cpp import revd_msg_s

import re

__all__ = [
    'get_sentence_type', 'get_basic_info', 'construct_cpp_msg', 'VDM', 'VDM_1',
    'VDM_2', 'VDM_3', 'VDM_5', 'VDM_6', 'VDM_8', 'VDM_12', 'VDM_14', 'VDM_18'
]

re_sentence_type = re.compile('[$!](?P<sentence_type>[A-Z0-9]*),')


def get_sentence_type(sentence):
    match = re_sentence_type.search(sentence)
    if match:
        return match.group(1)
    return None


re_basic_info = re.compile(',(?P<total_number>[1-9]?)'
                           ',(?P<sentence_number>[0-9]?)'
                           ',(?P<sequential_msg_identifier>[0-9]?)'
                           ',(?P<channel>[A-B]?)'
                           ',(?P<message>.*)'
                           ',')


def get_basic_info(sentence):
    match = re_basic_info.search(sentence)
    if match:
        total_num = int(match.group(1))
        sentence_num = int(match.group(2))
        sequential_msg_identifier = int(
            match.group(3)) if match.group(3) else ''
        channel = match.group(4)
        message = match.group(5)
    return total_num, sentence_num, sequential_msg_identifier, channel, message


def construct_cpp_msg(sentence, message):
    """为了使用cpp函数，构建msg结构体

    """
    msg = revd_msg_s()
    msg.count = len(sentence)
    for i in range(msg.count):
        msg.set_msg_by_count(i, sentence[i])
    msg.major_msg = ''.join(message)
    return msg


# get_message_id
VDM = VDM()

# VDM_1.get_navigational_status()
# VDM_1.get_sog()
# VDM_1.get_cog()
# VDM_1.get_true_heading()
# VDM_1.get_longitude()
# VDM_1.get_latitude()
VDM_1 = VDM_1()
VDM_2 = VDM_1
VDM_3 = VDM_1

# VDM_5.get_imo_number()
# VDM_5.get_call_sign()
# VDM_5.get_name()
# VDM_5.get_overall_dimension()
# VDM_5.get_maximum_draught()
VDM_5 = VDM_5()

# VDM_6.get_application_data()
VDM_6 = VDM_6()

# VDM_8.get_application_data()
VDM_8 = VDM_8()

# VDM_12.get_safety_text()
VDM_12 = VDM_12()

# VDM_14.get_safety_text()

VDM_14 = VDM_14()

# VDM_18.get_sog()
# VDM_18.get_cog()
# VDM_18.get_true_heading()
# VDM_18.get_longitude()
# VDM_18.get_latitude()
VDM_18 = VDM_18()
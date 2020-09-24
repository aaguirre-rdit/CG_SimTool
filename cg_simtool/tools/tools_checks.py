import numpy as np

def get_rigids(types):
    """
    Returns Array of [Start,End] indexes of rigid regions in the system
    :param types: Array
    :return:
    """
    r_bool = types >= 20
    rigids = []
    if any(r_bool):
        i = 0
        while i < len(types):
            if types[i]:
                start = i + 1
                j = i
                count = 1
                while j < len(types):
                    if types[j] is False:
                        end = j + 1
                        rigids.append([start,end])
                        i += count
                    else:
                        count += 1
                        j += 1
            else:
                i += 1
        return rigids
    return None

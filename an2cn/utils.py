def float_to_str(f: float) -> str:
    """
    异常情况：
    str(0.00005) == '5e-05'
    """
    ret = str(f)
    e_pos = ret.find('e')
    if e_pos == -1:
        return ret

    base = ret[:e_pos]
    if f < 0:
        sign = '-'
        base = base[1:]
    else:
        sign = ''
    # 如果转换成了科学计数法，此处的幂应该都是负数
    power = -int(ret[e_pos + 1 :])
    zeros = '0' * (power - 1)
    return f'{sign}0.{zeros}{base}'

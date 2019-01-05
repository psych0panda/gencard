from random import randint

ISSUER_ID = {
    'MASTERCARD': randint(511111, 551111),
    'VISA': randint(411111, 499999)
}


def userId() -> int:
    return randint(1111111111, 9999999999)


def issuerId(key: str) -> int:
    return ISSUER_ID.get(key)


def isCheckLuhn(list_int: list) -> bool:
    c_sum = list_int[-1]
    tmp_v = {i: v * 2 for i, v in enumerate(list_int[:-1]) if i == 0 or i % 2 == 0}
    for k, v in tmp_v.items():
        if v >= 10:
            y = str(v)[0]
            z = str(v)[1]
            w = int(y) + int(z)
            tmp_v.update({k: w})
    for k_, v_ in tmp_v.items():
        list_int[k_] = v_
    res = sum(list_int[:-1]) * 9
    if str(res)[-1] == str(c_sum):
        return True


def gen(bin: str = 'MASTERCARD') -> None:
    while 1:
        iid = str(issuerId(bin))
        uid = str(userId())
        num = iid + uid
        l_tmp = [int(i) for i in num]
        if checkLuhn(l_tmp):
            print(num)


if __name__ == '__main__':
    gen()

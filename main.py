from random import randint

MMI = {
    'ISO_TC68': 0,
    'AIRLINES': 1,
    'AIRLINES_AND_OTHER_INDUSTRY_ASSIGNMENT': 2,
    'TRAVEL_AND_ENTERTAINMENT': 3,
    'BANKING_AND_FINANCIAL': 4,
    'BANKING_AND_FINANCIAL': 5,
    'MERCHANDISING_AND_BANKING': 6,
    'PETROLEUM': 7,
    'TELECOMMUNICATIONS_AND_OTHER_INDUSTRY_ASSIGNMENT': 8,
    'NATIONAL_ASSIGNMENT': 9,
}

ISSUER_ID = {
    'MASTERCARD': randint(222100, 272099),
    'VISA': randint(411111, 499999)
}


def mmi(industry_id: int = 4) -> int:
    return industry_id


def userId() -> int:
    return randint(1111111111, 9999999999)


def issuerId() -> int:
    return ISSUER_ID.get('VISA')


def _translateToList(check_int: int) -> list:
    list_int = []
    for i in str(check_int):
        list_int.append(int(i))
    return list_int


def checkMod10(list_int: list) -> bool:
    c_int = list_int[-1]
    res = list_int.index(3)
    print(res)


if __name__ == '__main__':
    l_i = [3, 8, 5, 2, 0, 0, 0, 0, 0, 2, 3, 2, 3, 7]
    checkMod10(l_i)

def get_odds(n) -> int:
    """
    1 부터 n까지의 홀수를 발생시키는 제너레이터
    :param n: int
    :return: int
    """
    for i in range(1,n,2):
        yield i
cnt = 0
odds = get_odds(10)
for i in odds:
    cnt += 1
    if cnt == 3:
        print(i)
        break
def multiplication_table(times: int) -> None:
    last: int = 11
    li: list = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    for i in li:
        print(f'{times} X {i} = {times*i}')

multiplication_table(2)

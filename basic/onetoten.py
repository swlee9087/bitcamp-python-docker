class OneToTen(object):
    pass

    def one_to_ten_sum_1():
        sum = 0

        for i in range(1,10+1):
            sum += i
            print(sum)
    one_to_ten_sum_1()

    def one_to_ten_sum_2():
        print(sum(i for i in range(1, 10+1)))

    one_to_ten_sum_2()

    def one_to_ten_sum_3():
        print(sum(range(1, 10+1)))
    one_to_ten_sum_3()

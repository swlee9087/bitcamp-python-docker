class OneToTen(object):
    pass

    def one_to_ten_sum_1(self):
        sum = 0

        #    for i in []:  # basic

        for i in range(1,10+1):
            sum += i
            print(sum)

    def one_to_ten_sum_2(self):
        print(sum(i for i in range(1, 10+1)))

    def one_to_ten_sum_3(self):
        print(sum(range(1, 10+1)))


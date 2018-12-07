#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Bank():
    crisis = False

    def create_atm(self):
        while not self.crisis:
            yield ('$100')

    def count(self, n):
        while n > 0:
            yield n  # 生成值: n
            n -= 1


if __name__ == '__main__':
    bank = Bank()
    printer = bank.create_atm()
    print(printer.next())

    counter = bank.count(10)
    for i in range(0, 10, 1):
        print('counter: %d') % i
        print(counter.next())

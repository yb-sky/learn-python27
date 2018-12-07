#!/usr/bin/python
#-*-coding:utf-8-*-

# 最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：


class ListDemo:
    def list_append(self):
        nums = []
        for i in range(10):
            data = [i, i + 1, i + 2, i + 3]
            nums.append(data)

        print(nums)

    def list_foreach(self):
        words = 'marry,lily,jack'.split(',')
        for i in words:
            print(i)

    def list_foreach2(self):
        lists = ['huahua', 'caocao', 'niaoniao', 'shushu', [8, 6, 3, 1]]
        # for name in lists:
        #     print name
        #
        #     if type(name) == list:  # 判断元素类型
        #         for i in name:
        #             print(i)

        for i, val in enumerate(lists):
            print i, val


if __name__ == '__main__':
    obj = ListDemo()
    obj.list_foreach2()






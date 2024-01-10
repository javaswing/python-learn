"""
Python中的异常

在Python中使用 try exception进行异常的处理
"""

# 自定义异常
class EmptyContentException(Exception):
    def __init__(self, message):
        super().__init__(message)


def demo():
    try:

        with open('file-not-exits.txt', 'r') as file:
            content = file.read()
            lines = content.split("\n")

            for line in lines:
                if line.strip() != '':
                    print(line)

            if len(lines) == 0 or (len(lines) == 1 and lines[0].strip() == ''):
                raise EmptyContentException('empty file')

            first_line = lines[0].strip()
            print(f'first line : {first_line}')

            nums = [int(line) for line in lines]
            print(f'total lines is {sum(nums)}')

    # 可以有多个异常串行处理，但是一旦匹配到一个，就不会执行其它的。和java或者C#中一样
    except FileNotFoundError as err:
        print(f'file not found Error {str(err)}')
    except Exception as error:
        print(f'open file error {str(error)}')


if __name__ == '__main__':
    demo()

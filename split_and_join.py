
def split_and_join(line):
    # write your code here
    spliter = line.split(" ")
    joiner = "-".join(spliter)
    return joiner
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
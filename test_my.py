contents = "disk.fileexistandsize[/opt/mqadmin/FmsNpiDataLoader/tongfang/FMS-FM_SUM_1440-0-'(date -d '-4 day' +%Y%m%d)'000000-'(date -d '-4 day' +%Y%m%d)'000000-001.zip]"
print(len(contents.encode()))


def sum(a, b):
    print(a + b)


if __name__ == '__main__':
    sum(5, 6)

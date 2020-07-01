# main.py
#
# This is file is meant to be run through both Zerynth and Python3
# as to compare the two implementations.

try:
    # works in Zerynth
    import streams
    streams.serial()

except:
#-if False
    # works in Python
#-endif
    pass

### common ############################################################

test_total = 0
test_pass = 0
test_gran_total = 0
test_gran_pass = 0

def test (name, result=None, expect=None):
    global test_total
    global test_pass
    global test_gran_total
    global test_gran_pass

    if result == None and expect == None:
        if test_total:
            print('Total pass: %d/%d' %(test_pass, test_total))
        print('--- ', name, ' ---')
        test_total = 0
        test_pass = 0
    else:
        print("#%d: %s: " % (test_total, name), end='')
        result_str = str(result)
        expect_str = str(expect)
        if result_str == expect_str:
            print("%s (pass)" % result_str)
            test_pass += 1
            test_gran_pass += 1
        else:
            print("fail:\n  expected: %s\n  got: %s" % (expect_str, result_str))

        test_total += 1
        test_gran_total += 1

### main ##############################################################

try:
    test('suntime: example')

    import examples.main as example

    ###################################################################

    import suntime

    test('suntime')

    test('sr1', example.sr1, ( 6, 38))
    test('ss1', example.ss1, (15, 49))
    test('sr2', example.sr2, ( 4, 39))
    test('ss2', example.ss2, (16, 10))
    test('sr3', example.sr3, ( 3, 32))
    test('ss3', example.ss3, (17, 57))

    ###################################################################

    test('done')
    print('Gran total pass: %d/%d' %(test_gran_pass, test_gran_total))

except Exception as e:
#-if False
    raise
#-endif
    print("Something bad happened:",e)

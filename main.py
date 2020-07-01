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
    import suntime

    test('suntime: example')

    Rome     = suntime.Sun( 41.902782 , 12.496366 )
    Warsaw   = suntime.Sun( 51.21     , 21.01     )
    CapeTown = suntime.Sun(-33.9252192, 18.4240762)

    dt1 = (2000, 1, 1)
    sr1 = Rome.get_sunrise_time(*dt1) # (6, 38)
    ss1 = Rome.get_sunset_time (*dt1) # (15, 49)
    print('Rome:', sr1, ss1)

    dt2 = (2014, 10, 3)
    sr2 = Warsaw.get_sunrise_time(*dt2) # (4, 39)
    ss2 = Warsaw.get_sunset_time (*dt2) # (16, 10)
    print('Warsaw:', sr2, ss2)

    dt3 = (2016, 12, 21)
    sr3 = CapeTown.get_sunrise_time(*dt3) # (3, 32)
    ss3 = CapeTown.get_sunset_time (*dt3) # (17, 57)
    print('Cape Town:', sr3, ss3)

    # if `datetime` module is available
    #import datetime as datetimelib

    #timedelta = datetimelib.timedelta
    #timezone  = datetimelib.timezone
    #datetime  = datetimelib.datetime

    #utc = timezone.utc
    #tz1 = timezone(timedelta(hours=1))
    #tz2 = timezone(timedelta(hours=3))
    #tz3 = timezone(timedelta(hours=2))

    ## https://www.timeanddate.com/sun/italy/rome?month=1&year=2000
    #rt1 = datetime(*dt1, *sr1, tzinfo=utc).astimezone(tz1) # 2000-01-01 07:38:00+01:00
    #st1 = datetime(*dt1, *ss1, tzinfo=utc).astimezone(tz1) # 2000-01-01 16:49:00+01:00
    #print('Rome:\n  %s\n  %s' % (rt1, st1))

    ## https://www.timeanddate.com/sun/poland/warsaw?month=10&year=2014
    #rt2 = datetime(*dt2, *sr2, tzinfo=utc).astimezone(tz2) # 2014-10-03 07:39:00+03:00
    #st2 = datetime(*dt2, *ss2, tzinfo=utc).astimezone(tz2) # 2014-10-03 19:10:00+03:00
    #print('Warsaw:\n  %s\n  %s' % (rt2, st2))

    ## https://www.timeanddate.com/sun/south-africa/cape-town?month=12&year=2016
    #rt3 = datetime(*dt3, *sr3, tzinfo=utc).astimezone(tz3) # 2016-12-21 05:32:00+02:00
    #st3 = datetime(*dt3, *ss3, tzinfo=utc).astimezone(tz3) # 2016-12-21 19:57:00+02:00
    #print('Cape Town:\n  %s\n  %s' % (rt3, st3))

    ###################################################################

    test('suntime')

    test('sr1', sr1, ( 6, 38))
    test('ss1', ss1, (15, 49))
    test('sr2', sr2, ( 4, 39))
    test('ss2', ss2, (16, 10))
    test('sr3', sr3, ( 3, 32))
    test('ss3', ss3, (17, 57))

    ###################################################################

    test('done')
    print('Gran total pass: %d/%d' %(test_gran_pass, test_gran_total))

except Exception as e:
#-if False
    raise
#-endif
    print("Something bad happened:",e)

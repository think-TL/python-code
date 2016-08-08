def int_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0)or(year % 4 == 0 and year % 100 == 0):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    year = raw_input("Enter the year")
    print "year %s is leap year:%s" % (year, int_leap_year((int(year))))
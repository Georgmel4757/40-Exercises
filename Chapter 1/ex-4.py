def main():
    ex_1 = [9, 17, 30, 1.5]
    ex_2 = [16, 18, 30, 1.8]
    ex_3 = [13.25, 15, 30, 1.5]

    res_1 = overTime(*ex_1)
    res_2 = overTime(*ex_2)
    res_3 = overTime(*ex_3)

    print(res_1)
    print(res_2)
    print(res_3)


def overTime(first_hour, last_hour, hourly_rate, multiplier):
    result = 0

    if first_hour <= 17 and last_hour <= 17:
        result += (last_hour - first_hour) * hourly_rate

    elif first_hour <= 17 and last_hour >= 17:
        result += (17 - first_hour) * hourly_rate + \
                (last_hour - 17) * hourly_rate * multiplier

    elif first_hour >= 17 and last_hour >= 17:
        result += (last_hour - first_hour) * hourly_rate * multiplier
    
    result = "${}".format(format(result, ".2f"))
    
    return result


if __name__ == "__main__":
    main()

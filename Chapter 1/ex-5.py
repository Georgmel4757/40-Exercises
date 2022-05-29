def main():
    ex_1 = ["205 pounds", "73 inches"]
    ex_2 = ["55 kilos", "1.65 meters"]
    ex_3 = ["154 pounds", "2 meters"]

    res_1 = bmi(*ex_1)
    res_2 = bmi(*ex_2)
    res_3 = bmi(*ex_3)

    print(res_1)
    print(res_2)
    print(res_3)


def bmi(weight, height):
    weight = weight.split(" ")
    height = height.split(" ")

    weight_value, weight_unit = float(weight[0]), weight[1] 
    height_value, height_unit = float(height[0]), height[1]
    
    pounds_to_kilo = 0.4535
    inch_to_meter = 0.0254

    if weight_unit in "pounds":
        weight_value *= pounds_to_kilo
    if height_unit in "inches":
        height_value *= inch_to_meter
    
    bmi = round(weight_value / height_value ** 2, ndigits=1)

    if bmi < 18.5:
        message = "{0} Underweight".format(bmi)
    elif 18.5 <= bmi < 25.0:
        message = "{0} Normal weight".format(bmi)
    elif bmi >= 25.0:
        message = "{0} Overweight".format(bmi)

    return message


if __name__ == "__main__":
    main()

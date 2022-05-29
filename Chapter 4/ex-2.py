from math import sqrt


class Spider:
    def __init__(self, coords):
        self.sign_coord = coords[0]
        self.num_coord = int(coords[1])
    
    def __str__(self):
        return f"Coords - {self.sign_coord}{self.num_coord}"

    def get_coords(self):
        return f"{self.sign_coord}{self.num_coord}"
    
    def move_clockwise(self):
        if ord(self.sign_coord) + 1 == ord("I"):
            self.sign_coord = "A"
        else: 
            self.sign_coord = chr(ord(self.sign_coord) + 1)

    def move_counterclockwise(self):
        if ord(self.sign_coord) - 1 == ord("@"):
            self.sign_coord = "H"
        else: 
            self.sign_coord = chr(ord(self.sign_coord) - 1)
    
    def move_middle(self):
        if self.num_coord == 0:
            pass
        elif self.num_coord - 1 == 0:
            self.sign_coord = "A"
            self.num_coord = 0
        else: 
            self.num_coord -= 1
    
    def move_outside(self):
        if self.num_coord == 4:
            pass
        else: 
            self.num_coord += 1


class Fly:
    def __init__(self, coords):
        self.sign_coord = coords[0]
        self.num_coord = int(coords[1])
    
    def __str__(self):
        return (f"Class - Fly\n"
                f"Coordinates - {self.get_coords()}")

    def get_coords(self):
        return f"{self.sign_coord}{self.num_coord}"


def main():
    ex1 = ("H3", "E2") 
    ex2 = ("A4", "B2") 
    ex3 = ("A4", "C2") 

    res_1 = spiderVsFly(*ex1)
    res_2 = spiderVsFly(*ex2)
    res_3 = spiderVsFly(*ex3)

    print(res_1)
    print(res_2)
    print(res_3)
 

def spiderVsFly(spi_coords: str, fly_coords: str):
    range_a_z = [chr(num) for num in range(65, 73)]
    range_0_4 = [str(num) for num in range(5)]

    assert len(spi_coords) == 2, "Coords not valid" 
    assert len(fly_coords) == 2, "Coords not valid"

    if spi_coords[0] not in range_a_z or spi_coords[1] not in range_0_4:
        assert False, "Spider coords not in range 'A-H' or '0-4'"
    if fly_coords[0] not in range_a_z or fly_coords[1] not in range_0_4:
        assert False, "Fly coords not in range 'A-H' or '0-4'"
    
    if spi_coords[1] == "0":
        spi_coords = "A0"
    if fly_coords[1] == "0":
        fly_coords = "A0"

    count_around, steps_around = around_ring(spi_coords, fly_coords)
    count_through, steps_through = through_middle(spi_coords, fly_coords)

    if count_around > count_through:
        result = "-".join(steps_through)
    else:
        result = "-".join(steps_around)

    return result


def around_ring(spi_coords, fly_coords):
    distance = 0
    steps = []

    spi = Spider(spi_coords)
    fly = Fly(fly_coords)

    steps.append(spi.get_coords())

    while spi.get_coords() != fly.get_coords():
        if spi.num_coord < fly.num_coord:
            if (ord(fly.sign_coord) - ord(spi.sign_coord) 
                    in (1, 2, 3, 4, -5, -6, -7)):
                distance += spi.num_coord * sqrt(2 - sqrt(2))
                spi.move_clockwise()
            elif (ord(spi.sign_coord) - ord(fly.sign_coord) 
                    in (1, 2, 3, 4, -5, -6, -7)):
                distance += spi.num_coord * sqrt(2 - sqrt(2))
                spi.move_counterclockwise()
            else:
                distance += 1
                spi.move_outside()
                
        elif spi.num_coord > fly.num_coord:
            if spi.num_coord != fly.num_coord:
                distance += 1
                spi.move_middle()
            elif (ord(fly.sign_coord) - ord(spi.sign_coord) 
                    in (1, 2, 3, 4, -5, -6, -7)):
                distance += spi.num_coord * sqrt(2 - sqrt(2))
                spi.move_clockwise()
            elif (ord(spi.sign_coord) - ord(fly.sign_coord) 
                    in (1, 2, 3, 4, -5, -6, -7)):
                distance += spi.num_coord * sqrt(2 - sqrt(2))
                spi.move_counterclockwise()

        else:
            if (ord(fly.sign_coord) - ord(spi.sign_coord) 
                    in (1, 2, 3, 4, -5, -6, -7)):
                distance += spi.num_coord * sqrt(2 - sqrt(2))
                spi.move_clockwise()
            elif (ord(spi.sign_coord) - ord(fly.sign_coord) 
                    in (1, 2, 3, 4, -5, -6, -7)):
                distance += spi.num_coord * sqrt(2 - sqrt(2))
                spi.move_counterclockwise()
        
        steps.append(spi.get_coords())

    return (distance, steps)


def through_middle(spi_coords, fly_coords):
    distance = 0
    steps = []
    was_middle = False

    spi = Spider(spi_coords)
    fly = Fly(fly_coords)

    steps.append(spi.get_coords())

    while spi.get_coords() != fly.get_coords():
        if spi.num_coord == 0 and not was_middle:
            spi.sign_coord = fly.sign_coord
            was_middle = True
            continue
        elif was_middle:
            spi.move_outside()
            distance += 1
        elif not was_middle:
            spi.move_middle()
            distance += 1

        steps.append(spi.get_coords())

    return (distance, steps)


if __name__ == "__main__":
    main()
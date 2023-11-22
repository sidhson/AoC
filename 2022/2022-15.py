import load_data
import re


Y_POS_TO_CHECK = 2_000_000


def no_beacon_on_row(sensors: dict, beacons: set):
    no_beacon_at = set()
    for (sx, sy), sr in sensors.items():
        
        # If row to check in range. 
        if sy + sr >= Y_POS_TO_CHECK and sy - sr <= Y_POS_TO_CHECK:
            sr_width = sr - abs(sy - Y_POS_TO_CHECK)

            print(f'Sensor ({sx}, {sy}) within range! Width is {sr_width*2:,}')
            
            for i in range(sx - sr_width, sx + sr_width + 1):
                no_beacon_at.add(i) # Store positions where no beacon can be.
    return no_beacon_at


def find_distress_beacon(sensors: dict, beacons: set):
    # Only single location that is not covered by sensors.
    # Location must be at an intersection of the adjacent lines to the sensors.
    # Compute the coefficients a and b of y=kx+a and y=kx+b.
    # Then the intersection of the lines and check against the sensors. 
    
    a_coeff = set() # gradient 1 lines
    b_coeff = set() # gradient -1 lines

    for (sx,sy), sr in sensors.items():
        # Coefficients of lines. 
        a_coeff.add(sy - sx + sr + 1)
        a_coeff.add(sy - sx - sr - 1)
        b_coeff.add(sy + sx + sr + 1)
        b_coeff.add(sy + sx - sr - 1)
    
    for a in a_coeff:
        for b in b_coeff:
            # Compute the intersection of the two lines. 
            px = (b-a) // 2
            py = (a+b) // 2

            if 0 <= px <= 4_000_000 and 0 <= py <= 4_000_000:    
                # Out of range for all sensors. 
                if all([abs(sx-px)+abs(sy-py) > sr for (sx, sy), sr in sensors.items()]):
                    print(f'Distress beacon found at {px:,}:{py:,}')
                    print(f'Tuning frequency: {px*4_000_000 + py:,}')
                    return


def process_data(data):

    sensors = dict()
    beacons = set()

    for line in data:
        s, b = line.split(':')
        sx, sy = [int(re.sub('[^-0-9]','',txt)) for txt in s.split(',')]
        bx, by = [int(re.sub('[^-0-9]','',txt)) for txt in b.split(',')]

        sensors[(sx, sy)] = abs(sx-bx) + abs(sy-by)
        beacons.add((bx, by))

    # Part 1
    no_beacon_at = no_beacon_on_row(sensors, beacons)
    print(f'no beacon pos: {len(no_beacon_at):,}')
    print(f'beacon is at: {[b for b in beacons if b[1] == Y_POS_TO_CHECK]}')
    print(f'sensor is at: {[s for s in sensors.keys() if s[0] == Y_POS_TO_CHECK]}')
    print(f'unavailable positions: {len(no_beacon_at) - len([b for b in beacons if b[1] == Y_POS_TO_CHECK]):,}')

    # Part 2
    find_distress_beacon(sensors, beacons)        


def main():
    dl = load_data.DataLoader(day=15)
    data = dl.get_data(as_list=True)
    process_data(data)


if __name__=='__main__':
    main()

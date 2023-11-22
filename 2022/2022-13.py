import load_data

dl = load_data.DataLoader(day=13)
data = dl.get_data(as_list=False)


packet_pairs = data.split('\n\n')

from functools import cmp_to_key


def compare_packets(left_packet, right_packet) -> bool:
    '''Returns 
        True for left lower (correct oder)
        False for right lower (incorrect order)
        None for same (keep processing)
    '''
    # if isinstance(left_packet, int) and isinstance(right_packet, int)
    
    # If one of them are lists. Cast as list.
    if isinstance(left_packet, list) and isinstance(right_packet, int):
        right_packet = [right_packet]

    if isinstance(left_packet, int) and isinstance(right_packet, list):
        left_packet = [left_packet]

    if isinstance(left_packet, list) and isinstance(right_packet, list):
        # If left list runs out first, no issue. 
        for l, r in zip(left_packet, right_packet):
            # If right list shorter, then not correct. 
            res = compare_packets(l, r)
            if res is None:
                pass
            else:
                return res # res is True or False if not None.

        # If right is shorter than left. 
        if len(left_packet) < len(right_packet):
            return True
        elif len(left_packet) > len(right_packet):
            return False
        else:
            pass
        
    if isinstance(left_packet, int) and isinstance(right_packet, int):
        if left_packet < right_packet:
            return True
        elif left_packet > right_packet:
            return False
        else: 
            # if same integer, continue checking
            pass


def compare_packets_wrapper_for_sort(left, right) -> int:
    res = compare_packets(left,right)
    if res is None:
        return 0
    elif res == True:
        return 1
    else: 
        return -1
    

# Part 1
correct_order_indicies = []

for i, packet_pair in enumerate(packet_pairs):
    packet1, packet2 = packet_pair.split('\n')
    packet1 = eval(packet1)
    packet2 = eval(packet2)
    
    index = i + 1
    if compare_packets(packet1, packet2):
        correct_order_indicies.append(index)

print(correct_order_indicies)
print(sum(correct_order_indicies))


# Part 2
all_packets = []

for i, packet_pair in enumerate(packet_pairs):
    packet1, packet2 = packet_pair.split('\n')
    packet1 = eval(packet1)
    packet2 = eval(packet2)
    all_packets.append(packet1)
    all_packets.append(packet2)


divider_packet_1 = [[2]]
divider_packet_2 = [[6]]
all_packets.append(divider_packet_1)
all_packets.append(divider_packet_2)

sorted_packets = sorted(all_packets, key=cmp_to_key(compare_packets_wrapper_for_sort), reverse=True)
ind_1 = sorted_packets.index(divider_packet_1) + 1
ind_2 = sorted_packets.index(divider_packet_2) + 1
print('ind 1', ind_1)
print('ind 2', ind_2)
print('decoder key:', ind_1 * ind_2)

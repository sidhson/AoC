import os

def find_paths(starts : set, links : dict):
    paths_to_explore = [[s] for s in starts]
    paths_complete = []

    while len(paths_to_explore) > 0:
        path = paths_to_explore.pop()
        current = path[-1]

        if current == 'end':
            paths_complete.append(path)
        else:
            for next_cave in links[current]:
                path_add = path.copy()
                if next_cave.isupper() or next_cave not in path_add:
                    path_add.append(next_cave)
                    paths_to_explore.append(path_add)        
    return paths_complete

def find_paths_twice_allowed(starts : set, links : dict):
    paths_to_explore = [[s] for s in starts]
    paths_complete = []

    while len(paths_to_explore) > 0:
        path = paths_to_explore.pop()
        current = path[-1]

        if current == 'end':
            paths_complete.append(path)
        else:
            for next_cave in links[current]:
                path_add = path.copy()
                
                if next_cave.isupper() or next_cave not in path_add:
                    path_add.append(next_cave)
                    paths_to_explore.append(path_add)
                else: 
                    counts = [path.count(p) for p in path if p.islower()]
                    if all([nbr < 2 for nbr in counts]):
                        path_add.append(next_cave)
                        paths_to_explore.append(path_add)
    return paths_complete

if __name__ == '__main__':
    filename = 'input_' + os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    input_dir = os.path.join(os.path.dirname(__file__), 'input_2021', filename)
    with open(input_dir, 'r') as f:
        caves, starts = set(), set()
        link_list = list()
        
        for line in f.readlines():
            input_conn = line.strip().split('-')
            if 'start' in input_conn:
                input_conn.remove('start')
                starts.add(input_conn[0])
            else:
                caves.add(input_conn[0]), caves.add(input_conn[1])
                link_list.append(input_conn)
    
    links = dict()
    caves.remove('end')
    for cave in caves:
        cave_list = []
        for link in link_list:
            if cave in link:
                link_add = link.copy()
                link_add.remove(cave)
                cave_list.append(link_add[0])
        links[cave] = cave_list
    
    paths = find_paths(starts, links)
    print('Ans A:', len(paths))

    paths = find_paths_twice_allowed(starts, links)
    print('Ans B:', len(paths))

                

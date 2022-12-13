import load_data

dl = load_data.DataLoader(day=7)
data = dl.get_data(as_list=True)

from pathlib import Path
from dataclasses import dataclass


@dataclass
class Dir:
    file_path: Path
    size: int
    children: list

    def set_size(self):
        if not self.size:
            new_size = 0
            for c in self.children:
                # Set size of the child dirs that have not been set yet. 
                if not c.size:
                    c.set_size()
                
                new_size += c.size
            self.size = new_size

@dataclass
class File:
    file_path: Path
    size: int


root_path = Path()
root_dir = Dir(root_path, size=None, children=None)

dirs_list = [root_dir]
dirs_not_explored = [root_dir]


cmd_pos = 0
while cmd_pos < len(data):
    cmd = data[cmd_pos]

    # Update current path.
    if cmd[0:4] == '$ cd':
        _, _, cd_to = cmd.split()
        if cd_to == '/':
            current_path = root_path
        elif cd_to == '..':
            current_path = current_path.parent
        else:
            current_path = current_path / cd_to
        
        cmd_pos += 1
    

    # List all children of current dir and set as list in Dir object.
    elif cmd == '$ ls':
        dir_current = [dir for dir in dirs_not_explored if dir.file_path == current_path][0]
        dirs_list.append(dir_current)
        
        children = [] 
        while cmd_pos < len(data)-1 and data[cmd_pos+1][0] != '$': # while still listing dirs/files.
            cmd_pos += 1
            cmd_i = data[cmd_pos]

            if cmd_i.split()[0] != 'dir':
                size, file_name = cmd_i.split()
                children.append(File(current_path / file_name, size=int(size)))
                
            else:
                dir_name = cmd_i.split()[1]
                dir = Dir(current_path / dir_name, size=None, children=None)
                dirs_not_explored.append(dir)
                children.append(dir)
        
        dir_current.children = children
        cmd_pos += 1
        

# Initiates set size for all dirs
root_dir.set_size()


# Part 1
nbr_dirs_sub_100_000 = 0
total_size_dirs_sub_100_000 = 0
for dir in dirs_list: 
    if dir.size <= 100_000:
        nbr_dirs_sub_100_000 += 1
        total_size_dirs_sub_100_000 += dir.size
print(nbr_dirs_sub_100_000)
print(total_size_dirs_sub_100_000)


# Part 2
total_disk_space = 70_000_000
space_needed = 30_000_000
space_available = total_disk_space - root_dir.size 
space_to_remove = space_needed - space_available

print('current disk storage used', root_dir.size)
print('current disk storage available', space_available)
print('space needed to remove', space_to_remove)

dir_to_delete = root_dir
for dir in dirs_list:
    if dir.size >= space_to_remove and dir.size < dir_to_delete.size:
        dir_to_delete = dir

print('delete dir with size', dir_to_delete.size)

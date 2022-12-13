import load_data

dl = load_data.DataLoader(day=6)
data = dl.get_data(as_list=False)


# unique_chars = 4 # Part 1
unique_chars = 14 # Part 2

for pos in range(len(data)-unique_chars):
    marker = data[pos:pos+unique_chars]

    if len(set(marker)) == unique_chars:
        print(f'First unqique marker: {marker}. After processing: {pos + unique_chars}')
        break

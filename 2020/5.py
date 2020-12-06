
max_id = 0
ids = []
with open('5-input.txt', 'r') as f:
    for line in f:
        line = line.strip()

        row_char = line[:7]
        col_char = line[7:]

        row_bin = ""
        col_bin = ""

        for char in row_char:
            if char == 'B':
                row_bin += "1"
            else:
                row_bin += "0"

        for char in col_char:
            if char == 'R':
                col_bin += "1"
            else:
                col_bin += "0"

        row_num = int(row_bin, 2)
        col_num = int(col_bin, 2)

        seat_id = row_num * 8 + col_num

        #if seat_id > max_id:
            #max_id = seat_id

        ids.append(seat_id)

    ids.sort()

    prev = ids[0]
    for seat in ids:
        if prev + 1 != seat:
            print(prev)
            print(seat)
            print(ids[ids.index(seat)+1])
        prev = seat


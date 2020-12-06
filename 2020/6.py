
with open('6-input.txt', 'r') as f:
    total = 0

    answers = set()
    for line in f:

        if line =='\n':
            total += len(list(answers)) 

            answers = set()

        else:
            line = line.strip()
            for char in line:
                answers.add(char)


    total += len(list(answers)) 

    answers = set()
    
print(total)


with open('6-input.txt', 'r') as f:
    total = 0
    answers = ""
    total_ans = 0

    for line in f:
        if line == '\n':
            all_answered = []

            for ans in answers:
                if answers.count(ans) == total_ans and ans not in all_answered:
                    all_answered.append(ans)

            total += len(all_answered)

            answers = ""
            total_ans = 0

        else:
            answers += (line.strip())
            total_ans += 1

    all_answered = []

    for ans in answers:
        if answers.count(ans) == total_ans and ans not in all_answered:
            all_answered.append(ans)

    total += len(all_answered)

    answers = []
    total_ans = 0

print(total)

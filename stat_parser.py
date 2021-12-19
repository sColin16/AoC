from aoc_parser import read_stdin

from statistics import mean, median

class PartResult:
    def __init__(self, time, rank, global_score):
        self.time = time
        self.rank = rank
        self.global_score = global_score

    def tn_score(self, n):
        '''
        Computes a score based on performance in the top n places
        '''
        
        return max((n + 1) - self.rank, 0)

    def __repr__(self):
        return f'time: {self.time} rank: {self.rank} global_score: {self.global_score}'

def get_seconds(time_str):
    h, m, s = time_str.split(':')

    return 3600 * int(h) + 60 * int(m) + int(s)

def get_time_str(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds // 60) % 60)
    seconds = int(seconds % 60)

    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'

def parse_results():
    results = {}

    lines = read_stdin().split('\n')

    # First two lines are headers
    for line in lines[2:]:
        day, p1_time, p1_rank, p1_score, p2_time, p2_rank, p2_score = line.split()        

        p1_result = PartResult(get_seconds(p1_time), int(p1_rank), int(p1_score))
        p2_result = PartResult(get_seconds(p2_time), int(p2_rank), int(p2_score))

        results[int(day)] = [p1_result, p2_result]

    return results

def extract_partwise(results, callback):
    '''
    Extracts a list of statistics across all days for each part

    results is the dictionary storing the results from each day and part
    callback is executed on a PartResult object to extract a statistic
    '''
    
    p1_data = []
    p2_data = []

    for day, day_result in results.items():
        p1_data.append(callback(day_result[0]))
        p2_data.append(callback(day_result[1]))

    return p1_data, p2_data

def print_time(label, time):
    print(f'{label}: {get_time_str(time)}')

results = parse_results()

times = extract_partwise(results, lambda x: x.time)

p1_times = times[0]
overall_times = times[1]
delta_times = [overall_times[i] - p1_times[i] for i in range(len(p1_times))]

ranks = extract_partwise(results, lambda x: x.rank)

global_scores = extract_partwise(results, lambda x: x.global_score)
t500_scores = extract_partwise(results, lambda x: x.tn_score(500))
t1000_scores = extract_partwise(results, lambda x: x.tn_score(1000))

print_time('Mean part 1 time', mean(p1_times))
print_time('Mean delta time', mean(delta_times))
print_time('Mean completion time', mean(overall_times))
print()

print_time('Median part 1 time', median(p1_times))
print_time('Median delta time', median(delta_times))
print_time('Median completion time', median(overall_times))
print()

print_time('Total part 1 time', sum(p1_times))
print_time('Total delta time', sum(delta_times))
print_time('Total completion time', sum(overall_times))
print()

print(f'Mean part 1 rank: {mean(ranks[0])}')
print(f'Mean part 2 rank: {mean(ranks[1])}')
print(f'Mean rank overall: {mean(ranks[0] + ranks[1])}')
print()

print(f'Median part 1 rank: {median(ranks[0])}')
print(f'Median part 2 rank: {median(ranks[1])}')
print(f'Median rank overall: {median(ranks[0] + ranks[1])}')
print()

print(f'Sum part 1 rank: {sum(ranks[0])}')
print(f'Sum part 2 rank: {sum(ranks[1])}')
print(f'Sum rank overall: {sum(ranks[0] + ranks[1])}')
print()

print(f'Total part 1 global score: {sum(global_scores[0])}')
print(f'Total part 2 global score: {sum(global_scores[1])}')
print(f'Total overall global score: {sum(global_scores[0] + global_scores[1])}')
print()

print(f'Total part 1 t500 score: {sum(t500_scores[0])}')
print(f'Total part 2 t500 score: {sum(t500_scores[1])}')
print(f'Total overall t500 score: {sum(t500_scores[0] + t500_scores[1])}')
print()

print(f'Total part 1 t1000 score: {sum(t1000_scores[0])}')
print(f'Total part 2 t1000 score: {sum(t1000_scores[1])}')
print(f'Total overall t1000 score: {sum(t1000_scores[0] + t1000_scores[1])}')
print()

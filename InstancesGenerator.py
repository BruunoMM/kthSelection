import random
import LinearSelection
import BubbleSort
import time

# generate number instances for both algorithms
def generate_instances(size): 
    values = []
    for _ in range(size):
        value = random.randint(1,100000)
        values.append(value)
    
    return values

# uses linear selection to find kth element and measure its execution time
def get_linear_execution_time_for(values):
    instance_size = len(values)

    kLinearStart = time.time()
    k = instance_size // 2
    _ = LinearSelection.linear_selection(values, k)
    kLinearEnd = time.time()

    return kLinearEnd - kLinearStart

# uses sort selection with bubble sort to find kth element and measure its execution time
def get_bubble_execution_time_for(values):
    instance_size = len(values)

    kBubbleStart = time.time()
    k = instance_size // 2
    _ = BubbleSort.sort_selection(values, k)
    kBubbleEnd = time.time()

    return kBubbleEnd - kBubbleStart

def prepare_file():
    file = open('ComparisonResults.csv', 'w')
    file.write('Linear Selection, Bubble Sort Selection\n')
    file.close()


# write the results to a CSV file
def save_to_file(linearTime, bubbleTime):
    file = open('ComparisonResults.csv', 'a+')
    file.write('{},{}\n'.format(linearTime,bubbleTime))
    file.close()

STEP_SIZE = 1000
# runs both 
def comparison():
    prepare_file()
    for i in range(1,11):
        for _ in range(1):
            values = generate_instances(STEP_SIZE*i)
            linearTime = get_linear_execution_time_for(values)
            bubbleTime = get_bubble_execution_time_for(values)
            print('Linear Selection time: {}s | BubbleSort Selection time: {}s'.format(linearTime, bubbleTime))
            save_to_file(linearTime, bubbleTime)

comparison()
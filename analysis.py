def analyse_data(data):
    return sum(data) / len(data)



def filter_data(data, threshhold):
    return [d for d in data if d > threshhold]


data = [2,3,4,5,6]

print(filter_data(data,4))
from pprint import pprint

#Это метод выполняется за меньше итераций, но очень много кода(sory):)
def update(data, service, count):
    sum_gin,sum_cuc = sum(data['ginger'].values()),sum(data['cucumber'].values())
    if service not in data['ginger']:
        data['ginger'][service] = 0
    if service not in data['cucumber']:
        data['cucumber'][service] = 0
    if sum_gin == sum_cuc:
        count1 = count//2
        data['ginger'][service] += count1
        if count%2 != 0:
            data['cucumber'][service] += count1+1
        else:
            data['cucumber'][service] += count1
    else:
        if sum_gin > sum_cuc:
            pre_count = count - (count - (sum_gin - sum_cuc))
            next_count = count - (sum_gin - sum_cuc)
            data['cucumber'][service] += pre_count
        else:
            pre_count = count - (count - (sum_cuc - sum_gin))
            next_count = count - (sum_cuc - sum_gin)
            data['ginger'][service] += pre_count
        update(data, service, next_count)

#меньше кода, больше итераций.
def update_v1(data, service, count):
    sum_gin,sum_cuc = sum(data['ginger'].values()),sum(data['cucumber'].values())
    if service not in data['ginger']:
        data['ginger'][service] = 0
    if service not in data['cucumber']:
        data['cucumber'][service] = 0
    while count != 0:

        if sum_gin <= sum_cuc:
            data['ginger'][service] += 1
        elif sum_gin > sum_cuc:
            data['cucumber'][service] += 1
        count -= 1


def main():
    example_data = {
        'ginger': {
            'django': 0,
            'flask': 0,
        },
        'cucumber': {
            'flask': 0,
        },
    }

    print("Configuration before:")
    pprint(example_data)

    update(example_data, 'flask', 7)
    update(example_data, 'django', 7)

    print("Configuration after:")
    pprint(example_data)

if __name__ == '__main__':
    main()

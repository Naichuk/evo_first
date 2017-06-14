example_data = {
      'ginger': {
          'django': 0,
          'flask': 0,
      },
      'cucumber': {
          'flask': 0,
      },
  }

def update(data, service, count):
    sum_gin,sum_cuc = sum(data['ginger'].values()),sum(data['cucumber'].values())
    if service not in data['ginger']:
        data['ginger'][service] = 0
    if service not in data['cucumber']:
        data['cucumber'][service] = 0
    while count != 0:

        sum_gin, sum_cuc = sum(data['ginger'].values()), sum(data['cucumber'].values())

        if sum_gin < sum_cuc:
            data['ginger'][service] += 1
        elif sum_gin >= sum_cuc:
            data['cucumber'][service] += 1
        count -= 1
        print(count, sum_gin, sum_cuc)
    print(data)

update(example_data, 'flask', 7)
update(example_data,'pylons', 7)
update(example_data,'django', 25)

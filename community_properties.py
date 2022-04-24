
def unique_comm_ids(line):
    elem = line.split(',')
    comm_ids_list = []
    for e in elem:
        id = e.split(":")[1].strip()
        comm_ids_list.append(id)
    comm_ids = set(comm_ids_list)
    return comm_ids


def rotate(partition):
    community_dict = {}
    comm_ids = unique_comm_ids(partition)
    line_list_elem = partition.split(",")
    for comm_id in comm_ids:
        single_comm = []
        for e in line_list_elem:
            id = e.split(":")[1].strip()
            cell = e.split(":")[0].strip()
            if comm_id==id:
                single_comm.append(cell)
        community_dict[comm_id] = single_comm

    return community_dict


def avg_comm_size(comm_dict):
    keys = comm_dict.keys()
    values = comm_dict.values()
    size = len(comm_dict)
    sum = 0
    for val in values:
        sum = sum + len(val)
    avg_size = sum/size
    return avg_size


comm_prop = open("community_properties.csv", 'w')
comm_prop.write("ts,comm_num,avg_comm_size" + '\n')

with open("communities.csv", 'r') as communities:
    lines = communities.readlines()
    for line in lines[1:]:
        first = line.split('{')[0]
        second = line.split('{')[1]
        ts = first.split(',')[0]
        partition = second[:-2]
        comm_dict = rotate(partition)
        comm_num = len(comm_dict)
        avg_c_size = round(float(avg_comm_size(comm_dict)))
        comm_prop.write(str(ts) + ',' + str(comm_num) + ',' + str(avg_c_size) + '\n')

comm_prop.close()
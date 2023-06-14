import names
import random
import uuid
import numpy as np


passenger_count = 200
ticket_count = 300


# generate passenger data
csv_header = "id,first_name,last_name,employment_status"
passengers = []

for i in range(passenger_count):
    random.seed(uuid.uuid4())
    pid = "{:0>{}}".format(int(random.random() * 1_000_000), 6)
    fname, lname = names.get_full_name().split()
    estatus = random.choice(["employed", "employed", "student", "elderly"])

    csv_row = [pid, fname, lname, estatus]
    passengers.append(csv_row)

np.savetxt(
    fname="passenger.csv",
    header=csv_header,
    X=[x for x in passengers],
    delimiter=",",
    newline="\n",
    fmt="%s",
)


# generate train data
# done with excel


# generate station data
csv_header = "station_name"
stations = [
    "Nangang",
    "Taipei",
    "Banqiao",
    "Taoyuan",
    "Hsinchu",
    "Miaoli",
    "Taichung",
    "Changhua",
    "Yunlin",
    "Chiayi",
    "Tainan",
    "Zuoying",
]

np.savetxt(
    fname="station.csv",
    header=csv_header,
    X=[x for x in stations],
    delimiter=",",
    newline="\n",
    fmt="%s",
)


# generate stops_at data
csv_header = "train_number,day,station,stop_time"
stops_at = []

with open("DB_time_table.csv") as csv:
    lines = csv.readlines()
    lines = lines[1:]
    for line in lines:
        line_arr = line.split(",")
        train_num, day = line_arr[0], line_arr[1]
        stops = line_arr[2:]
        for i, stop in enumerate(stops):
            station = stations[i]
            stop = stop.rstrip()
            if stop != "null":
                csv_row = [train_num, day, station, stop]
                stops_at.append(csv_row)

np.savetxt(
    fname="stops_at.csv",
    header=csv_header,
    X=[x for x in stops_at],
    delimiter=",",
    newline="\n",
    fmt="%s",
)


# generate ticket data
csv_header = "ticket_nr,pid,train_num,day,from_station,to_station"
tickets = []

for i in range(ticket_count):
    random.seed(uuid.uuid4())
    ticket_nr = "{:0>{}}".format(int(random.random() * 1_000_000), 6)
    passenger_id = random.choice(passengers)[0]
    train = random.choice(stops_at)
    train_num = train[0]
    day = train[1]
    s_from = random.choice(stations)
    s_to = random.choice(stations)
    while s_from == s_to:
        s_to = random.choice(stations)
    csv_row = [ticket_nr, passenger_id, train_num, day, s_from, s_to]
    tickets.append(csv_row)

np.savetxt(
    fname="ticket.csv",
    header=csv_header,
    X=[x for x in tickets],
    delimiter=",",
    newline="\n",
    fmt="%s",
)


# generate between data
csv_header = "from_station,to_station, price"
between = []

prices = np.array(
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [70, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [200, 160, 130, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [330, 290, 260, 130, 0, 0, 0, 0, 0, 0, 0, 0],
        [480, 430, 400, 280, 140, 0, 0, 0, 0, 0, 0, 0],
        [750, 700, 670, 540, 410, 270, 0, 0, 0, 0, 0, 0],
        [870, 820, 790, 670, 540, 390, 130, 0, 0, 0, 0, 0],
        [970, 930, 900, 780, 640, 500, 230, 110, 0, 0, 0, 0],
        [1120, 1080, 1050, 920, 790, 640, 380, 250, 150, 0, 0, 0],
        [1390, 1350, 1320, 1060, 1060, 920, 650, 530, 420, 280, 0, 0],
        [1530, 1490, 1460, 1200, 1200, 1060, 790, 670, 560, 410, 140, 0],
    ]
)

for a in range(0, 12):
    for b in range(0, a):
        csv_row = [stations[a], stations[b], prices[a][b]]
        between.append(csv_row)

between_flipped = []
for line in between:
    csv_row = [line[1], line[0], line[2]]
    between_flipped.append(csv_row)

between += between_flipped

for i, station in enumerate(stations):
    csv_row = [stations[i], stations[i], 0]
    between.append(csv_row)

np.savetxt(
    fname="between.csv",
    header=csv_header,
    X=[x for x in between],
    delimiter=",",
    newline="\n",
    fmt="%s",
)

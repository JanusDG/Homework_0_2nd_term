import json
from dict_atd import Dictionary
from dict_usage import into_atd

with open("/home/janusdg/UCU/IT/Py/KURSOWA/useful/tracks_prof.json", 'r') as f:
    py = json.load(f)
    tracks = into_atd(py)

first_line = True
for key in tracks.keys:
    if key != "_USER_COUNTER":
        if first_line:
            line = "name"+";"+";".join([item for item in tracks[key].keys])+"\n"
            with open("tracks.csv", 'w') as f:
                f.write(line)
            first_line = False
        line = [tracks[key][item] for item in tracks[key].keys]
        if ";" in "".join([str(item) for item in line]):
            continue
        line[4] = ",".join(line[4])
        line_to_write = key+";"+";".join([str(item) for item in line]) + "\n"
        with open("tracks.csv", 'a') as f:
            f.write(line_to_write)
import json
import os
import os.path
import pandas as pd
import numpy as np

#preparation for access to video-IDs, labels and label indices
split_file = 'preprocess/nslt_100.json'
old_label_index = 'preprocess/wlasl_class_list.txt'

file = open(old_label_index, 'r')
lines = file.readlines()

classes = {}
content = json.load(open(split_file))
new_json = pd.read_json(split_file)

#open table with new labels and change old label indices to new labels in json file
new_labels_path = 'wlasl-alt-glosses.xlsx' 
df = pd.read_excel(new_labels_path, skiprows=1)
count = 0
for vid in content.keys():
    video_id = df.loc[df['video_id']== int(vid)]
    new_label = video_id["CLASS"].to_string(index=False).strip()
    classes_id = content[vid]['action'][0]
    old_label = lines[classes_id].upper().split('\t')[1].strip()
    if new_label == "Series([], )":
        if old_label not in classes:
            classes[old_label] = count
            count+=1
        content[vid]['action'][0] = old_label
    else:
        if new_label not in classes:
            classes[new_label] = count
            count+=1
        content[vid]['action'][0] = new_label
        
with open('nslt_100_alt_labels.json', 'w') as f:
    json.dump(content, f)


#write new labels with new indices to file
labels = [label for label in classes]

    

f = open("new_labels_indices.txt", "w")
i=0
while i < len(labels):
    f.write(str(i) + "\t" + labels[i] + "\n")
    i+=1
f.close()


#check for original label set length
def get_num_class(split_file):
    classes = set()

    content = json.load(open(split_file))

    for vid in content.keys():
        class_id = content[vid]['action'][0]
        
        classes.add(class_id)

    return len(classes)


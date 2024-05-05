import json
import os
import os.path
import pandas as pd

#save labels and indices in dictionary
old_label_indices = 'new_labels_indices.txt'
file = open(old_label_indices, 'r')
lines = file.readlines()

classes = {}
removed_labels = 0
for line in lines:
    label_id = int(line.split('\t')[0].strip())
    label = line.split('\t')[1].strip()
    classes[label_id]=label


#open json file with new labels
new_labels_path = 'nslt_100_alt_labels.json'
with open(new_labels_path, 'r') as j:
    new_json = json.loads(j.read())

#check whether each label occurs at least seven times in the dataset and create reduced list 'labels'
too_small = []
labels = []
# 168 because I have 168 different labels
for i in range(168):
    count = 0
    for vid in new_json.keys():
        if new_json[vid]['action'][0] == classes[i]:
            count += 1
    if count < 7:
        too_small.append(i)
    else:
        labels.append(classes[i])    

#delete videos to labels not occuring seven times
count=0
for label in too_small:
    for vid in list(new_json.keys()):
        if new_json[vid]['action'][0] == label:
            print('{} \'s label is not used often enough so the video will be taken out of the dataset.'.format(vid)) 
            del new_json[vid]
            count+=1
            
#save reduced dataset
with open('preprocess/nslt_100_alt_big.json', 'w') as fp:
    json.dump(new_json, fp)

#create new indices for reduced label list
file = open("final_labels_indices.txt", "w")
i=0
while i < len(labels):
    file.write(str(i) + ";" + labels[i] + "\n")
    i+=1
file.close()

#change json file: label names to final label indices
count = 0
file = open("final_labels_indices.txt", "r")
lines = file.readlines()
for vid in new_json.keys():
    #print(vid)  
    classes = new_json[vid]['action'][0]
    old_label = ''
    for line in lines:
        label_id = line.upper().split(';')[0].strip().replace('\'','')
        label = line.upper().split(';')[1].strip().replace('\n','')
        if label == classes:
            old_label = int(label_id)
            break
    new_json[vid]['action'][0] = old_label
   

with open('preprocess/nslt_100_alt_final.json', 'w') as f:
    json.dump(new_json, f)
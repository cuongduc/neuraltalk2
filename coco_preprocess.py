import os
import json

print "Download COCO annotatation file..."
os.system('wget http://msvocds.blob.core.windows.net/annotations-1-0-3/captions_train-val2014.zip -P coco/')

print "Unzip annotation file..."
os.system('unzip coco/captions_train-val2014.zip -d coco/')

val = json.load(open('coco/annotations/captions_val2014.json', 'r'))
train = json.load(open('coco/annotations/captions_train2014.json', 'r'))

print "Combine all images and annotations together"
imgs = val['images'] + train['images']
annos = val['annotations'] + train['annotations']

itoa = {}
for a in annos:
    imgid = a['image_id']
    if not imgid in itoa:
        itoa[imgid] = []
    itoa[imgid].append(a)

print "Create json blob"
out = []
for i, img in enumerate(imgs):
    imgid = img['id']

    loc = 'train2014' if 'train' in img['file_name'] else 'val2014'

    jimg = {}
    jimg['file_path'] = os.path.join(loc, img['file_name'])
    jimg['id'] = imgid

    sents = []
    annotsi = itoa[imgid]
    for a in annotsi:
        sents.append(a['caption'])
    jimg['captions'] = sents
    out.append(jimg)

print "Write output file..."
json.dump(out, open('coco/coco_raw.json', 'w'))

import keyvalue.sqlitekeyvalue as KeyValue
import keyvalue.parsetriples as ParseTriple
import keyvalue.stemmer as Stemmer

# Make connections to KeyValue
kv_labels = KeyValue.SqliteKeyValue("sqlite_labels.db", "labels", sortKey=True)
kv_images = KeyValue.SqliteKeyValue("sqlite_images.db", "images", sortKey=True)

# Process Logic.
print("-------------------------------------------")
labelsDataset = ParseTriple.ParseTriples('./datasets/labels_en.ttl');

for i in range(1,1000):
    word = labelsDataset.getNext()
    category = word[0]
    label = word[2]
    steam = Stemmer.stem(label)
    for x in steam.split(' '):
        print("category: " + category + " ____________ labe:" + x)
        kv_labels.putSort(x, i,category)

print("-------------------------------------------")

print("-------------------------------------------")
imagesDataset = ParseTriple.ParseTriples('./datasets/images.ttl')
for i in range(0,4000):
    img = imagesDataset.getNextImage()
    category = img[0]
    imgPath = img[2]
    print("category: " + category + " _________ imgPath: " + imgPath)
    kv_images.putSort(category, i, imgPath)



# Close KeyValues Storages
kv_labels.close()
kv_images.close()
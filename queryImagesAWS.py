import keyvalue.dynamostorage as KeyValue
import keyvalue.stemmer as Stemmer
import sys

# Make connections to KeyValue
kv_labels = KeyValue.DynamoDbKeyValue( "labels")
kv_images = KeyValue.DynamoDbKeyValue( "images")


def searchlabels(key):
    if key and key != '':
        response = kv_labels.get(key,len(key))
        if response.get('Item'):
            item = response['Item']
            value = item['value']
            return value['S']
    return


def searchimg(key):
    if key and key != '':
        response = kv_images.get(key,len(key))
        if response.get('Item'):
            item = response['Item']
            value = item['value']
            return value['S']
    return


def search(args):
    results = []
    for word in args:
        stem = Stemmer.stem(word)
        category = searchlabels(stem)
        if category:
            img = searchimg(category)
            if img:
                results.append({'category': stem, 'img': img})
                print(stem + " : " + img)
    return results


#sys.argv.pop(0)
#args = sys.argv
# Process Logic.
#args = ['south', 'america', 'england', 'chinese', 'abraham', 'beer', 'apollo', 'acid', 'africa', 'alaska']
#search(args)

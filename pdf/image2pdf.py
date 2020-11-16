#!/bin/bash
from PIL import Image
import uuid
import sys

def convert(image):
    uuid_set = str(uuid.uuid4().fields[-1])[:5]
    path = "/tmp/temp%s.pdf" % uuid_set
    try:
        img = Image.open(image)
        pdf = img.convert('RGB')
        pdf.save(path)
    except Exception, err:
        print(err)
        return False
    return path

if __name__ == "__main__":
    arg = sys.argv[1]
    result = convert(arg)
    if result:
        print "[*] Success convert %s and save it to %s" % (arg, result)
    else:
        print "[!] Whoops. something wrong dude. enable err var to track it"

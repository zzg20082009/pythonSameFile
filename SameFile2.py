import hashlib  
import os
import datetime
import Queue


def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    fh = file(filename, 'rb')
    while True:
        b = fh.read(8192)
        if not b:
            break
        myhash.update(b)
    fh.close()
    return myhash.hexdigest()

if __name__ == "__main__" :
    
    '''Get Filename in a folder first, then calculate it's md5'''
    '''We use mapofmd5 to store file's md5 sum value'''

    dirs = Queue.Queue(0)
    allfile = []
    
    filepath = raw_input("Please Input The File Folder to Inspect: ")
    
    dirs.put(filepath)
    while not dirs.empty():
        work_dir = dirs.get()
        fullname  = (os.path.join(work_dir, filename) for filename in os.listdir(work_dir))

        for fobj in fullname:
            if os.path.isfile(fobj):
                allfile.append(fobj)
            elif os.path.isdir(fobj):
                # if fobj == '.' or fobj == '..':
                #    continue
                # print fobj + " sub dir goes into the queue"
                dirs.put(fobj)

    mapofmd5 = { }
    dupofmd5 = { }

    totalrm = 0
    
    for f in allfile:
        md5sum = GetFileMd5(f)
        if md5sum in mapofmd5.keys():
            print f + " is the same as " + mapofmd5[md5sum]
            dupofmd5[f] = mapofmd5[md5sum]
            os.remove(f)
            totalrm += 1
        else:
            mapofmd5[md5sum] = f

    for key in dupofmd5.keys():
        print "file is  " + key + " is same with " + dupofmd5[key] + " deleted!"

    print "total " + str(totalrm) + " files are deleted!"
        

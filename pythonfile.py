# metod is expecting and call the number of records and filename
def descRecords(fileName,noofrecords):
    dict = {}
    # Handle FileNotFoundException
    try:
        f = open(fileName, 'rb')
        # i is to check the line number
        i=0
        for line in f:
            key, value = line.strip().split(': ')
            # Increment index to find line number
            i=i+1
            # throw excpetion if key is not int
            if not key.isdigit():
                raise ValueError("Key should be integer, Error at line#",i,line)
            # Handle invalid JSON
            try:
                data=json.loads(value)
                # insert id value into dictionary 
                dict[key.strip()] = data['id'] 
                # throw error when id is not available in json
                if "id" not in data:
                    raise ValueError("Invalid JSON missing id in document",i,line)
            except ValueError as jsonErr: 
                print("Invalid JSON error :{0}".format(jsonErr), "line# : ",i,"Document : ",line)

    except OSError as err:
        print("OS error: {0}".format(err))
    finally:
        f.close()   

    sortScore = sorted(dict.items(),reverse=True)[:noofrecords]
    # to display parsed json dictionary value in pretty print with indent
    print (json.dumps([{'score': k, 'id': v} for k,v in sortScore], indent=2))
            

if __name__ == "__main__":
    import json
    import sys
    # Pass the filename argv[1] and number of recrods as argv[2]
    descRecords(str(sys.argv[1]),int(sys.argv[2]))
import csv
import json

def to_csv(dst_file, src_file):
    with open(dst_file, 'wb') as csvfile:
        fieldnames = ['time', 'deviceNo', 'routeId', 'staId', 'direction']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()

        cnt = 0
        with open(src_file) as origin_file:
            try:
                for line in origin_file:
                    # cnt += 1
                    # if cnt > 10:
                    #     break

                    line = line.strip('\n')
                    # print line
                    # {time=1484064001,deviceNo=50027605,routeId=751,staId=25399,direction=4}
                    csvline = line.replace('time=', '"time":').replace('deviceNo=', '"deviceNo":').replace('routeId=', '"routeId":').replace('staId=', '"staId":').replace('direction=', '"direction":')

                    # print(csvline)
                    csvrow = json.loads(csvline)
                    print(csvrow)

                    csv_writer.writerow(csvrow)
            except:
                print("except...")
            else:
                print("finished ...")


if __name__ == '__main__':
    src_file = './dxt.log'
    dst_file = './csv.csv'

    to_csv(dst_file, src_file)

    # csvstr = '{"time":1484064040,"deviceNo":50069651,"routeId":754,"staId":30877,"direction":5}'
    # dictObj = json.loads('{time:1484064001,"deviceNo":50027605,"routeId":751,"staId":25399,"direction":4}')
    # dictObj = json.loads('{time:1484064001,deviceNo:50027605,routeId:751,staId:25399,direction:4}')
    # dictObj = json.loads(csvstr)
    # print(dictObj)

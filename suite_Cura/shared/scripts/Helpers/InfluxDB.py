from influxdb import InfluxDBClient


class InfluxDB:
    def __init__(self, host='10.183.1.147', port=8086):
        user = 'cura'
        password = 'oCxh9RN3bvtx68SvePPivJdLceJE2uVnjknczwXAW6BWbFLThYej4AuY5rMvPGZL'
        dbname = 'cura'

        self.client = InfluxDBClient(host, port, user, password, dbname)

    def write(self, data):
        print(f"Writing data ...")
        self.client.write_points(data)

indb = InfluxDB()

import urllib.request

config = open("config.txt", 'r')

path = config.readline().split("=")[1][1:-1]
homeLatitude = config.readline().replace(" ", "").strip().split("=")[1]
homeLongitude = config.readline().replace(" ", "").strip().split("=")[1]

data = urllib.request.urlopen("http://10.31.65.72:8000/get_coords")

coords = str(data.read())[2:-1].split(",")

destLat = coords[0]
destLong = coords[1]
destAlt = coords[2]

print(homeLatitude)
print(homeLongitude)
print(destLat)
print(destLong)
print(destAlt)

path = path + "/way.waypoints"
print(path)
wp = open(path, 'w')

wp.write("QGC WPL 110\n")
wp.write("0\t1\t0\t16\t0\t0\t0\t0\t" + homeLatitude + "\t" + homeLongitude + "\t" + "0.000000\t1\n")
wp.write("1\t0\t0\t22\t0.000000\t0.000000\t0.000000\t0.000000\t0.000000\t0.000000\t10.000000\t1\n")
wp.write("2\t0\t0\t16\t0.000000\t0.000000\t0.000000\t0.000000\t" + destLat + "\t" + destLong + "\t10.000000\t1\n")
wp.write("3\t0\t0\t20\t0.000000\t0.000000\t0.000000\t0.000000\t0.000000\t0.000000\t0.000000\t1")
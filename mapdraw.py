#HEAVILY borrows from the gmplot project here: https://github.com/vgm64/gmplot/tree/master/gmplot

def drawmap(filename, apikey, options, markers):
    f = open(filename, 'w')
    f.write('<html>\n')
    f.write('<head>\n')
    f.write('<meta name="viewport" content="initial-scale=1.0, user-scalable=no" />\n')
    f.write('<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>\n')
    f.write('<title>Google Maps - gmplot </title>\n')
    f.write('<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?libraries=visualization&sensor=true_or_false&key=%s"></script>\n' % apikey )
    f.write('<script type="text/javascript">\n')
    f.write('\tfunction initialize() {\n')

    write_map(options, f)
    write_markers(markers, f)

    f.write('\t}\n')
    f.write('</script>\n')
    f.write('</head>\n')
    f.write('<body style="margin:0px; padding:0px;" onload="initialize()">\n')
    f.write('\t<div id="map_canvas" style="width: 100%; height: 100%;"></div>\n')
    f.write('</body>\n')
    f.write('</html>\n')
    f.close()


def write_markers(markers, f):
    for marker in markers:
        write_marker(f, marker[0], marker[1], marker[2], marker[3])


def write_marker(f, lat, long, color, title):
    f.write('\t\tvar latlng = new google.maps.LatLng(%f, %f);\n' %(lat, long))
    f.write('\t\tvar img = new google.maps.MarkerImage(\'{0}\');\n'.format("static/markers/" + color + ".png"))
    f.write('\t\tvar marker = new google.maps.Marker({\n')
    f.write('\t\ttitle: "%s",\n' % title)
    f.write('\t\ticon: img,\n')
    f.write('\t\tposition: latlng\n')
    f.write('\t\t});\n')
    f.write('\t\tmarker.setMap(map);\n')
    f.write('\n')


def write_map(options, f):
    f.write('\t\tvar centerlatlng = new google.maps.LatLng(%f, %f);\n' %(options[0], options[1]))   #0 and 1 are starting lat and long coords
    f.write('\t\tvar myOptions = {\n')
    f.write('\t\t\tzoom: %d,\n' % (options[2])) #zoom level
    f.write('\t\t\tcenter: centerlatlng,\n')
    f.write('\t\t\tmapTypeId: google.maps.MapTypeId.ROADMAP\n')
    f.write('\t\t};\n')
    f.write('\t\tvar map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);\n')
    f.write('\n')
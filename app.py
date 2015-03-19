try:
    # Python 2
    from StringIO import StringIO as BytesIO
    from urllib import quote
except ImportError:
    # Python 3
    from io import BytesIO
    from urllib.parse import quote
import mimetypes
import logging, sys
import simplejson as json
import requests
from flask import Flask, request, make_response, redirect


app = Flask(__name__)
app.debug = True 
app.logger.setLevel(logging.DEBUG)
del app.logger.handlers[:]

handler = logging.StreamHandler(stream=sys.stdout)
handler.setLevel(logging.DEBUG)
handler.formatter = logging.Formatter(
    fmt=u"%(asctime)s level=%(levelname)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
)
app.logger.addHandler(handler)


# subject, status, color, format
SHIELD_URL = "http://img.shields.io/badge/%s-%s-%s.%s"
PACKAGE_CONTROL_URL = "https://packagecontrol.io/packages/%s.json"

def write_shield(subject, count, color, format, endpoint=SHIELD_URL):
    '''Obtain and write the shield to the response.'''
    shield_url = endpoint % (
        subject,
        count,
        color,
        format
    )
    shield_response = requests.get(shield_url)
    img = BytesIO(shield_response.content)
    img.seek(0)
    return img

def format_number(singular, number):
    value = singular % {'value': number}
    # Get rid of the .0 but keep the other decimals
    return value.replace('.0', '')

intword_converters = (
    (3, lambda number: format_number('%(value).1fk', number)),
    (6, lambda number: format_number('%(value).1fM', number)),
    (9, lambda number: format_number('%(value).1fB', number)),
)
def intword(value):
    try:
        value = int(value)
    except (TypeError, ValueError):
        return value

    if value < 1000:
        return str(value)

    for exponent, converters in intword_converters:
        large_number = 10 ** exponent
        if value < large_number * 1000:
            new_value = value / float(large_number)
            return converters(new_value)

@app.route('/', methods=['GET'])
def index():
    return redirect('https://github.com/geekpradd/Package-Control-Badges')

@app.route('/downloads/<package>.<format>', methods=['GET'])
def downloads(package,format='svg'):
    package_json = json.loads(requests.get(PACKAGE_CONTROL_URL % quote(package)).text)
    installs = intword(package_json['installs']['total'])

    if request.args.get('color') is None:
        color = "orange"
    else:
        color = request.args.get('color')

    if not request.args.get('style') is None:
        base_endpoint = '{0}?style={1}'.format(SHIELD_URL, request.args.get('style'))
    else:
        base_endpoint = SHIELD_URL
    print (base_endpoint)
    img = write_shield("Package Control", installs, color, format)
    resp = make_response(img.read())
    ##If SVG file is requested
    if format=="svg":
        resp.headers['Content-type'] = "image/svg+xml"
    else:
        resp.headers['Content-Type'] = mimetypes.types_map[".{0}".format(format)]
    return resp

if __name__ == "__main__":
    if '.svg' not in mimetypes.types_map:
        mimetypes.add_type("image/svg+xml", ".svg")
    app.run()


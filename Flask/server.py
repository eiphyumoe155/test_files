import time
from flask import Flask, Response, stream_with_context
import os

app = Flask(__name__)

@app.route('/stream')
def stream():
    def gen():
        i = 0
        while True:
            data = 'this is line {}'.format(i)
            print(data)
            yield data + '<br>'
            i += 1
            time.sleep(1)

    return Response(stream_with_context(gen()))



if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
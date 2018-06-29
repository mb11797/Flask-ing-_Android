from flask import Flask, jsonify, request

app = Flask(__name__)

# root

@app.route("/")
def index():
    """
    this ia a root dir of my server
    :return: str
    """
    return "This is root !!!"

# GET
@app.route('/users/<user>')
def hello_user(user):
    '''
    This serves as a demo purpose
    :param user:
    :return: str
    '''
    return "Hello %s !" % user

# POST
@app.route('/api/post_some_data', methods=['POST'])
def get_text_prediction():
    '''
    predicts requested text whether it is ham or spam
    :return: json
    '''
    json = request.get_json()
    print(json)

    if len(json['text']) == 0:
        return jsonify({'error' : 'invalid input'})

    return jsonify({'You sent this ' : json['text']})


# running web app in local machine
if __name__ == '__main__':
    # app.run(host='10.244.1.42')
    # app.run(host='0.0.0.0', port=8080)
    # app.run(host='10.244.1.42', port=4000)
    # app.run(host='10.244.1.42', port=8085)
    app.run(host='0.0.0.0', port=5000)



# # development way
# if __name__ == '__main__':
#     app.run()
#
# ##server on https://127.0.0.1:5000/
# ## (invisible across the network) won't work on other device, other than development machine
#
# # suggested way
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
#
# ## server on http://0.0.0.0:5000/
# ## visible accross the network
# ## BaseUrl for Android http://<your ip address>:5000/blah/blah
#
#
# # hackiest way (not preferred)
# if __name__ == '__main__':
#     app.run(host='<your ip address>')
#
# ## server on http://<your ip address>:5000/
# ## visible across the network
# ## BaseUrl for Android http://<your ip address>:5000/blah/blah
# ## whereas port=5000







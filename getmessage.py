# import the requests library so we can use it to make REST calls
import requests

from constants import token

# disable warnings about using certificate verification
requests.packages.urllib3.disable_warnings()

# the main function
def main(message_id):

    # add authorization to the header
    header = {"Authorization": "Bearer %s" % token}

    # create request url using message ID
    get_rooms_url = "https://api.ciscospark.com/v1/messages/" + message_id

    # send the GET request and do not verify SSL certificate for simplicity of this example
    api_response = requests.get(get_rooms_url, headers=header, verify=False)

    # parse the response in json
    response_json = api_response.json()

    # get the text value from the response
    text = response_json["text"]

    # return the text value
    return text

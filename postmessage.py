# import the requests library so we can use it to make REST calls
import requests, json

from constants import token

# disable warnings about using certificate verification
requests.packages.urllib3.disable_warnings()

# the main function
def main(room_id, text):

    # add authorization to the header
    header = {"Authorization": "Bearer %s" % token, "content-type": "application/json"}

    # specify request url
    post_message_url = "https://api.ciscospark.com/v1/messages"

    # create message in Spark room
    payload = {
        "roomId" : room_id,
		"text" : text,
    }

    # create POST request do not verify SSL certificate for simplicity of this example
    api_response = requests.post(post_message_url, json=payload, headers=header, verify=False)

    # get the response status code
    response_status = api_response.status_code

    # return the text value
    print(response_status)

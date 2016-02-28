# import the requests and json library so we can use it to make REST calls
import requests, json

from constants import token, room_id, webapp_url, webhook_name


# the main function
def main():

    # add authorization to the header
    header = {"Authorization": "Bearer %s" % token, "content-type": "application/json"}

    # disable warnings about using certificate verification
    requests.packages.urllib3.disable_warnings()

    # create request url
    post_message_url = "https://api.ciscospark.com/v1/webhooks"

    # create request body
    payload = {
        "resource": "messages",
        "event": "created",
        "filter": "roomId={room_id}".format(room_id=room_id),
        "targetUrl": "{url}".format(url=webapp_url),
        "name": "{webhook_name}".format(webhook_name=webhook_name)
    }

    # send the POST request resource and do not verify SSL certificate for simplicity of this example
    api_response = requests.post(post_message_url, json=payload, headers=header, verify=False)

    # get the response status code
    response_status = api_response.status_code

    # print the status code
    print(response_status)


if __name__ == "__main__":
    main()

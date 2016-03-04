Get it running locally:

* Spin up an AWS instance, or another cloud based VM with public IP addresses.
* Ensure the TCP port 5000 is globally accessible.  In AWS this control is located in the security group.
* Check out the code onto your VM:
    *git clone https://github.com/AustinHyland/spark-webhooks-sample.git

Dependencies:
Install python 3.4:
    * pip install python3.4
Install 'pip' for python 3.4:
    * wget https://bootstrap.pypa.io/get-pip.py 
    * python3.4 get-pip.py
Install the python dependencies:
    * pip3.4 install -r requirements.txt
* Run the app with: 
    python3.4 webhookapp.py


-----


Overview:

constants.py:

* defines constants that will be used in most files.

webhookapp.py:

* Defines the flask route '/webhook' that the spark webhook will POST to.
* registers the webhook with the spark servers
    * Botson webhook listens for a magic word and sends a response.
* Starts the main flask webapp.

register_webhook.py:

* GETs a list of active webhooks for the room.
* Iterates over the list.  If any of the active webhooks have the same name as our hook
DELETE them and POST a new webhook with our current IP address.

postwebhook.py:

creates a new webhook.

getmessage.py:

converts a message_id into the text of a message.

postmessage.py:

takes a room id, and a string, and posts the string into the room.
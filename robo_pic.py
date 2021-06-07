import numpy as np
from PIL import Image
import requests


original_image_url = "https://www.lufthansa-industry-solutions.com/fileadmin/_processed_/2/6/csm_kuenstliche-intelligenz-lhind_2be8820fbc.png"

orig_image = Image.open(requests.get(original_image_url, stream=True).raw)
orig_image.show()

edited_img = Image.open("our_robot_has_a_message_for_you.png")
edited_img.show()


# Hiding a message in plain sight. 
# One of our daily missions is to retrieve information out of data. 
# Like in this case where you can see the data clearly with your eyes, but not the hidden information.
# Are you able to extract it?
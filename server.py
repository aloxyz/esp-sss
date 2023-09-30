import sss, re
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")
    
    # Use regular expression to find all tuples in the string
    msg_string = re.findall(r'\((\d+), (\d+)\)', msg.payload.decode())
    shares = [(int(x), int(y)) for x, y in msg_string]

    reconstructed_secret = sss.shamir_reconstruct(shares)
    
    print('reconstructed secret:', reconstructed_secret)

if __name__ == '__main__':
    client = mqtt.Client('sss_server')
    client.message_callback_add('sss', on_message)

    client.connect("localhost", 1883, 60)
    client.subscribe('sss')
    client.loop_forever()
import paho.mqtt.client as mqtt
import redis

redis_conn = redis.Redis(host='localhost', port = 6379, password = 'raspberry')


def on_message(mosq, obj, msg):
    topic = msg.topic
    message = msg.payload.decode('utf-8')  #接收需要解碼
    redis_conn.rpush(topic,message)
    print(f'topic={topic}, message:{message}')  #注意大括號
    

if __name__ == '__main__':  #以下是老師新寫法
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_message = on_message
    client.connect('127.0.0.1')
    client.subscribe('501教室/老師桌燈', qos = 2)
    client.loop_forever()

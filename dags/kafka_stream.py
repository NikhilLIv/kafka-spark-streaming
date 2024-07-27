#importing libraries

from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import uuid

default_args ={
    'owner':'Nikhil',
    'start_date': datetime(2024,7,24,12,00)
}

#function to get data from api
def get_data():
    import requests

    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]

    return res

#function to modify data into suitable format
def format_data(res):
    data = {}
    location = res['location']
    data['id'] = str(uuid.uuid4())
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data

#function to stream data into kafka
def stream_data():
    
    import json
    from kafka import KafkaProducer
    import time
    import logging
    
    producer=KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=15000)
    curr_time=time.time()
    
    while True:
        if time.time()>curr_time+300:#5 minutes
            break
        try:
            res=get_data()
            res=format_data(res)
            producer.send('users_created', json.dumps(res).encode('utf-8'))
        except Exception as e:
            logging.error(f'An error occured: {e}')
            continue

#dag definition
with DAG('user_automation',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:
    
        streaming_task=PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data
    )
           

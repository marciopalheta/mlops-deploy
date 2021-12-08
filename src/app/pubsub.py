# -*- coding: utf-8 -*-

# https://cloud.google.com/pubsub/docs/quickstart-client-libraries

# Criação do tópico
# (uea_api) $ gcloud pubsub topics create topic-new-score-created
# Criação da assinatura
# (uea_api) $ gcloud pubsub subscriptions create sub-new-score-created --topic topic-new-score-created

# Instalação do módulo
# (uea_api) $ pip install --upgrade google-cloud-pubsub

# VARIAVEIS DE AMBIENTE
# (uea_api) $ export GCP_PROJECT=mlops-uea-2 
# (uea_api) $ export GOOGLE_APPLICATION_CREDENTIALS="mlops-uea-2-service-account.json"

# (uea_api) $ pip install google
# (uea_api) $ pip install --upgrade google-api-python-client
from google.cloud import pubsub_v1
import os

def publish_new_score_topic(msg):
    project_id = os.environ.get('GCP_PROJECT')
    topic_id = "topic-new-score-created"

    publisher = pubsub_v1.PublisherClient()
    # The `topic_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/topics/{topic_id}`
    topic_path = publisher.topic_path(project_id, topic_id)

    # Data must be a bytestring
    data = msg.encode("utf-8")
    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data)
    print(future.result())
    print(f"Published messages to {topic_path}.")

    return future

if __name__ == '__main__':
    publish_new_score_topic('{"cpf":123456789,"request_date":"2021-01-01", "score":750}')
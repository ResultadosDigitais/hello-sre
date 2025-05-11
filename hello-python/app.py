import os, pika
from flask import Flask, request, jsonify

app = Flask(__name__)

host = os.getenv("RABBITMQ_HOST", "localhost")
port = os.getenv("RABBITMQ_PORT", 5672)
queue = os.getenv("RABBITMQ_QUEUE", "hello")
# import json
from dataclasses import dataclass
from datetime import datetime

# import requests
from flask import Flask, request

# from flask import g
# from google.cloud import firestore_v1

# def get_db() -> firestore_v1.Client:
#     if "db" in g:
#         return g.db
#     db = firestore_v1.Client()
#     g.db = db
#     return g.db

app = Flask(__name__)


@app.route("/")
def hello():
    return {'ok': 'hello'}, 200


@app.route("/hi/<name>")
def hi(name):
    return {"user": name}


@app.route("/mail", methods=["POST"])
def mail():
    d = request.json
    # print('\n data:', d)
    print('\n mail:')
    print('from', d['headers']['from'])
    print('from', d['headers']['from'])
    print('message_id', d['headers']['message_id'])
    print('date', d['headers']['date'])
    print('plain', d['plain'])
    # print('html', d['html'])
    return 'ok', 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8085", debug=True)

# @dataclass
# class Base:
#     def to_dict(self):
#         return {k: v for k, v in self.__dict__.items() if v is not None}

#     @classmethod
#     def from_dict(cls, d: dict) -> 'Base':
#         return cls(**d)

# @dataclass
# class Headers(Base):
#     frm: str
#     to: str
#     date: datetime
#     message_id: str
#     subject: str

#     @classmethod
#     def from_dict(cls, d: dict) -> 'Base':
#         return cls(**d)

# @dataclass
# class Mail(Base):
#     plain: str
#     html: str
#     headers: Headers

#     @classmethod
#     def from_dict(cls, d: dict) -> 'Base':
#         return cls(**d)

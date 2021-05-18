import json

import pytest
# from google.cloud import firestore_v1
from src import main

# from datetime import datetime, timezone

# import testconf

# import sys  # isort:skip

# # sys.path.append("src")
# sys.path.append("/Users/v/code/nikita/aika-mail/src")


@pytest.fixture
def client():
    with main.app.test_client() as client:
        yield client


def test_hello_get(client):
    response = client.get("/")
    assert response.status_code == 200
    d = response.get_json()
    assert d["ok"] == 'hello'


def test_mail(client):
    body = {
        "headers": {
            "return_path":
            "from@example.com",
            "received": [
                "by 10.52.90.229 with SMTP id bz5cs75582vdb; Mon, 16 Jan 2012 09:00:07 -0800",
                "by 10.216.131.153 with SMTP id m25mr5479776wei.9.1326733205283; Mon, 16 Jan 2012 09:00:05 -0800",
                "from mail-wi0-f170.google.com (mail-wi0-f170.google.com [209.85.212.170]) by mx.google.com with ESMTPS id u74si9614172weq.62.2012.01.16.09.00.04 (version=TLSv1/SSLv3 cipher=OTHER); Mon, 16 Jan 2012 09:00:04 -0800"
            ],
            "date":
            "Mon, 16 Jan 2012 17:00:01 +0000",
            "from":
            "Message Sender <sender@example.com>",
            "to":
            "Message Recipient<to@example.co.uk>",
            "message_id":
            "<4F145791.8040802@example.com>",
            "subject":
            "Test Subject",
            "mime_version":
            "1.0",
            "content_type":
            "multipart/alternative; boundary=------------090409040602000601080801",
            "delivered_to":
            "to@example.com",
            "received_spf":
            "neutral (google.com: 10.0.10.1 is neither permitted nor denied by best guess record for domain of from@example.com) client-ip=10.0.10.1;",
            "authentication_results":
            "mx.google.com; spf=neutral (google.com: 10.0.10.1 is neither permitted nor denied by best guess record for domain of from@example.com) smtp.mail=from@example.com",
            "user_agent":
            "Postbox 3.0.2 (Macintosh/20111203)"
        },
        "envelope": {
            "to": "to@example.com",
            "from": "from@example.com",
            "helo_domain": "localhost",
            "remote_ip": "127.0.0.1",
            "recipients": ["to@example.com", "another@example.com"],
            "spf": {
                "result": "pass",
                "domain": "example.com"
            },
            "tls": 'true',
        },
        "plain":
        "Test with HTML.",
        "html":
        "<html><head>\n<meta http-equiv=\"content-type\" content=\"text/html; charset=ISO-8859-1\"></head><body\n bgcolor=\"#FFFFFF\" text=\"#000000\">\nTest with <span style=\"font-weight: bold;\">HTML</span>.<br>\n</body>\n</html>",
        "reply_plain":
        "Message reply if found.",
        "attachments": [{
            "content": "dGVzdGZpbGU=",
            "file_name": "file.txt",
            "content_type": "text/plain",
            "size": 8,
            "disposition": "attachment"
        }, {
            "content": "dGVzdGZpbGU=",
            "file_name": "file.txt",
            "content_type": "text/plain",
            "size": 8,
            "disposition": "attachment"
        }]
    }

    resp = client.post(
        '/mail',
        data=json.dumps(body),
        content_type="application/json",
    )
    assert resp.status_code == 200


def test_hi(client):
    response = client.get("/hi/bro")
    assert response.status_code == 200
    d = response.get_json()
    assert d["user"] == "bro"


def test_not_found(client):
    response = client.get("/noexist")
    assert response.status_code == 404


#

#

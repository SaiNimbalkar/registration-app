from app.app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_register_success():
    client = app.test_client()
    response = client.post('/register', data={
        'name': 'Sai',
        'email': 'sai@test.com'
    })
    assert b"registered successfully" in response.data

def test_register_fail():
    client = app.test_client()
    response = client.post('/register', data={
        'name': '',
        'email': ''
    })
    assert b"Error" in response.data
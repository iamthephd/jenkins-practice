# Testing if the project is working correctly
import requests

def test_api():
    response = requests.get('http://localhost:8000/')
    assert response.status_code == 200
    data = response.json()
    assert 'message' in data
    assert data['message'] == 'Hello World!'

if __name__ == "__main__":
    test_api()
    print("All tests passed!")
import pytest
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_prediction_case_8_0():
    payload = {
        "rollNo": "21CS417",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.41,
        "activeBacklogs": 3,
        "attendance": 61.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_1():
    payload = {
        "rollNo": "21CS736",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.49,
        "activeBacklogs": 1,
        "attendance": 68.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_2():
    payload = {
        "rollNo": "21CS942",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.23,
        "activeBacklogs": 2,
        "attendance": 39.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_3():
    payload = {
        "rollNo": "21CS903",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.01,
        "activeBacklogs": 5,
        "attendance": 96.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_4():
    payload = {
        "rollNo": "21CS620",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.72,
        "activeBacklogs": 1,
        "attendance": 66.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_5():
    payload = {
        "rollNo": "21CS438",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.97,
        "activeBacklogs": 1,
        "attendance": 34.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_6():
    payload = {
        "rollNo": "21CS649",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.12,
        "activeBacklogs": 5,
        "attendance": 65.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_7():
    payload = {
        "rollNo": "21CS738",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.67,
        "activeBacklogs": 4,
        "attendance": 44.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_8():
    payload = {
        "rollNo": "21CS130",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.71,
        "activeBacklogs": 3,
        "attendance": 95.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_9():
    payload = {
        "rollNo": "21CS266",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.67,
        "activeBacklogs": 2,
        "attendance": 72.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_10():
    payload = {
        "rollNo": "21CS804",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.25,
        "activeBacklogs": 2,
        "attendance": 68.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_11():
    payload = {
        "rollNo": "21CS989",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.15,
        "activeBacklogs": 0,
        "attendance": 37.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_12():
    payload = {
        "rollNo": "21CS108",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.1,
        "activeBacklogs": 4,
        "attendance": 67.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_13():
    payload = {
        "rollNo": "21CS639",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.65,
        "activeBacklogs": 1,
        "attendance": 77.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_14():
    payload = {
        "rollNo": "21CS405",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.74,
        "activeBacklogs": 0,
        "attendance": 55.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_15():
    payload = {
        "rollNo": "21CS419",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.41,
        "activeBacklogs": 1,
        "attendance": 46.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_16():
    payload = {
        "rollNo": "21CS548",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.72,
        "activeBacklogs": 4,
        "attendance": 30.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_17():
    payload = {
        "rollNo": "21CS308",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.78,
        "activeBacklogs": 1,
        "attendance": 37.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_18():
    payload = {
        "rollNo": "21CS424",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.17,
        "activeBacklogs": 2,
        "attendance": 66.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_19():
    payload = {
        "rollNo": "21CS609",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.79,
        "activeBacklogs": 4,
        "attendance": 43.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_20():
    payload = {
        "rollNo": "21CS931",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.55,
        "activeBacklogs": 5,
        "attendance": 45.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_21():
    payload = {
        "rollNo": "21CS256",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.7,
        "activeBacklogs": 5,
        "attendance": 61.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_22():
    payload = {
        "rollNo": "21CS969",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.6,
        "activeBacklogs": 4,
        "attendance": 86.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_23():
    payload = {
        "rollNo": "21CS796",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.92,
        "activeBacklogs": 5,
        "attendance": 61.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_24():
    payload = {
        "rollNo": "21CS708",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.14,
        "activeBacklogs": 4,
        "attendance": 59.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_25():
    payload = {
        "rollNo": "21CS699",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.93,
        "activeBacklogs": 3,
        "attendance": 41.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_26():
    payload = {
        "rollNo": "21CS209",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.26,
        "activeBacklogs": 1,
        "attendance": 77.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_27():
    payload = {
        "rollNo": "21CS843",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.31,
        "activeBacklogs": 2,
        "attendance": 99.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_28():
    payload = {
        "rollNo": "21CS443",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.21,
        "activeBacklogs": 2,
        "attendance": 99.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_29():
    payload = {
        "rollNo": "21CS332",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.78,
        "activeBacklogs": 5,
        "attendance": 30.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_30():
    payload = {
        "rollNo": "21CS491",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.3,
        "activeBacklogs": 3,
        "attendance": 70.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_31():
    payload = {
        "rollNo": "21CS538",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.61,
        "activeBacklogs": 1,
        "attendance": 47.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_32():
    payload = {
        "rollNo": "21CS784",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.11,
        "activeBacklogs": 3,
        "attendance": 80.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_33():
    payload = {
        "rollNo": "21CS547",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.68,
        "activeBacklogs": 2,
        "attendance": 35.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_34():
    payload = {
        "rollNo": "21CS358",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.8,
        "activeBacklogs": 0,
        "attendance": 36.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_35():
    payload = {
        "rollNo": "21CS671",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.77,
        "activeBacklogs": 5,
        "attendance": 50.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_36():
    payload = {
        "rollNo": "21CS277",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.49,
        "activeBacklogs": 4,
        "attendance": 62.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_37():
    payload = {
        "rollNo": "21CS252",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.75,
        "activeBacklogs": 1,
        "attendance": 38.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_38():
    payload = {
        "rollNo": "21CS419",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.95,
        "activeBacklogs": 5,
        "attendance": 51.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_39():
    payload = {
        "rollNo": "21CS721",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.82,
        "activeBacklogs": 1,
        "attendance": 85.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_40():
    payload = {
        "rollNo": "21CS883",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.39,
        "activeBacklogs": 4,
        "attendance": 98.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_41():
    payload = {
        "rollNo": "21CS789",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.11,
        "activeBacklogs": 3,
        "attendance": 91.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_42():
    payload = {
        "rollNo": "21CS811",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.82,
        "activeBacklogs": 0,
        "attendance": 93.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_43():
    payload = {
        "rollNo": "21CS207",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.26,
        "activeBacklogs": 3,
        "attendance": 50.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_44():
    payload = {
        "rollNo": "21CS983",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.21,
        "activeBacklogs": 5,
        "attendance": 40.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_45():
    payload = {
        "rollNo": "21CS815",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.49,
        "activeBacklogs": 5,
        "attendance": 45.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_46():
    payload = {
        "rollNo": "21CS789",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.81,
        "activeBacklogs": 5,
        "attendance": 60.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_47():
    payload = {
        "rollNo": "21CS116",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.92,
        "activeBacklogs": 2,
        "attendance": 36.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_48():
    payload = {
        "rollNo": "21CS906",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.54,
        "activeBacklogs": 4,
        "attendance": 44.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_49():
    payload = {
        "rollNo": "21CS209",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.8,
        "activeBacklogs": 2,
        "attendance": 54.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_50():
    payload = {
        "rollNo": "21CS381",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.66,
        "activeBacklogs": 1,
        "attendance": 98.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_51():
    payload = {
        "rollNo": "21CS322",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.59,
        "activeBacklogs": 4,
        "attendance": 49.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_52():
    payload = {
        "rollNo": "21CS886",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.39,
        "activeBacklogs": 3,
        "attendance": 43.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_53():
    payload = {
        "rollNo": "21CS194",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.69,
        "activeBacklogs": 4,
        "attendance": 75.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_54():
    payload = {
        "rollNo": "21CS414",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.68,
        "activeBacklogs": 2,
        "attendance": 38.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_55():
    payload = {
        "rollNo": "21CS406",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.28,
        "activeBacklogs": 0,
        "attendance": 72.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_56():
    payload = {
        "rollNo": "21CS489",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.58,
        "activeBacklogs": 0,
        "attendance": 60.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_57():
    payload = {
        "rollNo": "21CS155",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.52,
        "activeBacklogs": 2,
        "attendance": 61.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_58():
    payload = {
        "rollNo": "21CS888",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.56,
        "activeBacklogs": 0,
        "attendance": 60.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_59():
    payload = {
        "rollNo": "21CS950",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.99,
        "activeBacklogs": 0,
        "attendance": 58.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_60():
    payload = {
        "rollNo": "21CS669",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.21,
        "activeBacklogs": 5,
        "attendance": 48.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_61():
    payload = {
        "rollNo": "21CS251",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.5,
        "activeBacklogs": 2,
        "attendance": 84.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_62():
    payload = {
        "rollNo": "21CS419",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.19,
        "activeBacklogs": 3,
        "attendance": 80.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_63():
    payload = {
        "rollNo": "21CS418",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.47,
        "activeBacklogs": 0,
        "attendance": 81.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_64():
    payload = {
        "rollNo": "21CS476",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.97,
        "activeBacklogs": 4,
        "attendance": 94.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_65():
    payload = {
        "rollNo": "21CS625",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.27,
        "activeBacklogs": 1,
        "attendance": 31.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_66():
    payload = {
        "rollNo": "21CS865",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.85,
        "activeBacklogs": 0,
        "attendance": 33.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_67():
    payload = {
        "rollNo": "21CS919",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.77,
        "activeBacklogs": 0,
        "attendance": 66.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_68():
    payload = {
        "rollNo": "21CS442",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.55,
        "activeBacklogs": 4,
        "attendance": 94.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_69():
    payload = {
        "rollNo": "21CS529",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.43,
        "activeBacklogs": 2,
        "attendance": 62.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_70():
    payload = {
        "rollNo": "21CS439",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.81,
        "activeBacklogs": 2,
        "attendance": 30.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_71():
    payload = {
        "rollNo": "21CS320",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.84,
        "activeBacklogs": 5,
        "attendance": 48.04
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_72():
    payload = {
        "rollNo": "21CS720",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.98,
        "activeBacklogs": 1,
        "attendance": 80.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_73():
    payload = {
        "rollNo": "21CS960",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.16,
        "activeBacklogs": 4,
        "attendance": 86.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_74():
    payload = {
        "rollNo": "21CS148",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.83,
        "activeBacklogs": 2,
        "attendance": 85.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_75():
    payload = {
        "rollNo": "21CS298",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.59,
        "activeBacklogs": 2,
        "attendance": 47.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_76():
    payload = {
        "rollNo": "21CS585",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.77,
        "activeBacklogs": 1,
        "attendance": 88.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_77():
    payload = {
        "rollNo": "21CS391",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.32,
        "activeBacklogs": 2,
        "attendance": 92.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_78():
    payload = {
        "rollNo": "21CS615",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.48,
        "activeBacklogs": 4,
        "attendance": 85.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_79():
    payload = {
        "rollNo": "21CS460",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.58,
        "activeBacklogs": 5,
        "attendance": 39.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_80():
    payload = {
        "rollNo": "21CS349",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.21,
        "activeBacklogs": 1,
        "attendance": 51.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_81():
    payload = {
        "rollNo": "21CS701",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.64,
        "activeBacklogs": 0,
        "attendance": 81.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_82():
    payload = {
        "rollNo": "21CS902",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.21,
        "activeBacklogs": 0,
        "attendance": 30.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_83():
    payload = {
        "rollNo": "21CS744",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.82,
        "activeBacklogs": 2,
        "attendance": 74.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_84():
    payload = {
        "rollNo": "21CS184",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.31,
        "activeBacklogs": 0,
        "attendance": 75.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_85():
    payload = {
        "rollNo": "21CS222",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.1,
        "activeBacklogs": 2,
        "attendance": 70.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_86():
    payload = {
        "rollNo": "21CS229",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.78,
        "activeBacklogs": 4,
        "attendance": 52.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_87():
    payload = {
        "rollNo": "21CS356",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.47,
        "activeBacklogs": 3,
        "attendance": 88.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_88():
    payload = {
        "rollNo": "21CS885",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.41,
        "activeBacklogs": 5,
        "attendance": 34.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_89():
    payload = {
        "rollNo": "21CS784",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.38,
        "activeBacklogs": 3,
        "attendance": 79.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_90():
    payload = {
        "rollNo": "21CS899",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.56,
        "activeBacklogs": 0,
        "attendance": 62.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_91():
    payload = {
        "rollNo": "21CS107",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.89,
        "activeBacklogs": 4,
        "attendance": 57.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_92():
    payload = {
        "rollNo": "21CS860",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.37,
        "activeBacklogs": 3,
        "attendance": 45.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_93():
    payload = {
        "rollNo": "21CS919",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.89,
        "activeBacklogs": 4,
        "attendance": 57.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_94():
    payload = {
        "rollNo": "21CS953",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.65,
        "activeBacklogs": 4,
        "attendance": 34.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_95():
    payload = {
        "rollNo": "21CS413",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.76,
        "activeBacklogs": 0,
        "attendance": 62.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_96():
    payload = {
        "rollNo": "21CS135",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.32,
        "activeBacklogs": 2,
        "attendance": 75.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_97():
    payload = {
        "rollNo": "21CS551",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.81,
        "activeBacklogs": 4,
        "attendance": 56.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_98():
    payload = {
        "rollNo": "21CS707",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.98,
        "activeBacklogs": 3,
        "attendance": 89.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_99():
    payload = {
        "rollNo": "21CS522",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.81,
        "activeBacklogs": 0,
        "attendance": 79.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_100():
    payload = {
        "rollNo": "21CS819",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.93,
        "activeBacklogs": 2,
        "attendance": 31.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_101():
    payload = {
        "rollNo": "21CS547",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.83,
        "activeBacklogs": 3,
        "attendance": 91.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_102():
    payload = {
        "rollNo": "21CS131",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.85,
        "activeBacklogs": 1,
        "attendance": 52.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_103():
    payload = {
        "rollNo": "21CS109",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.27,
        "activeBacklogs": 3,
        "attendance": 34.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_104():
    payload = {
        "rollNo": "21CS722",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.51,
        "activeBacklogs": 4,
        "attendance": 40.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_105():
    payload = {
        "rollNo": "21CS898",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.91,
        "activeBacklogs": 0,
        "attendance": 89.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_106():
    payload = {
        "rollNo": "21CS431",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.28,
        "activeBacklogs": 3,
        "attendance": 83.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_107():
    payload = {
        "rollNo": "21CS835",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.13,
        "activeBacklogs": 0,
        "attendance": 58.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_108():
    payload = {
        "rollNo": "21CS706",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.15,
        "activeBacklogs": 4,
        "attendance": 65.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_109():
    payload = {
        "rollNo": "21CS551",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.11,
        "activeBacklogs": 1,
        "attendance": 46.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_110():
    payload = {
        "rollNo": "21CS689",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.2,
        "activeBacklogs": 3,
        "attendance": 64.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_111():
    payload = {
        "rollNo": "21CS338",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.96,
        "activeBacklogs": 1,
        "attendance": 61.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_112():
    payload = {
        "rollNo": "21CS442",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.91,
        "activeBacklogs": 2,
        "attendance": 78.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_113():
    payload = {
        "rollNo": "21CS424",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.27,
        "activeBacklogs": 0,
        "attendance": 48.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_114():
    payload = {
        "rollNo": "21CS266",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.59,
        "activeBacklogs": 4,
        "attendance": 80.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_115():
    payload = {
        "rollNo": "21CS794",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.98,
        "activeBacklogs": 0,
        "attendance": 55.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_116():
    payload = {
        "rollNo": "21CS750",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.05,
        "activeBacklogs": 2,
        "attendance": 85.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_117():
    payload = {
        "rollNo": "21CS353",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.27,
        "activeBacklogs": 1,
        "attendance": 86.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_118():
    payload = {
        "rollNo": "21CS823",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.3,
        "activeBacklogs": 5,
        "attendance": 38.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_119():
    payload = {
        "rollNo": "21CS760",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.23,
        "activeBacklogs": 3,
        "attendance": 48.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_120():
    payload = {
        "rollNo": "21CS601",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.32,
        "activeBacklogs": 2,
        "attendance": 34.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_121():
    payload = {
        "rollNo": "21CS522",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.59,
        "activeBacklogs": 3,
        "attendance": 56.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_122():
    payload = {
        "rollNo": "21CS158",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.52,
        "activeBacklogs": 4,
        "attendance": 66.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_123():
    payload = {
        "rollNo": "21CS542",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.53,
        "activeBacklogs": 5,
        "attendance": 83.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_124():
    payload = {
        "rollNo": "21CS340",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.71,
        "activeBacklogs": 1,
        "attendance": 66.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_125():
    payload = {
        "rollNo": "21CS575",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.76,
        "activeBacklogs": 5,
        "attendance": 79.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_126():
    payload = {
        "rollNo": "21CS119",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.55,
        "activeBacklogs": 3,
        "attendance": 55.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_127():
    payload = {
        "rollNo": "21CS213",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.61,
        "activeBacklogs": 2,
        "attendance": 61.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_128():
    payload = {
        "rollNo": "21CS117",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.97,
        "activeBacklogs": 0,
        "attendance": 72.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_129():
    payload = {
        "rollNo": "21CS445",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.56,
        "activeBacklogs": 1,
        "attendance": 98.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_130():
    payload = {
        "rollNo": "21CS385",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.54,
        "activeBacklogs": 2,
        "attendance": 70.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_131():
    payload = {
        "rollNo": "21CS411",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.77,
        "activeBacklogs": 1,
        "attendance": 59.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_132():
    payload = {
        "rollNo": "21CS773",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.98,
        "activeBacklogs": 1,
        "attendance": 92.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_133():
    payload = {
        "rollNo": "21CS948",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.03,
        "activeBacklogs": 4,
        "attendance": 81.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_134():
    payload = {
        "rollNo": "21CS500",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.19,
        "activeBacklogs": 4,
        "attendance": 89.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_135():
    payload = {
        "rollNo": "21CS743",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.46,
        "activeBacklogs": 4,
        "attendance": 32.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_136():
    payload = {
        "rollNo": "21CS630",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.53,
        "activeBacklogs": 3,
        "attendance": 56.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_137():
    payload = {
        "rollNo": "21CS511",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.9,
        "activeBacklogs": 4,
        "attendance": 32.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_138():
    payload = {
        "rollNo": "21CS327",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.23,
        "activeBacklogs": 0,
        "attendance": 73.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_139():
    payload = {
        "rollNo": "21CS607",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.54,
        "activeBacklogs": 1,
        "attendance": 65.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_140():
    payload = {
        "rollNo": "21CS886",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.45,
        "activeBacklogs": 1,
        "attendance": 85.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_141():
    payload = {
        "rollNo": "21CS410",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.94,
        "activeBacklogs": 4,
        "attendance": 36.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_142():
    payload = {
        "rollNo": "21CS533",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.85,
        "activeBacklogs": 5,
        "attendance": 56.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_143():
    payload = {
        "rollNo": "21CS567",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.98,
        "activeBacklogs": 4,
        "attendance": 67.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_144():
    payload = {
        "rollNo": "21CS709",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.33,
        "activeBacklogs": 1,
        "attendance": 50.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_145():
    payload = {
        "rollNo": "21CS574",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.79,
        "activeBacklogs": 3,
        "attendance": 59.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_146():
    payload = {
        "rollNo": "21CS698",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.87,
        "activeBacklogs": 2,
        "attendance": 92.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_147():
    payload = {
        "rollNo": "21CS364",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.02,
        "activeBacklogs": 3,
        "attendance": 93.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_148():
    payload = {
        "rollNo": "21CS498",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.73,
        "activeBacklogs": 1,
        "attendance": 73.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_149():
    payload = {
        "rollNo": "21CS180",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.19,
        "activeBacklogs": 1,
        "attendance": 80.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_150():
    payload = {
        "rollNo": "21CS185",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.81,
        "activeBacklogs": 2,
        "attendance": 35.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_151():
    payload = {
        "rollNo": "21CS636",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.44,
        "activeBacklogs": 3,
        "attendance": 74.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_152():
    payload = {
        "rollNo": "21CS843",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.65,
        "activeBacklogs": 2,
        "attendance": 95.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_153():
    payload = {
        "rollNo": "21CS695",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.14,
        "activeBacklogs": 0,
        "attendance": 34.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_154():
    payload = {
        "rollNo": "21CS377",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.11,
        "activeBacklogs": 3,
        "attendance": 67.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_155():
    payload = {
        "rollNo": "21CS143",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.4,
        "activeBacklogs": 1,
        "attendance": 52.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_156():
    payload = {
        "rollNo": "21CS669",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.32,
        "activeBacklogs": 1,
        "attendance": 32.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_157():
    payload = {
        "rollNo": "21CS258",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.52,
        "activeBacklogs": 5,
        "attendance": 54.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_158():
    payload = {
        "rollNo": "21CS288",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.58,
        "activeBacklogs": 0,
        "attendance": 97.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_159():
    payload = {
        "rollNo": "21CS967",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.4,
        "activeBacklogs": 1,
        "attendance": 57.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_160():
    payload = {
        "rollNo": "21CS470",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.66,
        "activeBacklogs": 1,
        "attendance": 94.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_161():
    payload = {
        "rollNo": "21CS180",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.01,
        "activeBacklogs": 3,
        "attendance": 76.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_162():
    payload = {
        "rollNo": "21CS712",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.49,
        "activeBacklogs": 4,
        "attendance": 66.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_163():
    payload = {
        "rollNo": "21CS837",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.47,
        "activeBacklogs": 3,
        "attendance": 80.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_164():
    payload = {
        "rollNo": "21CS718",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.49,
        "activeBacklogs": 5,
        "attendance": 37.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_165():
    payload = {
        "rollNo": "21CS478",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.81,
        "activeBacklogs": 0,
        "attendance": 30.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_166():
    payload = {
        "rollNo": "21CS297",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.14,
        "activeBacklogs": 2,
        "attendance": 80.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_167():
    payload = {
        "rollNo": "21CS886",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.22,
        "activeBacklogs": 3,
        "attendance": 70.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_168():
    payload = {
        "rollNo": "21CS754",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.62,
        "activeBacklogs": 4,
        "attendance": 95.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_169():
    payload = {
        "rollNo": "21CS423",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.59,
        "activeBacklogs": 0,
        "attendance": 32.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_170():
    payload = {
        "rollNo": "21CS385",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.72,
        "activeBacklogs": 0,
        "attendance": 84.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_171():
    payload = {
        "rollNo": "21CS532",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.87,
        "activeBacklogs": 2,
        "attendance": 48.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_172():
    payload = {
        "rollNo": "21CS925",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.34,
        "activeBacklogs": 2,
        "attendance": 98.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_173():
    payload = {
        "rollNo": "21CS427",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.75,
        "activeBacklogs": 2,
        "attendance": 33.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_174():
    payload = {
        "rollNo": "21CS831",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.32,
        "activeBacklogs": 2,
        "attendance": 68.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_175():
    payload = {
        "rollNo": "21CS989",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.62,
        "activeBacklogs": 3,
        "attendance": 87.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_176():
    payload = {
        "rollNo": "21CS157",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.65,
        "activeBacklogs": 3,
        "attendance": 38.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_177():
    payload = {
        "rollNo": "21CS743",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.25,
        "activeBacklogs": 4,
        "attendance": 42.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_178():
    payload = {
        "rollNo": "21CS643",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.38,
        "activeBacklogs": 0,
        "attendance": 88.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_179():
    payload = {
        "rollNo": "21CS930",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.86,
        "activeBacklogs": 5,
        "attendance": 70.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_180():
    payload = {
        "rollNo": "21CS627",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.39,
        "activeBacklogs": 4,
        "attendance": 43.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_181():
    payload = {
        "rollNo": "21CS466",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.58,
        "activeBacklogs": 2,
        "attendance": 58.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_182():
    payload = {
        "rollNo": "21CS869",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.86,
        "activeBacklogs": 1,
        "attendance": 89.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_183():
    payload = {
        "rollNo": "21CS412",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.25,
        "activeBacklogs": 4,
        "attendance": 89.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_184():
    payload = {
        "rollNo": "21CS769",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.03,
        "activeBacklogs": 0,
        "attendance": 48.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_185():
    payload = {
        "rollNo": "21CS998",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.63,
        "activeBacklogs": 2,
        "attendance": 43.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_186():
    payload = {
        "rollNo": "21CS288",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.43,
        "activeBacklogs": 2,
        "attendance": 38.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_187():
    payload = {
        "rollNo": "21CS660",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.47,
        "activeBacklogs": 1,
        "attendance": 34.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_188():
    payload = {
        "rollNo": "21CS716",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.86,
        "activeBacklogs": 4,
        "attendance": 67.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_189():
    payload = {
        "rollNo": "21CS334",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.86,
        "activeBacklogs": 1,
        "attendance": 49.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_190():
    payload = {
        "rollNo": "21CS193",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.77,
        "activeBacklogs": 1,
        "attendance": 39.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_191():
    payload = {
        "rollNo": "21CS668",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.06,
        "activeBacklogs": 1,
        "attendance": 39.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_192():
    payload = {
        "rollNo": "21CS520",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.0,
        "activeBacklogs": 3,
        "attendance": 41.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_193():
    payload = {
        "rollNo": "21CS321",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.01,
        "activeBacklogs": 1,
        "attendance": 82.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_194():
    payload = {
        "rollNo": "21CS619",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.79,
        "activeBacklogs": 1,
        "attendance": 55.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_195():
    payload = {
        "rollNo": "21CS589",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.87,
        "activeBacklogs": 2,
        "attendance": 97.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_196():
    payload = {
        "rollNo": "21CS998",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.88,
        "activeBacklogs": 3,
        "attendance": 32.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_197():
    payload = {
        "rollNo": "21CS426",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.56,
        "activeBacklogs": 0,
        "attendance": 52.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_198():
    payload = {
        "rollNo": "21CS979",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.38,
        "activeBacklogs": 0,
        "attendance": 36.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_199():
    payload = {
        "rollNo": "21CS126",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.44,
        "activeBacklogs": 5,
        "attendance": 69.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_200():
    payload = {
        "rollNo": "21CS366",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.49,
        "activeBacklogs": 0,
        "attendance": 34.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_201():
    payload = {
        "rollNo": "21CS869",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.48,
        "activeBacklogs": 0,
        "attendance": 75.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_202():
    payload = {
        "rollNo": "21CS719",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.88,
        "activeBacklogs": 5,
        "attendance": 71.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_203():
    payload = {
        "rollNo": "21CS399",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.71,
        "activeBacklogs": 4,
        "attendance": 46.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_204():
    payload = {
        "rollNo": "21CS665",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.91,
        "activeBacklogs": 0,
        "attendance": 56.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_205():
    payload = {
        "rollNo": "21CS367",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.11,
        "activeBacklogs": 4,
        "attendance": 69.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_206():
    payload = {
        "rollNo": "21CS637",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.3,
        "activeBacklogs": 4,
        "attendance": 61.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_207():
    payload = {
        "rollNo": "21CS413",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.92,
        "activeBacklogs": 5,
        "attendance": 31.04
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_208():
    payload = {
        "rollNo": "21CS200",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.26,
        "activeBacklogs": 2,
        "attendance": 63.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_209():
    payload = {
        "rollNo": "21CS112",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.51,
        "activeBacklogs": 0,
        "attendance": 41.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_210():
    payload = {
        "rollNo": "21CS881",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.61,
        "activeBacklogs": 4,
        "attendance": 55.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_211():
    payload = {
        "rollNo": "21CS218",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.5,
        "activeBacklogs": 5,
        "attendance": 63.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_212():
    payload = {
        "rollNo": "21CS536",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.52,
        "activeBacklogs": 0,
        "attendance": 54.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_213():
    payload = {
        "rollNo": "21CS978",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.22,
        "activeBacklogs": 0,
        "attendance": 56.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_214():
    payload = {
        "rollNo": "21CS691",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.14,
        "activeBacklogs": 2,
        "attendance": 68.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_215():
    payload = {
        "rollNo": "21CS765",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.29,
        "activeBacklogs": 5,
        "attendance": 69.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_216():
    payload = {
        "rollNo": "21CS107",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.56,
        "activeBacklogs": 5,
        "attendance": 32.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_217():
    payload = {
        "rollNo": "21CS272",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.84,
        "activeBacklogs": 3,
        "attendance": 30.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_218():
    payload = {
        "rollNo": "21CS475",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.88,
        "activeBacklogs": 3,
        "attendance": 46.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_219():
    payload = {
        "rollNo": "21CS783",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.46,
        "activeBacklogs": 5,
        "attendance": 79.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_220():
    payload = {
        "rollNo": "21CS151",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.39,
        "activeBacklogs": 1,
        "attendance": 73.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_221():
    payload = {
        "rollNo": "21CS864",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.46,
        "activeBacklogs": 2,
        "attendance": 34.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_222():
    payload = {
        "rollNo": "21CS339",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.08,
        "activeBacklogs": 1,
        "attendance": 71.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_223():
    payload = {
        "rollNo": "21CS403",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.83,
        "activeBacklogs": 3,
        "attendance": 53.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_224():
    payload = {
        "rollNo": "21CS614",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.25,
        "activeBacklogs": 4,
        "attendance": 71.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_225():
    payload = {
        "rollNo": "21CS421",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.54,
        "activeBacklogs": 0,
        "attendance": 31.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_226():
    payload = {
        "rollNo": "21CS781",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.48,
        "activeBacklogs": 5,
        "attendance": 59.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_227():
    payload = {
        "rollNo": "21CS207",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.48,
        "activeBacklogs": 0,
        "attendance": 71.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_228():
    payload = {
        "rollNo": "21CS321",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.43,
        "activeBacklogs": 4,
        "attendance": 85.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_229():
    payload = {
        "rollNo": "21CS635",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.57,
        "activeBacklogs": 5,
        "attendance": 83.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_230():
    payload = {
        "rollNo": "21CS931",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.01,
        "activeBacklogs": 1,
        "attendance": 41.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_231():
    payload = {
        "rollNo": "21CS634",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.12,
        "activeBacklogs": 0,
        "attendance": 90.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_232():
    payload = {
        "rollNo": "21CS620",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.73,
        "activeBacklogs": 3,
        "attendance": 39.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_233():
    payload = {
        "rollNo": "21CS997",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.26,
        "activeBacklogs": 0,
        "attendance": 34.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_234():
    payload = {
        "rollNo": "21CS565",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.98,
        "activeBacklogs": 2,
        "attendance": 50.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_235():
    payload = {
        "rollNo": "21CS201",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.66,
        "activeBacklogs": 0,
        "attendance": 73.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_236():
    payload = {
        "rollNo": "21CS279",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.49,
        "activeBacklogs": 4,
        "attendance": 59.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_237():
    payload = {
        "rollNo": "21CS424",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.8,
        "activeBacklogs": 3,
        "attendance": 94.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_238():
    payload = {
        "rollNo": "21CS840",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.85,
        "activeBacklogs": 1,
        "attendance": 89.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_239():
    payload = {
        "rollNo": "21CS820",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.58,
        "activeBacklogs": 1,
        "attendance": 50.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_240():
    payload = {
        "rollNo": "21CS469",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.68,
        "activeBacklogs": 0,
        "attendance": 88.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_241():
    payload = {
        "rollNo": "21CS381",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.79,
        "activeBacklogs": 4,
        "attendance": 83.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_242():
    payload = {
        "rollNo": "21CS815",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.47,
        "activeBacklogs": 4,
        "attendance": 31.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_243():
    payload = {
        "rollNo": "21CS573",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.58,
        "activeBacklogs": 2,
        "attendance": 83.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_244():
    payload = {
        "rollNo": "21CS764",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.6,
        "activeBacklogs": 2,
        "attendance": 90.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_245():
    payload = {
        "rollNo": "21CS705",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.53,
        "activeBacklogs": 1,
        "attendance": 45.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_246():
    payload = {
        "rollNo": "21CS550",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.67,
        "activeBacklogs": 3,
        "attendance": 66.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_247():
    payload = {
        "rollNo": "21CS731",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.78,
        "activeBacklogs": 1,
        "attendance": 62.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_248():
    payload = {
        "rollNo": "21CS974",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.49,
        "activeBacklogs": 1,
        "attendance": 33.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_8_249():
    payload = {
        "rollNo": "21CS261",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.07,
        "activeBacklogs": 1,
        "attendance": 58.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

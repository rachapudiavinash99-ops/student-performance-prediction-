import pytest
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_prediction_case_3_0():
    payload = {
        "rollNo": "21CS275",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.43,
        "activeBacklogs": 1,
        "attendance": 52.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_1():
    payload = {
        "rollNo": "21CS218",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.11,
        "activeBacklogs": 2,
        "attendance": 42.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_2():
    payload = {
        "rollNo": "21CS961",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.65,
        "activeBacklogs": 1,
        "attendance": 55.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_3():
    payload = {
        "rollNo": "21CS787",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.95,
        "activeBacklogs": 5,
        "attendance": 30.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_4():
    payload = {
        "rollNo": "21CS850",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.49,
        "activeBacklogs": 0,
        "attendance": 96.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_5():
    payload = {
        "rollNo": "21CS410",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.44,
        "activeBacklogs": 2,
        "attendance": 74.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_6():
    payload = {
        "rollNo": "21CS766",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.01,
        "activeBacklogs": 3,
        "attendance": 84.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_7():
    payload = {
        "rollNo": "21CS697",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.72,
        "activeBacklogs": 2,
        "attendance": 31.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_8():
    payload = {
        "rollNo": "21CS168",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.1,
        "activeBacklogs": 0,
        "attendance": 88.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_9():
    payload = {
        "rollNo": "21CS583",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.92,
        "activeBacklogs": 1,
        "attendance": 32.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_10():
    payload = {
        "rollNo": "21CS465",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.79,
        "activeBacklogs": 3,
        "attendance": 30.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_11():
    payload = {
        "rollNo": "21CS758",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.22,
        "activeBacklogs": 1,
        "attendance": 63.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_12():
    payload = {
        "rollNo": "21CS343",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.89,
        "activeBacklogs": 0,
        "attendance": 44.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_13():
    payload = {
        "rollNo": "21CS297",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.17,
        "activeBacklogs": 1,
        "attendance": 94.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_14():
    payload = {
        "rollNo": "21CS409",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.44,
        "activeBacklogs": 1,
        "attendance": 33.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_15():
    payload = {
        "rollNo": "21CS674",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.75,
        "activeBacklogs": 4,
        "attendance": 71.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_16():
    payload = {
        "rollNo": "21CS559",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.18,
        "activeBacklogs": 3,
        "attendance": 64.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_17():
    payload = {
        "rollNo": "21CS868",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.13,
        "activeBacklogs": 5,
        "attendance": 75.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_18():
    payload = {
        "rollNo": "21CS757",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.5,
        "activeBacklogs": 2,
        "attendance": 69.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_19():
    payload = {
        "rollNo": "21CS813",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.56,
        "activeBacklogs": 4,
        "attendance": 30.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_20():
    payload = {
        "rollNo": "21CS991",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.78,
        "activeBacklogs": 5,
        "attendance": 77.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_21():
    payload = {
        "rollNo": "21CS496",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.78,
        "activeBacklogs": 2,
        "attendance": 93.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_22():
    payload = {
        "rollNo": "21CS965",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.81,
        "activeBacklogs": 4,
        "attendance": 45.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_23():
    payload = {
        "rollNo": "21CS152",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.8,
        "activeBacklogs": 5,
        "attendance": 61.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_24():
    payload = {
        "rollNo": "21CS989",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.82,
        "activeBacklogs": 3,
        "attendance": 86.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_25():
    payload = {
        "rollNo": "21CS941",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.14,
        "activeBacklogs": 1,
        "attendance": 32.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_26():
    payload = {
        "rollNo": "21CS394",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.56,
        "activeBacklogs": 4,
        "attendance": 46.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_27():
    payload = {
        "rollNo": "21CS406",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.46,
        "activeBacklogs": 2,
        "attendance": 32.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_28():
    payload = {
        "rollNo": "21CS484",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.25,
        "activeBacklogs": 1,
        "attendance": 50.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_29():
    payload = {
        "rollNo": "21CS144",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.66,
        "activeBacklogs": 4,
        "attendance": 43.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_30():
    payload = {
        "rollNo": "21CS969",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.25,
        "activeBacklogs": 2,
        "attendance": 70.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_31():
    payload = {
        "rollNo": "21CS253",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.82,
        "activeBacklogs": 2,
        "attendance": 63.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_32():
    payload = {
        "rollNo": "21CS541",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.85,
        "activeBacklogs": 5,
        "attendance": 70.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_33():
    payload = {
        "rollNo": "21CS919",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.42,
        "activeBacklogs": 2,
        "attendance": 92.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_34():
    payload = {
        "rollNo": "21CS856",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.48,
        "activeBacklogs": 4,
        "attendance": 98.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_35():
    payload = {
        "rollNo": "21CS658",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.43,
        "activeBacklogs": 2,
        "attendance": 57.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_36():
    payload = {
        "rollNo": "21CS684",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.55,
        "activeBacklogs": 1,
        "attendance": 44.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_37():
    payload = {
        "rollNo": "21CS841",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.13,
        "activeBacklogs": 2,
        "attendance": 97.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_38():
    payload = {
        "rollNo": "21CS131",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.04,
        "activeBacklogs": 0,
        "attendance": 83.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_39():
    payload = {
        "rollNo": "21CS881",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.33,
        "activeBacklogs": 3,
        "attendance": 36.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_40():
    payload = {
        "rollNo": "21CS379",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.66,
        "activeBacklogs": 0,
        "attendance": 96.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_41():
    payload = {
        "rollNo": "21CS472",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.83,
        "activeBacklogs": 0,
        "attendance": 74.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_42():
    payload = {
        "rollNo": "21CS610",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.63,
        "activeBacklogs": 3,
        "attendance": 88.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_43():
    payload = {
        "rollNo": "21CS364",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.42,
        "activeBacklogs": 0,
        "attendance": 62.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_44():
    payload = {
        "rollNo": "21CS224",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.86,
        "activeBacklogs": 0,
        "attendance": 48.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_45():
    payload = {
        "rollNo": "21CS473",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.89,
        "activeBacklogs": 4,
        "attendance": 40.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_46():
    payload = {
        "rollNo": "21CS423",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.3,
        "activeBacklogs": 0,
        "attendance": 53.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_47():
    payload = {
        "rollNo": "21CS755",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.29,
        "activeBacklogs": 3,
        "attendance": 69.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_48():
    payload = {
        "rollNo": "21CS283",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.37,
        "activeBacklogs": 1,
        "attendance": 74.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_49():
    payload = {
        "rollNo": "21CS443",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.06,
        "activeBacklogs": 5,
        "attendance": 56.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_50():
    payload = {
        "rollNo": "21CS215",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.24,
        "activeBacklogs": 2,
        "attendance": 69.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_51():
    payload = {
        "rollNo": "21CS354",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.03,
        "activeBacklogs": 0,
        "attendance": 96.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_52():
    payload = {
        "rollNo": "21CS552",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.34,
        "activeBacklogs": 1,
        "attendance": 36.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_53():
    payload = {
        "rollNo": "21CS379",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.98,
        "activeBacklogs": 5,
        "attendance": 67.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_54():
    payload = {
        "rollNo": "21CS772",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.11,
        "activeBacklogs": 1,
        "attendance": 48.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_55():
    payload = {
        "rollNo": "21CS579",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.97,
        "activeBacklogs": 3,
        "attendance": 92.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_56():
    payload = {
        "rollNo": "21CS279",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.81,
        "activeBacklogs": 4,
        "attendance": 57.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_57():
    payload = {
        "rollNo": "21CS653",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.46,
        "activeBacklogs": 5,
        "attendance": 41.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_58():
    payload = {
        "rollNo": "21CS806",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.69,
        "activeBacklogs": 5,
        "attendance": 72.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_59():
    payload = {
        "rollNo": "21CS712",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.43,
        "activeBacklogs": 0,
        "attendance": 51.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_60():
    payload = {
        "rollNo": "21CS139",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.02,
        "activeBacklogs": 5,
        "attendance": 55.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_61():
    payload = {
        "rollNo": "21CS732",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.39,
        "activeBacklogs": 4,
        "attendance": 82.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_62():
    payload = {
        "rollNo": "21CS758",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.75,
        "activeBacklogs": 5,
        "attendance": 73.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_63():
    payload = {
        "rollNo": "21CS880",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.95,
        "activeBacklogs": 1,
        "attendance": 62.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_64():
    payload = {
        "rollNo": "21CS366",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.53,
        "activeBacklogs": 1,
        "attendance": 55.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_65():
    payload = {
        "rollNo": "21CS300",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.71,
        "activeBacklogs": 0,
        "attendance": 40.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_66():
    payload = {
        "rollNo": "21CS858",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.54,
        "activeBacklogs": 2,
        "attendance": 98.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_67():
    payload = {
        "rollNo": "21CS672",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.54,
        "activeBacklogs": 0,
        "attendance": 46.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_68():
    payload = {
        "rollNo": "21CS265",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.35,
        "activeBacklogs": 0,
        "attendance": 95.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_69():
    payload = {
        "rollNo": "21CS137",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.98,
        "activeBacklogs": 3,
        "attendance": 92.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_70():
    payload = {
        "rollNo": "21CS500",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.03,
        "activeBacklogs": 2,
        "attendance": 49.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_71():
    payload = {
        "rollNo": "21CS109",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.8,
        "activeBacklogs": 3,
        "attendance": 46.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_72():
    payload = {
        "rollNo": "21CS333",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.0,
        "activeBacklogs": 3,
        "attendance": 65.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_73():
    payload = {
        "rollNo": "21CS425",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.62,
        "activeBacklogs": 3,
        "attendance": 31.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_74():
    payload = {
        "rollNo": "21CS567",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.69,
        "activeBacklogs": 3,
        "attendance": 72.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_75():
    payload = {
        "rollNo": "21CS907",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.89,
        "activeBacklogs": 1,
        "attendance": 47.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_76():
    payload = {
        "rollNo": "21CS442",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.22,
        "activeBacklogs": 4,
        "attendance": 96.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_77():
    payload = {
        "rollNo": "21CS560",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.19,
        "activeBacklogs": 1,
        "attendance": 47.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_78():
    payload = {
        "rollNo": "21CS766",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.61,
        "activeBacklogs": 2,
        "attendance": 38.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_79():
    payload = {
        "rollNo": "21CS580",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.1,
        "activeBacklogs": 5,
        "attendance": 60.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_80():
    payload = {
        "rollNo": "21CS320",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.09,
        "activeBacklogs": 1,
        "attendance": 31.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_81():
    payload = {
        "rollNo": "21CS140",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.75,
        "activeBacklogs": 1,
        "attendance": 33.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_82():
    payload = {
        "rollNo": "21CS403",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.36,
        "activeBacklogs": 2,
        "attendance": 56.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_83():
    payload = {
        "rollNo": "21CS553",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.48,
        "activeBacklogs": 2,
        "attendance": 72.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_84():
    payload = {
        "rollNo": "21CS993",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.9,
        "activeBacklogs": 1,
        "attendance": 73.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_85():
    payload = {
        "rollNo": "21CS331",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.8,
        "activeBacklogs": 1,
        "attendance": 56.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_86():
    payload = {
        "rollNo": "21CS223",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.1,
        "activeBacklogs": 4,
        "attendance": 62.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_87():
    payload = {
        "rollNo": "21CS873",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.1,
        "activeBacklogs": 1,
        "attendance": 87.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_88():
    payload = {
        "rollNo": "21CS421",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.5,
        "activeBacklogs": 1,
        "attendance": 97.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_89():
    payload = {
        "rollNo": "21CS668",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.91,
        "activeBacklogs": 5,
        "attendance": 65.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_90():
    payload = {
        "rollNo": "21CS452",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.9,
        "activeBacklogs": 1,
        "attendance": 79.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_91():
    payload = {
        "rollNo": "21CS863",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.82,
        "activeBacklogs": 5,
        "attendance": 74.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_92():
    payload = {
        "rollNo": "21CS115",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.79,
        "activeBacklogs": 0,
        "attendance": 43.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_93():
    payload = {
        "rollNo": "21CS355",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.79,
        "activeBacklogs": 3,
        "attendance": 32.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_94():
    payload = {
        "rollNo": "21CS394",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.57,
        "activeBacklogs": 2,
        "attendance": 77.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_95():
    payload = {
        "rollNo": "21CS168",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.61,
        "activeBacklogs": 4,
        "attendance": 65.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_96():
    payload = {
        "rollNo": "21CS491",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.14,
        "activeBacklogs": 1,
        "attendance": 73.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_97():
    payload = {
        "rollNo": "21CS306",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.82,
        "activeBacklogs": 5,
        "attendance": 57.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_98():
    payload = {
        "rollNo": "21CS972",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.1,
        "activeBacklogs": 2,
        "attendance": 38.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_99():
    payload = {
        "rollNo": "21CS879",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.24,
        "activeBacklogs": 5,
        "attendance": 32.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_100():
    payload = {
        "rollNo": "21CS987",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.73,
        "activeBacklogs": 2,
        "attendance": 93.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_101():
    payload = {
        "rollNo": "21CS146",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.74,
        "activeBacklogs": 0,
        "attendance": 83.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_102():
    payload = {
        "rollNo": "21CS597",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.11,
        "activeBacklogs": 2,
        "attendance": 55.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_103():
    payload = {
        "rollNo": "21CS848",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.56,
        "activeBacklogs": 4,
        "attendance": 63.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_104():
    payload = {
        "rollNo": "21CS803",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.92,
        "activeBacklogs": 3,
        "attendance": 40.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_105():
    payload = {
        "rollNo": "21CS842",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.15,
        "activeBacklogs": 3,
        "attendance": 46.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_106():
    payload = {
        "rollNo": "21CS744",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.46,
        "activeBacklogs": 4,
        "attendance": 68.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_107():
    payload = {
        "rollNo": "21CS861",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.66,
        "activeBacklogs": 0,
        "attendance": 71.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_108():
    payload = {
        "rollNo": "21CS295",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.53,
        "activeBacklogs": 3,
        "attendance": 88.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_109():
    payload = {
        "rollNo": "21CS124",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.38,
        "activeBacklogs": 1,
        "attendance": 56.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_110():
    payload = {
        "rollNo": "21CS426",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.01,
        "activeBacklogs": 0,
        "attendance": 32.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_111():
    payload = {
        "rollNo": "21CS479",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.33,
        "activeBacklogs": 0,
        "attendance": 79.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_112():
    payload = {
        "rollNo": "21CS871",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.03,
        "activeBacklogs": 0,
        "attendance": 45.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_113():
    payload = {
        "rollNo": "21CS486",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.98,
        "activeBacklogs": 1,
        "attendance": 55.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_114():
    payload = {
        "rollNo": "21CS387",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.76,
        "activeBacklogs": 3,
        "attendance": 90.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_115():
    payload = {
        "rollNo": "21CS900",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.37,
        "activeBacklogs": 4,
        "attendance": 83.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_116():
    payload = {
        "rollNo": "21CS846",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.55,
        "activeBacklogs": 5,
        "attendance": 36.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_117():
    payload = {
        "rollNo": "21CS141",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.31,
        "activeBacklogs": 3,
        "attendance": 34.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_118():
    payload = {
        "rollNo": "21CS700",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.07,
        "activeBacklogs": 5,
        "attendance": 40.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_119():
    payload = {
        "rollNo": "21CS972",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.15,
        "activeBacklogs": 3,
        "attendance": 83.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_120():
    payload = {
        "rollNo": "21CS870",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.89,
        "activeBacklogs": 3,
        "attendance": 69.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_121():
    payload = {
        "rollNo": "21CS818",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.17,
        "activeBacklogs": 3,
        "attendance": 83.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_122():
    payload = {
        "rollNo": "21CS379",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.74,
        "activeBacklogs": 2,
        "attendance": 44.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_123():
    payload = {
        "rollNo": "21CS744",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.3,
        "activeBacklogs": 0,
        "attendance": 30.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_124():
    payload = {
        "rollNo": "21CS659",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.66,
        "activeBacklogs": 2,
        "attendance": 57.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_125():
    payload = {
        "rollNo": "21CS889",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.71,
        "activeBacklogs": 5,
        "attendance": 60.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_126():
    payload = {
        "rollNo": "21CS186",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.08,
        "activeBacklogs": 5,
        "attendance": 89.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_127():
    payload = {
        "rollNo": "21CS293",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.89,
        "activeBacklogs": 5,
        "attendance": 41.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_128():
    payload = {
        "rollNo": "21CS177",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.07,
        "activeBacklogs": 5,
        "attendance": 41.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_129():
    payload = {
        "rollNo": "21CS957",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.58,
        "activeBacklogs": 2,
        "attendance": 60.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_130():
    payload = {
        "rollNo": "21CS254",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.78,
        "activeBacklogs": 2,
        "attendance": 72.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_131():
    payload = {
        "rollNo": "21CS644",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.49,
        "activeBacklogs": 5,
        "attendance": 37.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_132():
    payload = {
        "rollNo": "21CS806",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.07,
        "activeBacklogs": 3,
        "attendance": 43.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_133():
    payload = {
        "rollNo": "21CS354",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.95,
        "activeBacklogs": 4,
        "attendance": 72.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_134():
    payload = {
        "rollNo": "21CS812",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.36,
        "activeBacklogs": 0,
        "attendance": 66.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_135():
    payload = {
        "rollNo": "21CS125",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.95,
        "activeBacklogs": 4,
        "attendance": 50.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_136():
    payload = {
        "rollNo": "21CS671",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.3,
        "activeBacklogs": 4,
        "attendance": 65.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_137():
    payload = {
        "rollNo": "21CS798",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.24,
        "activeBacklogs": 1,
        "attendance": 90.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_138():
    payload = {
        "rollNo": "21CS627",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.33,
        "activeBacklogs": 4,
        "attendance": 36.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_139():
    payload = {
        "rollNo": "21CS411",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.77,
        "activeBacklogs": 0,
        "attendance": 77.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_140():
    payload = {
        "rollNo": "21CS136",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.07,
        "activeBacklogs": 2,
        "attendance": 65.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_141():
    payload = {
        "rollNo": "21CS300",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.53,
        "activeBacklogs": 0,
        "attendance": 49.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_142():
    payload = {
        "rollNo": "21CS767",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.11,
        "activeBacklogs": 1,
        "attendance": 75.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_143():
    payload = {
        "rollNo": "21CS381",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.85,
        "activeBacklogs": 1,
        "attendance": 66.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_144():
    payload = {
        "rollNo": "21CS716",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.96,
        "activeBacklogs": 0,
        "attendance": 90.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_145():
    payload = {
        "rollNo": "21CS895",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.86,
        "activeBacklogs": 3,
        "attendance": 77.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_146():
    payload = {
        "rollNo": "21CS877",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.21,
        "activeBacklogs": 0,
        "attendance": 62.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_147():
    payload = {
        "rollNo": "21CS309",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.83,
        "activeBacklogs": 2,
        "attendance": 44.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_148():
    payload = {
        "rollNo": "21CS509",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.32,
        "activeBacklogs": 0,
        "attendance": 76.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_149():
    payload = {
        "rollNo": "21CS479",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.07,
        "activeBacklogs": 3,
        "attendance": 44.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_150():
    payload = {
        "rollNo": "21CS894",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.66,
        "activeBacklogs": 3,
        "attendance": 43.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_151():
    payload = {
        "rollNo": "21CS536",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.62,
        "activeBacklogs": 1,
        "attendance": 59.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_152():
    payload = {
        "rollNo": "21CS297",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.67,
        "activeBacklogs": 4,
        "attendance": 58.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_153():
    payload = {
        "rollNo": "21CS588",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.85,
        "activeBacklogs": 1,
        "attendance": 46.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_154():
    payload = {
        "rollNo": "21CS733",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.92,
        "activeBacklogs": 5,
        "attendance": 77.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_155():
    payload = {
        "rollNo": "21CS454",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.17,
        "activeBacklogs": 4,
        "attendance": 95.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_156():
    payload = {
        "rollNo": "21CS510",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.18,
        "activeBacklogs": 5,
        "attendance": 79.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_157():
    payload = {
        "rollNo": "21CS490",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.6,
        "activeBacklogs": 4,
        "attendance": 34.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_158():
    payload = {
        "rollNo": "21CS489",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.53,
        "activeBacklogs": 5,
        "attendance": 35.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_159():
    payload = {
        "rollNo": "21CS953",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.63,
        "activeBacklogs": 5,
        "attendance": 49.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_160():
    payload = {
        "rollNo": "21CS124",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.41,
        "activeBacklogs": 1,
        "attendance": 37.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_161():
    payload = {
        "rollNo": "21CS745",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.91,
        "activeBacklogs": 5,
        "attendance": 92.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_162():
    payload = {
        "rollNo": "21CS972",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.8,
        "activeBacklogs": 1,
        "attendance": 75.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_163():
    payload = {
        "rollNo": "21CS778",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.51,
        "activeBacklogs": 1,
        "attendance": 79.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_164():
    payload = {
        "rollNo": "21CS877",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.31,
        "activeBacklogs": 5,
        "attendance": 36.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_165():
    payload = {
        "rollNo": "21CS353",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.54,
        "activeBacklogs": 3,
        "attendance": 80.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_166():
    payload = {
        "rollNo": "21CS417",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.18,
        "activeBacklogs": 4,
        "attendance": 37.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_167():
    payload = {
        "rollNo": "21CS479",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.12,
        "activeBacklogs": 1,
        "attendance": 49.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_168():
    payload = {
        "rollNo": "21CS401",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.94,
        "activeBacklogs": 4,
        "attendance": 64.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_169():
    payload = {
        "rollNo": "21CS625",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.78,
        "activeBacklogs": 3,
        "attendance": 47.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_170():
    payload = {
        "rollNo": "21CS588",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.31,
        "activeBacklogs": 3,
        "attendance": 83.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_171():
    payload = {
        "rollNo": "21CS268",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.26,
        "activeBacklogs": 5,
        "attendance": 83.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_172():
    payload = {
        "rollNo": "21CS242",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.0,
        "activeBacklogs": 3,
        "attendance": 80.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_173():
    payload = {
        "rollNo": "21CS229",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.31,
        "activeBacklogs": 5,
        "attendance": 35.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_174():
    payload = {
        "rollNo": "21CS590",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.69,
        "activeBacklogs": 2,
        "attendance": 79.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_175():
    payload = {
        "rollNo": "21CS962",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.78,
        "activeBacklogs": 3,
        "attendance": 38.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_176():
    payload = {
        "rollNo": "21CS254",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.61,
        "activeBacklogs": 3,
        "attendance": 50.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_177():
    payload = {
        "rollNo": "21CS560",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.62,
        "activeBacklogs": 1,
        "attendance": 94.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_178():
    payload = {
        "rollNo": "21CS774",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.47,
        "activeBacklogs": 2,
        "attendance": 81.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_179():
    payload = {
        "rollNo": "21CS512",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.83,
        "activeBacklogs": 0,
        "attendance": 94.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_180():
    payload = {
        "rollNo": "21CS817",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.68,
        "activeBacklogs": 3,
        "attendance": 93.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_181():
    payload = {
        "rollNo": "21CS873",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.9,
        "activeBacklogs": 3,
        "attendance": 49.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_182():
    payload = {
        "rollNo": "21CS670",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.66,
        "activeBacklogs": 4,
        "attendance": 65.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_183():
    payload = {
        "rollNo": "21CS592",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.81,
        "activeBacklogs": 1,
        "attendance": 88.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_184():
    payload = {
        "rollNo": "21CS234",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.16,
        "activeBacklogs": 5,
        "attendance": 92.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_185():
    payload = {
        "rollNo": "21CS508",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.35,
        "activeBacklogs": 0,
        "attendance": 58.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_186():
    payload = {
        "rollNo": "21CS707",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.31,
        "activeBacklogs": 4,
        "attendance": 86.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_187():
    payload = {
        "rollNo": "21CS322",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.43,
        "activeBacklogs": 3,
        "attendance": 48.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_188():
    payload = {
        "rollNo": "21CS776",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.87,
        "activeBacklogs": 0,
        "attendance": 65.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_189():
    payload = {
        "rollNo": "21CS324",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.87,
        "activeBacklogs": 4,
        "attendance": 76.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_190():
    payload = {
        "rollNo": "21CS615",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.99,
        "activeBacklogs": 4,
        "attendance": 83.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_191():
    payload = {
        "rollNo": "21CS947",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.03,
        "activeBacklogs": 0,
        "attendance": 55.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_192():
    payload = {
        "rollNo": "21CS116",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.66,
        "activeBacklogs": 1,
        "attendance": 35.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_193():
    payload = {
        "rollNo": "21CS863",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.81,
        "activeBacklogs": 5,
        "attendance": 85.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_194():
    payload = {
        "rollNo": "21CS649",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.8,
        "activeBacklogs": 1,
        "attendance": 79.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_195():
    payload = {
        "rollNo": "21CS494",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.89,
        "activeBacklogs": 1,
        "attendance": 93.04
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_196():
    payload = {
        "rollNo": "21CS703",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.37,
        "activeBacklogs": 0,
        "attendance": 41.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_197():
    payload = {
        "rollNo": "21CS151",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.9,
        "activeBacklogs": 5,
        "attendance": 98.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_198():
    payload = {
        "rollNo": "21CS319",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.26,
        "activeBacklogs": 4,
        "attendance": 52.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_199():
    payload = {
        "rollNo": "21CS304",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.11,
        "activeBacklogs": 4,
        "attendance": 59.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_200():
    payload = {
        "rollNo": "21CS972",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.06,
        "activeBacklogs": 4,
        "attendance": 66.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_201():
    payload = {
        "rollNo": "21CS153",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.1,
        "activeBacklogs": 3,
        "attendance": 96.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_202():
    payload = {
        "rollNo": "21CS114",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.75,
        "activeBacklogs": 0,
        "attendance": 91.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_203():
    payload = {
        "rollNo": "21CS618",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.13,
        "activeBacklogs": 4,
        "attendance": 49.04
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_204():
    payload = {
        "rollNo": "21CS166",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.52,
        "activeBacklogs": 0,
        "attendance": 77.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_205():
    payload = {
        "rollNo": "21CS204",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.48,
        "activeBacklogs": 5,
        "attendance": 76.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_206():
    payload = {
        "rollNo": "21CS209",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.1,
        "activeBacklogs": 3,
        "attendance": 93.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_207():
    payload = {
        "rollNo": "21CS207",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.91,
        "activeBacklogs": 3,
        "attendance": 52.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_208():
    payload = {
        "rollNo": "21CS765",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.2,
        "activeBacklogs": 1,
        "attendance": 59.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_209():
    payload = {
        "rollNo": "21CS732",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.75,
        "activeBacklogs": 2,
        "attendance": 97.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_210():
    payload = {
        "rollNo": "21CS712",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.93,
        "activeBacklogs": 1,
        "attendance": 61.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_211():
    payload = {
        "rollNo": "21CS805",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.62,
        "activeBacklogs": 5,
        "attendance": 74.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_212():
    payload = {
        "rollNo": "21CS838",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.47,
        "activeBacklogs": 3,
        "attendance": 48.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_213():
    payload = {
        "rollNo": "21CS662",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.45,
        "activeBacklogs": 3,
        "attendance": 70.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_214():
    payload = {
        "rollNo": "21CS764",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.55,
        "activeBacklogs": 1,
        "attendance": 81.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_215():
    payload = {
        "rollNo": "21CS520",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.52,
        "activeBacklogs": 2,
        "attendance": 33.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_216():
    payload = {
        "rollNo": "21CS658",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.22,
        "activeBacklogs": 0,
        "attendance": 81.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_217():
    payload = {
        "rollNo": "21CS998",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.54,
        "activeBacklogs": 5,
        "attendance": 65.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_218():
    payload = {
        "rollNo": "21CS324",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.62,
        "activeBacklogs": 0,
        "attendance": 50.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_219():
    payload = {
        "rollNo": "21CS801",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.81,
        "activeBacklogs": 4,
        "attendance": 31.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_220():
    payload = {
        "rollNo": "21CS167",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.43,
        "activeBacklogs": 5,
        "attendance": 85.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_221():
    payload = {
        "rollNo": "21CS301",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.23,
        "activeBacklogs": 5,
        "attendance": 35.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_222():
    payload = {
        "rollNo": "21CS832",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.32,
        "activeBacklogs": 1,
        "attendance": 70.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_223():
    payload = {
        "rollNo": "21CS891",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.31,
        "activeBacklogs": 0,
        "attendance": 33.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_224():
    payload = {
        "rollNo": "21CS553",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.36,
        "activeBacklogs": 1,
        "attendance": 47.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_225():
    payload = {
        "rollNo": "21CS906",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.4,
        "activeBacklogs": 2,
        "attendance": 81.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_226():
    payload = {
        "rollNo": "21CS705",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.61,
        "activeBacklogs": 0,
        "attendance": 90.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_227():
    payload = {
        "rollNo": "21CS921",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.42,
        "activeBacklogs": 2,
        "attendance": 80.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_228():
    payload = {
        "rollNo": "21CS940",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.98,
        "activeBacklogs": 3,
        "attendance": 60.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_229():
    payload = {
        "rollNo": "21CS128",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.36,
        "activeBacklogs": 2,
        "attendance": 54.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_230():
    payload = {
        "rollNo": "21CS814",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.58,
        "activeBacklogs": 1,
        "attendance": 73.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_231():
    payload = {
        "rollNo": "21CS251",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.15,
        "activeBacklogs": 4,
        "attendance": 47.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_232():
    payload = {
        "rollNo": "21CS711",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.4,
        "activeBacklogs": 4,
        "attendance": 65.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_233():
    payload = {
        "rollNo": "21CS444",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.87,
        "activeBacklogs": 0,
        "attendance": 68.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_234():
    payload = {
        "rollNo": "21CS541",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.34,
        "activeBacklogs": 5,
        "attendance": 52.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_235():
    payload = {
        "rollNo": "21CS232",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.51,
        "activeBacklogs": 4,
        "attendance": 84.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_236():
    payload = {
        "rollNo": "21CS405",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.81,
        "activeBacklogs": 1,
        "attendance": 43.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_237():
    payload = {
        "rollNo": "21CS221",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.98,
        "activeBacklogs": 0,
        "attendance": 77.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_238():
    payload = {
        "rollNo": "21CS187",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.65,
        "activeBacklogs": 3,
        "attendance": 35.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_239():
    payload = {
        "rollNo": "21CS701",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.23,
        "activeBacklogs": 3,
        "attendance": 72.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_240():
    payload = {
        "rollNo": "21CS514",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.05,
        "activeBacklogs": 5,
        "attendance": 32.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_241():
    payload = {
        "rollNo": "21CS542",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.55,
        "activeBacklogs": 3,
        "attendance": 44.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_242():
    payload = {
        "rollNo": "21CS523",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.86,
        "activeBacklogs": 1,
        "attendance": 54.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_243():
    payload = {
        "rollNo": "21CS813",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.21,
        "activeBacklogs": 2,
        "attendance": 80.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_244():
    payload = {
        "rollNo": "21CS211",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.24,
        "activeBacklogs": 1,
        "attendance": 47.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_245():
    payload = {
        "rollNo": "21CS878",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.39,
        "activeBacklogs": 3,
        "attendance": 56.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_246():
    payload = {
        "rollNo": "21CS407",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.95,
        "activeBacklogs": 0,
        "attendance": 39.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_247():
    payload = {
        "rollNo": "21CS198",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.0,
        "activeBacklogs": 0,
        "attendance": 73.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_248():
    payload = {
        "rollNo": "21CS343",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.81,
        "activeBacklogs": 0,
        "attendance": 79.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_3_249():
    payload = {
        "rollNo": "21CS466",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.44,
        "activeBacklogs": 2,
        "attendance": 74.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

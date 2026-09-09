import pytest
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_prediction_case_11_0():
    payload = {
        "rollNo": "21CS786",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.34,
        "activeBacklogs": 1,
        "attendance": 32.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_1():
    payload = {
        "rollNo": "21CS203",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.47,
        "activeBacklogs": 3,
        "attendance": 75.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_2():
    payload = {
        "rollNo": "21CS392",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.35,
        "activeBacklogs": 5,
        "attendance": 54.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_3():
    payload = {
        "rollNo": "21CS515",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.38,
        "activeBacklogs": 4,
        "attendance": 55.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_4():
    payload = {
        "rollNo": "21CS362",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.7,
        "activeBacklogs": 0,
        "attendance": 82.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_5():
    payload = {
        "rollNo": "21CS816",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.91,
        "activeBacklogs": 2,
        "attendance": 32.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_6():
    payload = {
        "rollNo": "21CS648",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.24,
        "activeBacklogs": 5,
        "attendance": 80.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_7():
    payload = {
        "rollNo": "21CS603",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.91,
        "activeBacklogs": 2,
        "attendance": 51.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_8():
    payload = {
        "rollNo": "21CS705",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.05,
        "activeBacklogs": 1,
        "attendance": 73.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_9():
    payload = {
        "rollNo": "21CS577",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.73,
        "activeBacklogs": 0,
        "attendance": 35.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_10():
    payload = {
        "rollNo": "21CS119",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.08,
        "activeBacklogs": 4,
        "attendance": 53.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_11():
    payload = {
        "rollNo": "21CS526",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.33,
        "activeBacklogs": 4,
        "attendance": 55.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_12():
    payload = {
        "rollNo": "21CS727",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.58,
        "activeBacklogs": 5,
        "attendance": 43.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_13():
    payload = {
        "rollNo": "21CS553",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.76,
        "activeBacklogs": 1,
        "attendance": 64.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_14():
    payload = {
        "rollNo": "21CS892",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.17,
        "activeBacklogs": 3,
        "attendance": 98.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_15():
    payload = {
        "rollNo": "21CS928",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.99,
        "activeBacklogs": 4,
        "attendance": 73.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_16():
    payload = {
        "rollNo": "21CS499",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.33,
        "activeBacklogs": 3,
        "attendance": 64.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_17():
    payload = {
        "rollNo": "21CS452",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.31,
        "activeBacklogs": 5,
        "attendance": 74.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_18():
    payload = {
        "rollNo": "21CS637",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.93,
        "activeBacklogs": 5,
        "attendance": 31.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_19():
    payload = {
        "rollNo": "21CS705",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.28,
        "activeBacklogs": 0,
        "attendance": 75.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_20():
    payload = {
        "rollNo": "21CS269",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.33,
        "activeBacklogs": 3,
        "attendance": 49.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_21():
    payload = {
        "rollNo": "21CS715",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.46,
        "activeBacklogs": 2,
        "attendance": 94.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_22():
    payload = {
        "rollNo": "21CS658",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.73,
        "activeBacklogs": 2,
        "attendance": 57.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_23():
    payload = {
        "rollNo": "21CS285",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.83,
        "activeBacklogs": 0,
        "attendance": 30.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_24():
    payload = {
        "rollNo": "21CS184",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.33,
        "activeBacklogs": 1,
        "attendance": 63.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_25():
    payload = {
        "rollNo": "21CS567",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.65,
        "activeBacklogs": 4,
        "attendance": 83.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_26():
    payload = {
        "rollNo": "21CS535",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.73,
        "activeBacklogs": 1,
        "attendance": 91.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_27():
    payload = {
        "rollNo": "21CS299",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.18,
        "activeBacklogs": 3,
        "attendance": 67.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_28():
    payload = {
        "rollNo": "21CS392",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.39,
        "activeBacklogs": 3,
        "attendance": 54.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_29():
    payload = {
        "rollNo": "21CS567",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.64,
        "activeBacklogs": 2,
        "attendance": 69.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_30():
    payload = {
        "rollNo": "21CS149",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.14,
        "activeBacklogs": 1,
        "attendance": 38.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_31():
    payload = {
        "rollNo": "21CS739",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.0,
        "activeBacklogs": 4,
        "attendance": 74.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_32():
    payload = {
        "rollNo": "21CS614",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.18,
        "activeBacklogs": 5,
        "attendance": 65.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_33():
    payload = {
        "rollNo": "21CS690",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.83,
        "activeBacklogs": 0,
        "attendance": 88.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_34():
    payload = {
        "rollNo": "21CS412",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.87,
        "activeBacklogs": 1,
        "attendance": 86.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_35():
    payload = {
        "rollNo": "21CS135",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.84,
        "activeBacklogs": 5,
        "attendance": 46.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_36():
    payload = {
        "rollNo": "21CS947",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.68,
        "activeBacklogs": 1,
        "attendance": 51.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_37():
    payload = {
        "rollNo": "21CS621",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.54,
        "activeBacklogs": 3,
        "attendance": 42.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_38():
    payload = {
        "rollNo": "21CS594",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.99,
        "activeBacklogs": 2,
        "attendance": 63.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_39():
    payload = {
        "rollNo": "21CS158",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.57,
        "activeBacklogs": 1,
        "attendance": 31.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_40():
    payload = {
        "rollNo": "21CS147",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.3,
        "activeBacklogs": 3,
        "attendance": 63.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_41():
    payload = {
        "rollNo": "21CS972",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.31,
        "activeBacklogs": 0,
        "attendance": 47.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_42():
    payload = {
        "rollNo": "21CS439",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.32,
        "activeBacklogs": 0,
        "attendance": 37.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_43():
    payload = {
        "rollNo": "21CS987",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.21,
        "activeBacklogs": 4,
        "attendance": 77.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_44():
    payload = {
        "rollNo": "21CS904",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.44,
        "activeBacklogs": 5,
        "attendance": 45.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_45():
    payload = {
        "rollNo": "21CS620",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.72,
        "activeBacklogs": 4,
        "attendance": 65.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_46():
    payload = {
        "rollNo": "21CS782",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.05,
        "activeBacklogs": 2,
        "attendance": 58.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_47():
    payload = {
        "rollNo": "21CS787",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.59,
        "activeBacklogs": 1,
        "attendance": 89.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_48():
    payload = {
        "rollNo": "21CS243",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.44,
        "activeBacklogs": 4,
        "attendance": 53.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_49():
    payload = {
        "rollNo": "21CS748",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.39,
        "activeBacklogs": 0,
        "attendance": 86.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_50():
    payload = {
        "rollNo": "21CS496",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.42,
        "activeBacklogs": 0,
        "attendance": 30.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_51():
    payload = {
        "rollNo": "21CS595",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.13,
        "activeBacklogs": 5,
        "attendance": 54.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_52():
    payload = {
        "rollNo": "21CS320",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.84,
        "activeBacklogs": 3,
        "attendance": 90.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_53():
    payload = {
        "rollNo": "21CS462",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.34,
        "activeBacklogs": 3,
        "attendance": 87.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_54():
    payload = {
        "rollNo": "21CS348",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.15,
        "activeBacklogs": 5,
        "attendance": 36.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_55():
    payload = {
        "rollNo": "21CS183",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.87,
        "activeBacklogs": 4,
        "attendance": 70.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_56():
    payload = {
        "rollNo": "21CS861",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.47,
        "activeBacklogs": 2,
        "attendance": 59.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_57():
    payload = {
        "rollNo": "21CS650",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.43,
        "activeBacklogs": 5,
        "attendance": 87.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_58():
    payload = {
        "rollNo": "21CS347",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.95,
        "activeBacklogs": 4,
        "attendance": 37.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_59():
    payload = {
        "rollNo": "21CS954",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.18,
        "activeBacklogs": 4,
        "attendance": 49.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_60():
    payload = {
        "rollNo": "21CS332",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.75,
        "activeBacklogs": 3,
        "attendance": 69.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_61():
    payload = {
        "rollNo": "21CS217",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.43,
        "activeBacklogs": 5,
        "attendance": 97.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_62():
    payload = {
        "rollNo": "21CS325",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.65,
        "activeBacklogs": 2,
        "attendance": 70.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_63():
    payload = {
        "rollNo": "21CS614",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.67,
        "activeBacklogs": 5,
        "attendance": 81.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_64():
    payload = {
        "rollNo": "21CS198",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.38,
        "activeBacklogs": 2,
        "attendance": 75.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_65():
    payload = {
        "rollNo": "21CS968",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.02,
        "activeBacklogs": 5,
        "attendance": 76.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_66():
    payload = {
        "rollNo": "21CS515",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.62,
        "activeBacklogs": 2,
        "attendance": 63.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_67():
    payload = {
        "rollNo": "21CS325",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.82,
        "activeBacklogs": 1,
        "attendance": 81.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_68():
    payload = {
        "rollNo": "21CS920",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.03,
        "activeBacklogs": 4,
        "attendance": 93.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_69():
    payload = {
        "rollNo": "21CS759",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.36,
        "activeBacklogs": 3,
        "attendance": 56.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_70():
    payload = {
        "rollNo": "21CS675",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.76,
        "activeBacklogs": 3,
        "attendance": 73.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_71():
    payload = {
        "rollNo": "21CS738",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.93,
        "activeBacklogs": 1,
        "attendance": 52.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_72():
    payload = {
        "rollNo": "21CS708",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.74,
        "activeBacklogs": 5,
        "attendance": 66.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_73():
    payload = {
        "rollNo": "21CS503",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.62,
        "activeBacklogs": 3,
        "attendance": 75.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_74():
    payload = {
        "rollNo": "21CS369",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.59,
        "activeBacklogs": 4,
        "attendance": 79.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_75():
    payload = {
        "rollNo": "21CS763",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.66,
        "activeBacklogs": 5,
        "attendance": 95.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_76():
    payload = {
        "rollNo": "21CS814",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.0,
        "activeBacklogs": 0,
        "attendance": 32.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_77():
    payload = {
        "rollNo": "21CS462",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.36,
        "activeBacklogs": 4,
        "attendance": 48.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_78():
    payload = {
        "rollNo": "21CS354",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.37,
        "activeBacklogs": 0,
        "attendance": 80.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_79():
    payload = {
        "rollNo": "21CS851",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.13,
        "activeBacklogs": 4,
        "attendance": 75.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_80():
    payload = {
        "rollNo": "21CS974",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.0,
        "activeBacklogs": 3,
        "attendance": 72.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_81():
    payload = {
        "rollNo": "21CS968",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.39,
        "activeBacklogs": 5,
        "attendance": 33.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_82():
    payload = {
        "rollNo": "21CS575",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.63,
        "activeBacklogs": 3,
        "attendance": 85.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_83():
    payload = {
        "rollNo": "21CS930",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.89,
        "activeBacklogs": 2,
        "attendance": 88.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_84():
    payload = {
        "rollNo": "21CS345",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.91,
        "activeBacklogs": 5,
        "attendance": 59.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_85():
    payload = {
        "rollNo": "21CS484",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.53,
        "activeBacklogs": 3,
        "attendance": 41.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_86():
    payload = {
        "rollNo": "21CS670",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.27,
        "activeBacklogs": 2,
        "attendance": 71.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_87():
    payload = {
        "rollNo": "21CS653",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.22,
        "activeBacklogs": 0,
        "attendance": 91.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_88():
    payload = {
        "rollNo": "21CS965",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.28,
        "activeBacklogs": 4,
        "attendance": 88.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_89():
    payload = {
        "rollNo": "21CS107",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.85,
        "activeBacklogs": 2,
        "attendance": 71.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_90():
    payload = {
        "rollNo": "21CS543",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.55,
        "activeBacklogs": 1,
        "attendance": 83.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_91():
    payload = {
        "rollNo": "21CS442",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.54,
        "activeBacklogs": 2,
        "attendance": 68.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_92():
    payload = {
        "rollNo": "21CS721",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.16,
        "activeBacklogs": 2,
        "attendance": 32.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_93():
    payload = {
        "rollNo": "21CS417",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.24,
        "activeBacklogs": 5,
        "attendance": 93.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_94():
    payload = {
        "rollNo": "21CS372",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.65,
        "activeBacklogs": 1,
        "attendance": 36.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_95():
    payload = {
        "rollNo": "21CS857",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.65,
        "activeBacklogs": 0,
        "attendance": 98.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_96():
    payload = {
        "rollNo": "21CS117",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.54,
        "activeBacklogs": 5,
        "attendance": 48.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_97():
    payload = {
        "rollNo": "21CS557",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.01,
        "activeBacklogs": 4,
        "attendance": 69.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_98():
    payload = {
        "rollNo": "21CS912",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.38,
        "activeBacklogs": 0,
        "attendance": 80.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_99():
    payload = {
        "rollNo": "21CS748",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.61,
        "activeBacklogs": 4,
        "attendance": 62.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_100():
    payload = {
        "rollNo": "21CS327",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.3,
        "activeBacklogs": 0,
        "attendance": 58.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_101():
    payload = {
        "rollNo": "21CS969",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.96,
        "activeBacklogs": 4,
        "attendance": 61.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_102():
    payload = {
        "rollNo": "21CS932",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.65,
        "activeBacklogs": 0,
        "attendance": 97.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_103():
    payload = {
        "rollNo": "21CS597",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.22,
        "activeBacklogs": 2,
        "attendance": 74.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_104():
    payload = {
        "rollNo": "21CS389",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.78,
        "activeBacklogs": 2,
        "attendance": 67.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_105():
    payload = {
        "rollNo": "21CS379",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.88,
        "activeBacklogs": 2,
        "attendance": 65.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_106():
    payload = {
        "rollNo": "21CS828",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.86,
        "activeBacklogs": 2,
        "attendance": 48.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_107():
    payload = {
        "rollNo": "21CS668",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.31,
        "activeBacklogs": 3,
        "attendance": 58.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_108():
    payload = {
        "rollNo": "21CS381",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.26,
        "activeBacklogs": 0,
        "attendance": 45.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_109():
    payload = {
        "rollNo": "21CS773",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.84,
        "activeBacklogs": 0,
        "attendance": 54.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_110():
    payload = {
        "rollNo": "21CS483",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.3,
        "activeBacklogs": 3,
        "attendance": 50.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_111():
    payload = {
        "rollNo": "21CS100",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.8,
        "activeBacklogs": 2,
        "attendance": 74.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_112():
    payload = {
        "rollNo": "21CS743",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.01,
        "activeBacklogs": 1,
        "attendance": 44.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_113():
    payload = {
        "rollNo": "21CS190",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.55,
        "activeBacklogs": 4,
        "attendance": 80.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_114():
    payload = {
        "rollNo": "21CS958",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.62,
        "activeBacklogs": 4,
        "attendance": 33.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_115():
    payload = {
        "rollNo": "21CS428",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.27,
        "activeBacklogs": 5,
        "attendance": 87.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_116():
    payload = {
        "rollNo": "21CS350",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.11,
        "activeBacklogs": 2,
        "attendance": 82.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_117():
    payload = {
        "rollNo": "21CS969",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.65,
        "activeBacklogs": 0,
        "attendance": 52.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_118():
    payload = {
        "rollNo": "21CS228",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.37,
        "activeBacklogs": 0,
        "attendance": 65.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_119():
    payload = {
        "rollNo": "21CS812",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.74,
        "activeBacklogs": 0,
        "attendance": 40.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_120():
    payload = {
        "rollNo": "21CS231",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.38,
        "activeBacklogs": 4,
        "attendance": 94.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_121():
    payload = {
        "rollNo": "21CS890",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.92,
        "activeBacklogs": 0,
        "attendance": 77.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_122():
    payload = {
        "rollNo": "21CS623",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.14,
        "activeBacklogs": 5,
        "attendance": 49.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_123():
    payload = {
        "rollNo": "21CS123",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.54,
        "activeBacklogs": 0,
        "attendance": 69.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_124():
    payload = {
        "rollNo": "21CS559",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.1,
        "activeBacklogs": 0,
        "attendance": 66.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_125():
    payload = {
        "rollNo": "21CS802",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.67,
        "activeBacklogs": 1,
        "attendance": 59.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_126():
    payload = {
        "rollNo": "21CS295",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.05,
        "activeBacklogs": 4,
        "attendance": 70.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_127():
    payload = {
        "rollNo": "21CS549",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.81,
        "activeBacklogs": 2,
        "attendance": 37.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_128():
    payload = {
        "rollNo": "21CS292",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.3,
        "activeBacklogs": 0,
        "attendance": 85.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_129():
    payload = {
        "rollNo": "21CS160",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.52,
        "activeBacklogs": 5,
        "attendance": 49.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_130():
    payload = {
        "rollNo": "21CS809",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.83,
        "activeBacklogs": 2,
        "attendance": 97.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_131():
    payload = {
        "rollNo": "21CS757",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.49,
        "activeBacklogs": 3,
        "attendance": 63.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_132():
    payload = {
        "rollNo": "21CS450",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.54,
        "activeBacklogs": 0,
        "attendance": 66.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_133():
    payload = {
        "rollNo": "21CS371",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.26,
        "activeBacklogs": 4,
        "attendance": 40.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_134():
    payload = {
        "rollNo": "21CS645",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.77,
        "activeBacklogs": 4,
        "attendance": 62.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_135():
    payload = {
        "rollNo": "21CS996",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.32,
        "activeBacklogs": 1,
        "attendance": 58.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_136():
    payload = {
        "rollNo": "21CS682",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.6,
        "activeBacklogs": 3,
        "attendance": 85.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_137():
    payload = {
        "rollNo": "21CS807",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.47,
        "activeBacklogs": 2,
        "attendance": 98.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_138():
    payload = {
        "rollNo": "21CS178",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.09,
        "activeBacklogs": 2,
        "attendance": 47.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_139():
    payload = {
        "rollNo": "21CS691",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.96,
        "activeBacklogs": 1,
        "attendance": 46.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_140():
    payload = {
        "rollNo": "21CS341",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.69,
        "activeBacklogs": 3,
        "attendance": 71.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_141():
    payload = {
        "rollNo": "21CS704",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.53,
        "activeBacklogs": 3,
        "attendance": 91.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_142():
    payload = {
        "rollNo": "21CS366",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.9,
        "activeBacklogs": 0,
        "attendance": 79.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_143():
    payload = {
        "rollNo": "21CS568",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.86,
        "activeBacklogs": 3,
        "attendance": 60.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_144():
    payload = {
        "rollNo": "21CS733",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.68,
        "activeBacklogs": 1,
        "attendance": 78.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_145():
    payload = {
        "rollNo": "21CS317",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.39,
        "activeBacklogs": 5,
        "attendance": 42.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_146():
    payload = {
        "rollNo": "21CS862",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.08,
        "activeBacklogs": 1,
        "attendance": 68.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_147():
    payload = {
        "rollNo": "21CS782",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.73,
        "activeBacklogs": 5,
        "attendance": 93.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_148():
    payload = {
        "rollNo": "21CS676",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.43,
        "activeBacklogs": 1,
        "attendance": 79.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_149():
    payload = {
        "rollNo": "21CS979",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.76,
        "activeBacklogs": 0,
        "attendance": 88.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_150():
    payload = {
        "rollNo": "21CS310",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.53,
        "activeBacklogs": 1,
        "attendance": 39.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_151():
    payload = {
        "rollNo": "21CS374",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.9,
        "activeBacklogs": 2,
        "attendance": 35.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_152():
    payload = {
        "rollNo": "21CS888",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.39,
        "activeBacklogs": 1,
        "attendance": 54.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_153():
    payload = {
        "rollNo": "21CS659",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.4,
        "activeBacklogs": 4,
        "attendance": 91.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_154():
    payload = {
        "rollNo": "21CS175",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.85,
        "activeBacklogs": 5,
        "attendance": 96.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_155():
    payload = {
        "rollNo": "21CS366",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.47,
        "activeBacklogs": 4,
        "attendance": 98.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_156():
    payload = {
        "rollNo": "21CS366",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.5,
        "activeBacklogs": 1,
        "attendance": 93.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_157():
    payload = {
        "rollNo": "21CS580",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.75,
        "activeBacklogs": 3,
        "attendance": 84.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_158():
    payload = {
        "rollNo": "21CS920",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.02,
        "activeBacklogs": 0,
        "attendance": 69.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_159():
    payload = {
        "rollNo": "21CS609",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.94,
        "activeBacklogs": 4,
        "attendance": 90.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_160():
    payload = {
        "rollNo": "21CS647",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.18,
        "activeBacklogs": 3,
        "attendance": 42.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_161():
    payload = {
        "rollNo": "21CS136",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.39,
        "activeBacklogs": 2,
        "attendance": 30.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_162():
    payload = {
        "rollNo": "21CS393",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.29,
        "activeBacklogs": 1,
        "attendance": 62.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_163():
    payload = {
        "rollNo": "21CS287",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.78,
        "activeBacklogs": 3,
        "attendance": 47.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_164():
    payload = {
        "rollNo": "21CS203",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.08,
        "activeBacklogs": 2,
        "attendance": 88.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_165():
    payload = {
        "rollNo": "21CS620",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.23,
        "activeBacklogs": 1,
        "attendance": 65.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_166():
    payload = {
        "rollNo": "21CS529",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.5,
        "activeBacklogs": 3,
        "attendance": 42.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_167():
    payload = {
        "rollNo": "21CS919",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.89,
        "activeBacklogs": 1,
        "attendance": 38.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_168():
    payload = {
        "rollNo": "21CS783",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.51,
        "activeBacklogs": 4,
        "attendance": 73.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_169():
    payload = {
        "rollNo": "21CS598",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.77,
        "activeBacklogs": 0,
        "attendance": 95.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_170():
    payload = {
        "rollNo": "21CS986",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.91,
        "activeBacklogs": 0,
        "attendance": 65.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_171():
    payload = {
        "rollNo": "21CS786",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.55,
        "activeBacklogs": 5,
        "attendance": 75.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_172():
    payload = {
        "rollNo": "21CS382",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.03,
        "activeBacklogs": 3,
        "attendance": 77.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_173():
    payload = {
        "rollNo": "21CS835",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.85,
        "activeBacklogs": 0,
        "attendance": 52.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_174():
    payload = {
        "rollNo": "21CS722",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.65,
        "activeBacklogs": 4,
        "attendance": 34.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_175():
    payload = {
        "rollNo": "21CS293",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.53,
        "activeBacklogs": 0,
        "attendance": 45.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_176():
    payload = {
        "rollNo": "21CS181",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.36,
        "activeBacklogs": 1,
        "attendance": 83.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_177():
    payload = {
        "rollNo": "21CS188",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.21,
        "activeBacklogs": 0,
        "attendance": 67.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_178():
    payload = {
        "rollNo": "21CS710",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.92,
        "activeBacklogs": 5,
        "attendance": 47.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_179():
    payload = {
        "rollNo": "21CS354",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.34,
        "activeBacklogs": 5,
        "attendance": 73.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_180():
    payload = {
        "rollNo": "21CS191",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.57,
        "activeBacklogs": 1,
        "attendance": 67.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_181():
    payload = {
        "rollNo": "21CS725",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.45,
        "activeBacklogs": 1,
        "attendance": 59.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_182():
    payload = {
        "rollNo": "21CS785",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.63,
        "activeBacklogs": 5,
        "attendance": 59.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_183():
    payload = {
        "rollNo": "21CS280",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.91,
        "activeBacklogs": 3,
        "attendance": 64.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_184():
    payload = {
        "rollNo": "21CS975",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.09,
        "activeBacklogs": 3,
        "attendance": 71.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_185():
    payload = {
        "rollNo": "21CS984",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.72,
        "activeBacklogs": 4,
        "attendance": 50.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_186():
    payload = {
        "rollNo": "21CS657",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.33,
        "activeBacklogs": 2,
        "attendance": 50.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_187():
    payload = {
        "rollNo": "21CS853",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.08,
        "activeBacklogs": 4,
        "attendance": 73.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_188():
    payload = {
        "rollNo": "21CS971",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.36,
        "activeBacklogs": 0,
        "attendance": 86.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_189():
    payload = {
        "rollNo": "21CS486",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.12,
        "activeBacklogs": 3,
        "attendance": 36.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_190():
    payload = {
        "rollNo": "21CS328",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.04,
        "activeBacklogs": 0,
        "attendance": 86.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_191():
    payload = {
        "rollNo": "21CS686",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.97,
        "activeBacklogs": 3,
        "attendance": 81.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_192():
    payload = {
        "rollNo": "21CS616",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.1,
        "activeBacklogs": 5,
        "attendance": 57.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_193():
    payload = {
        "rollNo": "21CS232",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.44,
        "activeBacklogs": 3,
        "attendance": 77.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_194():
    payload = {
        "rollNo": "21CS735",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.55,
        "activeBacklogs": 4,
        "attendance": 61.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_195():
    payload = {
        "rollNo": "21CS477",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.91,
        "activeBacklogs": 3,
        "attendance": 52.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_196():
    payload = {
        "rollNo": "21CS585",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.97,
        "activeBacklogs": 0,
        "attendance": 55.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_197():
    payload = {
        "rollNo": "21CS493",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.1,
        "activeBacklogs": 5,
        "attendance": 43.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_198():
    payload = {
        "rollNo": "21CS583",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.21,
        "activeBacklogs": 0,
        "attendance": 70.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_199():
    payload = {
        "rollNo": "21CS968",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.03,
        "activeBacklogs": 2,
        "attendance": 64.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_200():
    payload = {
        "rollNo": "21CS505",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.77,
        "activeBacklogs": 4,
        "attendance": 84.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_201():
    payload = {
        "rollNo": "21CS958",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.33,
        "activeBacklogs": 4,
        "attendance": 48.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_202():
    payload = {
        "rollNo": "21CS115",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.35,
        "activeBacklogs": 2,
        "attendance": 35.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_203():
    payload = {
        "rollNo": "21CS254",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.81,
        "activeBacklogs": 5,
        "attendance": 55.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_204():
    payload = {
        "rollNo": "21CS622",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.24,
        "activeBacklogs": 5,
        "attendance": 38.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_205():
    payload = {
        "rollNo": "21CS713",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.46,
        "activeBacklogs": 4,
        "attendance": 83.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_206():
    payload = {
        "rollNo": "21CS626",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.33,
        "activeBacklogs": 5,
        "attendance": 43.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_207():
    payload = {
        "rollNo": "21CS682",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.76,
        "activeBacklogs": 0,
        "attendance": 77.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_208():
    payload = {
        "rollNo": "21CS438",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.29,
        "activeBacklogs": 2,
        "attendance": 98.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_209():
    payload = {
        "rollNo": "21CS280",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.57,
        "activeBacklogs": 3,
        "attendance": 61.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_210():
    payload = {
        "rollNo": "21CS201",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.12,
        "activeBacklogs": 0,
        "attendance": 60.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_211():
    payload = {
        "rollNo": "21CS509",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.84,
        "activeBacklogs": 1,
        "attendance": 98.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_212():
    payload = {
        "rollNo": "21CS522",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.95,
        "activeBacklogs": 0,
        "attendance": 82.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_213():
    payload = {
        "rollNo": "21CS633",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.62,
        "activeBacklogs": 0,
        "attendance": 73.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_214():
    payload = {
        "rollNo": "21CS522",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.83,
        "activeBacklogs": 5,
        "attendance": 41.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_215():
    payload = {
        "rollNo": "21CS104",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.11,
        "activeBacklogs": 5,
        "attendance": 94.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_216():
    payload = {
        "rollNo": "21CS744",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.55,
        "activeBacklogs": 4,
        "attendance": 38.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_217():
    payload = {
        "rollNo": "21CS406",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.83,
        "activeBacklogs": 0,
        "attendance": 42.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_218():
    payload = {
        "rollNo": "21CS676",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.39,
        "activeBacklogs": 1,
        "attendance": 55.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_219():
    payload = {
        "rollNo": "21CS236",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.69,
        "activeBacklogs": 5,
        "attendance": 54.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_220():
    payload = {
        "rollNo": "21CS690",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.55,
        "activeBacklogs": 1,
        "attendance": 97.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_221():
    payload = {
        "rollNo": "21CS365",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.43,
        "activeBacklogs": 5,
        "attendance": 91.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_222():
    payload = {
        "rollNo": "21CS361",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.91,
        "activeBacklogs": 4,
        "attendance": 39.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_223():
    payload = {
        "rollNo": "21CS561",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.34,
        "activeBacklogs": 3,
        "attendance": 61.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_224():
    payload = {
        "rollNo": "21CS705",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.28,
        "activeBacklogs": 2,
        "attendance": 90.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_225():
    payload = {
        "rollNo": "21CS378",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.3,
        "activeBacklogs": 3,
        "attendance": 88.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_226():
    payload = {
        "rollNo": "21CS671",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.97,
        "activeBacklogs": 2,
        "attendance": 70.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_227():
    payload = {
        "rollNo": "21CS599",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.61,
        "activeBacklogs": 3,
        "attendance": 74.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_228():
    payload = {
        "rollNo": "21CS245",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.09,
        "activeBacklogs": 3,
        "attendance": 74.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_229():
    payload = {
        "rollNo": "21CS630",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.52,
        "activeBacklogs": 1,
        "attendance": 33.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_230():
    payload = {
        "rollNo": "21CS214",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.39,
        "activeBacklogs": 3,
        "attendance": 89.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_231():
    payload = {
        "rollNo": "21CS373",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.55,
        "activeBacklogs": 5,
        "attendance": 49.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_232():
    payload = {
        "rollNo": "21CS236",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.53,
        "activeBacklogs": 0,
        "attendance": 94.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_233():
    payload = {
        "rollNo": "21CS538",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.87,
        "activeBacklogs": 0,
        "attendance": 70.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_234():
    payload = {
        "rollNo": "21CS924",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.44,
        "activeBacklogs": 0,
        "attendance": 39.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_235():
    payload = {
        "rollNo": "21CS830",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.55,
        "activeBacklogs": 5,
        "attendance": 68.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_236():
    payload = {
        "rollNo": "21CS805",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.65,
        "activeBacklogs": 4,
        "attendance": 74.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_237():
    payload = {
        "rollNo": "21CS909",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.01,
        "activeBacklogs": 2,
        "attendance": 69.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_238():
    payload = {
        "rollNo": "21CS918",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.34,
        "activeBacklogs": 1,
        "attendance": 40.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_239():
    payload = {
        "rollNo": "21CS435",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.74,
        "activeBacklogs": 1,
        "attendance": 95.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_240():
    payload = {
        "rollNo": "21CS536",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.78,
        "activeBacklogs": 0,
        "attendance": 50.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_241():
    payload = {
        "rollNo": "21CS589",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.97,
        "activeBacklogs": 4,
        "attendance": 30.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_242():
    payload = {
        "rollNo": "21CS657",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.33,
        "activeBacklogs": 3,
        "attendance": 81.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_243():
    payload = {
        "rollNo": "21CS951",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.73,
        "activeBacklogs": 2,
        "attendance": 38.04
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_244():
    payload = {
        "rollNo": "21CS945",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.22,
        "activeBacklogs": 2,
        "attendance": 91.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_245():
    payload = {
        "rollNo": "21CS932",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.98,
        "activeBacklogs": 0,
        "attendance": 83.04
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_246():
    payload = {
        "rollNo": "21CS585",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.31,
        "activeBacklogs": 1,
        "attendance": 40.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_247():
    payload = {
        "rollNo": "21CS327",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.28,
        "activeBacklogs": 2,
        "attendance": 98.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_248():
    payload = {
        "rollNo": "21CS479",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.51,
        "activeBacklogs": 2,
        "attendance": 90.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_11_249():
    payload = {
        "rollNo": "21CS819",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.2,
        "activeBacklogs": 4,
        "attendance": 61.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

import pytest
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_prediction_case_6_0():
    payload = {
        "rollNo": "21CS565",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.27,
        "activeBacklogs": 0,
        "attendance": 53.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_1():
    payload = {
        "rollNo": "21CS775",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.02,
        "activeBacklogs": 0,
        "attendance": 49.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_2():
    payload = {
        "rollNo": "21CS964",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.64,
        "activeBacklogs": 1,
        "attendance": 40.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_3():
    payload = {
        "rollNo": "21CS337",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.16,
        "activeBacklogs": 0,
        "attendance": 99.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_4():
    payload = {
        "rollNo": "21CS883",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.02,
        "activeBacklogs": 0,
        "attendance": 77.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_5():
    payload = {
        "rollNo": "21CS928",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.3,
        "activeBacklogs": 2,
        "attendance": 87.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_6():
    payload = {
        "rollNo": "21CS190",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.45,
        "activeBacklogs": 4,
        "attendance": 77.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_7():
    payload = {
        "rollNo": "21CS503",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.38,
        "activeBacklogs": 1,
        "attendance": 60.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_8():
    payload = {
        "rollNo": "21CS750",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.41,
        "activeBacklogs": 4,
        "attendance": 76.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_9():
    payload = {
        "rollNo": "21CS500",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.96,
        "activeBacklogs": 1,
        "attendance": 51.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_10():
    payload = {
        "rollNo": "21CS759",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.69,
        "activeBacklogs": 3,
        "attendance": 98.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_11():
    payload = {
        "rollNo": "21CS449",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.97,
        "activeBacklogs": 3,
        "attendance": 42.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_12():
    payload = {
        "rollNo": "21CS703",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.2,
        "activeBacklogs": 5,
        "attendance": 57.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_13():
    payload = {
        "rollNo": "21CS340",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.19,
        "activeBacklogs": 3,
        "attendance": 96.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_14():
    payload = {
        "rollNo": "21CS580",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.4,
        "activeBacklogs": 0,
        "attendance": 42.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_15():
    payload = {
        "rollNo": "21CS381",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.7,
        "activeBacklogs": 5,
        "attendance": 97.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_16():
    payload = {
        "rollNo": "21CS389",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.71,
        "activeBacklogs": 1,
        "attendance": 63.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_17():
    payload = {
        "rollNo": "21CS499",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.37,
        "activeBacklogs": 4,
        "attendance": 56.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_18():
    payload = {
        "rollNo": "21CS730",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.85,
        "activeBacklogs": 4,
        "attendance": 60.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_19():
    payload = {
        "rollNo": "21CS223",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.14,
        "activeBacklogs": 1,
        "attendance": 68.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_20():
    payload = {
        "rollNo": "21CS767",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.65,
        "activeBacklogs": 5,
        "attendance": 32.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_21():
    payload = {
        "rollNo": "21CS195",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.49,
        "activeBacklogs": 5,
        "attendance": 98.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_22():
    payload = {
        "rollNo": "21CS485",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.96,
        "activeBacklogs": 0,
        "attendance": 92.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_23():
    payload = {
        "rollNo": "21CS513",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.76,
        "activeBacklogs": 4,
        "attendance": 56.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_24():
    payload = {
        "rollNo": "21CS502",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.95,
        "activeBacklogs": 3,
        "attendance": 87.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_25():
    payload = {
        "rollNo": "21CS285",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.0,
        "activeBacklogs": 5,
        "attendance": 95.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_26():
    payload = {
        "rollNo": "21CS949",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.6,
        "activeBacklogs": 4,
        "attendance": 50.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_27():
    payload = {
        "rollNo": "21CS172",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.12,
        "activeBacklogs": 4,
        "attendance": 96.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_28():
    payload = {
        "rollNo": "21CS273",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.55,
        "activeBacklogs": 2,
        "attendance": 85.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_29():
    payload = {
        "rollNo": "21CS225",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.75,
        "activeBacklogs": 3,
        "attendance": 69.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_30():
    payload = {
        "rollNo": "21CS240",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.49,
        "activeBacklogs": 3,
        "attendance": 38.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_31():
    payload = {
        "rollNo": "21CS785",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.08,
        "activeBacklogs": 4,
        "attendance": 66.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_32():
    payload = {
        "rollNo": "21CS771",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.71,
        "activeBacklogs": 5,
        "attendance": 35.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_33():
    payload = {
        "rollNo": "21CS734",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.06,
        "activeBacklogs": 5,
        "attendance": 98.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_34():
    payload = {
        "rollNo": "21CS916",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.71,
        "activeBacklogs": 4,
        "attendance": 79.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_35():
    payload = {
        "rollNo": "21CS689",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.28,
        "activeBacklogs": 5,
        "attendance": 30.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_36():
    payload = {
        "rollNo": "21CS455",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.67,
        "activeBacklogs": 1,
        "attendance": 76.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_37():
    payload = {
        "rollNo": "21CS446",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.5,
        "activeBacklogs": 5,
        "attendance": 56.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_38():
    payload = {
        "rollNo": "21CS857",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.4,
        "activeBacklogs": 4,
        "attendance": 65.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_39():
    payload = {
        "rollNo": "21CS371",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.49,
        "activeBacklogs": 2,
        "attendance": 67.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_40():
    payload = {
        "rollNo": "21CS705",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.4,
        "activeBacklogs": 5,
        "attendance": 42.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_41():
    payload = {
        "rollNo": "21CS244",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.26,
        "activeBacklogs": 0,
        "attendance": 54.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_42():
    payload = {
        "rollNo": "21CS318",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.92,
        "activeBacklogs": 1,
        "attendance": 55.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_43():
    payload = {
        "rollNo": "21CS369",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.58,
        "activeBacklogs": 5,
        "attendance": 95.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_44():
    payload = {
        "rollNo": "21CS763",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.48,
        "activeBacklogs": 4,
        "attendance": 50.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_45():
    payload = {
        "rollNo": "21CS888",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.64,
        "activeBacklogs": 2,
        "attendance": 43.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_46():
    payload = {
        "rollNo": "21CS158",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.43,
        "activeBacklogs": 1,
        "attendance": 63.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_47():
    payload = {
        "rollNo": "21CS745",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.54,
        "activeBacklogs": 0,
        "attendance": 55.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_48():
    payload = {
        "rollNo": "21CS872",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.34,
        "activeBacklogs": 2,
        "attendance": 54.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_49():
    payload = {
        "rollNo": "21CS975",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.64,
        "activeBacklogs": 0,
        "attendance": 57.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_50():
    payload = {
        "rollNo": "21CS676",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.06,
        "activeBacklogs": 5,
        "attendance": 32.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_51():
    payload = {
        "rollNo": "21CS347",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.56,
        "activeBacklogs": 5,
        "attendance": 94.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_52():
    payload = {
        "rollNo": "21CS513",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.31,
        "activeBacklogs": 5,
        "attendance": 65.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_53():
    payload = {
        "rollNo": "21CS582",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.93,
        "activeBacklogs": 1,
        "attendance": 87.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_54():
    payload = {
        "rollNo": "21CS973",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.89,
        "activeBacklogs": 5,
        "attendance": 30.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_55():
    payload = {
        "rollNo": "21CS675",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.7,
        "activeBacklogs": 2,
        "attendance": 50.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_56():
    payload = {
        "rollNo": "21CS696",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.81,
        "activeBacklogs": 1,
        "attendance": 98.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_57():
    payload = {
        "rollNo": "21CS739",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.78,
        "activeBacklogs": 5,
        "attendance": 89.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_58():
    payload = {
        "rollNo": "21CS750",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.3,
        "activeBacklogs": 4,
        "attendance": 98.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_59():
    payload = {
        "rollNo": "21CS953",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.59,
        "activeBacklogs": 0,
        "attendance": 35.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_60():
    payload = {
        "rollNo": "21CS941",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.4,
        "activeBacklogs": 4,
        "attendance": 60.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_61():
    payload = {
        "rollNo": "21CS830",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.17,
        "activeBacklogs": 0,
        "attendance": 30.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_62():
    payload = {
        "rollNo": "21CS934",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.83,
        "activeBacklogs": 5,
        "attendance": 92.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_63():
    payload = {
        "rollNo": "21CS751",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.75,
        "activeBacklogs": 1,
        "attendance": 98.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_64():
    payload = {
        "rollNo": "21CS122",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.11,
        "activeBacklogs": 3,
        "attendance": 64.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_65():
    payload = {
        "rollNo": "21CS550",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.82,
        "activeBacklogs": 5,
        "attendance": 59.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_66():
    payload = {
        "rollNo": "21CS608",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.93,
        "activeBacklogs": 1,
        "attendance": 69.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_67():
    payload = {
        "rollNo": "21CS982",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.19,
        "activeBacklogs": 1,
        "attendance": 78.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_68():
    payload = {
        "rollNo": "21CS993",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.46,
        "activeBacklogs": 5,
        "attendance": 73.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_69():
    payload = {
        "rollNo": "21CS195",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.23,
        "activeBacklogs": 4,
        "attendance": 39.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_70():
    payload = {
        "rollNo": "21CS196",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.87,
        "activeBacklogs": 4,
        "attendance": 55.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_71():
    payload = {
        "rollNo": "21CS666",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.84,
        "activeBacklogs": 5,
        "attendance": 35.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_72():
    payload = {
        "rollNo": "21CS240",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.45,
        "activeBacklogs": 5,
        "attendance": 73.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_73():
    payload = {
        "rollNo": "21CS371",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.65,
        "activeBacklogs": 2,
        "attendance": 61.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_74():
    payload = {
        "rollNo": "21CS210",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.33,
        "activeBacklogs": 2,
        "attendance": 98.04
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_75():
    payload = {
        "rollNo": "21CS250",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.17,
        "activeBacklogs": 4,
        "attendance": 38.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_76():
    payload = {
        "rollNo": "21CS820",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.9,
        "activeBacklogs": 5,
        "attendance": 87.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_77():
    payload = {
        "rollNo": "21CS117",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.72,
        "activeBacklogs": 1,
        "attendance": 37.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_78():
    payload = {
        "rollNo": "21CS983",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.26,
        "activeBacklogs": 0,
        "attendance": 93.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_79():
    payload = {
        "rollNo": "21CS830",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.79,
        "activeBacklogs": 2,
        "attendance": 41.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_80():
    payload = {
        "rollNo": "21CS778",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.54,
        "activeBacklogs": 1,
        "attendance": 52.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_81():
    payload = {
        "rollNo": "21CS630",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.11,
        "activeBacklogs": 3,
        "attendance": 76.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_82():
    payload = {
        "rollNo": "21CS436",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.38,
        "activeBacklogs": 3,
        "attendance": 36.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_83():
    payload = {
        "rollNo": "21CS247",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.21,
        "activeBacklogs": 0,
        "attendance": 68.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_84():
    payload = {
        "rollNo": "21CS243",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.81,
        "activeBacklogs": 2,
        "attendance": 44.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_85():
    payload = {
        "rollNo": "21CS510",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.04,
        "activeBacklogs": 3,
        "attendance": 52.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_86():
    payload = {
        "rollNo": "21CS784",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.79,
        "activeBacklogs": 4,
        "attendance": 33.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_87():
    payload = {
        "rollNo": "21CS720",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.83,
        "activeBacklogs": 0,
        "attendance": 46.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_88():
    payload = {
        "rollNo": "21CS253",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.57,
        "activeBacklogs": 5,
        "attendance": 85.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_89():
    payload = {
        "rollNo": "21CS819",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.43,
        "activeBacklogs": 3,
        "attendance": 97.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_90():
    payload = {
        "rollNo": "21CS184",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.72,
        "activeBacklogs": 5,
        "attendance": 99.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_91():
    payload = {
        "rollNo": "21CS596",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.97,
        "activeBacklogs": 5,
        "attendance": 59.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_92():
    payload = {
        "rollNo": "21CS229",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.09,
        "activeBacklogs": 5,
        "attendance": 91.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_93():
    payload = {
        "rollNo": "21CS792",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.56,
        "activeBacklogs": 1,
        "attendance": 89.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_94():
    payload = {
        "rollNo": "21CS577",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.43,
        "activeBacklogs": 2,
        "attendance": 98.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_95():
    payload = {
        "rollNo": "21CS689",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.66,
        "activeBacklogs": 4,
        "attendance": 76.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_96():
    payload = {
        "rollNo": "21CS522",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.52,
        "activeBacklogs": 0,
        "attendance": 60.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_97():
    payload = {
        "rollNo": "21CS839",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.15,
        "activeBacklogs": 2,
        "attendance": 78.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_98():
    payload = {
        "rollNo": "21CS850",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.43,
        "activeBacklogs": 2,
        "attendance": 74.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_99():
    payload = {
        "rollNo": "21CS141",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.34,
        "activeBacklogs": 5,
        "attendance": 33.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_100():
    payload = {
        "rollNo": "21CS191",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.51,
        "activeBacklogs": 0,
        "attendance": 51.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_101():
    payload = {
        "rollNo": "21CS744",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.94,
        "activeBacklogs": 4,
        "attendance": 86.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_102():
    payload = {
        "rollNo": "21CS580",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.35,
        "activeBacklogs": 5,
        "attendance": 61.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_103():
    payload = {
        "rollNo": "21CS261",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.23,
        "activeBacklogs": 4,
        "attendance": 69.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_104():
    payload = {
        "rollNo": "21CS103",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.71,
        "activeBacklogs": 1,
        "attendance": 90.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_105():
    payload = {
        "rollNo": "21CS205",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.14,
        "activeBacklogs": 2,
        "attendance": 98.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_106():
    payload = {
        "rollNo": "21CS386",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.89,
        "activeBacklogs": 2,
        "attendance": 34.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_107():
    payload = {
        "rollNo": "21CS631",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.83,
        "activeBacklogs": 5,
        "attendance": 65.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_108():
    payload = {
        "rollNo": "21CS791",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.55,
        "activeBacklogs": 1,
        "attendance": 46.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_109():
    payload = {
        "rollNo": "21CS661",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.72,
        "activeBacklogs": 2,
        "attendance": 53.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_110():
    payload = {
        "rollNo": "21CS585",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.12,
        "activeBacklogs": 2,
        "attendance": 68.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_111():
    payload = {
        "rollNo": "21CS665",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.57,
        "activeBacklogs": 4,
        "attendance": 45.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_112():
    payload = {
        "rollNo": "21CS835",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.37,
        "activeBacklogs": 4,
        "attendance": 93.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_113():
    payload = {
        "rollNo": "21CS569",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.35,
        "activeBacklogs": 3,
        "attendance": 63.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_114():
    payload = {
        "rollNo": "21CS202",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.99,
        "activeBacklogs": 4,
        "attendance": 76.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_115():
    payload = {
        "rollNo": "21CS558",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.75,
        "activeBacklogs": 3,
        "attendance": 89.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_116():
    payload = {
        "rollNo": "21CS553",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.45,
        "activeBacklogs": 3,
        "attendance": 56.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_117():
    payload = {
        "rollNo": "21CS452",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.85,
        "activeBacklogs": 4,
        "attendance": 65.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_118():
    payload = {
        "rollNo": "21CS742",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.73,
        "activeBacklogs": 3,
        "attendance": 86.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_119():
    payload = {
        "rollNo": "21CS981",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.51,
        "activeBacklogs": 4,
        "attendance": 80.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_120():
    payload = {
        "rollNo": "21CS252",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.43,
        "activeBacklogs": 0,
        "attendance": 75.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_121():
    payload = {
        "rollNo": "21CS969",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.98,
        "activeBacklogs": 3,
        "attendance": 90.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_122():
    payload = {
        "rollNo": "21CS155",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.81,
        "activeBacklogs": 1,
        "attendance": 32.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_123():
    payload = {
        "rollNo": "21CS858",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.14,
        "activeBacklogs": 1,
        "attendance": 87.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_124():
    payload = {
        "rollNo": "21CS400",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.8,
        "activeBacklogs": 4,
        "attendance": 49.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_125():
    payload = {
        "rollNo": "21CS883",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.25,
        "activeBacklogs": 3,
        "attendance": 80.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_126():
    payload = {
        "rollNo": "21CS807",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.2,
        "activeBacklogs": 2,
        "attendance": 42.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_127():
    payload = {
        "rollNo": "21CS123",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.03,
        "activeBacklogs": 0,
        "attendance": 30.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_128():
    payload = {
        "rollNo": "21CS637",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.25,
        "activeBacklogs": 3,
        "attendance": 95.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_129():
    payload = {
        "rollNo": "21CS811",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.55,
        "activeBacklogs": 3,
        "attendance": 64.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_130():
    payload = {
        "rollNo": "21CS749",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.89,
        "activeBacklogs": 2,
        "attendance": 52.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_131():
    payload = {
        "rollNo": "21CS503",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.84,
        "activeBacklogs": 0,
        "attendance": 42.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_132():
    payload = {
        "rollNo": "21CS530",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.17,
        "activeBacklogs": 4,
        "attendance": 47.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_133():
    payload = {
        "rollNo": "21CS945",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.27,
        "activeBacklogs": 2,
        "attendance": 86.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_134():
    payload = {
        "rollNo": "21CS710",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.06,
        "activeBacklogs": 1,
        "attendance": 41.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_135():
    payload = {
        "rollNo": "21CS511",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.0,
        "activeBacklogs": 5,
        "attendance": 44.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_136():
    payload = {
        "rollNo": "21CS287",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.17,
        "activeBacklogs": 1,
        "attendance": 50.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_137():
    payload = {
        "rollNo": "21CS370",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.37,
        "activeBacklogs": 5,
        "attendance": 36.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_138():
    payload = {
        "rollNo": "21CS207",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.59,
        "activeBacklogs": 1,
        "attendance": 59.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_139():
    payload = {
        "rollNo": "21CS420",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.13,
        "activeBacklogs": 2,
        "attendance": 83.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_140():
    payload = {
        "rollNo": "21CS612",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.06,
        "activeBacklogs": 3,
        "attendance": 91.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_141():
    payload = {
        "rollNo": "21CS325",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.6,
        "activeBacklogs": 5,
        "attendance": 51.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_142():
    payload = {
        "rollNo": "21CS857",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.71,
        "activeBacklogs": 0,
        "attendance": 70.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_143():
    payload = {
        "rollNo": "21CS664",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.49,
        "activeBacklogs": 2,
        "attendance": 41.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_144():
    payload = {
        "rollNo": "21CS285",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.77,
        "activeBacklogs": 3,
        "attendance": 89.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_145():
    payload = {
        "rollNo": "21CS877",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.09,
        "activeBacklogs": 1,
        "attendance": 96.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_146():
    payload = {
        "rollNo": "21CS773",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.55,
        "activeBacklogs": 5,
        "attendance": 37.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_147():
    payload = {
        "rollNo": "21CS727",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.85,
        "activeBacklogs": 5,
        "attendance": 85.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_148():
    payload = {
        "rollNo": "21CS872",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.84,
        "activeBacklogs": 0,
        "attendance": 45.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_149():
    payload = {
        "rollNo": "21CS457",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.85,
        "activeBacklogs": 5,
        "attendance": 72.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_150():
    payload = {
        "rollNo": "21CS472",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.48,
        "activeBacklogs": 0,
        "attendance": 85.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_151():
    payload = {
        "rollNo": "21CS582",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.65,
        "activeBacklogs": 2,
        "attendance": 57.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_152():
    payload = {
        "rollNo": "21CS606",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.03,
        "activeBacklogs": 2,
        "attendance": 52.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_153():
    payload = {
        "rollNo": "21CS489",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.17,
        "activeBacklogs": 0,
        "attendance": 33.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_154():
    payload = {
        "rollNo": "21CS988",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.29,
        "activeBacklogs": 3,
        "attendance": 39.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_155():
    payload = {
        "rollNo": "21CS390",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.78,
        "activeBacklogs": 5,
        "attendance": 43.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_156():
    payload = {
        "rollNo": "21CS693",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.34,
        "activeBacklogs": 2,
        "attendance": 84.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_157():
    payload = {
        "rollNo": "21CS323",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.9,
        "activeBacklogs": 3,
        "attendance": 62.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_158():
    payload = {
        "rollNo": "21CS305",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.02,
        "activeBacklogs": 2,
        "attendance": 71.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_159():
    payload = {
        "rollNo": "21CS422",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.67,
        "activeBacklogs": 0,
        "attendance": 63.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_160():
    payload = {
        "rollNo": "21CS822",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.54,
        "activeBacklogs": 4,
        "attendance": 78.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_161():
    payload = {
        "rollNo": "21CS162",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.06,
        "activeBacklogs": 2,
        "attendance": 47.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_162():
    payload = {
        "rollNo": "21CS290",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.38,
        "activeBacklogs": 4,
        "attendance": 62.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_163():
    payload = {
        "rollNo": "21CS722",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.45,
        "activeBacklogs": 0,
        "attendance": 79.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_164():
    payload = {
        "rollNo": "21CS561",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.08,
        "activeBacklogs": 1,
        "attendance": 74.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_165():
    payload = {
        "rollNo": "21CS210",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.81,
        "activeBacklogs": 2,
        "attendance": 43.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_166():
    payload = {
        "rollNo": "21CS930",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.23,
        "activeBacklogs": 4,
        "attendance": 41.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_167():
    payload = {
        "rollNo": "21CS818",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.35,
        "activeBacklogs": 2,
        "attendance": 39.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_168():
    payload = {
        "rollNo": "21CS607",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.81,
        "activeBacklogs": 0,
        "attendance": 82.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_169():
    payload = {
        "rollNo": "21CS367",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.93,
        "activeBacklogs": 1,
        "attendance": 66.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_170():
    payload = {
        "rollNo": "21CS386",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.03,
        "activeBacklogs": 0,
        "attendance": 40.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_171():
    payload = {
        "rollNo": "21CS540",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.53,
        "activeBacklogs": 1,
        "attendance": 39.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_172():
    payload = {
        "rollNo": "21CS618",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.29,
        "activeBacklogs": 5,
        "attendance": 41.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_173():
    payload = {
        "rollNo": "21CS517",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.95,
        "activeBacklogs": 1,
        "attendance": 46.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_174():
    payload = {
        "rollNo": "21CS882",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.09,
        "activeBacklogs": 5,
        "attendance": 57.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_175():
    payload = {
        "rollNo": "21CS683",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.9,
        "activeBacklogs": 4,
        "attendance": 64.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_176():
    payload = {
        "rollNo": "21CS549",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.52,
        "activeBacklogs": 0,
        "attendance": 72.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_177():
    payload = {
        "rollNo": "21CS740",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.71,
        "activeBacklogs": 3,
        "attendance": 39.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_178():
    payload = {
        "rollNo": "21CS640",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.36,
        "activeBacklogs": 5,
        "attendance": 30.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_179():
    payload = {
        "rollNo": "21CS390",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.15,
        "activeBacklogs": 1,
        "attendance": 96.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_180():
    payload = {
        "rollNo": "21CS554",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.22,
        "activeBacklogs": 0,
        "attendance": 71.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_181():
    payload = {
        "rollNo": "21CS916",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.39,
        "activeBacklogs": 2,
        "attendance": 51.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_182():
    payload = {
        "rollNo": "21CS997",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.95,
        "activeBacklogs": 0,
        "attendance": 38.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_183():
    payload = {
        "rollNo": "21CS236",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.03,
        "activeBacklogs": 5,
        "attendance": 34.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_184():
    payload = {
        "rollNo": "21CS533",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.65,
        "activeBacklogs": 4,
        "attendance": 32.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_185():
    payload = {
        "rollNo": "21CS652",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.65,
        "activeBacklogs": 1,
        "attendance": 86.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_186():
    payload = {
        "rollNo": "21CS999",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.84,
        "activeBacklogs": 3,
        "attendance": 53.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_187():
    payload = {
        "rollNo": "21CS732",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.17,
        "activeBacklogs": 2,
        "attendance": 69.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_188():
    payload = {
        "rollNo": "21CS213",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.87,
        "activeBacklogs": 5,
        "attendance": 66.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_189():
    payload = {
        "rollNo": "21CS442",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.15,
        "activeBacklogs": 4,
        "attendance": 80.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_190():
    payload = {
        "rollNo": "21CS511",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.34,
        "activeBacklogs": 0,
        "attendance": 34.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_191():
    payload = {
        "rollNo": "21CS717",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.61,
        "activeBacklogs": 4,
        "attendance": 47.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_192():
    payload = {
        "rollNo": "21CS417",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.74,
        "activeBacklogs": 5,
        "attendance": 75.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_193():
    payload = {
        "rollNo": "21CS980",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.23,
        "activeBacklogs": 5,
        "attendance": 42.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_194():
    payload = {
        "rollNo": "21CS334",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.08,
        "activeBacklogs": 0,
        "attendance": 85.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_195():
    payload = {
        "rollNo": "21CS207",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.22,
        "activeBacklogs": 3,
        "attendance": 80.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_196():
    payload = {
        "rollNo": "21CS537",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.76,
        "activeBacklogs": 4,
        "attendance": 32.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_197():
    payload = {
        "rollNo": "21CS413",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.24,
        "activeBacklogs": 0,
        "attendance": 95.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_198():
    payload = {
        "rollNo": "21CS894",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.31,
        "activeBacklogs": 3,
        "attendance": 76.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_199():
    payload = {
        "rollNo": "21CS111",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.22,
        "activeBacklogs": 3,
        "attendance": 81.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_200():
    payload = {
        "rollNo": "21CS816",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.34,
        "activeBacklogs": 3,
        "attendance": 42.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_201():
    payload = {
        "rollNo": "21CS721",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.14,
        "activeBacklogs": 4,
        "attendance": 66.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_202():
    payload = {
        "rollNo": "21CS444",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.7,
        "activeBacklogs": 4,
        "attendance": 64.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_203():
    payload = {
        "rollNo": "21CS745",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.37,
        "activeBacklogs": 4,
        "attendance": 34.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_204():
    payload = {
        "rollNo": "21CS398",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.97,
        "activeBacklogs": 1,
        "attendance": 59.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_205():
    payload = {
        "rollNo": "21CS279",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.12,
        "activeBacklogs": 5,
        "attendance": 88.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_206():
    payload = {
        "rollNo": "21CS792",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.37,
        "activeBacklogs": 5,
        "attendance": 88.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_207():
    payload = {
        "rollNo": "21CS452",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.9,
        "activeBacklogs": 0,
        "attendance": 48.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_208():
    payload = {
        "rollNo": "21CS686",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.22,
        "activeBacklogs": 1,
        "attendance": 73.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_209():
    payload = {
        "rollNo": "21CS998",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.43,
        "activeBacklogs": 3,
        "attendance": 51.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_210():
    payload = {
        "rollNo": "21CS169",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.66,
        "activeBacklogs": 0,
        "attendance": 56.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_211():
    payload = {
        "rollNo": "21CS791",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.63,
        "activeBacklogs": 2,
        "attendance": 38.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_212():
    payload = {
        "rollNo": "21CS672",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.12,
        "activeBacklogs": 3,
        "attendance": 61.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_213():
    payload = {
        "rollNo": "21CS988",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.06,
        "activeBacklogs": 4,
        "attendance": 72.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_214():
    payload = {
        "rollNo": "21CS820",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.46,
        "activeBacklogs": 1,
        "attendance": 95.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_215():
    payload = {
        "rollNo": "21CS843",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.31,
        "activeBacklogs": 0,
        "attendance": 43.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_216():
    payload = {
        "rollNo": "21CS955",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.55,
        "activeBacklogs": 0,
        "attendance": 77.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_217():
    payload = {
        "rollNo": "21CS664",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.29,
        "activeBacklogs": 0,
        "attendance": 38.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_218():
    payload = {
        "rollNo": "21CS171",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.81,
        "activeBacklogs": 4,
        "attendance": 78.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_219():
    payload = {
        "rollNo": "21CS265",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.68,
        "activeBacklogs": 1,
        "attendance": 54.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_220():
    payload = {
        "rollNo": "21CS319",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.61,
        "activeBacklogs": 5,
        "attendance": 53.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_221():
    payload = {
        "rollNo": "21CS567",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.56,
        "activeBacklogs": 1,
        "attendance": 34.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_222():
    payload = {
        "rollNo": "21CS107",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.85,
        "activeBacklogs": 0,
        "attendance": 67.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_223():
    payload = {
        "rollNo": "21CS689",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.19,
        "activeBacklogs": 4,
        "attendance": 54.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_224():
    payload = {
        "rollNo": "21CS449",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.04,
        "activeBacklogs": 2,
        "attendance": 79.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_225():
    payload = {
        "rollNo": "21CS137",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.5,
        "activeBacklogs": 2,
        "attendance": 94.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_226():
    payload = {
        "rollNo": "21CS614",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.56,
        "activeBacklogs": 5,
        "attendance": 55.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_227():
    payload = {
        "rollNo": "21CS400",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.29,
        "activeBacklogs": 2,
        "attendance": 92.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_228():
    payload = {
        "rollNo": "21CS442",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.02,
        "activeBacklogs": 2,
        "attendance": 42.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_229():
    payload = {
        "rollNo": "21CS242",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.1,
        "activeBacklogs": 2,
        "attendance": 81.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_230():
    payload = {
        "rollNo": "21CS244",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.87,
        "activeBacklogs": 1,
        "attendance": 75.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_231():
    payload = {
        "rollNo": "21CS639",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.84,
        "activeBacklogs": 3,
        "attendance": 60.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_232():
    payload = {
        "rollNo": "21CS965",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.15,
        "activeBacklogs": 1,
        "attendance": 44.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_233():
    payload = {
        "rollNo": "21CS439",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.49,
        "activeBacklogs": 4,
        "attendance": 72.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_234():
    payload = {
        "rollNo": "21CS717",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.44,
        "activeBacklogs": 4,
        "attendance": 68.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_235():
    payload = {
        "rollNo": "21CS753",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.8,
        "activeBacklogs": 0,
        "attendance": 58.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_236():
    payload = {
        "rollNo": "21CS541",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.7,
        "activeBacklogs": 4,
        "attendance": 42.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_237():
    payload = {
        "rollNo": "21CS304",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.49,
        "activeBacklogs": 1,
        "attendance": 65.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_238():
    payload = {
        "rollNo": "21CS609",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.56,
        "activeBacklogs": 2,
        "attendance": 81.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_239():
    payload = {
        "rollNo": "21CS714",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.67,
        "activeBacklogs": 3,
        "attendance": 37.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_240():
    payload = {
        "rollNo": "21CS779",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.36,
        "activeBacklogs": 2,
        "attendance": 56.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_241():
    payload = {
        "rollNo": "21CS469",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.15,
        "activeBacklogs": 4,
        "attendance": 96.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_242():
    payload = {
        "rollNo": "21CS734",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.8,
        "activeBacklogs": 4,
        "attendance": 52.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_243():
    payload = {
        "rollNo": "21CS160",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.32,
        "activeBacklogs": 3,
        "attendance": 56.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_244():
    payload = {
        "rollNo": "21CS615",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.31,
        "activeBacklogs": 4,
        "attendance": 67.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_245():
    payload = {
        "rollNo": "21CS100",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.1,
        "activeBacklogs": 4,
        "attendance": 97.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_246():
    payload = {
        "rollNo": "21CS525",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.99,
        "activeBacklogs": 1,
        "attendance": 87.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_247():
    payload = {
        "rollNo": "21CS246",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.32,
        "activeBacklogs": 3,
        "attendance": 93.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_248():
    payload = {
        "rollNo": "21CS332",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.6,
        "activeBacklogs": 0,
        "attendance": 82.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_6_249():
    payload = {
        "rollNo": "21CS540",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.9,
        "activeBacklogs": 0,
        "attendance": 36.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

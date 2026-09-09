import pytest
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_prediction_case_13_0():
    payload = {
        "rollNo": "21CS755",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.23,
        "activeBacklogs": 5,
        "attendance": 63.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_1():
    payload = {
        "rollNo": "21CS301",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.75,
        "activeBacklogs": 0,
        "attendance": 62.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_2():
    payload = {
        "rollNo": "21CS667",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.11,
        "activeBacklogs": 5,
        "attendance": 38.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_3():
    payload = {
        "rollNo": "21CS262",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.99,
        "activeBacklogs": 5,
        "attendance": 61.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_4():
    payload = {
        "rollNo": "21CS189",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.0,
        "activeBacklogs": 5,
        "attendance": 79.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_5():
    payload = {
        "rollNo": "21CS908",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.54,
        "activeBacklogs": 2,
        "attendance": 56.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_6():
    payload = {
        "rollNo": "21CS387",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.78,
        "activeBacklogs": 4,
        "attendance": 73.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_7():
    payload = {
        "rollNo": "21CS306",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.7,
        "activeBacklogs": 0,
        "attendance": 97.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_8():
    payload = {
        "rollNo": "21CS520",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.18,
        "activeBacklogs": 5,
        "attendance": 95.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_9():
    payload = {
        "rollNo": "21CS618",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.56,
        "activeBacklogs": 2,
        "attendance": 48.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_10():
    payload = {
        "rollNo": "21CS117",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.45,
        "activeBacklogs": 2,
        "attendance": 98.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_11():
    payload = {
        "rollNo": "21CS591",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.11,
        "activeBacklogs": 3,
        "attendance": 96.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_12():
    payload = {
        "rollNo": "21CS525",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.93,
        "activeBacklogs": 0,
        "attendance": 44.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_13():
    payload = {
        "rollNo": "21CS887",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.6,
        "activeBacklogs": 1,
        "attendance": 51.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_14():
    payload = {
        "rollNo": "21CS105",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.38,
        "activeBacklogs": 5,
        "attendance": 50.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_15():
    payload = {
        "rollNo": "21CS276",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.09,
        "activeBacklogs": 2,
        "attendance": 68.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_16():
    payload = {
        "rollNo": "21CS680",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.09,
        "activeBacklogs": 1,
        "attendance": 73.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_17():
    payload = {
        "rollNo": "21CS282",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.65,
        "activeBacklogs": 3,
        "attendance": 60.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_18():
    payload = {
        "rollNo": "21CS557",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.33,
        "activeBacklogs": 3,
        "attendance": 71.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_19():
    payload = {
        "rollNo": "21CS650",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.38,
        "activeBacklogs": 1,
        "attendance": 67.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_20():
    payload = {
        "rollNo": "21CS727",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.19,
        "activeBacklogs": 1,
        "attendance": 71.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_21():
    payload = {
        "rollNo": "21CS484",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.52,
        "activeBacklogs": 3,
        "attendance": 64.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_22():
    payload = {
        "rollNo": "21CS976",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.35,
        "activeBacklogs": 5,
        "attendance": 62.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_23():
    payload = {
        "rollNo": "21CS620",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.53,
        "activeBacklogs": 2,
        "attendance": 72.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_24():
    payload = {
        "rollNo": "21CS884",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.09,
        "activeBacklogs": 1,
        "attendance": 54.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_25():
    payload = {
        "rollNo": "21CS805",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.24,
        "activeBacklogs": 2,
        "attendance": 67.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_26():
    payload = {
        "rollNo": "21CS448",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.81,
        "activeBacklogs": 3,
        "attendance": 39.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_27():
    payload = {
        "rollNo": "21CS923",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.1,
        "activeBacklogs": 4,
        "attendance": 85.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_28():
    payload = {
        "rollNo": "21CS727",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.47,
        "activeBacklogs": 4,
        "attendance": 71.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_29():
    payload = {
        "rollNo": "21CS221",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.86,
        "activeBacklogs": 1,
        "attendance": 46.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_30():
    payload = {
        "rollNo": "21CS794",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.75,
        "activeBacklogs": 1,
        "attendance": 83.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_31():
    payload = {
        "rollNo": "21CS681",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.41,
        "activeBacklogs": 4,
        "attendance": 77.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_32():
    payload = {
        "rollNo": "21CS644",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.05,
        "activeBacklogs": 1,
        "attendance": 49.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_33():
    payload = {
        "rollNo": "21CS270",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.64,
        "activeBacklogs": 4,
        "attendance": 69.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_34():
    payload = {
        "rollNo": "21CS806",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.27,
        "activeBacklogs": 4,
        "attendance": 61.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_35():
    payload = {
        "rollNo": "21CS168",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.8,
        "activeBacklogs": 5,
        "attendance": 52.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_36():
    payload = {
        "rollNo": "21CS989",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.96,
        "activeBacklogs": 2,
        "attendance": 82.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_37():
    payload = {
        "rollNo": "21CS525",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.52,
        "activeBacklogs": 1,
        "attendance": 63.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_38():
    payload = {
        "rollNo": "21CS132",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.24,
        "activeBacklogs": 0,
        "attendance": 35.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_39():
    payload = {
        "rollNo": "21CS168",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.46,
        "activeBacklogs": 4,
        "attendance": 49.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_40():
    payload = {
        "rollNo": "21CS828",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.72,
        "activeBacklogs": 5,
        "attendance": 84.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_41():
    payload = {
        "rollNo": "21CS696",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.12,
        "activeBacklogs": 2,
        "attendance": 58.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_42():
    payload = {
        "rollNo": "21CS635",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.34,
        "activeBacklogs": 3,
        "attendance": 91.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_43():
    payload = {
        "rollNo": "21CS782",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.62,
        "activeBacklogs": 1,
        "attendance": 61.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_44():
    payload = {
        "rollNo": "21CS542",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.08,
        "activeBacklogs": 3,
        "attendance": 60.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_45():
    payload = {
        "rollNo": "21CS906",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.19,
        "activeBacklogs": 2,
        "attendance": 92.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_46():
    payload = {
        "rollNo": "21CS756",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.69,
        "activeBacklogs": 3,
        "attendance": 81.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_47():
    payload = {
        "rollNo": "21CS663",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.92,
        "activeBacklogs": 4,
        "attendance": 87.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_48():
    payload = {
        "rollNo": "21CS922",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.9,
        "activeBacklogs": 0,
        "attendance": 43.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_49():
    payload = {
        "rollNo": "21CS360",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 10.0,
        "activeBacklogs": 2,
        "attendance": 82.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_50():
    payload = {
        "rollNo": "21CS380",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.86,
        "activeBacklogs": 1,
        "attendance": 79.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_51():
    payload = {
        "rollNo": "21CS929",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.03,
        "activeBacklogs": 1,
        "attendance": 87.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_52():
    payload = {
        "rollNo": "21CS200",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.78,
        "activeBacklogs": 3,
        "attendance": 67.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_53():
    payload = {
        "rollNo": "21CS497",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.13,
        "activeBacklogs": 5,
        "attendance": 52.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_54():
    payload = {
        "rollNo": "21CS331",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.32,
        "activeBacklogs": 4,
        "attendance": 91.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_55():
    payload = {
        "rollNo": "21CS897",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.58,
        "activeBacklogs": 0,
        "attendance": 39.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_56():
    payload = {
        "rollNo": "21CS778",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.27,
        "activeBacklogs": 4,
        "attendance": 83.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_57():
    payload = {
        "rollNo": "21CS729",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.24,
        "activeBacklogs": 5,
        "attendance": 33.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_58():
    payload = {
        "rollNo": "21CS761",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.9,
        "activeBacklogs": 1,
        "attendance": 57.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_59():
    payload = {
        "rollNo": "21CS258",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.79,
        "activeBacklogs": 3,
        "attendance": 75.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_60():
    payload = {
        "rollNo": "21CS105",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.61,
        "activeBacklogs": 4,
        "attendance": 37.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_61():
    payload = {
        "rollNo": "21CS253",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.25,
        "activeBacklogs": 4,
        "attendance": 67.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_62():
    payload = {
        "rollNo": "21CS174",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.03,
        "activeBacklogs": 3,
        "attendance": 54.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_63():
    payload = {
        "rollNo": "21CS851",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.49,
        "activeBacklogs": 0,
        "attendance": 97.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_64():
    payload = {
        "rollNo": "21CS213",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.74,
        "activeBacklogs": 4,
        "attendance": 79.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_65():
    payload = {
        "rollNo": "21CS211",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.81,
        "activeBacklogs": 0,
        "attendance": 84.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_66():
    payload = {
        "rollNo": "21CS562",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.36,
        "activeBacklogs": 4,
        "attendance": 99.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_67():
    payload = {
        "rollNo": "21CS846",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.65,
        "activeBacklogs": 0,
        "attendance": 51.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_68():
    payload = {
        "rollNo": "21CS535",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.18,
        "activeBacklogs": 1,
        "attendance": 68.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_69():
    payload = {
        "rollNo": "21CS473",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.17,
        "activeBacklogs": 3,
        "attendance": 86.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_70():
    payload = {
        "rollNo": "21CS712",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.87,
        "activeBacklogs": 4,
        "attendance": 32.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_71():
    payload = {
        "rollNo": "21CS622",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.56,
        "activeBacklogs": 2,
        "attendance": 52.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_72():
    payload = {
        "rollNo": "21CS157",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.03,
        "activeBacklogs": 3,
        "attendance": 86.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_73():
    payload = {
        "rollNo": "21CS678",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.59,
        "activeBacklogs": 2,
        "attendance": 72.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_74():
    payload = {
        "rollNo": "21CS554",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.57,
        "activeBacklogs": 5,
        "attendance": 90.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_75():
    payload = {
        "rollNo": "21CS976",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.45,
        "activeBacklogs": 3,
        "attendance": 94.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_76():
    payload = {
        "rollNo": "21CS905",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 10.0,
        "activeBacklogs": 1,
        "attendance": 57.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_77():
    payload = {
        "rollNo": "21CS450",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.76,
        "activeBacklogs": 3,
        "attendance": 60.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_78():
    payload = {
        "rollNo": "21CS580",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.25,
        "activeBacklogs": 4,
        "attendance": 48.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_79():
    payload = {
        "rollNo": "21CS974",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.31,
        "activeBacklogs": 4,
        "attendance": 75.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_80():
    payload = {
        "rollNo": "21CS980",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.79,
        "activeBacklogs": 1,
        "attendance": 52.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_81():
    payload = {
        "rollNo": "21CS983",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.14,
        "activeBacklogs": 1,
        "attendance": 93.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_82():
    payload = {
        "rollNo": "21CS660",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.04,
        "activeBacklogs": 5,
        "attendance": 92.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_83():
    payload = {
        "rollNo": "21CS891",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.44,
        "activeBacklogs": 4,
        "attendance": 89.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_84():
    payload = {
        "rollNo": "21CS433",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.26,
        "activeBacklogs": 5,
        "attendance": 57.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_85():
    payload = {
        "rollNo": "21CS348",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.82,
        "activeBacklogs": 4,
        "attendance": 42.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_86():
    payload = {
        "rollNo": "21CS357",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.77,
        "activeBacklogs": 4,
        "attendance": 77.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_87():
    payload = {
        "rollNo": "21CS338",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.25,
        "activeBacklogs": 5,
        "attendance": 71.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_88():
    payload = {
        "rollNo": "21CS967",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.27,
        "activeBacklogs": 4,
        "attendance": 70.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_89():
    payload = {
        "rollNo": "21CS349",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.1,
        "activeBacklogs": 3,
        "attendance": 67.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_90():
    payload = {
        "rollNo": "21CS966",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.21,
        "activeBacklogs": 1,
        "attendance": 43.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_91():
    payload = {
        "rollNo": "21CS599",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.12,
        "activeBacklogs": 1,
        "attendance": 91.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_92():
    payload = {
        "rollNo": "21CS566",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.32,
        "activeBacklogs": 5,
        "attendance": 89.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_93():
    payload = {
        "rollNo": "21CS603",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.27,
        "activeBacklogs": 2,
        "attendance": 55.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_94():
    payload = {
        "rollNo": "21CS375",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.06,
        "activeBacklogs": 1,
        "attendance": 37.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_95():
    payload = {
        "rollNo": "21CS500",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.65,
        "activeBacklogs": 0,
        "attendance": 76.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_96():
    payload = {
        "rollNo": "21CS619",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.76,
        "activeBacklogs": 3,
        "attendance": 77.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_97():
    payload = {
        "rollNo": "21CS861",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.27,
        "activeBacklogs": 1,
        "attendance": 42.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_98():
    payload = {
        "rollNo": "21CS435",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.04,
        "activeBacklogs": 2,
        "attendance": 74.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_99():
    payload = {
        "rollNo": "21CS364",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.61,
        "activeBacklogs": 3,
        "attendance": 78.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_100():
    payload = {
        "rollNo": "21CS945",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.38,
        "activeBacklogs": 3,
        "attendance": 44.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_101():
    payload = {
        "rollNo": "21CS830",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.32,
        "activeBacklogs": 2,
        "attendance": 71.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_102():
    payload = {
        "rollNo": "21CS169",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.5,
        "activeBacklogs": 4,
        "attendance": 86.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_103():
    payload = {
        "rollNo": "21CS827",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.03,
        "activeBacklogs": 0,
        "attendance": 75.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_104():
    payload = {
        "rollNo": "21CS444",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.73,
        "activeBacklogs": 0,
        "attendance": 69.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_105():
    payload = {
        "rollNo": "21CS448",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.97,
        "activeBacklogs": 3,
        "attendance": 59.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_106():
    payload = {
        "rollNo": "21CS903",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.26,
        "activeBacklogs": 0,
        "attendance": 81.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_107():
    payload = {
        "rollNo": "21CS516",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.47,
        "activeBacklogs": 2,
        "attendance": 44.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_108():
    payload = {
        "rollNo": "21CS735",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.55,
        "activeBacklogs": 0,
        "attendance": 93.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_109():
    payload = {
        "rollNo": "21CS664",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.62,
        "activeBacklogs": 1,
        "attendance": 97.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_110():
    payload = {
        "rollNo": "21CS499",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.31,
        "activeBacklogs": 2,
        "attendance": 31.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_111():
    payload = {
        "rollNo": "21CS855",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.59,
        "activeBacklogs": 0,
        "attendance": 66.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_112():
    payload = {
        "rollNo": "21CS446",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.75,
        "activeBacklogs": 0,
        "attendance": 59.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_113():
    payload = {
        "rollNo": "21CS379",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.36,
        "activeBacklogs": 4,
        "attendance": 59.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_114():
    payload = {
        "rollNo": "21CS453",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.57,
        "activeBacklogs": 4,
        "attendance": 31.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_115():
    payload = {
        "rollNo": "21CS433",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.72,
        "activeBacklogs": 0,
        "attendance": 81.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_116():
    payload = {
        "rollNo": "21CS876",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.56,
        "activeBacklogs": 3,
        "attendance": 96.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_117():
    payload = {
        "rollNo": "21CS114",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.23,
        "activeBacklogs": 5,
        "attendance": 93.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_118():
    payload = {
        "rollNo": "21CS128",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.75,
        "activeBacklogs": 5,
        "attendance": 32.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_119():
    payload = {
        "rollNo": "21CS530",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.27,
        "activeBacklogs": 5,
        "attendance": 65.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_120():
    payload = {
        "rollNo": "21CS985",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.76,
        "activeBacklogs": 2,
        "attendance": 56.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_121():
    payload = {
        "rollNo": "21CS624",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.66,
        "activeBacklogs": 3,
        "attendance": 80.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_122():
    payload = {
        "rollNo": "21CS548",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.64,
        "activeBacklogs": 0,
        "attendance": 80.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_123():
    payload = {
        "rollNo": "21CS761",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.39,
        "activeBacklogs": 2,
        "attendance": 70.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_124():
    payload = {
        "rollNo": "21CS113",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.25,
        "activeBacklogs": 5,
        "attendance": 66.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_125():
    payload = {
        "rollNo": "21CS610",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.59,
        "activeBacklogs": 4,
        "attendance": 52.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_126():
    payload = {
        "rollNo": "21CS349",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.88,
        "activeBacklogs": 4,
        "attendance": 87.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_127():
    payload = {
        "rollNo": "21CS615",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.34,
        "activeBacklogs": 1,
        "attendance": 62.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_128():
    payload = {
        "rollNo": "21CS966",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.84,
        "activeBacklogs": 2,
        "attendance": 98.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_129():
    payload = {
        "rollNo": "21CS810",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.71,
        "activeBacklogs": 1,
        "attendance": 34.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_130():
    payload = {
        "rollNo": "21CS442",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.31,
        "activeBacklogs": 0,
        "attendance": 37.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_131():
    payload = {
        "rollNo": "21CS750",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.48,
        "activeBacklogs": 0,
        "attendance": 32.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_132():
    payload = {
        "rollNo": "21CS177",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.81,
        "activeBacklogs": 0,
        "attendance": 46.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_133():
    payload = {
        "rollNo": "21CS808",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.98,
        "activeBacklogs": 1,
        "attendance": 42.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_134():
    payload = {
        "rollNo": "21CS832",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.34,
        "activeBacklogs": 4,
        "attendance": 49.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_135():
    payload = {
        "rollNo": "21CS267",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.89,
        "activeBacklogs": 0,
        "attendance": 62.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_136():
    payload = {
        "rollNo": "21CS683",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.81,
        "activeBacklogs": 4,
        "attendance": 58.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_137():
    payload = {
        "rollNo": "21CS741",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.48,
        "activeBacklogs": 5,
        "attendance": 50.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_138():
    payload = {
        "rollNo": "21CS426",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.91,
        "activeBacklogs": 4,
        "attendance": 59.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_139():
    payload = {
        "rollNo": "21CS130",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.99,
        "activeBacklogs": 0,
        "attendance": 89.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_140():
    payload = {
        "rollNo": "21CS522",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.25,
        "activeBacklogs": 5,
        "attendance": 72.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_141():
    payload = {
        "rollNo": "21CS782",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.14,
        "activeBacklogs": 5,
        "attendance": 94.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_142():
    payload = {
        "rollNo": "21CS975",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.42,
        "activeBacklogs": 3,
        "attendance": 68.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_143():
    payload = {
        "rollNo": "21CS426",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.64,
        "activeBacklogs": 2,
        "attendance": 86.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_144():
    payload = {
        "rollNo": "21CS192",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.69,
        "activeBacklogs": 3,
        "attendance": 84.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_145():
    payload = {
        "rollNo": "21CS510",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.03,
        "activeBacklogs": 2,
        "attendance": 57.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_146():
    payload = {
        "rollNo": "21CS651",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.32,
        "activeBacklogs": 2,
        "attendance": 97.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_147():
    payload = {
        "rollNo": "21CS812",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.1,
        "activeBacklogs": 3,
        "attendance": 43.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_148():
    payload = {
        "rollNo": "21CS868",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.13,
        "activeBacklogs": 3,
        "attendance": 75.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_149():
    payload = {
        "rollNo": "21CS216",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.88,
        "activeBacklogs": 2,
        "attendance": 62.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_150():
    payload = {
        "rollNo": "21CS377",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.85,
        "activeBacklogs": 5,
        "attendance": 30.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_151():
    payload = {
        "rollNo": "21CS690",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.85,
        "activeBacklogs": 3,
        "attendance": 63.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_152():
    payload = {
        "rollNo": "21CS698",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.49,
        "activeBacklogs": 0,
        "attendance": 86.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_153():
    payload = {
        "rollNo": "21CS923",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.79,
        "activeBacklogs": 1,
        "attendance": 50.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_154():
    payload = {
        "rollNo": "21CS358",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.04,
        "activeBacklogs": 1,
        "attendance": 83.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_155():
    payload = {
        "rollNo": "21CS100",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.21,
        "activeBacklogs": 1,
        "attendance": 94.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_156():
    payload = {
        "rollNo": "21CS875",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.32,
        "activeBacklogs": 4,
        "attendance": 97.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_157():
    payload = {
        "rollNo": "21CS543",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.55,
        "activeBacklogs": 4,
        "attendance": 52.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_158():
    payload = {
        "rollNo": "21CS907",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.56,
        "activeBacklogs": 1,
        "attendance": 40.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_159():
    payload = {
        "rollNo": "21CS430",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.03,
        "activeBacklogs": 5,
        "attendance": 78.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_160():
    payload = {
        "rollNo": "21CS544",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.91,
        "activeBacklogs": 4,
        "attendance": 93.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_161():
    payload = {
        "rollNo": "21CS792",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.75,
        "activeBacklogs": 2,
        "attendance": 97.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_162():
    payload = {
        "rollNo": "21CS230",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.75,
        "activeBacklogs": 2,
        "attendance": 97.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_163():
    payload = {
        "rollNo": "21CS417",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.6,
        "activeBacklogs": 0,
        "attendance": 83.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_164():
    payload = {
        "rollNo": "21CS557",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.92,
        "activeBacklogs": 4,
        "attendance": 43.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_165():
    payload = {
        "rollNo": "21CS859",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.15,
        "activeBacklogs": 1,
        "attendance": 96.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_166():
    payload = {
        "rollNo": "21CS514",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.86,
        "activeBacklogs": 4,
        "attendance": 75.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_167():
    payload = {
        "rollNo": "21CS882",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.24,
        "activeBacklogs": 0,
        "attendance": 66.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_168():
    payload = {
        "rollNo": "21CS780",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.66,
        "activeBacklogs": 2,
        "attendance": 69.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_169():
    payload = {
        "rollNo": "21CS194",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.02,
        "activeBacklogs": 5,
        "attendance": 45.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_170():
    payload = {
        "rollNo": "21CS313",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.77,
        "activeBacklogs": 0,
        "attendance": 48.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_171():
    payload = {
        "rollNo": "21CS868",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.59,
        "activeBacklogs": 0,
        "attendance": 32.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_172():
    payload = {
        "rollNo": "21CS340",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.65,
        "activeBacklogs": 0,
        "attendance": 57.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_173():
    payload = {
        "rollNo": "21CS553",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.25,
        "activeBacklogs": 1,
        "attendance": 46.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_174():
    payload = {
        "rollNo": "21CS404",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.53,
        "activeBacklogs": 0,
        "attendance": 84.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_175():
    payload = {
        "rollNo": "21CS595",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.94,
        "activeBacklogs": 4,
        "attendance": 54.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_176():
    payload = {
        "rollNo": "21CS979",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.38,
        "activeBacklogs": 3,
        "attendance": 32.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_177():
    payload = {
        "rollNo": "21CS795",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.71,
        "activeBacklogs": 1,
        "attendance": 84.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_178():
    payload = {
        "rollNo": "21CS429",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.39,
        "activeBacklogs": 5,
        "attendance": 96.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_179():
    payload = {
        "rollNo": "21CS281",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.04,
        "activeBacklogs": 5,
        "attendance": 79.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_180():
    payload = {
        "rollNo": "21CS567",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.19,
        "activeBacklogs": 1,
        "attendance": 71.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_181():
    payload = {
        "rollNo": "21CS372",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.71,
        "activeBacklogs": 4,
        "attendance": 52.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_182():
    payload = {
        "rollNo": "21CS397",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.46,
        "activeBacklogs": 3,
        "attendance": 94.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_183():
    payload = {
        "rollNo": "21CS135",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.01,
        "activeBacklogs": 2,
        "attendance": 35.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_184():
    payload = {
        "rollNo": "21CS546",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.84,
        "activeBacklogs": 3,
        "attendance": 50.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_185():
    payload = {
        "rollNo": "21CS106",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.65,
        "activeBacklogs": 4,
        "attendance": 82.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_186():
    payload = {
        "rollNo": "21CS564",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.26,
        "activeBacklogs": 1,
        "attendance": 31.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_187():
    payload = {
        "rollNo": "21CS967",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.13,
        "activeBacklogs": 3,
        "attendance": 37.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_188():
    payload = {
        "rollNo": "21CS527",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.45,
        "activeBacklogs": 5,
        "attendance": 42.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_189():
    payload = {
        "rollNo": "21CS510",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.53,
        "activeBacklogs": 3,
        "attendance": 49.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_190():
    payload = {
        "rollNo": "21CS262",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.69,
        "activeBacklogs": 5,
        "attendance": 65.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_191():
    payload = {
        "rollNo": "21CS749",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.64,
        "activeBacklogs": 3,
        "attendance": 36.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_192():
    payload = {
        "rollNo": "21CS312",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.83,
        "activeBacklogs": 1,
        "attendance": 78.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_193():
    payload = {
        "rollNo": "21CS556",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.84,
        "activeBacklogs": 5,
        "attendance": 30.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_194():
    payload = {
        "rollNo": "21CS483",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.95,
        "activeBacklogs": 3,
        "attendance": 44.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_195():
    payload = {
        "rollNo": "21CS152",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.72,
        "activeBacklogs": 2,
        "attendance": 79.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_196():
    payload = {
        "rollNo": "21CS164",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.32,
        "activeBacklogs": 2,
        "attendance": 32.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_197():
    payload = {
        "rollNo": "21CS181",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.84,
        "activeBacklogs": 3,
        "attendance": 85.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_198():
    payload = {
        "rollNo": "21CS148",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.18,
        "activeBacklogs": 0,
        "attendance": 47.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_199():
    payload = {
        "rollNo": "21CS111",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.43,
        "activeBacklogs": 5,
        "attendance": 35.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_200():
    payload = {
        "rollNo": "21CS224",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.3,
        "activeBacklogs": 3,
        "attendance": 36.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_201():
    payload = {
        "rollNo": "21CS373",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.76,
        "activeBacklogs": 2,
        "attendance": 31.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_202():
    payload = {
        "rollNo": "21CS851",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.52,
        "activeBacklogs": 3,
        "attendance": 58.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_203():
    payload = {
        "rollNo": "21CS227",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.3,
        "activeBacklogs": 4,
        "attendance": 67.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_204():
    payload = {
        "rollNo": "21CS922",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.16,
        "activeBacklogs": 2,
        "attendance": 32.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_205():
    payload = {
        "rollNo": "21CS117",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.06,
        "activeBacklogs": 3,
        "attendance": 38.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_206():
    payload = {
        "rollNo": "21CS967",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.35,
        "activeBacklogs": 1,
        "attendance": 31.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_207():
    payload = {
        "rollNo": "21CS787",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.84,
        "activeBacklogs": 3,
        "attendance": 73.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_208():
    payload = {
        "rollNo": "21CS942",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.53,
        "activeBacklogs": 2,
        "attendance": 70.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_209():
    payload = {
        "rollNo": "21CS819",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.58,
        "activeBacklogs": 4,
        "attendance": 67.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_210():
    payload = {
        "rollNo": "21CS966",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.7,
        "activeBacklogs": 3,
        "attendance": 88.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_211():
    payload = {
        "rollNo": "21CS948",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.04,
        "activeBacklogs": 1,
        "attendance": 73.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_212():
    payload = {
        "rollNo": "21CS582",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.98,
        "activeBacklogs": 0,
        "attendance": 58.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_213():
    payload = {
        "rollNo": "21CS158",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.47,
        "activeBacklogs": 4,
        "attendance": 71.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_214():
    payload = {
        "rollNo": "21CS878",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.22,
        "activeBacklogs": 2,
        "attendance": 87.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_215():
    payload = {
        "rollNo": "21CS770",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.01,
        "activeBacklogs": 1,
        "attendance": 53.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_216():
    payload = {
        "rollNo": "21CS951",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.62,
        "activeBacklogs": 1,
        "attendance": 79.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_217():
    payload = {
        "rollNo": "21CS845",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.88,
        "activeBacklogs": 5,
        "attendance": 77.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_218():
    payload = {
        "rollNo": "21CS357",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.73,
        "activeBacklogs": 4,
        "attendance": 56.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_219():
    payload = {
        "rollNo": "21CS968",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.93,
        "activeBacklogs": 2,
        "attendance": 90.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_220():
    payload = {
        "rollNo": "21CS929",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.99,
        "activeBacklogs": 5,
        "attendance": 56.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_221():
    payload = {
        "rollNo": "21CS270",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.56,
        "activeBacklogs": 3,
        "attendance": 40.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_222():
    payload = {
        "rollNo": "21CS796",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.57,
        "activeBacklogs": 4,
        "attendance": 86.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_223():
    payload = {
        "rollNo": "21CS227",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.09,
        "activeBacklogs": 3,
        "attendance": 58.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_224():
    payload = {
        "rollNo": "21CS235",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.57,
        "activeBacklogs": 0,
        "attendance": 42.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_225():
    payload = {
        "rollNo": "21CS580",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.04,
        "activeBacklogs": 4,
        "attendance": 34.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_226():
    payload = {
        "rollNo": "21CS399",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.02,
        "activeBacklogs": 2,
        "attendance": 95.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_227():
    payload = {
        "rollNo": "21CS928",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.54,
        "activeBacklogs": 3,
        "attendance": 88.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_228():
    payload = {
        "rollNo": "21CS133",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.83,
        "activeBacklogs": 4,
        "attendance": 65.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_229():
    payload = {
        "rollNo": "21CS577",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.54,
        "activeBacklogs": 2,
        "attendance": 70.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_230():
    payload = {
        "rollNo": "21CS512",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.4,
        "activeBacklogs": 0,
        "attendance": 45.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_231():
    payload = {
        "rollNo": "21CS278",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.32,
        "activeBacklogs": 2,
        "attendance": 93.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_232():
    payload = {
        "rollNo": "21CS104",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.5,
        "activeBacklogs": 4,
        "attendance": 74.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_233():
    payload = {
        "rollNo": "21CS819",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.91,
        "activeBacklogs": 1,
        "attendance": 63.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_234():
    payload = {
        "rollNo": "21CS349",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.75,
        "activeBacklogs": 3,
        "attendance": 71.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_235():
    payload = {
        "rollNo": "21CS793",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.72,
        "activeBacklogs": 3,
        "attendance": 83.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_236():
    payload = {
        "rollNo": "21CS881",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.7,
        "activeBacklogs": 1,
        "attendance": 86.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_237():
    payload = {
        "rollNo": "21CS505",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.35,
        "activeBacklogs": 0,
        "attendance": 70.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_238():
    payload = {
        "rollNo": "21CS594",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.2,
        "activeBacklogs": 2,
        "attendance": 35.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_239():
    payload = {
        "rollNo": "21CS362",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.86,
        "activeBacklogs": 5,
        "attendance": 30.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_240():
    payload = {
        "rollNo": "21CS671",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.75,
        "activeBacklogs": 2,
        "attendance": 80.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_241():
    payload = {
        "rollNo": "21CS120",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.27,
        "activeBacklogs": 5,
        "attendance": 52.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_242():
    payload = {
        "rollNo": "21CS835",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.07,
        "activeBacklogs": 0,
        "attendance": 77.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_243():
    payload = {
        "rollNo": "21CS742",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.02,
        "activeBacklogs": 0,
        "attendance": 55.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_244():
    payload = {
        "rollNo": "21CS605",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.61,
        "activeBacklogs": 4,
        "attendance": 67.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_245():
    payload = {
        "rollNo": "21CS207",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.58,
        "activeBacklogs": 3,
        "attendance": 67.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_246():
    payload = {
        "rollNo": "21CS342",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.01,
        "activeBacklogs": 2,
        "attendance": 90.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_247():
    payload = {
        "rollNo": "21CS962",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.72,
        "activeBacklogs": 0,
        "attendance": 30.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_248():
    payload = {
        "rollNo": "21CS520",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.41,
        "activeBacklogs": 2,
        "attendance": 93.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_13_249():
    payload = {
        "rollNo": "21CS125",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.87,
        "activeBacklogs": 0,
        "attendance": 85.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

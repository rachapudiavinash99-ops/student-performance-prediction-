import pytest
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_prediction_case_12_0():
    payload = {
        "rollNo": "21CS601",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.2,
        "activeBacklogs": 0,
        "attendance": 35.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_1():
    payload = {
        "rollNo": "21CS921",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.46,
        "activeBacklogs": 5,
        "attendance": 33.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_2():
    payload = {
        "rollNo": "21CS413",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.65,
        "activeBacklogs": 3,
        "attendance": 53.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_3():
    payload = {
        "rollNo": "21CS118",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.26,
        "activeBacklogs": 4,
        "attendance": 42.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_4():
    payload = {
        "rollNo": "21CS325",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.09,
        "activeBacklogs": 1,
        "attendance": 33.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_5():
    payload = {
        "rollNo": "21CS848",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.6,
        "activeBacklogs": 5,
        "attendance": 37.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_6():
    payload = {
        "rollNo": "21CS194",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.16,
        "activeBacklogs": 3,
        "attendance": 68.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_7():
    payload = {
        "rollNo": "21CS471",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.55,
        "activeBacklogs": 0,
        "attendance": 38.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_8():
    payload = {
        "rollNo": "21CS891",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.88,
        "activeBacklogs": 5,
        "attendance": 37.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_9():
    payload = {
        "rollNo": "21CS371",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.03,
        "activeBacklogs": 2,
        "attendance": 86.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_10():
    payload = {
        "rollNo": "21CS213",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.37,
        "activeBacklogs": 4,
        "attendance": 38.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_11():
    payload = {
        "rollNo": "21CS529",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.89,
        "activeBacklogs": 5,
        "attendance": 76.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_12():
    payload = {
        "rollNo": "21CS195",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.01,
        "activeBacklogs": 5,
        "attendance": 63.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_13():
    payload = {
        "rollNo": "21CS945",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.96,
        "activeBacklogs": 3,
        "attendance": 80.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_14():
    payload = {
        "rollNo": "21CS552",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.89,
        "activeBacklogs": 2,
        "attendance": 37.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_15():
    payload = {
        "rollNo": "21CS600",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.6,
        "activeBacklogs": 4,
        "attendance": 60.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_16():
    payload = {
        "rollNo": "21CS630",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.65,
        "activeBacklogs": 2,
        "attendance": 98.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_17():
    payload = {
        "rollNo": "21CS915",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.2,
        "activeBacklogs": 3,
        "attendance": 67.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_18():
    payload = {
        "rollNo": "21CS768",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.55,
        "activeBacklogs": 5,
        "attendance": 35.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_19():
    payload = {
        "rollNo": "21CS183",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.54,
        "activeBacklogs": 3,
        "attendance": 63.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_20():
    payload = {
        "rollNo": "21CS566",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.95,
        "activeBacklogs": 2,
        "attendance": 37.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_21():
    payload = {
        "rollNo": "21CS740",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.4,
        "activeBacklogs": 1,
        "attendance": 96.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_22():
    payload = {
        "rollNo": "21CS866",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.88,
        "activeBacklogs": 4,
        "attendance": 42.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_23():
    payload = {
        "rollNo": "21CS906",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.83,
        "activeBacklogs": 5,
        "attendance": 49.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_24():
    payload = {
        "rollNo": "21CS698",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.83,
        "activeBacklogs": 5,
        "attendance": 46.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_25():
    payload = {
        "rollNo": "21CS828",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.86,
        "activeBacklogs": 2,
        "attendance": 91.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_26():
    payload = {
        "rollNo": "21CS501",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.76,
        "activeBacklogs": 3,
        "attendance": 77.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_27():
    payload = {
        "rollNo": "21CS940",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.58,
        "activeBacklogs": 4,
        "attendance": 91.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_28():
    payload = {
        "rollNo": "21CS216",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.75,
        "activeBacklogs": 3,
        "attendance": 68.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_29():
    payload = {
        "rollNo": "21CS908",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.34,
        "activeBacklogs": 5,
        "attendance": 81.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_30():
    payload = {
        "rollNo": "21CS758",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.85,
        "activeBacklogs": 4,
        "attendance": 56.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_31():
    payload = {
        "rollNo": "21CS630",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.55,
        "activeBacklogs": 2,
        "attendance": 83.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_32():
    payload = {
        "rollNo": "21CS776",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.0,
        "activeBacklogs": 0,
        "attendance": 82.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_33():
    payload = {
        "rollNo": "21CS125",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.77,
        "activeBacklogs": 1,
        "attendance": 46.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_34():
    payload = {
        "rollNo": "21CS107",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.69,
        "activeBacklogs": 3,
        "attendance": 41.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_35():
    payload = {
        "rollNo": "21CS376",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.36,
        "activeBacklogs": 2,
        "attendance": 79.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_36():
    payload = {
        "rollNo": "21CS835",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.34,
        "activeBacklogs": 0,
        "attendance": 86.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_37():
    payload = {
        "rollNo": "21CS740",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.45,
        "activeBacklogs": 5,
        "attendance": 78.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_38():
    payload = {
        "rollNo": "21CS718",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.66,
        "activeBacklogs": 5,
        "attendance": 33.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_39():
    payload = {
        "rollNo": "21CS153",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.63,
        "activeBacklogs": 2,
        "attendance": 55.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_40():
    payload = {
        "rollNo": "21CS676",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.93,
        "activeBacklogs": 0,
        "attendance": 86.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_41():
    payload = {
        "rollNo": "21CS683",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.2,
        "activeBacklogs": 3,
        "attendance": 63.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_42():
    payload = {
        "rollNo": "21CS232",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.24,
        "activeBacklogs": 3,
        "attendance": 48.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_43():
    payload = {
        "rollNo": "21CS194",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.95,
        "activeBacklogs": 1,
        "attendance": 60.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_44():
    payload = {
        "rollNo": "21CS328",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.57,
        "activeBacklogs": 5,
        "attendance": 35.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_45():
    payload = {
        "rollNo": "21CS213",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.97,
        "activeBacklogs": 1,
        "attendance": 61.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_46():
    payload = {
        "rollNo": "21CS278",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.48,
        "activeBacklogs": 3,
        "attendance": 83.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_47():
    payload = {
        "rollNo": "21CS459",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.8,
        "activeBacklogs": 0,
        "attendance": 87.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_48():
    payload = {
        "rollNo": "21CS847",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.57,
        "activeBacklogs": 5,
        "attendance": 63.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_49():
    payload = {
        "rollNo": "21CS346",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.9,
        "activeBacklogs": 0,
        "attendance": 85.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_50():
    payload = {
        "rollNo": "21CS211",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.77,
        "activeBacklogs": 0,
        "attendance": 64.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_51():
    payload = {
        "rollNo": "21CS888",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.32,
        "activeBacklogs": 1,
        "attendance": 63.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_52():
    payload = {
        "rollNo": "21CS614",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.94,
        "activeBacklogs": 2,
        "attendance": 92.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_53():
    payload = {
        "rollNo": "21CS906",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.33,
        "activeBacklogs": 5,
        "attendance": 32.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_54():
    payload = {
        "rollNo": "21CS606",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.19,
        "activeBacklogs": 5,
        "attendance": 66.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_55():
    payload = {
        "rollNo": "21CS722",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.64,
        "activeBacklogs": 0,
        "attendance": 74.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_56():
    payload = {
        "rollNo": "21CS268",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.28,
        "activeBacklogs": 0,
        "attendance": 74.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_57():
    payload = {
        "rollNo": "21CS132",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.04,
        "activeBacklogs": 1,
        "attendance": 95.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_58():
    payload = {
        "rollNo": "21CS732",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.78,
        "activeBacklogs": 5,
        "attendance": 59.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_59():
    payload = {
        "rollNo": "21CS903",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.89,
        "activeBacklogs": 4,
        "attendance": 39.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_60():
    payload = {
        "rollNo": "21CS934",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.79,
        "activeBacklogs": 0,
        "attendance": 83.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_61():
    payload = {
        "rollNo": "21CS713",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.85,
        "activeBacklogs": 4,
        "attendance": 87.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_62():
    payload = {
        "rollNo": "21CS434",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.36,
        "activeBacklogs": 2,
        "attendance": 36.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_63():
    payload = {
        "rollNo": "21CS539",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.07,
        "activeBacklogs": 4,
        "attendance": 55.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_64():
    payload = {
        "rollNo": "21CS864",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.45,
        "activeBacklogs": 4,
        "attendance": 70.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_65():
    payload = {
        "rollNo": "21CS366",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.65,
        "activeBacklogs": 3,
        "attendance": 38.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_66():
    payload = {
        "rollNo": "21CS742",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.99,
        "activeBacklogs": 0,
        "attendance": 30.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_67():
    payload = {
        "rollNo": "21CS954",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.07,
        "activeBacklogs": 5,
        "attendance": 35.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_68():
    payload = {
        "rollNo": "21CS962",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.57,
        "activeBacklogs": 3,
        "attendance": 62.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_69():
    payload = {
        "rollNo": "21CS958",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.61,
        "activeBacklogs": 3,
        "attendance": 46.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_70():
    payload = {
        "rollNo": "21CS326",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.59,
        "activeBacklogs": 1,
        "attendance": 86.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_71():
    payload = {
        "rollNo": "21CS678",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.0,
        "activeBacklogs": 3,
        "attendance": 85.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_72():
    payload = {
        "rollNo": "21CS463",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.61,
        "activeBacklogs": 2,
        "attendance": 53.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_73():
    payload = {
        "rollNo": "21CS211",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.45,
        "activeBacklogs": 2,
        "attendance": 33.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_74():
    payload = {
        "rollNo": "21CS260",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.87,
        "activeBacklogs": 0,
        "attendance": 58.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_75():
    payload = {
        "rollNo": "21CS208",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.94,
        "activeBacklogs": 5,
        "attendance": 77.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_76():
    payload = {
        "rollNo": "21CS758",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.41,
        "activeBacklogs": 1,
        "attendance": 44.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_77():
    payload = {
        "rollNo": "21CS382",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.86,
        "activeBacklogs": 0,
        "attendance": 65.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_78():
    payload = {
        "rollNo": "21CS405",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.15,
        "activeBacklogs": 4,
        "attendance": 73.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_79():
    payload = {
        "rollNo": "21CS244",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.08,
        "activeBacklogs": 0,
        "attendance": 39.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_80():
    payload = {
        "rollNo": "21CS919",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.62,
        "activeBacklogs": 5,
        "attendance": 67.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_81():
    payload = {
        "rollNo": "21CS708",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.8,
        "activeBacklogs": 1,
        "attendance": 96.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_82():
    payload = {
        "rollNo": "21CS954",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.96,
        "activeBacklogs": 3,
        "attendance": 37.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_83():
    payload = {
        "rollNo": "21CS514",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.64,
        "activeBacklogs": 1,
        "attendance": 71.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_84():
    payload = {
        "rollNo": "21CS877",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.5,
        "activeBacklogs": 5,
        "attendance": 78.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_85():
    payload = {
        "rollNo": "21CS876",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.58,
        "activeBacklogs": 0,
        "attendance": 44.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_86():
    payload = {
        "rollNo": "21CS140",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.8,
        "activeBacklogs": 4,
        "attendance": 87.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_87():
    payload = {
        "rollNo": "21CS339",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.95,
        "activeBacklogs": 2,
        "attendance": 44.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_88():
    payload = {
        "rollNo": "21CS853",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.9,
        "activeBacklogs": 0,
        "attendance": 31.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_89():
    payload = {
        "rollNo": "21CS627",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.73,
        "activeBacklogs": 1,
        "attendance": 90.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_90():
    payload = {
        "rollNo": "21CS529",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.26,
        "activeBacklogs": 0,
        "attendance": 53.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_91():
    payload = {
        "rollNo": "21CS310",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.19,
        "activeBacklogs": 2,
        "attendance": 86.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_92():
    payload = {
        "rollNo": "21CS523",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.67,
        "activeBacklogs": 1,
        "attendance": 35.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_93():
    payload = {
        "rollNo": "21CS502",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.93,
        "activeBacklogs": 4,
        "attendance": 83.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_94():
    payload = {
        "rollNo": "21CS488",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.34,
        "activeBacklogs": 4,
        "attendance": 72.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_95():
    payload = {
        "rollNo": "21CS670",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.97,
        "activeBacklogs": 0,
        "attendance": 47.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_96():
    payload = {
        "rollNo": "21CS418",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.34,
        "activeBacklogs": 3,
        "attendance": 81.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_97():
    payload = {
        "rollNo": "21CS244",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.29,
        "activeBacklogs": 3,
        "attendance": 59.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_98():
    payload = {
        "rollNo": "21CS404",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.6,
        "activeBacklogs": 2,
        "attendance": 99.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_99():
    payload = {
        "rollNo": "21CS601",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.92,
        "activeBacklogs": 5,
        "attendance": 60.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_100():
    payload = {
        "rollNo": "21CS329",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.14,
        "activeBacklogs": 4,
        "attendance": 45.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_101():
    payload = {
        "rollNo": "21CS714",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.61,
        "activeBacklogs": 3,
        "attendance": 85.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_102():
    payload = {
        "rollNo": "21CS776",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.07,
        "activeBacklogs": 1,
        "attendance": 87.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_103():
    payload = {
        "rollNo": "21CS773",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.27,
        "activeBacklogs": 1,
        "attendance": 35.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_104():
    payload = {
        "rollNo": "21CS534",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.62,
        "activeBacklogs": 4,
        "attendance": 57.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_105():
    payload = {
        "rollNo": "21CS603",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.44,
        "activeBacklogs": 5,
        "attendance": 88.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_106():
    payload = {
        "rollNo": "21CS482",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.52,
        "activeBacklogs": 3,
        "attendance": 51.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_107():
    payload = {
        "rollNo": "21CS930",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.42,
        "activeBacklogs": 0,
        "attendance": 39.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_108():
    payload = {
        "rollNo": "21CS864",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.28,
        "activeBacklogs": 0,
        "attendance": 36.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_109():
    payload = {
        "rollNo": "21CS811",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.98,
        "activeBacklogs": 0,
        "attendance": 87.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_110():
    payload = {
        "rollNo": "21CS619",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.11,
        "activeBacklogs": 3,
        "attendance": 34.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_111():
    payload = {
        "rollNo": "21CS805",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.2,
        "activeBacklogs": 2,
        "attendance": 66.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_112():
    payload = {
        "rollNo": "21CS409",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.2,
        "activeBacklogs": 3,
        "attendance": 61.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_113():
    payload = {
        "rollNo": "21CS476",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.65,
        "activeBacklogs": 2,
        "attendance": 66.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_114():
    payload = {
        "rollNo": "21CS615",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.65,
        "activeBacklogs": 2,
        "attendance": 60.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_115():
    payload = {
        "rollNo": "21CS685",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.52,
        "activeBacklogs": 0,
        "attendance": 97.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_116():
    payload = {
        "rollNo": "21CS968",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.79,
        "activeBacklogs": 4,
        "attendance": 75.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_117():
    payload = {
        "rollNo": "21CS287",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.96,
        "activeBacklogs": 1,
        "attendance": 37.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_118():
    payload = {
        "rollNo": "21CS416",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.88,
        "activeBacklogs": 4,
        "attendance": 60.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_119():
    payload = {
        "rollNo": "21CS470",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.96,
        "activeBacklogs": 2,
        "attendance": 92.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_120():
    payload = {
        "rollNo": "21CS794",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.03,
        "activeBacklogs": 5,
        "attendance": 34.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_121():
    payload = {
        "rollNo": "21CS824",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.98,
        "activeBacklogs": 0,
        "attendance": 90.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_122():
    payload = {
        "rollNo": "21CS895",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.07,
        "activeBacklogs": 5,
        "attendance": 34.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_123():
    payload = {
        "rollNo": "21CS255",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.0,
        "activeBacklogs": 4,
        "attendance": 37.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_124():
    payload = {
        "rollNo": "21CS834",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.56,
        "activeBacklogs": 0,
        "attendance": 69.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_125():
    payload = {
        "rollNo": "21CS594",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.15,
        "activeBacklogs": 1,
        "attendance": 90.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_126():
    payload = {
        "rollNo": "21CS857",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.9,
        "activeBacklogs": 3,
        "attendance": 73.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_127():
    payload = {
        "rollNo": "21CS604",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.55,
        "activeBacklogs": 5,
        "attendance": 50.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_128():
    payload = {
        "rollNo": "21CS260",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.89,
        "activeBacklogs": 1,
        "attendance": 31.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_129():
    payload = {
        "rollNo": "21CS674",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.65,
        "activeBacklogs": 5,
        "attendance": 43.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_130():
    payload = {
        "rollNo": "21CS216",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.84,
        "activeBacklogs": 2,
        "attendance": 35.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_131():
    payload = {
        "rollNo": "21CS234",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.61,
        "activeBacklogs": 5,
        "attendance": 36.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_132():
    payload = {
        "rollNo": "21CS764",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.55,
        "activeBacklogs": 5,
        "attendance": 72.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_133():
    payload = {
        "rollNo": "21CS913",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.11,
        "activeBacklogs": 5,
        "attendance": 65.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_134():
    payload = {
        "rollNo": "21CS547",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.44,
        "activeBacklogs": 2,
        "attendance": 57.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_135():
    payload = {
        "rollNo": "21CS823",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.3,
        "activeBacklogs": 2,
        "attendance": 31.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_136():
    payload = {
        "rollNo": "21CS122",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.94,
        "activeBacklogs": 1,
        "attendance": 77.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_137():
    payload = {
        "rollNo": "21CS243",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.09,
        "activeBacklogs": 0,
        "attendance": 50.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_138():
    payload = {
        "rollNo": "21CS175",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.54,
        "activeBacklogs": 5,
        "attendance": 71.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_139():
    payload = {
        "rollNo": "21CS180",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.5,
        "activeBacklogs": 1,
        "attendance": 69.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_140():
    payload = {
        "rollNo": "21CS972",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.88,
        "activeBacklogs": 1,
        "attendance": 60.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_141():
    payload = {
        "rollNo": "21CS394",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.27,
        "activeBacklogs": 0,
        "attendance": 61.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_142():
    payload = {
        "rollNo": "21CS653",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.17,
        "activeBacklogs": 0,
        "attendance": 42.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_143():
    payload = {
        "rollNo": "21CS568",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.93,
        "activeBacklogs": 3,
        "attendance": 94.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_144():
    payload = {
        "rollNo": "21CS417",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.67,
        "activeBacklogs": 5,
        "attendance": 91.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_145():
    payload = {
        "rollNo": "21CS731",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.33,
        "activeBacklogs": 4,
        "attendance": 92.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_146():
    payload = {
        "rollNo": "21CS129",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.8,
        "activeBacklogs": 5,
        "attendance": 38.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_147():
    payload = {
        "rollNo": "21CS997",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.89,
        "activeBacklogs": 5,
        "attendance": 36.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_148():
    payload = {
        "rollNo": "21CS364",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.5,
        "activeBacklogs": 4,
        "attendance": 89.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_149():
    payload = {
        "rollNo": "21CS274",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.47,
        "activeBacklogs": 2,
        "attendance": 93.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_150():
    payload = {
        "rollNo": "21CS780",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.93,
        "activeBacklogs": 1,
        "attendance": 73.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_151():
    payload = {
        "rollNo": "21CS427",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.25,
        "activeBacklogs": 3,
        "attendance": 90.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_152():
    payload = {
        "rollNo": "21CS319",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.81,
        "activeBacklogs": 0,
        "attendance": 90.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_153():
    payload = {
        "rollNo": "21CS582",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.48,
        "activeBacklogs": 4,
        "attendance": 32.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_154():
    payload = {
        "rollNo": "21CS687",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.26,
        "activeBacklogs": 0,
        "attendance": 56.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_155():
    payload = {
        "rollNo": "21CS547",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.5,
        "activeBacklogs": 0,
        "attendance": 87.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_156():
    payload = {
        "rollNo": "21CS183",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.73,
        "activeBacklogs": 5,
        "attendance": 70.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_157():
    payload = {
        "rollNo": "21CS222",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.96,
        "activeBacklogs": 0,
        "attendance": 87.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_158():
    payload = {
        "rollNo": "21CS688",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.22,
        "activeBacklogs": 2,
        "attendance": 55.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_159():
    payload = {
        "rollNo": "21CS288",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.52,
        "activeBacklogs": 5,
        "attendance": 64.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_160():
    payload = {
        "rollNo": "21CS637",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.2,
        "activeBacklogs": 3,
        "attendance": 93.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_161():
    payload = {
        "rollNo": "21CS881",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.97,
        "activeBacklogs": 3,
        "attendance": 60.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_162():
    payload = {
        "rollNo": "21CS436",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.68,
        "activeBacklogs": 5,
        "attendance": 36.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_163():
    payload = {
        "rollNo": "21CS893",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.23,
        "activeBacklogs": 5,
        "attendance": 55.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_164():
    payload = {
        "rollNo": "21CS312",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.43,
        "activeBacklogs": 3,
        "attendance": 56.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_165():
    payload = {
        "rollNo": "21CS443",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.75,
        "activeBacklogs": 3,
        "attendance": 68.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_166():
    payload = {
        "rollNo": "21CS632",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.58,
        "activeBacklogs": 3,
        "attendance": 80.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_167():
    payload = {
        "rollNo": "21CS302",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.52,
        "activeBacklogs": 5,
        "attendance": 57.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_168():
    payload = {
        "rollNo": "21CS109",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.39,
        "activeBacklogs": 2,
        "attendance": 59.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_169():
    payload = {
        "rollNo": "21CS207",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.55,
        "activeBacklogs": 1,
        "attendance": 76.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_170():
    payload = {
        "rollNo": "21CS127",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.23,
        "activeBacklogs": 0,
        "attendance": 85.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_171():
    payload = {
        "rollNo": "21CS161",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.6,
        "activeBacklogs": 0,
        "attendance": 50.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_172():
    payload = {
        "rollNo": "21CS327",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.96,
        "activeBacklogs": 3,
        "attendance": 41.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_173():
    payload = {
        "rollNo": "21CS339",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.12,
        "activeBacklogs": 5,
        "attendance": 66.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_174():
    payload = {
        "rollNo": "21CS315",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.28,
        "activeBacklogs": 1,
        "attendance": 54.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_175():
    payload = {
        "rollNo": "21CS265",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.85,
        "activeBacklogs": 3,
        "attendance": 37.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_176():
    payload = {
        "rollNo": "21CS134",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.41,
        "activeBacklogs": 5,
        "attendance": 86.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_177():
    payload = {
        "rollNo": "21CS325",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.32,
        "activeBacklogs": 5,
        "attendance": 74.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_178():
    payload = {
        "rollNo": "21CS810",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.21,
        "activeBacklogs": 1,
        "attendance": 85.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_179():
    payload = {
        "rollNo": "21CS720",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.4,
        "activeBacklogs": 1,
        "attendance": 32.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_180():
    payload = {
        "rollNo": "21CS719",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.56,
        "activeBacklogs": 5,
        "attendance": 70.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_181():
    payload = {
        "rollNo": "21CS455",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.73,
        "activeBacklogs": 3,
        "attendance": 64.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_182():
    payload = {
        "rollNo": "21CS653",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.01,
        "activeBacklogs": 2,
        "attendance": 69.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_183():
    payload = {
        "rollNo": "21CS758",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.57,
        "activeBacklogs": 4,
        "attendance": 47.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_184():
    payload = {
        "rollNo": "21CS894",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.35,
        "activeBacklogs": 0,
        "attendance": 98.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_185():
    payload = {
        "rollNo": "21CS147",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.8,
        "activeBacklogs": 3,
        "attendance": 75.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_186():
    payload = {
        "rollNo": "21CS900",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.56,
        "activeBacklogs": 2,
        "attendance": 67.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_187():
    payload = {
        "rollNo": "21CS651",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.59,
        "activeBacklogs": 4,
        "attendance": 44.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_188():
    payload = {
        "rollNo": "21CS119",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.95,
        "activeBacklogs": 5,
        "attendance": 53.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_189():
    payload = {
        "rollNo": "21CS231",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.89,
        "activeBacklogs": 3,
        "attendance": 51.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_190():
    payload = {
        "rollNo": "21CS941",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.93,
        "activeBacklogs": 0,
        "attendance": 68.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_191():
    payload = {
        "rollNo": "21CS861",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.7,
        "activeBacklogs": 3,
        "attendance": 61.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_192():
    payload = {
        "rollNo": "21CS959",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.46,
        "activeBacklogs": 3,
        "attendance": 50.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_193():
    payload = {
        "rollNo": "21CS365",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.97,
        "activeBacklogs": 3,
        "attendance": 54.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_194():
    payload = {
        "rollNo": "21CS397",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.24,
        "activeBacklogs": 5,
        "attendance": 90.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_195():
    payload = {
        "rollNo": "21CS803",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.48,
        "activeBacklogs": 4,
        "attendance": 79.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_196():
    payload = {
        "rollNo": "21CS881",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.57,
        "activeBacklogs": 4,
        "attendance": 98.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_197():
    payload = {
        "rollNo": "21CS759",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.13,
        "activeBacklogs": 2,
        "attendance": 79.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_198():
    payload = {
        "rollNo": "21CS199",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.29,
        "activeBacklogs": 2,
        "attendance": 85.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_199():
    payload = {
        "rollNo": "21CS661",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.24,
        "activeBacklogs": 1,
        "attendance": 62.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_200():
    payload = {
        "rollNo": "21CS151",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.97,
        "activeBacklogs": 0,
        "attendance": 88.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_201():
    payload = {
        "rollNo": "21CS536",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.48,
        "activeBacklogs": 3,
        "attendance": 82.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_202():
    payload = {
        "rollNo": "21CS838",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.53,
        "activeBacklogs": 2,
        "attendance": 40.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_203():
    payload = {
        "rollNo": "21CS507",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.58,
        "activeBacklogs": 0,
        "attendance": 34.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_204():
    payload = {
        "rollNo": "21CS206",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.58,
        "activeBacklogs": 4,
        "attendance": 92.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_205():
    payload = {
        "rollNo": "21CS866",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.52,
        "activeBacklogs": 1,
        "attendance": 46.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_206():
    payload = {
        "rollNo": "21CS435",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.37,
        "activeBacklogs": 0,
        "attendance": 86.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_207():
    payload = {
        "rollNo": "21CS640",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.42,
        "activeBacklogs": 5,
        "attendance": 73.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_208():
    payload = {
        "rollNo": "21CS245",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.99,
        "activeBacklogs": 0,
        "attendance": 33.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_209():
    payload = {
        "rollNo": "21CS914",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.52,
        "activeBacklogs": 3,
        "attendance": 65.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_210():
    payload = {
        "rollNo": "21CS171",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.02,
        "activeBacklogs": 1,
        "attendance": 52.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_211():
    payload = {
        "rollNo": "21CS782",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.94,
        "activeBacklogs": 2,
        "attendance": 58.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_212():
    payload = {
        "rollNo": "21CS289",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.29,
        "activeBacklogs": 5,
        "attendance": 37.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_213():
    payload = {
        "rollNo": "21CS318",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.34,
        "activeBacklogs": 2,
        "attendance": 88.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_214():
    payload = {
        "rollNo": "21CS366",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.98,
        "activeBacklogs": 5,
        "attendance": 81.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_215():
    payload = {
        "rollNo": "21CS386",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.15,
        "activeBacklogs": 0,
        "attendance": 45.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_216():
    payload = {
        "rollNo": "21CS669",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.62,
        "activeBacklogs": 0,
        "attendance": 32.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_217():
    payload = {
        "rollNo": "21CS855",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.91,
        "activeBacklogs": 5,
        "attendance": 92.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_218():
    payload = {
        "rollNo": "21CS407",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.71,
        "activeBacklogs": 5,
        "attendance": 60.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_219():
    payload = {
        "rollNo": "21CS942",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.79,
        "activeBacklogs": 3,
        "attendance": 37.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_220():
    payload = {
        "rollNo": "21CS818",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.26,
        "activeBacklogs": 1,
        "attendance": 74.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_221():
    payload = {
        "rollNo": "21CS202",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.91,
        "activeBacklogs": 5,
        "attendance": 76.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_222():
    payload = {
        "rollNo": "21CS612",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.82,
        "activeBacklogs": 4,
        "attendance": 32.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_223():
    payload = {
        "rollNo": "21CS271",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.23,
        "activeBacklogs": 3,
        "attendance": 87.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_224():
    payload = {
        "rollNo": "21CS894",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.69,
        "activeBacklogs": 0,
        "attendance": 89.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_225():
    payload = {
        "rollNo": "21CS260",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.46,
        "activeBacklogs": 4,
        "attendance": 67.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_226():
    payload = {
        "rollNo": "21CS973",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.13,
        "activeBacklogs": 3,
        "attendance": 62.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_227():
    payload = {
        "rollNo": "21CS844",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.27,
        "activeBacklogs": 0,
        "attendance": 53.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_228():
    payload = {
        "rollNo": "21CS974",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.58,
        "activeBacklogs": 5,
        "attendance": 75.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_229():
    payload = {
        "rollNo": "21CS581",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.9,
        "activeBacklogs": 5,
        "attendance": 88.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_230():
    payload = {
        "rollNo": "21CS598",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.56,
        "activeBacklogs": 1,
        "attendance": 47.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_231():
    payload = {
        "rollNo": "21CS848",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.28,
        "activeBacklogs": 1,
        "attendance": 81.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_232():
    payload = {
        "rollNo": "21CS741",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.15,
        "activeBacklogs": 5,
        "attendance": 97.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_233():
    payload = {
        "rollNo": "21CS963",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.47,
        "activeBacklogs": 2,
        "attendance": 41.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_234():
    payload = {
        "rollNo": "21CS525",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.05,
        "activeBacklogs": 5,
        "attendance": 65.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_235():
    payload = {
        "rollNo": "21CS939",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.73,
        "activeBacklogs": 5,
        "attendance": 70.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_236():
    payload = {
        "rollNo": "21CS865",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.93,
        "activeBacklogs": 0,
        "attendance": 77.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_237():
    payload = {
        "rollNo": "21CS397",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.29,
        "activeBacklogs": 3,
        "attendance": 89.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_238():
    payload = {
        "rollNo": "21CS164",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 10.0,
        "activeBacklogs": 2,
        "attendance": 77.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_239():
    payload = {
        "rollNo": "21CS869",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.68,
        "activeBacklogs": 2,
        "attendance": 82.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_240():
    payload = {
        "rollNo": "21CS848",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.39,
        "activeBacklogs": 1,
        "attendance": 93.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_241():
    payload = {
        "rollNo": "21CS942",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.47,
        "activeBacklogs": 4,
        "attendance": 95.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_242():
    payload = {
        "rollNo": "21CS118",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.45,
        "activeBacklogs": 2,
        "attendance": 85.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_243():
    payload = {
        "rollNo": "21CS776",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.94,
        "activeBacklogs": 0,
        "attendance": 63.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_244():
    payload = {
        "rollNo": "21CS838",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.91,
        "activeBacklogs": 3,
        "attendance": 87.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_245():
    payload = {
        "rollNo": "21CS988",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.41,
        "activeBacklogs": 5,
        "attendance": 86.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_246():
    payload = {
        "rollNo": "21CS489",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.51,
        "activeBacklogs": 5,
        "attendance": 48.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_247():
    payload = {
        "rollNo": "21CS871",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.44,
        "activeBacklogs": 5,
        "attendance": 55.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_248():
    payload = {
        "rollNo": "21CS981",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.58,
        "activeBacklogs": 3,
        "attendance": 96.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_12_249():
    payload = {
        "rollNo": "21CS555",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.81,
        "activeBacklogs": 0,
        "attendance": 72.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

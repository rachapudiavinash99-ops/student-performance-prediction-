import pytest
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_prediction_case_17_0():
    payload = {
        "rollNo": "21CS855",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.78,
        "activeBacklogs": 4,
        "attendance": 79.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_1():
    payload = {
        "rollNo": "21CS696",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.52,
        "activeBacklogs": 0,
        "attendance": 71.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_2():
    payload = {
        "rollNo": "21CS155",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.68,
        "activeBacklogs": 0,
        "attendance": 59.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_3():
    payload = {
        "rollNo": "21CS341",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.94,
        "activeBacklogs": 1,
        "attendance": 62.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_4():
    payload = {
        "rollNo": "21CS976",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.68,
        "activeBacklogs": 1,
        "attendance": 67.04
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_5():
    payload = {
        "rollNo": "21CS801",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.54,
        "activeBacklogs": 0,
        "attendance": 72.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_6():
    payload = {
        "rollNo": "21CS136",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.29,
        "activeBacklogs": 5,
        "attendance": 46.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_7():
    payload = {
        "rollNo": "21CS981",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.72,
        "activeBacklogs": 2,
        "attendance": 51.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_8():
    payload = {
        "rollNo": "21CS971",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.05,
        "activeBacklogs": 2,
        "attendance": 97.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_9():
    payload = {
        "rollNo": "21CS636",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.55,
        "activeBacklogs": 0,
        "attendance": 67.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_10():
    payload = {
        "rollNo": "21CS202",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.87,
        "activeBacklogs": 3,
        "attendance": 76.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_11():
    payload = {
        "rollNo": "21CS922",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.99,
        "activeBacklogs": 5,
        "attendance": 40.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_12():
    payload = {
        "rollNo": "21CS182",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.04,
        "activeBacklogs": 1,
        "attendance": 66.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_13():
    payload = {
        "rollNo": "21CS250",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.91,
        "activeBacklogs": 4,
        "attendance": 63.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_14():
    payload = {
        "rollNo": "21CS307",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.41,
        "activeBacklogs": 5,
        "attendance": 60.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_15():
    payload = {
        "rollNo": "21CS338",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.63,
        "activeBacklogs": 2,
        "attendance": 71.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_16():
    payload = {
        "rollNo": "21CS711",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.51,
        "activeBacklogs": 0,
        "attendance": 96.04
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_17():
    payload = {
        "rollNo": "21CS848",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.47,
        "activeBacklogs": 1,
        "attendance": 65.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_18():
    payload = {
        "rollNo": "21CS192",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.42,
        "activeBacklogs": 4,
        "attendance": 95.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_19():
    payload = {
        "rollNo": "21CS704",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.3,
        "activeBacklogs": 2,
        "attendance": 72.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_20():
    payload = {
        "rollNo": "21CS485",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.5,
        "activeBacklogs": 2,
        "attendance": 61.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_21():
    payload = {
        "rollNo": "21CS431",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.24,
        "activeBacklogs": 1,
        "attendance": 44.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_22():
    payload = {
        "rollNo": "21CS238",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.82,
        "activeBacklogs": 4,
        "attendance": 52.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_23():
    payload = {
        "rollNo": "21CS128",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.14,
        "activeBacklogs": 3,
        "attendance": 74.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_24():
    payload = {
        "rollNo": "21CS471",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.53,
        "activeBacklogs": 0,
        "attendance": 52.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_25():
    payload = {
        "rollNo": "21CS531",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.52,
        "activeBacklogs": 0,
        "attendance": 76.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_26():
    payload = {
        "rollNo": "21CS335",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.58,
        "activeBacklogs": 3,
        "attendance": 88.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_27():
    payload = {
        "rollNo": "21CS666",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.37,
        "activeBacklogs": 1,
        "attendance": 86.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_28():
    payload = {
        "rollNo": "21CS358",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.99,
        "activeBacklogs": 0,
        "attendance": 48.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_29():
    payload = {
        "rollNo": "21CS410",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.88,
        "activeBacklogs": 5,
        "attendance": 61.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_30():
    payload = {
        "rollNo": "21CS608",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.9,
        "activeBacklogs": 3,
        "attendance": 49.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_31():
    payload = {
        "rollNo": "21CS965",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.22,
        "activeBacklogs": 4,
        "attendance": 37.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_32():
    payload = {
        "rollNo": "21CS240",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.44,
        "activeBacklogs": 3,
        "attendance": 90.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_33():
    payload = {
        "rollNo": "21CS164",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.65,
        "activeBacklogs": 5,
        "attendance": 35.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_34():
    payload = {
        "rollNo": "21CS714",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.68,
        "activeBacklogs": 3,
        "attendance": 35.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_35():
    payload = {
        "rollNo": "21CS950",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.69,
        "activeBacklogs": 3,
        "attendance": 93.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_36():
    payload = {
        "rollNo": "21CS144",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.22,
        "activeBacklogs": 1,
        "attendance": 98.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_37():
    payload = {
        "rollNo": "21CS490",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.15,
        "activeBacklogs": 1,
        "attendance": 53.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_38():
    payload = {
        "rollNo": "21CS526",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.77,
        "activeBacklogs": 0,
        "attendance": 61.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_39():
    payload = {
        "rollNo": "21CS588",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.45,
        "activeBacklogs": 0,
        "attendance": 78.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_40():
    payload = {
        "rollNo": "21CS860",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.94,
        "activeBacklogs": 3,
        "attendance": 56.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_41():
    payload = {
        "rollNo": "21CS325",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.95,
        "activeBacklogs": 2,
        "attendance": 47.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_42():
    payload = {
        "rollNo": "21CS715",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.48,
        "activeBacklogs": 4,
        "attendance": 48.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_43():
    payload = {
        "rollNo": "21CS843",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.84,
        "activeBacklogs": 1,
        "attendance": 64.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_44():
    payload = {
        "rollNo": "21CS406",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.89,
        "activeBacklogs": 1,
        "attendance": 52.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_45():
    payload = {
        "rollNo": "21CS801",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.29,
        "activeBacklogs": 1,
        "attendance": 35.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_46():
    payload = {
        "rollNo": "21CS700",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.78,
        "activeBacklogs": 4,
        "attendance": 31.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_47():
    payload = {
        "rollNo": "21CS428",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.28,
        "activeBacklogs": 4,
        "attendance": 32.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_48():
    payload = {
        "rollNo": "21CS512",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.93,
        "activeBacklogs": 4,
        "attendance": 41.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_49():
    payload = {
        "rollNo": "21CS588",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.02,
        "activeBacklogs": 2,
        "attendance": 78.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_50():
    payload = {
        "rollNo": "21CS904",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.03,
        "activeBacklogs": 4,
        "attendance": 48.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_51():
    payload = {
        "rollNo": "21CS198",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.29,
        "activeBacklogs": 1,
        "attendance": 93.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_52():
    payload = {
        "rollNo": "21CS337",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.85,
        "activeBacklogs": 4,
        "attendance": 48.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_53():
    payload = {
        "rollNo": "21CS839",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.23,
        "activeBacklogs": 0,
        "attendance": 93.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_54():
    payload = {
        "rollNo": "21CS494",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.99,
        "activeBacklogs": 5,
        "attendance": 80.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_55():
    payload = {
        "rollNo": "21CS978",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.15,
        "activeBacklogs": 4,
        "attendance": 43.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_56():
    payload = {
        "rollNo": "21CS555",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.12,
        "activeBacklogs": 1,
        "attendance": 80.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_57():
    payload = {
        "rollNo": "21CS586",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.76,
        "activeBacklogs": 2,
        "attendance": 90.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_58():
    payload = {
        "rollNo": "21CS680",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.41,
        "activeBacklogs": 0,
        "attendance": 83.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_59():
    payload = {
        "rollNo": "21CS281",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.28,
        "activeBacklogs": 5,
        "attendance": 71.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_60():
    payload = {
        "rollNo": "21CS456",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.83,
        "activeBacklogs": 3,
        "attendance": 96.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_61():
    payload = {
        "rollNo": "21CS100",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.32,
        "activeBacklogs": 3,
        "attendance": 50.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_62():
    payload = {
        "rollNo": "21CS834",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.71,
        "activeBacklogs": 3,
        "attendance": 70.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_63():
    payload = {
        "rollNo": "21CS206",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.74,
        "activeBacklogs": 3,
        "attendance": 52.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_64():
    payload = {
        "rollNo": "21CS724",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.52,
        "activeBacklogs": 4,
        "attendance": 32.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_65():
    payload = {
        "rollNo": "21CS709",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.55,
        "activeBacklogs": 2,
        "attendance": 38.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_66():
    payload = {
        "rollNo": "21CS848",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.49,
        "activeBacklogs": 2,
        "attendance": 51.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_67():
    payload = {
        "rollNo": "21CS168",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.36,
        "activeBacklogs": 1,
        "attendance": 77.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_68():
    payload = {
        "rollNo": "21CS733",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.93,
        "activeBacklogs": 5,
        "attendance": 51.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_69():
    payload = {
        "rollNo": "21CS107",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.65,
        "activeBacklogs": 0,
        "attendance": 96.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_70():
    payload = {
        "rollNo": "21CS807",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.0,
        "activeBacklogs": 1,
        "attendance": 74.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_71():
    payload = {
        "rollNo": "21CS423",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.5,
        "activeBacklogs": 1,
        "attendance": 79.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_72():
    payload = {
        "rollNo": "21CS355",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.66,
        "activeBacklogs": 0,
        "attendance": 83.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_73():
    payload = {
        "rollNo": "21CS176",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.38,
        "activeBacklogs": 3,
        "attendance": 99.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_74():
    payload = {
        "rollNo": "21CS842",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.93,
        "activeBacklogs": 2,
        "attendance": 32.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_75():
    payload = {
        "rollNo": "21CS950",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.27,
        "activeBacklogs": 5,
        "attendance": 84.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_76():
    payload = {
        "rollNo": "21CS568",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.26,
        "activeBacklogs": 0,
        "attendance": 71.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_77():
    payload = {
        "rollNo": "21CS222",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.34,
        "activeBacklogs": 0,
        "attendance": 66.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_78():
    payload = {
        "rollNo": "21CS982",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.52,
        "activeBacklogs": 1,
        "attendance": 69.04
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_79():
    payload = {
        "rollNo": "21CS450",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.83,
        "activeBacklogs": 4,
        "attendance": 57.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_80():
    payload = {
        "rollNo": "21CS873",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.01,
        "activeBacklogs": 1,
        "attendance": 78.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_81():
    payload = {
        "rollNo": "21CS919",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.16,
        "activeBacklogs": 0,
        "attendance": 38.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_82():
    payload = {
        "rollNo": "21CS247",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.51,
        "activeBacklogs": 5,
        "attendance": 64.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_83():
    payload = {
        "rollNo": "21CS624",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.0,
        "activeBacklogs": 4,
        "attendance": 72.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_84():
    payload = {
        "rollNo": "21CS153",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.56,
        "activeBacklogs": 5,
        "attendance": 71.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_85():
    payload = {
        "rollNo": "21CS470",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.65,
        "activeBacklogs": 4,
        "attendance": 85.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_86():
    payload = {
        "rollNo": "21CS100",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.17,
        "activeBacklogs": 5,
        "attendance": 87.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_87():
    payload = {
        "rollNo": "21CS796",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.38,
        "activeBacklogs": 1,
        "attendance": 73.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_88():
    payload = {
        "rollNo": "21CS492",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.22,
        "activeBacklogs": 1,
        "attendance": 63.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_89():
    payload = {
        "rollNo": "21CS997",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.78,
        "activeBacklogs": 4,
        "attendance": 74.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_90():
    payload = {
        "rollNo": "21CS760",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.41,
        "activeBacklogs": 0,
        "attendance": 31.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_91():
    payload = {
        "rollNo": "21CS525",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.69,
        "activeBacklogs": 4,
        "attendance": 42.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_92():
    payload = {
        "rollNo": "21CS887",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.89,
        "activeBacklogs": 5,
        "attendance": 77.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_93():
    payload = {
        "rollNo": "21CS712",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.13,
        "activeBacklogs": 5,
        "attendance": 30.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_94():
    payload = {
        "rollNo": "21CS684",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.78,
        "activeBacklogs": 4,
        "attendance": 72.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_95():
    payload = {
        "rollNo": "21CS852",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.46,
        "activeBacklogs": 0,
        "attendance": 99.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_96():
    payload = {
        "rollNo": "21CS670",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.52,
        "activeBacklogs": 4,
        "attendance": 59.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_97():
    payload = {
        "rollNo": "21CS786",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.04,
        "activeBacklogs": 0,
        "attendance": 72.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_98():
    payload = {
        "rollNo": "21CS116",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.54,
        "activeBacklogs": 1,
        "attendance": 86.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_99():
    payload = {
        "rollNo": "21CS138",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.75,
        "activeBacklogs": 5,
        "attendance": 86.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_100():
    payload = {
        "rollNo": "21CS612",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.16,
        "activeBacklogs": 4,
        "attendance": 66.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_101():
    payload = {
        "rollNo": "21CS468",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.31,
        "activeBacklogs": 5,
        "attendance": 45.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_102():
    payload = {
        "rollNo": "21CS225",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.67,
        "activeBacklogs": 2,
        "attendance": 91.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_103():
    payload = {
        "rollNo": "21CS134",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.79,
        "activeBacklogs": 0,
        "attendance": 88.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_104():
    payload = {
        "rollNo": "21CS313",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.78,
        "activeBacklogs": 1,
        "attendance": 94.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_105():
    payload = {
        "rollNo": "21CS755",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.13,
        "activeBacklogs": 4,
        "attendance": 82.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_106():
    payload = {
        "rollNo": "21CS274",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.16,
        "activeBacklogs": 1,
        "attendance": 86.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_107():
    payload = {
        "rollNo": "21CS680",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.15,
        "activeBacklogs": 5,
        "attendance": 38.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_108():
    payload = {
        "rollNo": "21CS667",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.74,
        "activeBacklogs": 0,
        "attendance": 72.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_109():
    payload = {
        "rollNo": "21CS646",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.99,
        "activeBacklogs": 3,
        "attendance": 82.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_110():
    payload = {
        "rollNo": "21CS375",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.46,
        "activeBacklogs": 1,
        "attendance": 85.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_111():
    payload = {
        "rollNo": "21CS969",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.39,
        "activeBacklogs": 0,
        "attendance": 97.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_112():
    payload = {
        "rollNo": "21CS101",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.29,
        "activeBacklogs": 5,
        "attendance": 58.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_113():
    payload = {
        "rollNo": "21CS284",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.08,
        "activeBacklogs": 5,
        "attendance": 55.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_114():
    payload = {
        "rollNo": "21CS697",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.17,
        "activeBacklogs": 0,
        "attendance": 95.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_115():
    payload = {
        "rollNo": "21CS399",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.88,
        "activeBacklogs": 3,
        "attendance": 50.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_116():
    payload = {
        "rollNo": "21CS363",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.48,
        "activeBacklogs": 5,
        "attendance": 49.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_117():
    payload = {
        "rollNo": "21CS343",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.7,
        "activeBacklogs": 1,
        "attendance": 48.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_118():
    payload = {
        "rollNo": "21CS569",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.51,
        "activeBacklogs": 0,
        "attendance": 61.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_119():
    payload = {
        "rollNo": "21CS134",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.57,
        "activeBacklogs": 1,
        "attendance": 99.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_120():
    payload = {
        "rollNo": "21CS191",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.21,
        "activeBacklogs": 5,
        "attendance": 52.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_121():
    payload = {
        "rollNo": "21CS203",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.5,
        "activeBacklogs": 2,
        "attendance": 43.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_122():
    payload = {
        "rollNo": "21CS611",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.18,
        "activeBacklogs": 5,
        "attendance": 74.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_123():
    payload = {
        "rollNo": "21CS284",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.5,
        "activeBacklogs": 2,
        "attendance": 73.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_124():
    payload = {
        "rollNo": "21CS179",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.75,
        "activeBacklogs": 1,
        "attendance": 90.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_125():
    payload = {
        "rollNo": "21CS629",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.08,
        "activeBacklogs": 0,
        "attendance": 77.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_126():
    payload = {
        "rollNo": "21CS337",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.69,
        "activeBacklogs": 3,
        "attendance": 40.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_127():
    payload = {
        "rollNo": "21CS893",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.09,
        "activeBacklogs": 1,
        "attendance": 48.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_128():
    payload = {
        "rollNo": "21CS711",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.58,
        "activeBacklogs": 1,
        "attendance": 58.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_129():
    payload = {
        "rollNo": "21CS573",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.18,
        "activeBacklogs": 4,
        "attendance": 41.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_130():
    payload = {
        "rollNo": "21CS628",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.86,
        "activeBacklogs": 3,
        "attendance": 83.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_131():
    payload = {
        "rollNo": "21CS832",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.98,
        "activeBacklogs": 2,
        "attendance": 45.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_132():
    payload = {
        "rollNo": "21CS183",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.87,
        "activeBacklogs": 4,
        "attendance": 98.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_133():
    payload = {
        "rollNo": "21CS325",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.58,
        "activeBacklogs": 1,
        "attendance": 43.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_134():
    payload = {
        "rollNo": "21CS891",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.88,
        "activeBacklogs": 4,
        "attendance": 66.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_135():
    payload = {
        "rollNo": "21CS398",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.73,
        "activeBacklogs": 5,
        "attendance": 61.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_136():
    payload = {
        "rollNo": "21CS118",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.29,
        "activeBacklogs": 1,
        "attendance": 40.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_137():
    payload = {
        "rollNo": "21CS778",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.35,
        "activeBacklogs": 2,
        "attendance": 45.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_138():
    payload = {
        "rollNo": "21CS129",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.55,
        "activeBacklogs": 0,
        "attendance": 82.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_139():
    payload = {
        "rollNo": "21CS507",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.65,
        "activeBacklogs": 2,
        "attendance": 76.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_140():
    payload = {
        "rollNo": "21CS177",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.44,
        "activeBacklogs": 5,
        "attendance": 77.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_141():
    payload = {
        "rollNo": "21CS382",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.07,
        "activeBacklogs": 5,
        "attendance": 53.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_142():
    payload = {
        "rollNo": "21CS698",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.97,
        "activeBacklogs": 0,
        "attendance": 53.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_143():
    payload = {
        "rollNo": "21CS511",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.73,
        "activeBacklogs": 4,
        "attendance": 59.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_144():
    payload = {
        "rollNo": "21CS211",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.24,
        "activeBacklogs": 3,
        "attendance": 30.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_145():
    payload = {
        "rollNo": "21CS445",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.7,
        "activeBacklogs": 5,
        "attendance": 86.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_146():
    payload = {
        "rollNo": "21CS565",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.51,
        "activeBacklogs": 2,
        "attendance": 32.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_147():
    payload = {
        "rollNo": "21CS504",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.83,
        "activeBacklogs": 5,
        "attendance": 92.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_148():
    payload = {
        "rollNo": "21CS190",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.78,
        "activeBacklogs": 4,
        "attendance": 56.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_149():
    payload = {
        "rollNo": "21CS451",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.55,
        "activeBacklogs": 0,
        "attendance": 96.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_150():
    payload = {
        "rollNo": "21CS852",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.79,
        "activeBacklogs": 5,
        "attendance": 70.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_151():
    payload = {
        "rollNo": "21CS110",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.53,
        "activeBacklogs": 5,
        "attendance": 57.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_152():
    payload = {
        "rollNo": "21CS849",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.43,
        "activeBacklogs": 5,
        "attendance": 39.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_153():
    payload = {
        "rollNo": "21CS477",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.74,
        "activeBacklogs": 0,
        "attendance": 68.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_154():
    payload = {
        "rollNo": "21CS994",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.22,
        "activeBacklogs": 2,
        "attendance": 85.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_155():
    payload = {
        "rollNo": "21CS689",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.2,
        "activeBacklogs": 2,
        "attendance": 40.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_156():
    payload = {
        "rollNo": "21CS927",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.76,
        "activeBacklogs": 5,
        "attendance": 46.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_157():
    payload = {
        "rollNo": "21CS603",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.0,
        "activeBacklogs": 2,
        "attendance": 64.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_158():
    payload = {
        "rollNo": "21CS821",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.6,
        "activeBacklogs": 3,
        "attendance": 88.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_159():
    payload = {
        "rollNo": "21CS739",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.71,
        "activeBacklogs": 0,
        "attendance": 61.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_160():
    payload = {
        "rollNo": "21CS613",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.11,
        "activeBacklogs": 4,
        "attendance": 92.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_161():
    payload = {
        "rollNo": "21CS217",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.42,
        "activeBacklogs": 2,
        "attendance": 30.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_162():
    payload = {
        "rollNo": "21CS132",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.37,
        "activeBacklogs": 1,
        "attendance": 70.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_163():
    payload = {
        "rollNo": "21CS878",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.81,
        "activeBacklogs": 2,
        "attendance": 90.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_164():
    payload = {
        "rollNo": "21CS169",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.91,
        "activeBacklogs": 4,
        "attendance": 90.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_165():
    payload = {
        "rollNo": "21CS382",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.39,
        "activeBacklogs": 4,
        "attendance": 52.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_166():
    payload = {
        "rollNo": "21CS829",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.34,
        "activeBacklogs": 4,
        "attendance": 87.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_167():
    payload = {
        "rollNo": "21CS453",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.93,
        "activeBacklogs": 5,
        "attendance": 64.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_168():
    payload = {
        "rollNo": "21CS148",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.25,
        "activeBacklogs": 1,
        "attendance": 65.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_169():
    payload = {
        "rollNo": "21CS362",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.93,
        "activeBacklogs": 4,
        "attendance": 63.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_170():
    payload = {
        "rollNo": "21CS200",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.3,
        "activeBacklogs": 5,
        "attendance": 42.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_171():
    payload = {
        "rollNo": "21CS876",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.73,
        "activeBacklogs": 3,
        "attendance": 63.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_172():
    payload = {
        "rollNo": "21CS803",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.17,
        "activeBacklogs": 5,
        "attendance": 91.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_173():
    payload = {
        "rollNo": "21CS256",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.6,
        "activeBacklogs": 4,
        "attendance": 30.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_174():
    payload = {
        "rollNo": "21CS124",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.19,
        "activeBacklogs": 3,
        "attendance": 98.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_175():
    payload = {
        "rollNo": "21CS891",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.39,
        "activeBacklogs": 1,
        "attendance": 96.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_176():
    payload = {
        "rollNo": "21CS262",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.29,
        "activeBacklogs": 1,
        "attendance": 30.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_177():
    payload = {
        "rollNo": "21CS492",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.29,
        "activeBacklogs": 1,
        "attendance": 93.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_178():
    payload = {
        "rollNo": "21CS393",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.99,
        "activeBacklogs": 4,
        "attendance": 90.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_179():
    payload = {
        "rollNo": "21CS801",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.94,
        "activeBacklogs": 1,
        "attendance": 64.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_180():
    payload = {
        "rollNo": "21CS644",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.82,
        "activeBacklogs": 0,
        "attendance": 73.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_181():
    payload = {
        "rollNo": "21CS890",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.03,
        "activeBacklogs": 3,
        "attendance": 40.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_182():
    payload = {
        "rollNo": "21CS638",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.72,
        "activeBacklogs": 4,
        "attendance": 53.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_183():
    payload = {
        "rollNo": "21CS211",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.75,
        "activeBacklogs": 5,
        "attendance": 83.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_184():
    payload = {
        "rollNo": "21CS672",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.7,
        "activeBacklogs": 1,
        "attendance": 59.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_185():
    payload = {
        "rollNo": "21CS437",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.19,
        "activeBacklogs": 3,
        "attendance": 97.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_186():
    payload = {
        "rollNo": "21CS580",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.32,
        "activeBacklogs": 1,
        "attendance": 70.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_187():
    payload = {
        "rollNo": "21CS722",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.28,
        "activeBacklogs": 2,
        "attendance": 54.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_188():
    payload = {
        "rollNo": "21CS948",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.68,
        "activeBacklogs": 0,
        "attendance": 95.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_189():
    payload = {
        "rollNo": "21CS700",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.8,
        "activeBacklogs": 2,
        "attendance": 49.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_190():
    payload = {
        "rollNo": "21CS892",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.9,
        "activeBacklogs": 0,
        "attendance": 78.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_191():
    payload = {
        "rollNo": "21CS157",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.32,
        "activeBacklogs": 4,
        "attendance": 49.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_192():
    payload = {
        "rollNo": "21CS587",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.66,
        "activeBacklogs": 4,
        "attendance": 31.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_193():
    payload = {
        "rollNo": "21CS898",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.27,
        "activeBacklogs": 4,
        "attendance": 69.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_194():
    payload = {
        "rollNo": "21CS447",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.24,
        "activeBacklogs": 1,
        "attendance": 32.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_195():
    payload = {
        "rollNo": "21CS129",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.32,
        "activeBacklogs": 1,
        "attendance": 45.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_196():
    payload = {
        "rollNo": "21CS565",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.77,
        "activeBacklogs": 2,
        "attendance": 98.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_197():
    payload = {
        "rollNo": "21CS446",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.34,
        "activeBacklogs": 1,
        "attendance": 99.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_198():
    payload = {
        "rollNo": "21CS721",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.51,
        "activeBacklogs": 2,
        "attendance": 38.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_199():
    payload = {
        "rollNo": "21CS566",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.49,
        "activeBacklogs": 2,
        "attendance": 45.04
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_200():
    payload = {
        "rollNo": "21CS221",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.58,
        "activeBacklogs": 2,
        "attendance": 61.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_201():
    payload = {
        "rollNo": "21CS561",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.08,
        "activeBacklogs": 1,
        "attendance": 83.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_202():
    payload = {
        "rollNo": "21CS729",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.27,
        "activeBacklogs": 0,
        "attendance": 41.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_203():
    payload = {
        "rollNo": "21CS363",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.24,
        "activeBacklogs": 0,
        "attendance": 35.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_204():
    payload = {
        "rollNo": "21CS416",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.88,
        "activeBacklogs": 0,
        "attendance": 78.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_205():
    payload = {
        "rollNo": "21CS742",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.18,
        "activeBacklogs": 0,
        "attendance": 67.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_206():
    payload = {
        "rollNo": "21CS999",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.47,
        "activeBacklogs": 1,
        "attendance": 76.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_207():
    payload = {
        "rollNo": "21CS336",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.15,
        "activeBacklogs": 3,
        "attendance": 87.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_208():
    payload = {
        "rollNo": "21CS202",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.71,
        "activeBacklogs": 2,
        "attendance": 42.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_209():
    payload = {
        "rollNo": "21CS100",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.96,
        "activeBacklogs": 2,
        "attendance": 93.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_210():
    payload = {
        "rollNo": "21CS263",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.24,
        "activeBacklogs": 4,
        "attendance": 78.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_211():
    payload = {
        "rollNo": "21CS980",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.74,
        "activeBacklogs": 3,
        "attendance": 73.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_212():
    payload = {
        "rollNo": "21CS716",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.78,
        "activeBacklogs": 1,
        "attendance": 64.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_213():
    payload = {
        "rollNo": "21CS658",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.36,
        "activeBacklogs": 4,
        "attendance": 90.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_214():
    payload = {
        "rollNo": "21CS632",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.21,
        "activeBacklogs": 3,
        "attendance": 95.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_215():
    payload = {
        "rollNo": "21CS837",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.64,
        "activeBacklogs": 3,
        "attendance": 90.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_216():
    payload = {
        "rollNo": "21CS821",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.58,
        "activeBacklogs": 5,
        "attendance": 85.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_217():
    payload = {
        "rollNo": "21CS131",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.44,
        "activeBacklogs": 2,
        "attendance": 75.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_218():
    payload = {
        "rollNo": "21CS335",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.26,
        "activeBacklogs": 2,
        "attendance": 49.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_219():
    payload = {
        "rollNo": "21CS740",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.48,
        "activeBacklogs": 4,
        "attendance": 35.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_220():
    payload = {
        "rollNo": "21CS559",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.65,
        "activeBacklogs": 4,
        "attendance": 41.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_221():
    payload = {
        "rollNo": "21CS622",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.14,
        "activeBacklogs": 2,
        "attendance": 93.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_222():
    payload = {
        "rollNo": "21CS917",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.21,
        "activeBacklogs": 4,
        "attendance": 44.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_223():
    payload = {
        "rollNo": "21CS254",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.0,
        "activeBacklogs": 1,
        "attendance": 31.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_224():
    payload = {
        "rollNo": "21CS958",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.22,
        "activeBacklogs": 4,
        "attendance": 84.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_225():
    payload = {
        "rollNo": "21CS798",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.54,
        "activeBacklogs": 0,
        "attendance": 43.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_226():
    payload = {
        "rollNo": "21CS143",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.95,
        "activeBacklogs": 4,
        "attendance": 95.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_227():
    payload = {
        "rollNo": "21CS197",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.53,
        "activeBacklogs": 4,
        "attendance": 59.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_228():
    payload = {
        "rollNo": "21CS359",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.95,
        "activeBacklogs": 4,
        "attendance": 57.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_229():
    payload = {
        "rollNo": "21CS938",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.71,
        "activeBacklogs": 3,
        "attendance": 62.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_230():
    payload = {
        "rollNo": "21CS434",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.16,
        "activeBacklogs": 3,
        "attendance": 89.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_231():
    payload = {
        "rollNo": "21CS155",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.08,
        "activeBacklogs": 0,
        "attendance": 31.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_232():
    payload = {
        "rollNo": "21CS173",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.88,
        "activeBacklogs": 2,
        "attendance": 59.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_233():
    payload = {
        "rollNo": "21CS493",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.74,
        "activeBacklogs": 0,
        "attendance": 89.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_234():
    payload = {
        "rollNo": "21CS723",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.98,
        "activeBacklogs": 3,
        "attendance": 89.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_235():
    payload = {
        "rollNo": "21CS209",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.1,
        "activeBacklogs": 3,
        "attendance": 34.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_236():
    payload = {
        "rollNo": "21CS343",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.76,
        "activeBacklogs": 3,
        "attendance": 71.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_237():
    payload = {
        "rollNo": "21CS276",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.3,
        "activeBacklogs": 4,
        "attendance": 36.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_238():
    payload = {
        "rollNo": "21CS907",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.64,
        "activeBacklogs": 0,
        "attendance": 64.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_239():
    payload = {
        "rollNo": "21CS803",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.23,
        "activeBacklogs": 2,
        "attendance": 75.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_240():
    payload = {
        "rollNo": "21CS755",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.08,
        "activeBacklogs": 5,
        "attendance": 76.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_241():
    payload = {
        "rollNo": "21CS984",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.43,
        "activeBacklogs": 3,
        "attendance": 83.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_242():
    payload = {
        "rollNo": "21CS522",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.32,
        "activeBacklogs": 4,
        "attendance": 72.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_243():
    payload = {
        "rollNo": "21CS299",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.99,
        "activeBacklogs": 3,
        "attendance": 54.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_244():
    payload = {
        "rollNo": "21CS313",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.27,
        "activeBacklogs": 3,
        "attendance": 88.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_245():
    payload = {
        "rollNo": "21CS344",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.96,
        "activeBacklogs": 5,
        "attendance": 90.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_246():
    payload = {
        "rollNo": "21CS858",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.75,
        "activeBacklogs": 0,
        "attendance": 33.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_247():
    payload = {
        "rollNo": "21CS413",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.12,
        "activeBacklogs": 4,
        "attendance": 35.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_248():
    payload = {
        "rollNo": "21CS517",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.96,
        "activeBacklogs": 5,
        "attendance": 32.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_17_249():
    payload = {
        "rollNo": "21CS506",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.85,
        "activeBacklogs": 4,
        "attendance": 49.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

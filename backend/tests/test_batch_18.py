import pytest
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_prediction_case_18_0():
    payload = {
        "rollNo": "21CS689",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.52,
        "activeBacklogs": 4,
        "attendance": 61.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_1():
    payload = {
        "rollNo": "21CS724",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.69,
        "activeBacklogs": 5,
        "attendance": 33.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_2():
    payload = {
        "rollNo": "21CS432",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.51,
        "activeBacklogs": 3,
        "attendance": 51.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_3():
    payload = {
        "rollNo": "21CS456",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.1,
        "activeBacklogs": 2,
        "attendance": 81.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_4():
    payload = {
        "rollNo": "21CS399",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.54,
        "activeBacklogs": 2,
        "attendance": 75.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_5():
    payload = {
        "rollNo": "21CS565",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.79,
        "activeBacklogs": 2,
        "attendance": 54.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_6():
    payload = {
        "rollNo": "21CS637",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.44,
        "activeBacklogs": 5,
        "attendance": 33.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_7():
    payload = {
        "rollNo": "21CS566",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.44,
        "activeBacklogs": 1,
        "attendance": 95.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_8():
    payload = {
        "rollNo": "21CS258",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.33,
        "activeBacklogs": 1,
        "attendance": 50.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_9():
    payload = {
        "rollNo": "21CS961",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.73,
        "activeBacklogs": 1,
        "attendance": 83.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_10():
    payload = {
        "rollNo": "21CS500",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.42,
        "activeBacklogs": 1,
        "attendance": 89.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_11():
    payload = {
        "rollNo": "21CS661",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.26,
        "activeBacklogs": 5,
        "attendance": 48.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_12():
    payload = {
        "rollNo": "21CS581",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.58,
        "activeBacklogs": 3,
        "attendance": 38.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_13():
    payload = {
        "rollNo": "21CS561",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.06,
        "activeBacklogs": 1,
        "attendance": 50.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_14():
    payload = {
        "rollNo": "21CS370",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.42,
        "activeBacklogs": 0,
        "attendance": 64.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_15():
    payload = {
        "rollNo": "21CS935",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.69,
        "activeBacklogs": 1,
        "attendance": 52.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_16():
    payload = {
        "rollNo": "21CS363",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.55,
        "activeBacklogs": 3,
        "attendance": 70.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_17():
    payload = {
        "rollNo": "21CS319",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.16,
        "activeBacklogs": 5,
        "attendance": 84.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_18():
    payload = {
        "rollNo": "21CS165",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.93,
        "activeBacklogs": 5,
        "attendance": 36.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_19():
    payload = {
        "rollNo": "21CS583",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.4,
        "activeBacklogs": 2,
        "attendance": 33.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_20():
    payload = {
        "rollNo": "21CS107",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.96,
        "activeBacklogs": 4,
        "attendance": 63.04
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_21():
    payload = {
        "rollNo": "21CS935",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.43,
        "activeBacklogs": 5,
        "attendance": 64.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_22():
    payload = {
        "rollNo": "21CS547",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.26,
        "activeBacklogs": 3,
        "attendance": 36.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_23():
    payload = {
        "rollNo": "21CS938",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.23,
        "activeBacklogs": 0,
        "attendance": 96.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_24():
    payload = {
        "rollNo": "21CS704",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.22,
        "activeBacklogs": 3,
        "attendance": 37.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_25():
    payload = {
        "rollNo": "21CS559",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.04,
        "activeBacklogs": 3,
        "attendance": 82.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_26():
    payload = {
        "rollNo": "21CS909",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.31,
        "activeBacklogs": 0,
        "attendance": 99.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_27():
    payload = {
        "rollNo": "21CS610",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.87,
        "activeBacklogs": 3,
        "attendance": 77.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_28():
    payload = {
        "rollNo": "21CS925",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.31,
        "activeBacklogs": 0,
        "attendance": 90.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_29():
    payload = {
        "rollNo": "21CS932",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.22,
        "activeBacklogs": 2,
        "attendance": 57.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_30():
    payload = {
        "rollNo": "21CS979",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.67,
        "activeBacklogs": 5,
        "attendance": 63.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_31():
    payload = {
        "rollNo": "21CS985",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.09,
        "activeBacklogs": 3,
        "attendance": 91.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_32():
    payload = {
        "rollNo": "21CS647",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.18,
        "activeBacklogs": 4,
        "attendance": 45.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_33():
    payload = {
        "rollNo": "21CS341",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.08,
        "activeBacklogs": 3,
        "attendance": 63.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_34():
    payload = {
        "rollNo": "21CS642",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.5,
        "activeBacklogs": 0,
        "attendance": 95.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_35():
    payload = {
        "rollNo": "21CS609",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.09,
        "activeBacklogs": 4,
        "attendance": 55.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_36():
    payload = {
        "rollNo": "21CS874",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.37,
        "activeBacklogs": 2,
        "attendance": 64.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_37():
    payload = {
        "rollNo": "21CS754",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.49,
        "activeBacklogs": 1,
        "attendance": 57.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_38():
    payload = {
        "rollNo": "21CS200",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.16,
        "activeBacklogs": 1,
        "attendance": 63.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_39():
    payload = {
        "rollNo": "21CS746",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.84,
        "activeBacklogs": 2,
        "attendance": 39.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_40():
    payload = {
        "rollNo": "21CS958",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.74,
        "activeBacklogs": 3,
        "attendance": 94.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_41():
    payload = {
        "rollNo": "21CS312",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.13,
        "activeBacklogs": 2,
        "attendance": 64.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_42():
    payload = {
        "rollNo": "21CS816",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.52,
        "activeBacklogs": 4,
        "attendance": 83.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_43():
    payload = {
        "rollNo": "21CS766",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.07,
        "activeBacklogs": 0,
        "attendance": 36.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_44():
    payload = {
        "rollNo": "21CS832",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.51,
        "activeBacklogs": 4,
        "attendance": 52.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_45():
    payload = {
        "rollNo": "21CS231",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.55,
        "activeBacklogs": 3,
        "attendance": 60.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_46():
    payload = {
        "rollNo": "21CS679",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.94,
        "activeBacklogs": 3,
        "attendance": 36.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_47():
    payload = {
        "rollNo": "21CS627",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.77,
        "activeBacklogs": 4,
        "attendance": 86.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_48():
    payload = {
        "rollNo": "21CS864",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.93,
        "activeBacklogs": 5,
        "attendance": 80.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_49():
    payload = {
        "rollNo": "21CS370",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.22,
        "activeBacklogs": 4,
        "attendance": 47.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_50():
    payload = {
        "rollNo": "21CS882",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.04,
        "activeBacklogs": 5,
        "attendance": 65.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_51():
    payload = {
        "rollNo": "21CS529",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.55,
        "activeBacklogs": 3,
        "attendance": 59.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_52():
    payload = {
        "rollNo": "21CS911",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.09,
        "activeBacklogs": 1,
        "attendance": 92.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_53():
    payload = {
        "rollNo": "21CS430",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.43,
        "activeBacklogs": 3,
        "attendance": 60.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_54():
    payload = {
        "rollNo": "21CS591",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.67,
        "activeBacklogs": 3,
        "attendance": 52.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_55():
    payload = {
        "rollNo": "21CS367",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.95,
        "activeBacklogs": 5,
        "attendance": 64.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_56():
    payload = {
        "rollNo": "21CS638",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.25,
        "activeBacklogs": 1,
        "attendance": 85.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_57():
    payload = {
        "rollNo": "21CS985",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.48,
        "activeBacklogs": 3,
        "attendance": 65.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_58():
    payload = {
        "rollNo": "21CS616",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.17,
        "activeBacklogs": 3,
        "attendance": 38.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_59():
    payload = {
        "rollNo": "21CS137",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.04,
        "activeBacklogs": 1,
        "attendance": 93.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_60():
    payload = {
        "rollNo": "21CS494",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.85,
        "activeBacklogs": 5,
        "attendance": 79.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_61():
    payload = {
        "rollNo": "21CS146",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.37,
        "activeBacklogs": 1,
        "attendance": 47.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_62():
    payload = {
        "rollNo": "21CS746",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.78,
        "activeBacklogs": 4,
        "attendance": 59.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_63():
    payload = {
        "rollNo": "21CS224",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.19,
        "activeBacklogs": 4,
        "attendance": 31.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_64():
    payload = {
        "rollNo": "21CS942",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.65,
        "activeBacklogs": 1,
        "attendance": 71.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_65():
    payload = {
        "rollNo": "21CS160",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.44,
        "activeBacklogs": 3,
        "attendance": 37.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_66():
    payload = {
        "rollNo": "21CS761",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.38,
        "activeBacklogs": 1,
        "attendance": 49.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_67():
    payload = {
        "rollNo": "21CS647",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.45,
        "activeBacklogs": 4,
        "attendance": 60.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_68():
    payload = {
        "rollNo": "21CS647",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.03,
        "activeBacklogs": 1,
        "attendance": 99.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_69():
    payload = {
        "rollNo": "21CS534",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.09,
        "activeBacklogs": 0,
        "attendance": 99.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_70():
    payload = {
        "rollNo": "21CS698",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.94,
        "activeBacklogs": 4,
        "attendance": 97.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_71():
    payload = {
        "rollNo": "21CS387",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.23,
        "activeBacklogs": 1,
        "attendance": 67.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_72():
    payload = {
        "rollNo": "21CS280",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.55,
        "activeBacklogs": 2,
        "attendance": 60.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_73():
    payload = {
        "rollNo": "21CS596",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.29,
        "activeBacklogs": 0,
        "attendance": 65.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_74():
    payload = {
        "rollNo": "21CS505",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.08,
        "activeBacklogs": 5,
        "attendance": 99.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_75():
    payload = {
        "rollNo": "21CS239",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.82,
        "activeBacklogs": 4,
        "attendance": 56.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_76():
    payload = {
        "rollNo": "21CS299",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.76,
        "activeBacklogs": 0,
        "attendance": 53.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_77():
    payload = {
        "rollNo": "21CS277",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.59,
        "activeBacklogs": 1,
        "attendance": 64.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_78():
    payload = {
        "rollNo": "21CS919",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.47,
        "activeBacklogs": 4,
        "attendance": 57.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_79():
    payload = {
        "rollNo": "21CS592",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.59,
        "activeBacklogs": 0,
        "attendance": 48.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_80():
    payload = {
        "rollNo": "21CS422",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.07,
        "activeBacklogs": 1,
        "attendance": 77.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_81():
    payload = {
        "rollNo": "21CS786",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.0,
        "activeBacklogs": 4,
        "attendance": 36.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_82():
    payload = {
        "rollNo": "21CS736",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.31,
        "activeBacklogs": 4,
        "attendance": 44.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_83():
    payload = {
        "rollNo": "21CS924",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.86,
        "activeBacklogs": 1,
        "attendance": 77.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_84():
    payload = {
        "rollNo": "21CS118",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.37,
        "activeBacklogs": 4,
        "attendance": 83.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_85():
    payload = {
        "rollNo": "21CS639",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.91,
        "activeBacklogs": 1,
        "attendance": 70.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_86():
    payload = {
        "rollNo": "21CS682",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.36,
        "activeBacklogs": 1,
        "attendance": 79.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_87():
    payload = {
        "rollNo": "21CS119",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.35,
        "activeBacklogs": 1,
        "attendance": 37.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_88():
    payload = {
        "rollNo": "21CS618",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.51,
        "activeBacklogs": 0,
        "attendance": 93.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_89():
    payload = {
        "rollNo": "21CS938",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.07,
        "activeBacklogs": 2,
        "attendance": 53.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_90():
    payload = {
        "rollNo": "21CS585",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.03,
        "activeBacklogs": 0,
        "attendance": 55.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_91():
    payload = {
        "rollNo": "21CS546",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.23,
        "activeBacklogs": 0,
        "attendance": 81.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_92():
    payload = {
        "rollNo": "21CS760",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.08,
        "activeBacklogs": 3,
        "attendance": 91.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_93():
    payload = {
        "rollNo": "21CS499",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.1,
        "activeBacklogs": 3,
        "attendance": 71.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_94():
    payload = {
        "rollNo": "21CS996",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.37,
        "activeBacklogs": 2,
        "attendance": 53.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_95():
    payload = {
        "rollNo": "21CS609",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.73,
        "activeBacklogs": 3,
        "attendance": 80.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_96():
    payload = {
        "rollNo": "21CS309",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.09,
        "activeBacklogs": 1,
        "attendance": 61.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_97():
    payload = {
        "rollNo": "21CS911",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.5,
        "activeBacklogs": 4,
        "attendance": 61.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_98():
    payload = {
        "rollNo": "21CS967",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.03,
        "activeBacklogs": 0,
        "attendance": 80.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_99():
    payload = {
        "rollNo": "21CS687",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.46,
        "activeBacklogs": 4,
        "attendance": 83.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_100():
    payload = {
        "rollNo": "21CS508",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.3,
        "activeBacklogs": 5,
        "attendance": 44.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_101():
    payload = {
        "rollNo": "21CS946",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.36,
        "activeBacklogs": 2,
        "attendance": 94.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_102():
    payload = {
        "rollNo": "21CS438",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.05,
        "activeBacklogs": 0,
        "attendance": 66.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_103():
    payload = {
        "rollNo": "21CS528",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.46,
        "activeBacklogs": 0,
        "attendance": 47.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_104():
    payload = {
        "rollNo": "21CS703",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.4,
        "activeBacklogs": 3,
        "attendance": 65.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_105():
    payload = {
        "rollNo": "21CS532",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.29,
        "activeBacklogs": 2,
        "attendance": 39.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_106():
    payload = {
        "rollNo": "21CS324",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.68,
        "activeBacklogs": 5,
        "attendance": 39.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_107():
    payload = {
        "rollNo": "21CS876",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.76,
        "activeBacklogs": 2,
        "attendance": 94.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_108():
    payload = {
        "rollNo": "21CS299",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.28,
        "activeBacklogs": 4,
        "attendance": 85.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_109():
    payload = {
        "rollNo": "21CS229",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.72,
        "activeBacklogs": 3,
        "attendance": 53.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_110():
    payload = {
        "rollNo": "21CS764",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.57,
        "activeBacklogs": 2,
        "attendance": 78.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_111():
    payload = {
        "rollNo": "21CS164",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.68,
        "activeBacklogs": 5,
        "attendance": 65.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_112():
    payload = {
        "rollNo": "21CS225",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.27,
        "activeBacklogs": 3,
        "attendance": 57.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_113():
    payload = {
        "rollNo": "21CS794",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.26,
        "activeBacklogs": 0,
        "attendance": 74.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_114():
    payload = {
        "rollNo": "21CS385",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.22,
        "activeBacklogs": 5,
        "attendance": 92.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_115():
    payload = {
        "rollNo": "21CS698",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.04,
        "activeBacklogs": 5,
        "attendance": 59.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_116():
    payload = {
        "rollNo": "21CS829",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.65,
        "activeBacklogs": 4,
        "attendance": 33.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_117():
    payload = {
        "rollNo": "21CS528",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.12,
        "activeBacklogs": 4,
        "attendance": 50.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_118():
    payload = {
        "rollNo": "21CS265",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.4,
        "activeBacklogs": 1,
        "attendance": 95.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_119():
    payload = {
        "rollNo": "21CS553",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.96,
        "activeBacklogs": 2,
        "attendance": 48.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_120():
    payload = {
        "rollNo": "21CS433",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.51,
        "activeBacklogs": 0,
        "attendance": 32.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_121():
    payload = {
        "rollNo": "21CS678",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.32,
        "activeBacklogs": 4,
        "attendance": 51.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_122():
    payload = {
        "rollNo": "21CS852",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.15,
        "activeBacklogs": 1,
        "attendance": 74.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_123():
    payload = {
        "rollNo": "21CS160",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.11,
        "activeBacklogs": 4,
        "attendance": 56.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_124():
    payload = {
        "rollNo": "21CS810",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.3,
        "activeBacklogs": 1,
        "attendance": 50.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_125():
    payload = {
        "rollNo": "21CS289",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.15,
        "activeBacklogs": 3,
        "attendance": 73.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_126():
    payload = {
        "rollNo": "21CS620",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.1,
        "activeBacklogs": 0,
        "attendance": 73.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_127():
    payload = {
        "rollNo": "21CS907",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.13,
        "activeBacklogs": 2,
        "attendance": 57.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_128():
    payload = {
        "rollNo": "21CS480",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.41,
        "activeBacklogs": 2,
        "attendance": 55.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_129():
    payload = {
        "rollNo": "21CS968",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.89,
        "activeBacklogs": 5,
        "attendance": 74.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_130():
    payload = {
        "rollNo": "21CS909",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.77,
        "activeBacklogs": 2,
        "attendance": 69.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_131():
    payload = {
        "rollNo": "21CS688",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.25,
        "activeBacklogs": 0,
        "attendance": 98.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_132():
    payload = {
        "rollNo": "21CS354",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.07,
        "activeBacklogs": 1,
        "attendance": 62.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_133():
    payload = {
        "rollNo": "21CS878",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.59,
        "activeBacklogs": 2,
        "attendance": 65.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_134():
    payload = {
        "rollNo": "21CS665",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.78,
        "activeBacklogs": 2,
        "attendance": 54.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_135():
    payload = {
        "rollNo": "21CS732",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.39,
        "activeBacklogs": 3,
        "attendance": 33.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_136():
    payload = {
        "rollNo": "21CS879",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.82,
        "activeBacklogs": 2,
        "attendance": 66.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_137():
    payload = {
        "rollNo": "21CS699",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.64,
        "activeBacklogs": 2,
        "attendance": 72.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_138():
    payload = {
        "rollNo": "21CS366",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.56,
        "activeBacklogs": 4,
        "attendance": 78.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_139():
    payload = {
        "rollNo": "21CS508",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.85,
        "activeBacklogs": 1,
        "attendance": 31.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_140():
    payload = {
        "rollNo": "21CS201",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.14,
        "activeBacklogs": 5,
        "attendance": 52.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_141():
    payload = {
        "rollNo": "21CS365",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.04,
        "activeBacklogs": 4,
        "attendance": 93.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_142():
    payload = {
        "rollNo": "21CS876",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.1,
        "activeBacklogs": 1,
        "attendance": 78.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_143():
    payload = {
        "rollNo": "21CS759",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.19,
        "activeBacklogs": 2,
        "attendance": 75.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_144():
    payload = {
        "rollNo": "21CS372",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.37,
        "activeBacklogs": 1,
        "attendance": 36.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_145():
    payload = {
        "rollNo": "21CS336",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.2,
        "activeBacklogs": 3,
        "attendance": 49.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_146():
    payload = {
        "rollNo": "21CS130",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.3,
        "activeBacklogs": 4,
        "attendance": 31.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_147():
    payload = {
        "rollNo": "21CS928",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.06,
        "activeBacklogs": 0,
        "attendance": 56.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_148():
    payload = {
        "rollNo": "21CS403",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.93,
        "activeBacklogs": 0,
        "attendance": 74.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_149():
    payload = {
        "rollNo": "21CS523",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.71,
        "activeBacklogs": 3,
        "attendance": 76.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_150():
    payload = {
        "rollNo": "21CS291",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.0,
        "activeBacklogs": 4,
        "attendance": 57.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_151():
    payload = {
        "rollNo": "21CS946",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.51,
        "activeBacklogs": 3,
        "attendance": 64.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_152():
    payload = {
        "rollNo": "21CS907",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.36,
        "activeBacklogs": 0,
        "attendance": 53.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_153():
    payload = {
        "rollNo": "21CS713",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.4,
        "activeBacklogs": 5,
        "attendance": 86.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_154():
    payload = {
        "rollNo": "21CS386",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.21,
        "activeBacklogs": 1,
        "attendance": 81.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_155():
    payload = {
        "rollNo": "21CS588",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.29,
        "activeBacklogs": 2,
        "attendance": 40.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_156():
    payload = {
        "rollNo": "21CS720",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.73,
        "activeBacklogs": 3,
        "attendance": 69.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_157():
    payload = {
        "rollNo": "21CS599",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.19,
        "activeBacklogs": 2,
        "attendance": 75.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_158():
    payload = {
        "rollNo": "21CS736",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.29,
        "activeBacklogs": 4,
        "attendance": 96.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_159():
    payload = {
        "rollNo": "21CS267",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.61,
        "activeBacklogs": 3,
        "attendance": 43.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_160():
    payload = {
        "rollNo": "21CS289",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.79,
        "activeBacklogs": 1,
        "attendance": 95.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_161():
    payload = {
        "rollNo": "21CS556",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.46,
        "activeBacklogs": 2,
        "attendance": 95.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_162():
    payload = {
        "rollNo": "21CS417",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.68,
        "activeBacklogs": 1,
        "attendance": 81.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_163():
    payload = {
        "rollNo": "21CS439",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.74,
        "activeBacklogs": 2,
        "attendance": 30.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_164():
    payload = {
        "rollNo": "21CS719",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.77,
        "activeBacklogs": 1,
        "attendance": 59.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_165():
    payload = {
        "rollNo": "21CS986",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.07,
        "activeBacklogs": 0,
        "attendance": 85.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_166():
    payload = {
        "rollNo": "21CS420",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.4,
        "activeBacklogs": 0,
        "attendance": 34.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_167():
    payload = {
        "rollNo": "21CS873",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.71,
        "activeBacklogs": 4,
        "attendance": 87.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_168():
    payload = {
        "rollNo": "21CS543",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.56,
        "activeBacklogs": 2,
        "attendance": 66.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_169():
    payload = {
        "rollNo": "21CS698",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.43,
        "activeBacklogs": 1,
        "attendance": 48.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_170():
    payload = {
        "rollNo": "21CS984",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.67,
        "activeBacklogs": 2,
        "attendance": 87.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_171():
    payload = {
        "rollNo": "21CS990",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.63,
        "activeBacklogs": 3,
        "attendance": 46.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_172():
    payload = {
        "rollNo": "21CS693",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.76,
        "activeBacklogs": 0,
        "attendance": 83.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_173():
    payload = {
        "rollNo": "21CS198",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.25,
        "activeBacklogs": 4,
        "attendance": 73.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_174():
    payload = {
        "rollNo": "21CS740",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.0,
        "activeBacklogs": 5,
        "attendance": 60.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_175():
    payload = {
        "rollNo": "21CS641",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.42,
        "activeBacklogs": 5,
        "attendance": 70.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_176():
    payload = {
        "rollNo": "21CS969",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.85,
        "activeBacklogs": 0,
        "attendance": 37.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_177():
    payload = {
        "rollNo": "21CS123",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.69,
        "activeBacklogs": 5,
        "attendance": 91.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_178():
    payload = {
        "rollNo": "21CS566",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.84,
        "activeBacklogs": 0,
        "attendance": 33.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_179():
    payload = {
        "rollNo": "21CS921",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.59,
        "activeBacklogs": 4,
        "attendance": 77.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_180():
    payload = {
        "rollNo": "21CS848",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.6,
        "activeBacklogs": 3,
        "attendance": 41.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_181():
    payload = {
        "rollNo": "21CS219",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.61,
        "activeBacklogs": 0,
        "attendance": 89.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_182():
    payload = {
        "rollNo": "21CS761",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.26,
        "activeBacklogs": 1,
        "attendance": 88.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_183():
    payload = {
        "rollNo": "21CS935",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.82,
        "activeBacklogs": 4,
        "attendance": 71.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_184():
    payload = {
        "rollNo": "21CS186",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.9,
        "activeBacklogs": 2,
        "attendance": 69.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_185():
    payload = {
        "rollNo": "21CS763",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.45,
        "activeBacklogs": 0,
        "attendance": 80.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_186():
    payload = {
        "rollNo": "21CS202",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.3,
        "activeBacklogs": 4,
        "attendance": 34.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_187():
    payload = {
        "rollNo": "21CS819",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.73,
        "activeBacklogs": 2,
        "attendance": 81.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_188():
    payload = {
        "rollNo": "21CS733",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.93,
        "activeBacklogs": 4,
        "attendance": 65.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_189():
    payload = {
        "rollNo": "21CS914",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.72,
        "activeBacklogs": 5,
        "attendance": 63.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_190():
    payload = {
        "rollNo": "21CS369",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.15,
        "activeBacklogs": 0,
        "attendance": 88.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_191():
    payload = {
        "rollNo": "21CS701",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.14,
        "activeBacklogs": 2,
        "attendance": 92.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_192():
    payload = {
        "rollNo": "21CS892",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.89,
        "activeBacklogs": 4,
        "attendance": 31.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_193():
    payload = {
        "rollNo": "21CS677",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.88,
        "activeBacklogs": 5,
        "attendance": 33.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_194():
    payload = {
        "rollNo": "21CS883",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.04,
        "activeBacklogs": 2,
        "attendance": 64.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_195():
    payload = {
        "rollNo": "21CS745",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.54,
        "activeBacklogs": 2,
        "attendance": 39.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_196():
    payload = {
        "rollNo": "21CS529",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.95,
        "activeBacklogs": 2,
        "attendance": 92.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_197():
    payload = {
        "rollNo": "21CS376",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.9,
        "activeBacklogs": 2,
        "attendance": 88.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_198():
    payload = {
        "rollNo": "21CS203",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.37,
        "activeBacklogs": 4,
        "attendance": 97.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_199():
    payload = {
        "rollNo": "21CS424",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.31,
        "activeBacklogs": 1,
        "attendance": 36.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_200():
    payload = {
        "rollNo": "21CS677",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.98,
        "activeBacklogs": 3,
        "attendance": 32.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_201():
    payload = {
        "rollNo": "21CS551",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.95,
        "activeBacklogs": 0,
        "attendance": 36.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_202():
    payload = {
        "rollNo": "21CS954",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.98,
        "activeBacklogs": 4,
        "attendance": 47.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_203():
    payload = {
        "rollNo": "21CS984",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.98,
        "activeBacklogs": 1,
        "attendance": 42.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_204():
    payload = {
        "rollNo": "21CS434",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.18,
        "activeBacklogs": 4,
        "attendance": 89.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_205():
    payload = {
        "rollNo": "21CS780",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.77,
        "activeBacklogs": 2,
        "attendance": 89.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_206():
    payload = {
        "rollNo": "21CS203",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.46,
        "activeBacklogs": 0,
        "attendance": 49.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_207():
    payload = {
        "rollNo": "21CS226",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.37,
        "activeBacklogs": 1,
        "attendance": 67.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_208():
    payload = {
        "rollNo": "21CS356",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.18,
        "activeBacklogs": 5,
        "attendance": 98.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_209():
    payload = {
        "rollNo": "21CS758",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.24,
        "activeBacklogs": 1,
        "attendance": 75.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_210():
    payload = {
        "rollNo": "21CS104",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.88,
        "activeBacklogs": 4,
        "attendance": 76.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_211():
    payload = {
        "rollNo": "21CS499",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.4,
        "activeBacklogs": 4,
        "attendance": 64.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_212():
    payload = {
        "rollNo": "21CS346",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.96,
        "activeBacklogs": 3,
        "attendance": 55.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_213():
    payload = {
        "rollNo": "21CS822",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.41,
        "activeBacklogs": 2,
        "attendance": 32.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_214():
    payload = {
        "rollNo": "21CS746",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.89,
        "activeBacklogs": 2,
        "attendance": 89.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_215():
    payload = {
        "rollNo": "21CS683",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.07,
        "activeBacklogs": 5,
        "attendance": 77.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_216():
    payload = {
        "rollNo": "21CS440",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.47,
        "activeBacklogs": 4,
        "attendance": 49.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_217():
    payload = {
        "rollNo": "21CS951",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.51,
        "activeBacklogs": 0,
        "attendance": 39.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_218():
    payload = {
        "rollNo": "21CS622",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.74,
        "activeBacklogs": 0,
        "attendance": 92.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_219():
    payload = {
        "rollNo": "21CS663",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.09,
        "activeBacklogs": 4,
        "attendance": 63.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_220():
    payload = {
        "rollNo": "21CS458",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.11,
        "activeBacklogs": 1,
        "attendance": 53.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_221():
    payload = {
        "rollNo": "21CS705",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.13,
        "activeBacklogs": 5,
        "attendance": 95.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_222():
    payload = {
        "rollNo": "21CS820",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.23,
        "activeBacklogs": 2,
        "attendance": 74.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_223():
    payload = {
        "rollNo": "21CS224",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.13,
        "activeBacklogs": 4,
        "attendance": 58.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_224():
    payload = {
        "rollNo": "21CS722",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.15,
        "activeBacklogs": 1,
        "attendance": 77.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_225():
    payload = {
        "rollNo": "21CS288",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.77,
        "activeBacklogs": 1,
        "attendance": 66.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_226():
    payload = {
        "rollNo": "21CS548",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.47,
        "activeBacklogs": 3,
        "attendance": 66.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_227():
    payload = {
        "rollNo": "21CS526",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.0,
        "activeBacklogs": 5,
        "attendance": 68.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_228():
    payload = {
        "rollNo": "21CS372",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.61,
        "activeBacklogs": 0,
        "attendance": 42.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_229():
    payload = {
        "rollNo": "21CS316",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.06,
        "activeBacklogs": 4,
        "attendance": 65.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_230():
    payload = {
        "rollNo": "21CS207",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.97,
        "activeBacklogs": 5,
        "attendance": 47.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_231():
    payload = {
        "rollNo": "21CS144",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.87,
        "activeBacklogs": 4,
        "attendance": 35.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_232():
    payload = {
        "rollNo": "21CS583",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.29,
        "activeBacklogs": 4,
        "attendance": 62.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_233():
    payload = {
        "rollNo": "21CS765",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.83,
        "activeBacklogs": 0,
        "attendance": 84.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_234():
    payload = {
        "rollNo": "21CS100",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.96,
        "activeBacklogs": 2,
        "attendance": 55.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_235():
    payload = {
        "rollNo": "21CS107",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.08,
        "activeBacklogs": 1,
        "attendance": 51.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_236():
    payload = {
        "rollNo": "21CS118",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.98,
        "activeBacklogs": 5,
        "attendance": 80.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_237():
    payload = {
        "rollNo": "21CS582",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.63,
        "activeBacklogs": 1,
        "attendance": 44.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_238():
    payload = {
        "rollNo": "21CS247",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.19,
        "activeBacklogs": 5,
        "attendance": 34.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_239():
    payload = {
        "rollNo": "21CS619",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.14,
        "activeBacklogs": 0,
        "attendance": 68.04
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_240():
    payload = {
        "rollNo": "21CS847",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.09,
        "activeBacklogs": 5,
        "attendance": 54.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_241():
    payload = {
        "rollNo": "21CS331",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.1,
        "activeBacklogs": 1,
        "attendance": 72.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_242():
    payload = {
        "rollNo": "21CS926",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.73,
        "activeBacklogs": 5,
        "attendance": 35.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_243():
    payload = {
        "rollNo": "21CS112",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.93,
        "activeBacklogs": 2,
        "attendance": 78.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_244():
    payload = {
        "rollNo": "21CS812",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.98,
        "activeBacklogs": 1,
        "attendance": 58.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_245():
    payload = {
        "rollNo": "21CS200",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.91,
        "activeBacklogs": 0,
        "attendance": 81.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_246():
    payload = {
        "rollNo": "21CS806",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.88,
        "activeBacklogs": 2,
        "attendance": 79.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_247():
    payload = {
        "rollNo": "21CS780",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.53,
        "activeBacklogs": 2,
        "attendance": 52.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_248():
    payload = {
        "rollNo": "21CS803",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.54,
        "activeBacklogs": 5,
        "attendance": 36.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_18_249():
    payload = {
        "rollNo": "21CS162",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.19,
        "activeBacklogs": 4,
        "attendance": 62.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

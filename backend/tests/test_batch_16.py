import pytest
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_prediction_case_16_0():
    payload = {
        "rollNo": "21CS427",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.08,
        "activeBacklogs": 1,
        "attendance": 72.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_1():
    payload = {
        "rollNo": "21CS504",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.62,
        "activeBacklogs": 0,
        "attendance": 87.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_2():
    payload = {
        "rollNo": "21CS659",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.27,
        "activeBacklogs": 5,
        "attendance": 54.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_3():
    payload = {
        "rollNo": "21CS582",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.83,
        "activeBacklogs": 2,
        "attendance": 78.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_4():
    payload = {
        "rollNo": "21CS115",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.45,
        "activeBacklogs": 0,
        "attendance": 51.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_5():
    payload = {
        "rollNo": "21CS366",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.97,
        "activeBacklogs": 4,
        "attendance": 54.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_6():
    payload = {
        "rollNo": "21CS375",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.96,
        "activeBacklogs": 1,
        "attendance": 61.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_7():
    payload = {
        "rollNo": "21CS932",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.37,
        "activeBacklogs": 3,
        "attendance": 31.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_8():
    payload = {
        "rollNo": "21CS609",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.28,
        "activeBacklogs": 0,
        "attendance": 93.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_9():
    payload = {
        "rollNo": "21CS333",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.3,
        "activeBacklogs": 5,
        "attendance": 49.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_10():
    payload = {
        "rollNo": "21CS473",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.66,
        "activeBacklogs": 4,
        "attendance": 38.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_11():
    payload = {
        "rollNo": "21CS536",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.18,
        "activeBacklogs": 2,
        "attendance": 34.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_12():
    payload = {
        "rollNo": "21CS205",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.79,
        "activeBacklogs": 3,
        "attendance": 49.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_13():
    payload = {
        "rollNo": "21CS153",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.2,
        "activeBacklogs": 2,
        "attendance": 70.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_14():
    payload = {
        "rollNo": "21CS313",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.12,
        "activeBacklogs": 5,
        "attendance": 99.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_15():
    payload = {
        "rollNo": "21CS766",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.02,
        "activeBacklogs": 1,
        "attendance": 57.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_16():
    payload = {
        "rollNo": "21CS538",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.0,
        "activeBacklogs": 5,
        "attendance": 42.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_17():
    payload = {
        "rollNo": "21CS104",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.82,
        "activeBacklogs": 2,
        "attendance": 85.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_18():
    payload = {
        "rollNo": "21CS130",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.64,
        "activeBacklogs": 0,
        "attendance": 66.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_19():
    payload = {
        "rollNo": "21CS145",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.41,
        "activeBacklogs": 2,
        "attendance": 52.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_20():
    payload = {
        "rollNo": "21CS899",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.95,
        "activeBacklogs": 2,
        "attendance": 47.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_21():
    payload = {
        "rollNo": "21CS826",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.49,
        "activeBacklogs": 2,
        "attendance": 71.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_22():
    payload = {
        "rollNo": "21CS942",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.28,
        "activeBacklogs": 5,
        "attendance": 96.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_23():
    payload = {
        "rollNo": "21CS988",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.07,
        "activeBacklogs": 1,
        "attendance": 92.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_24():
    payload = {
        "rollNo": "21CS421",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.77,
        "activeBacklogs": 3,
        "attendance": 69.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_25():
    payload = {
        "rollNo": "21CS876",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.39,
        "activeBacklogs": 5,
        "attendance": 76.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_26():
    payload = {
        "rollNo": "21CS666",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.64,
        "activeBacklogs": 4,
        "attendance": 57.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_27():
    payload = {
        "rollNo": "21CS603",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.08,
        "activeBacklogs": 1,
        "attendance": 49.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_28():
    payload = {
        "rollNo": "21CS306",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.92,
        "activeBacklogs": 4,
        "attendance": 62.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_29():
    payload = {
        "rollNo": "21CS216",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.07,
        "activeBacklogs": 3,
        "attendance": 75.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_30():
    payload = {
        "rollNo": "21CS404",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.55,
        "activeBacklogs": 0,
        "attendance": 31.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_31():
    payload = {
        "rollNo": "21CS306",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.75,
        "activeBacklogs": 5,
        "attendance": 88.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_32():
    payload = {
        "rollNo": "21CS455",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.32,
        "activeBacklogs": 5,
        "attendance": 55.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_33():
    payload = {
        "rollNo": "21CS504",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.15,
        "activeBacklogs": 1,
        "attendance": 39.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_34():
    payload = {
        "rollNo": "21CS298",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.06,
        "activeBacklogs": 1,
        "attendance": 87.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_35():
    payload = {
        "rollNo": "21CS877",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.17,
        "activeBacklogs": 2,
        "attendance": 85.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_36():
    payload = {
        "rollNo": "21CS705",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.32,
        "activeBacklogs": 4,
        "attendance": 40.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_37():
    payload = {
        "rollNo": "21CS766",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.65,
        "activeBacklogs": 5,
        "attendance": 42.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_38():
    payload = {
        "rollNo": "21CS831",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.16,
        "activeBacklogs": 4,
        "attendance": 50.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_39():
    payload = {
        "rollNo": "21CS808",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.86,
        "activeBacklogs": 3,
        "attendance": 66.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_40():
    payload = {
        "rollNo": "21CS564",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.08,
        "activeBacklogs": 3,
        "attendance": 82.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_41():
    payload = {
        "rollNo": "21CS860",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.79,
        "activeBacklogs": 0,
        "attendance": 35.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_42():
    payload = {
        "rollNo": "21CS685",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.15,
        "activeBacklogs": 4,
        "attendance": 61.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_43():
    payload = {
        "rollNo": "21CS382",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.1,
        "activeBacklogs": 4,
        "attendance": 43.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_44():
    payload = {
        "rollNo": "21CS867",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.99,
        "activeBacklogs": 0,
        "attendance": 77.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_45():
    payload = {
        "rollNo": "21CS268",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.11,
        "activeBacklogs": 3,
        "attendance": 64.04
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_46():
    payload = {
        "rollNo": "21CS663",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.82,
        "activeBacklogs": 2,
        "attendance": 80.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_47():
    payload = {
        "rollNo": "21CS753",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.4,
        "activeBacklogs": 1,
        "attendance": 65.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_48():
    payload = {
        "rollNo": "21CS737",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.58,
        "activeBacklogs": 4,
        "attendance": 53.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_49():
    payload = {
        "rollNo": "21CS649",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.6,
        "activeBacklogs": 4,
        "attendance": 82.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_50():
    payload = {
        "rollNo": "21CS770",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.14,
        "activeBacklogs": 5,
        "attendance": 70.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_51():
    payload = {
        "rollNo": "21CS584",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.57,
        "activeBacklogs": 2,
        "attendance": 83.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_52():
    payload = {
        "rollNo": "21CS491",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.03,
        "activeBacklogs": 3,
        "attendance": 74.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_53():
    payload = {
        "rollNo": "21CS152",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.92,
        "activeBacklogs": 0,
        "attendance": 30.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_54():
    payload = {
        "rollNo": "21CS775",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.35,
        "activeBacklogs": 3,
        "attendance": 60.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_55():
    payload = {
        "rollNo": "21CS561",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.03,
        "activeBacklogs": 3,
        "attendance": 77.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_56():
    payload = {
        "rollNo": "21CS376",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.76,
        "activeBacklogs": 5,
        "attendance": 42.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_57():
    payload = {
        "rollNo": "21CS241",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.22,
        "activeBacklogs": 5,
        "attendance": 57.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_58():
    payload = {
        "rollNo": "21CS307",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.04,
        "activeBacklogs": 1,
        "attendance": 40.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_59():
    payload = {
        "rollNo": "21CS370",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.31,
        "activeBacklogs": 2,
        "attendance": 94.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_60():
    payload = {
        "rollNo": "21CS266",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.26,
        "activeBacklogs": 4,
        "attendance": 86.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_61():
    payload = {
        "rollNo": "21CS129",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.65,
        "activeBacklogs": 5,
        "attendance": 48.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_62():
    payload = {
        "rollNo": "21CS803",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.2,
        "activeBacklogs": 3,
        "attendance": 42.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_63():
    payload = {
        "rollNo": "21CS778",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.97,
        "activeBacklogs": 1,
        "attendance": 44.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_64():
    payload = {
        "rollNo": "21CS753",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.18,
        "activeBacklogs": 0,
        "attendance": 78.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_65():
    payload = {
        "rollNo": "21CS282",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.93,
        "activeBacklogs": 0,
        "attendance": 36.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_66():
    payload = {
        "rollNo": "21CS209",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.36,
        "activeBacklogs": 1,
        "attendance": 40.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_67():
    payload = {
        "rollNo": "21CS112",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.48,
        "activeBacklogs": 4,
        "attendance": 91.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_68():
    payload = {
        "rollNo": "21CS833",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.68,
        "activeBacklogs": 5,
        "attendance": 37.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_69():
    payload = {
        "rollNo": "21CS327",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.22,
        "activeBacklogs": 2,
        "attendance": 99.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_70():
    payload = {
        "rollNo": "21CS643",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.92,
        "activeBacklogs": 2,
        "attendance": 86.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_71():
    payload = {
        "rollNo": "21CS246",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.15,
        "activeBacklogs": 4,
        "attendance": 62.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_72():
    payload = {
        "rollNo": "21CS137",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.25,
        "activeBacklogs": 3,
        "attendance": 88.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_73():
    payload = {
        "rollNo": "21CS497",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.03,
        "activeBacklogs": 3,
        "attendance": 44.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_74():
    payload = {
        "rollNo": "21CS194",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.65,
        "activeBacklogs": 0,
        "attendance": 76.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_75():
    payload = {
        "rollNo": "21CS568",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.49,
        "activeBacklogs": 5,
        "attendance": 55.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_76():
    payload = {
        "rollNo": "21CS406",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.36,
        "activeBacklogs": 3,
        "attendance": 56.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_77():
    payload = {
        "rollNo": "21CS869",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.76,
        "activeBacklogs": 2,
        "attendance": 58.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_78():
    payload = {
        "rollNo": "21CS470",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.93,
        "activeBacklogs": 1,
        "attendance": 86.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_79():
    payload = {
        "rollNo": "21CS858",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.63,
        "activeBacklogs": 4,
        "attendance": 58.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_80():
    payload = {
        "rollNo": "21CS291",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.94,
        "activeBacklogs": 3,
        "attendance": 36.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_81():
    payload = {
        "rollNo": "21CS204",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.93,
        "activeBacklogs": 3,
        "attendance": 91.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_82():
    payload = {
        "rollNo": "21CS365",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.39,
        "activeBacklogs": 3,
        "attendance": 95.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_83():
    payload = {
        "rollNo": "21CS355",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.14,
        "activeBacklogs": 5,
        "attendance": 97.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_84():
    payload = {
        "rollNo": "21CS906",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.83,
        "activeBacklogs": 0,
        "attendance": 65.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_85():
    payload = {
        "rollNo": "21CS989",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.56,
        "activeBacklogs": 5,
        "attendance": 59.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_86():
    payload = {
        "rollNo": "21CS537",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.59,
        "activeBacklogs": 4,
        "attendance": 41.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_87():
    payload = {
        "rollNo": "21CS269",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.34,
        "activeBacklogs": 4,
        "attendance": 49.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_88():
    payload = {
        "rollNo": "21CS414",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.04,
        "activeBacklogs": 5,
        "attendance": 88.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_89():
    payload = {
        "rollNo": "21CS107",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.49,
        "activeBacklogs": 3,
        "attendance": 91.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_90():
    payload = {
        "rollNo": "21CS733",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.74,
        "activeBacklogs": 3,
        "attendance": 55.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_91():
    payload = {
        "rollNo": "21CS473",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.8,
        "activeBacklogs": 2,
        "attendance": 40.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_92():
    payload = {
        "rollNo": "21CS260",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.52,
        "activeBacklogs": 4,
        "attendance": 33.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_93():
    payload = {
        "rollNo": "21CS127",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.48,
        "activeBacklogs": 4,
        "attendance": 66.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_94():
    payload = {
        "rollNo": "21CS378",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.79,
        "activeBacklogs": 3,
        "attendance": 64.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_95():
    payload = {
        "rollNo": "21CS481",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.35,
        "activeBacklogs": 4,
        "attendance": 74.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_96():
    payload = {
        "rollNo": "21CS491",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.77,
        "activeBacklogs": 3,
        "attendance": 52.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_97():
    payload = {
        "rollNo": "21CS399",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.9,
        "activeBacklogs": 4,
        "attendance": 81.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_98():
    payload = {
        "rollNo": "21CS719",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.8,
        "activeBacklogs": 0,
        "attendance": 79.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_99():
    payload = {
        "rollNo": "21CS222",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.1,
        "activeBacklogs": 2,
        "attendance": 69.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_100():
    payload = {
        "rollNo": "21CS398",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.17,
        "activeBacklogs": 2,
        "attendance": 30.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_101():
    payload = {
        "rollNo": "21CS297",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.86,
        "activeBacklogs": 4,
        "attendance": 81.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_102():
    payload = {
        "rollNo": "21CS353",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.5,
        "activeBacklogs": 2,
        "attendance": 32.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_103():
    payload = {
        "rollNo": "21CS719",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.56,
        "activeBacklogs": 5,
        "attendance": 51.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_104():
    payload = {
        "rollNo": "21CS522",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.33,
        "activeBacklogs": 2,
        "attendance": 55.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_105():
    payload = {
        "rollNo": "21CS307",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.49,
        "activeBacklogs": 0,
        "attendance": 92.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_106():
    payload = {
        "rollNo": "21CS187",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.41,
        "activeBacklogs": 2,
        "attendance": 43.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_107():
    payload = {
        "rollNo": "21CS405",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.78,
        "activeBacklogs": 5,
        "attendance": 98.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_108():
    payload = {
        "rollNo": "21CS875",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.6,
        "activeBacklogs": 3,
        "attendance": 38.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_109():
    payload = {
        "rollNo": "21CS663",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.01,
        "activeBacklogs": 0,
        "attendance": 37.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_110():
    payload = {
        "rollNo": "21CS118",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.27,
        "activeBacklogs": 4,
        "attendance": 59.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_111():
    payload = {
        "rollNo": "21CS862",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.21,
        "activeBacklogs": 2,
        "attendance": 32.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_112():
    payload = {
        "rollNo": "21CS982",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.4,
        "activeBacklogs": 5,
        "attendance": 68.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_113():
    payload = {
        "rollNo": "21CS139",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.77,
        "activeBacklogs": 3,
        "attendance": 52.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_114():
    payload = {
        "rollNo": "21CS628",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.1,
        "activeBacklogs": 5,
        "attendance": 52.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_115():
    payload = {
        "rollNo": "21CS815",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.85,
        "activeBacklogs": 3,
        "attendance": 52.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_116():
    payload = {
        "rollNo": "21CS936",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.0,
        "activeBacklogs": 5,
        "attendance": 65.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_117():
    payload = {
        "rollNo": "21CS486",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.76,
        "activeBacklogs": 5,
        "attendance": 52.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_118():
    payload = {
        "rollNo": "21CS178",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.16,
        "activeBacklogs": 3,
        "attendance": 86.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_119():
    payload = {
        "rollNo": "21CS261",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.45,
        "activeBacklogs": 2,
        "attendance": 47.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_120():
    payload = {
        "rollNo": "21CS720",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.77,
        "activeBacklogs": 3,
        "attendance": 61.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_121():
    payload = {
        "rollNo": "21CS362",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.84,
        "activeBacklogs": 2,
        "attendance": 80.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_122():
    payload = {
        "rollNo": "21CS544",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.13,
        "activeBacklogs": 2,
        "attendance": 39.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_123():
    payload = {
        "rollNo": "21CS664",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.94,
        "activeBacklogs": 0,
        "attendance": 52.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_124():
    payload = {
        "rollNo": "21CS183",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.95,
        "activeBacklogs": 2,
        "attendance": 77.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_125():
    payload = {
        "rollNo": "21CS780",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.62,
        "activeBacklogs": 2,
        "attendance": 93.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_126():
    payload = {
        "rollNo": "21CS833",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.72,
        "activeBacklogs": 2,
        "attendance": 70.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_127():
    payload = {
        "rollNo": "21CS722",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.64,
        "activeBacklogs": 4,
        "attendance": 68.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_128():
    payload = {
        "rollNo": "21CS473",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.66,
        "activeBacklogs": 1,
        "attendance": 42.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_129():
    payload = {
        "rollNo": "21CS492",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.96,
        "activeBacklogs": 3,
        "attendance": 33.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_130():
    payload = {
        "rollNo": "21CS965",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.44,
        "activeBacklogs": 0,
        "attendance": 44.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_131():
    payload = {
        "rollNo": "21CS481",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.3,
        "activeBacklogs": 5,
        "attendance": 91.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_132():
    payload = {
        "rollNo": "21CS867",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.61,
        "activeBacklogs": 0,
        "attendance": 83.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_133():
    payload = {
        "rollNo": "21CS272",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.05,
        "activeBacklogs": 3,
        "attendance": 97.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_134():
    payload = {
        "rollNo": "21CS182",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.32,
        "activeBacklogs": 0,
        "attendance": 75.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_135():
    payload = {
        "rollNo": "21CS208",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.85,
        "activeBacklogs": 2,
        "attendance": 64.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_136():
    payload = {
        "rollNo": "21CS640",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.75,
        "activeBacklogs": 5,
        "attendance": 47.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_137():
    payload = {
        "rollNo": "21CS835",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.95,
        "activeBacklogs": 4,
        "attendance": 49.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_138():
    payload = {
        "rollNo": "21CS878",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.99,
        "activeBacklogs": 0,
        "attendance": 70.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_139():
    payload = {
        "rollNo": "21CS894",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.79,
        "activeBacklogs": 2,
        "attendance": 30.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_140():
    payload = {
        "rollNo": "21CS426",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.76,
        "activeBacklogs": 0,
        "attendance": 36.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_141():
    payload = {
        "rollNo": "21CS842",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.52,
        "activeBacklogs": 5,
        "attendance": 50.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_142():
    payload = {
        "rollNo": "21CS783",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.62,
        "activeBacklogs": 5,
        "attendance": 65.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_143():
    payload = {
        "rollNo": "21CS386",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.59,
        "activeBacklogs": 3,
        "attendance": 70.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_144():
    payload = {
        "rollNo": "21CS876",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.94,
        "activeBacklogs": 1,
        "attendance": 76.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_145():
    payload = {
        "rollNo": "21CS671",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.71,
        "activeBacklogs": 5,
        "attendance": 33.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_146():
    payload = {
        "rollNo": "21CS202",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.81,
        "activeBacklogs": 3,
        "attendance": 71.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_147():
    payload = {
        "rollNo": "21CS575",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.34,
        "activeBacklogs": 4,
        "attendance": 36.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_148():
    payload = {
        "rollNo": "21CS473",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.42,
        "activeBacklogs": 5,
        "attendance": 31.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_149():
    payload = {
        "rollNo": "21CS478",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.19,
        "activeBacklogs": 5,
        "attendance": 31.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_150():
    payload = {
        "rollNo": "21CS492",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.84,
        "activeBacklogs": 4,
        "attendance": 73.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_151():
    payload = {
        "rollNo": "21CS572",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.04,
        "activeBacklogs": 1,
        "attendance": 66.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_152():
    payload = {
        "rollNo": "21CS745",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.38,
        "activeBacklogs": 1,
        "attendance": 96.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_153():
    payload = {
        "rollNo": "21CS461",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.69,
        "activeBacklogs": 4,
        "attendance": 50.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_154():
    payload = {
        "rollNo": "21CS277",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.44,
        "activeBacklogs": 5,
        "attendance": 90.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_155():
    payload = {
        "rollNo": "21CS287",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.61,
        "activeBacklogs": 3,
        "attendance": 91.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_156():
    payload = {
        "rollNo": "21CS999",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.25,
        "activeBacklogs": 2,
        "attendance": 94.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_157():
    payload = {
        "rollNo": "21CS151",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.31,
        "activeBacklogs": 5,
        "attendance": 98.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_158():
    payload = {
        "rollNo": "21CS604",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.11,
        "activeBacklogs": 1,
        "attendance": 66.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_159():
    payload = {
        "rollNo": "21CS435",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.96,
        "activeBacklogs": 4,
        "attendance": 65.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_160():
    payload = {
        "rollNo": "21CS926",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.8,
        "activeBacklogs": 1,
        "attendance": 61.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_161():
    payload = {
        "rollNo": "21CS886",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.47,
        "activeBacklogs": 4,
        "attendance": 75.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_162():
    payload = {
        "rollNo": "21CS979",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.97,
        "activeBacklogs": 1,
        "attendance": 70.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_163():
    payload = {
        "rollNo": "21CS242",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.16,
        "activeBacklogs": 0,
        "attendance": 96.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_164():
    payload = {
        "rollNo": "21CS591",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.9,
        "activeBacklogs": 1,
        "attendance": 94.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_165():
    payload = {
        "rollNo": "21CS120",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.9,
        "activeBacklogs": 1,
        "attendance": 98.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_166():
    payload = {
        "rollNo": "21CS907",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.61,
        "activeBacklogs": 5,
        "attendance": 89.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_167():
    payload = {
        "rollNo": "21CS361",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.27,
        "activeBacklogs": 3,
        "attendance": 43.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_168():
    payload = {
        "rollNo": "21CS921",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.98,
        "activeBacklogs": 4,
        "attendance": 96.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_169():
    payload = {
        "rollNo": "21CS213",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.37,
        "activeBacklogs": 5,
        "attendance": 48.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_170():
    payload = {
        "rollNo": "21CS317",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.89,
        "activeBacklogs": 5,
        "attendance": 95.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_171():
    payload = {
        "rollNo": "21CS773",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.63,
        "activeBacklogs": 5,
        "attendance": 49.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_172():
    payload = {
        "rollNo": "21CS987",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.06,
        "activeBacklogs": 2,
        "attendance": 55.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_173():
    payload = {
        "rollNo": "21CS630",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.37,
        "activeBacklogs": 1,
        "attendance": 60.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_174():
    payload = {
        "rollNo": "21CS630",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.37,
        "activeBacklogs": 2,
        "attendance": 77.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_175():
    payload = {
        "rollNo": "21CS401",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.34,
        "activeBacklogs": 4,
        "attendance": 65.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_176():
    payload = {
        "rollNo": "21CS935",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.13,
        "activeBacklogs": 4,
        "attendance": 47.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_177():
    payload = {
        "rollNo": "21CS858",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.05,
        "activeBacklogs": 3,
        "attendance": 84.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_178():
    payload = {
        "rollNo": "21CS774",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.97,
        "activeBacklogs": 1,
        "attendance": 49.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_179():
    payload = {
        "rollNo": "21CS570",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.35,
        "activeBacklogs": 1,
        "attendance": 93.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_180():
    payload = {
        "rollNo": "21CS126",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.07,
        "activeBacklogs": 2,
        "attendance": 96.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_181():
    payload = {
        "rollNo": "21CS498",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.12,
        "activeBacklogs": 1,
        "attendance": 97.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_182():
    payload = {
        "rollNo": "21CS705",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.3,
        "activeBacklogs": 4,
        "attendance": 78.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_183():
    payload = {
        "rollNo": "21CS752",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.88,
        "activeBacklogs": 3,
        "attendance": 97.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_184():
    payload = {
        "rollNo": "21CS377",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.38,
        "activeBacklogs": 0,
        "attendance": 76.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_185():
    payload = {
        "rollNo": "21CS135",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.81,
        "activeBacklogs": 1,
        "attendance": 46.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_186():
    payload = {
        "rollNo": "21CS803",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.27,
        "activeBacklogs": 5,
        "attendance": 35.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_187():
    payload = {
        "rollNo": "21CS261",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.69,
        "activeBacklogs": 5,
        "attendance": 34.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_188():
    payload = {
        "rollNo": "21CS231",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.39,
        "activeBacklogs": 4,
        "attendance": 56.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_189():
    payload = {
        "rollNo": "21CS609",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.44,
        "activeBacklogs": 4,
        "attendance": 67.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_190():
    payload = {
        "rollNo": "21CS633",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.06,
        "activeBacklogs": 1,
        "attendance": 33.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_191():
    payload = {
        "rollNo": "21CS338",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.18,
        "activeBacklogs": 1,
        "attendance": 65.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_192():
    payload = {
        "rollNo": "21CS229",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.31,
        "activeBacklogs": 4,
        "attendance": 98.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_193():
    payload = {
        "rollNo": "21CS810",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.45,
        "activeBacklogs": 4,
        "attendance": 81.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_194():
    payload = {
        "rollNo": "21CS877",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.73,
        "activeBacklogs": 0,
        "attendance": 61.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_195():
    payload = {
        "rollNo": "21CS363",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.77,
        "activeBacklogs": 0,
        "attendance": 42.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_196():
    payload = {
        "rollNo": "21CS517",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.89,
        "activeBacklogs": 2,
        "attendance": 93.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_197():
    payload = {
        "rollNo": "21CS568",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.62,
        "activeBacklogs": 5,
        "attendance": 95.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_198():
    payload = {
        "rollNo": "21CS256",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.17,
        "activeBacklogs": 0,
        "attendance": 93.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_199():
    payload = {
        "rollNo": "21CS634",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.56,
        "activeBacklogs": 4,
        "attendance": 61.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_200():
    payload = {
        "rollNo": "21CS492",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.13,
        "activeBacklogs": 4,
        "attendance": 58.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_201():
    payload = {
        "rollNo": "21CS672",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.35,
        "activeBacklogs": 5,
        "attendance": 33.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_202():
    payload = {
        "rollNo": "21CS966",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.82,
        "activeBacklogs": 4,
        "attendance": 35.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_203():
    payload = {
        "rollNo": "21CS130",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.67,
        "activeBacklogs": 4,
        "attendance": 84.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_204():
    payload = {
        "rollNo": "21CS878",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.87,
        "activeBacklogs": 2,
        "attendance": 58.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_205():
    payload = {
        "rollNo": "21CS935",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.4,
        "activeBacklogs": 2,
        "attendance": 61.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_206():
    payload = {
        "rollNo": "21CS916",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.67,
        "activeBacklogs": 2,
        "attendance": 78.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_207():
    payload = {
        "rollNo": "21CS444",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.14,
        "activeBacklogs": 2,
        "attendance": 79.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_208():
    payload = {
        "rollNo": "21CS282",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.67,
        "activeBacklogs": 1,
        "attendance": 83.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_209():
    payload = {
        "rollNo": "21CS799",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.87,
        "activeBacklogs": 3,
        "attendance": 47.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_210():
    payload = {
        "rollNo": "21CS105",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.44,
        "activeBacklogs": 2,
        "attendance": 36.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_211():
    payload = {
        "rollNo": "21CS488",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.78,
        "activeBacklogs": 2,
        "attendance": 65.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_212():
    payload = {
        "rollNo": "21CS187",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.55,
        "activeBacklogs": 1,
        "attendance": 68.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_213():
    payload = {
        "rollNo": "21CS351",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.83,
        "activeBacklogs": 4,
        "attendance": 90.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_214():
    payload = {
        "rollNo": "21CS655",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.42,
        "activeBacklogs": 2,
        "attendance": 69.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_215():
    payload = {
        "rollNo": "21CS309",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.17,
        "activeBacklogs": 5,
        "attendance": 83.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_216():
    payload = {
        "rollNo": "21CS535",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.87,
        "activeBacklogs": 1,
        "attendance": 79.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_217():
    payload = {
        "rollNo": "21CS644",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.1,
        "activeBacklogs": 0,
        "attendance": 94.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_218():
    payload = {
        "rollNo": "21CS222",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.82,
        "activeBacklogs": 4,
        "attendance": 98.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_219():
    payload = {
        "rollNo": "21CS479",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.44,
        "activeBacklogs": 2,
        "attendance": 83.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_220():
    payload = {
        "rollNo": "21CS386",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.25,
        "activeBacklogs": 2,
        "attendance": 72.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_221():
    payload = {
        "rollNo": "21CS828",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.58,
        "activeBacklogs": 5,
        "attendance": 88.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_222():
    payload = {
        "rollNo": "21CS608",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.96,
        "activeBacklogs": 3,
        "attendance": 45.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_223():
    payload = {
        "rollNo": "21CS962",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.81,
        "activeBacklogs": 2,
        "attendance": 46.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_224():
    payload = {
        "rollNo": "21CS974",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.18,
        "activeBacklogs": 3,
        "attendance": 32.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_225():
    payload = {
        "rollNo": "21CS637",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.55,
        "activeBacklogs": 0,
        "attendance": 94.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_226():
    payload = {
        "rollNo": "21CS348",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.2,
        "activeBacklogs": 2,
        "attendance": 78.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_227():
    payload = {
        "rollNo": "21CS114",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.64,
        "activeBacklogs": 5,
        "attendance": 71.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_228():
    payload = {
        "rollNo": "21CS814",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.52,
        "activeBacklogs": 1,
        "attendance": 64.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_229():
    payload = {
        "rollNo": "21CS919",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.01,
        "activeBacklogs": 5,
        "attendance": 96.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_230():
    payload = {
        "rollNo": "21CS316",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.06,
        "activeBacklogs": 3,
        "attendance": 88.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_231():
    payload = {
        "rollNo": "21CS243",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.61,
        "activeBacklogs": 4,
        "attendance": 95.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_232():
    payload = {
        "rollNo": "21CS772",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.25,
        "activeBacklogs": 4,
        "attendance": 33.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_233():
    payload = {
        "rollNo": "21CS564",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.21,
        "activeBacklogs": 3,
        "attendance": 96.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_234():
    payload = {
        "rollNo": "21CS365",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.01,
        "activeBacklogs": 0,
        "attendance": 34.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_235():
    payload = {
        "rollNo": "21CS338",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.06,
        "activeBacklogs": 0,
        "attendance": 96.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_236():
    payload = {
        "rollNo": "21CS988",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.67,
        "activeBacklogs": 3,
        "attendance": 32.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_237():
    payload = {
        "rollNo": "21CS179",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.81,
        "activeBacklogs": 0,
        "attendance": 35.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_238():
    payload = {
        "rollNo": "21CS190",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.86,
        "activeBacklogs": 5,
        "attendance": 74.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_239():
    payload = {
        "rollNo": "21CS915",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.05,
        "activeBacklogs": 3,
        "attendance": 60.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_240():
    payload = {
        "rollNo": "21CS931",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.77,
        "activeBacklogs": 2,
        "attendance": 90.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_241():
    payload = {
        "rollNo": "21CS359",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.68,
        "activeBacklogs": 3,
        "attendance": 44.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_242():
    payload = {
        "rollNo": "21CS747",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.15,
        "activeBacklogs": 3,
        "attendance": 73.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_243():
    payload = {
        "rollNo": "21CS125",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.02,
        "activeBacklogs": 3,
        "attendance": 88.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_244():
    payload = {
        "rollNo": "21CS392",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.95,
        "activeBacklogs": 1,
        "attendance": 96.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_245():
    payload = {
        "rollNo": "21CS383",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.64,
        "activeBacklogs": 0,
        "attendance": 82.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_246():
    payload = {
        "rollNo": "21CS435",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.48,
        "activeBacklogs": 2,
        "attendance": 60.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_247():
    payload = {
        "rollNo": "21CS580",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.15,
        "activeBacklogs": 4,
        "attendance": 90.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_248():
    payload = {
        "rollNo": "21CS253",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.43,
        "activeBacklogs": 4,
        "attendance": 75.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_16_249():
    payload = {
        "rollNo": "21CS659",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.73,
        "activeBacklogs": 2,
        "attendance": 96.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

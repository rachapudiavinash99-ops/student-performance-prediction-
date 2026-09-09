import pytest
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_prediction_case_1_0():
    payload = {
        "rollNo": "21CS247",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.64,
        "activeBacklogs": 1,
        "attendance": 80.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_1():
    payload = {
        "rollNo": "21CS720",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.12,
        "activeBacklogs": 2,
        "attendance": 67.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_2():
    payload = {
        "rollNo": "21CS785",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.94,
        "activeBacklogs": 5,
        "attendance": 58.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_3():
    payload = {
        "rollNo": "21CS531",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.71,
        "activeBacklogs": 5,
        "attendance": 74.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_4():
    payload = {
        "rollNo": "21CS529",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.69,
        "activeBacklogs": 2,
        "attendance": 42.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_5():
    payload = {
        "rollNo": "21CS645",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.62,
        "activeBacklogs": 0,
        "attendance": 70.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_6():
    payload = {
        "rollNo": "21CS181",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.02,
        "activeBacklogs": 3,
        "attendance": 67.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_7():
    payload = {
        "rollNo": "21CS853",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.76,
        "activeBacklogs": 4,
        "attendance": 70.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_8():
    payload = {
        "rollNo": "21CS856",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.37,
        "activeBacklogs": 2,
        "attendance": 35.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_9():
    payload = {
        "rollNo": "21CS478",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.1,
        "activeBacklogs": 2,
        "attendance": 35.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_10():
    payload = {
        "rollNo": "21CS436",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.21,
        "activeBacklogs": 2,
        "attendance": 92.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_11():
    payload = {
        "rollNo": "21CS815",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.05,
        "activeBacklogs": 2,
        "attendance": 36.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_12():
    payload = {
        "rollNo": "21CS440",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.25,
        "activeBacklogs": 3,
        "attendance": 73.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_13():
    payload = {
        "rollNo": "21CS566",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.97,
        "activeBacklogs": 5,
        "attendance": 91.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_14():
    payload = {
        "rollNo": "21CS617",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.9,
        "activeBacklogs": 5,
        "attendance": 59.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_15():
    payload = {
        "rollNo": "21CS500",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.81,
        "activeBacklogs": 1,
        "attendance": 52.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_16():
    payload = {
        "rollNo": "21CS958",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.18,
        "activeBacklogs": 2,
        "attendance": 73.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_17():
    payload = {
        "rollNo": "21CS323",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.1,
        "activeBacklogs": 0,
        "attendance": 88.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_18():
    payload = {
        "rollNo": "21CS599",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.82,
        "activeBacklogs": 4,
        "attendance": 69.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_19():
    payload = {
        "rollNo": "21CS301",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.28,
        "activeBacklogs": 0,
        "attendance": 32.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_20():
    payload = {
        "rollNo": "21CS698",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.06,
        "activeBacklogs": 3,
        "attendance": 31.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_21():
    payload = {
        "rollNo": "21CS272",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.26,
        "activeBacklogs": 4,
        "attendance": 86.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_22():
    payload = {
        "rollNo": "21CS605",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.29,
        "activeBacklogs": 0,
        "attendance": 33.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_23():
    payload = {
        "rollNo": "21CS748",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.43,
        "activeBacklogs": 4,
        "attendance": 34.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_24():
    payload = {
        "rollNo": "21CS272",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.97,
        "activeBacklogs": 4,
        "attendance": 72.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_25():
    payload = {
        "rollNo": "21CS917",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.07,
        "activeBacklogs": 3,
        "attendance": 60.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_26():
    payload = {
        "rollNo": "21CS713",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.56,
        "activeBacklogs": 2,
        "attendance": 89.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_27():
    payload = {
        "rollNo": "21CS437",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.34,
        "activeBacklogs": 2,
        "attendance": 43.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_28():
    payload = {
        "rollNo": "21CS314",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.19,
        "activeBacklogs": 3,
        "attendance": 86.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_29():
    payload = {
        "rollNo": "21CS194",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.81,
        "activeBacklogs": 5,
        "attendance": 62.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_30():
    payload = {
        "rollNo": "21CS995",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.52,
        "activeBacklogs": 4,
        "attendance": 48.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_31():
    payload = {
        "rollNo": "21CS292",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.98,
        "activeBacklogs": 3,
        "attendance": 39.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_32():
    payload = {
        "rollNo": "21CS596",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.15,
        "activeBacklogs": 3,
        "attendance": 35.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_33():
    payload = {
        "rollNo": "21CS491",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.35,
        "activeBacklogs": 3,
        "attendance": 47.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_34():
    payload = {
        "rollNo": "21CS527",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.27,
        "activeBacklogs": 1,
        "attendance": 30.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_35():
    payload = {
        "rollNo": "21CS580",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.79,
        "activeBacklogs": 5,
        "attendance": 52.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_36():
    payload = {
        "rollNo": "21CS489",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.61,
        "activeBacklogs": 0,
        "attendance": 37.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_37():
    payload = {
        "rollNo": "21CS324",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.15,
        "activeBacklogs": 3,
        "attendance": 78.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_38():
    payload = {
        "rollNo": "21CS811",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.83,
        "activeBacklogs": 2,
        "attendance": 36.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_39():
    payload = {
        "rollNo": "21CS654",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.82,
        "activeBacklogs": 2,
        "attendance": 56.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_40():
    payload = {
        "rollNo": "21CS904",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.97,
        "activeBacklogs": 5,
        "attendance": 30.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_41():
    payload = {
        "rollNo": "21CS793",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.12,
        "activeBacklogs": 2,
        "attendance": 70.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_42():
    payload = {
        "rollNo": "21CS169",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.15,
        "activeBacklogs": 0,
        "attendance": 31.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_43():
    payload = {
        "rollNo": "21CS336",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.28,
        "activeBacklogs": 2,
        "attendance": 53.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_44():
    payload = {
        "rollNo": "21CS488",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.0,
        "activeBacklogs": 5,
        "attendance": 64.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_45():
    payload = {
        "rollNo": "21CS401",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.15,
        "activeBacklogs": 4,
        "attendance": 87.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_46():
    payload = {
        "rollNo": "21CS667",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.77,
        "activeBacklogs": 2,
        "attendance": 79.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_47():
    payload = {
        "rollNo": "21CS624",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.91,
        "activeBacklogs": 4,
        "attendance": 43.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_48():
    payload = {
        "rollNo": "21CS823",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.45,
        "activeBacklogs": 1,
        "attendance": 33.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_49():
    payload = {
        "rollNo": "21CS142",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.95,
        "activeBacklogs": 5,
        "attendance": 50.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_50():
    payload = {
        "rollNo": "21CS765",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.16,
        "activeBacklogs": 3,
        "attendance": 98.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_51():
    payload = {
        "rollNo": "21CS694",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.07,
        "activeBacklogs": 4,
        "attendance": 90.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_52():
    payload = {
        "rollNo": "21CS820",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.67,
        "activeBacklogs": 2,
        "attendance": 84.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_53():
    payload = {
        "rollNo": "21CS414",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.94,
        "activeBacklogs": 5,
        "attendance": 33.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_54():
    payload = {
        "rollNo": "21CS196",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.06,
        "activeBacklogs": 4,
        "attendance": 47.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_55():
    payload = {
        "rollNo": "21CS580",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.71,
        "activeBacklogs": 1,
        "attendance": 94.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_56():
    payload = {
        "rollNo": "21CS317",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.99,
        "activeBacklogs": 1,
        "attendance": 92.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_57():
    payload = {
        "rollNo": "21CS378",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.57,
        "activeBacklogs": 1,
        "attendance": 74.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_58():
    payload = {
        "rollNo": "21CS754",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.88,
        "activeBacklogs": 4,
        "attendance": 39.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_59():
    payload = {
        "rollNo": "21CS339",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.49,
        "activeBacklogs": 4,
        "attendance": 90.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_60():
    payload = {
        "rollNo": "21CS587",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.71,
        "activeBacklogs": 5,
        "attendance": 48.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_61():
    payload = {
        "rollNo": "21CS265",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.94,
        "activeBacklogs": 1,
        "attendance": 91.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_62():
    payload = {
        "rollNo": "21CS770",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.58,
        "activeBacklogs": 1,
        "attendance": 74.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_63():
    payload = {
        "rollNo": "21CS653",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.25,
        "activeBacklogs": 3,
        "attendance": 43.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_64():
    payload = {
        "rollNo": "21CS474",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.06,
        "activeBacklogs": 1,
        "attendance": 61.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_65():
    payload = {
        "rollNo": "21CS312",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.91,
        "activeBacklogs": 3,
        "attendance": 59.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_66():
    payload = {
        "rollNo": "21CS246",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.25,
        "activeBacklogs": 0,
        "attendance": 95.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_67():
    payload = {
        "rollNo": "21CS285",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.6,
        "activeBacklogs": 4,
        "attendance": 51.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_68():
    payload = {
        "rollNo": "21CS411",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.31,
        "activeBacklogs": 0,
        "attendance": 57.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_69():
    payload = {
        "rollNo": "21CS684",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.28,
        "activeBacklogs": 3,
        "attendance": 46.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_70():
    payload = {
        "rollNo": "21CS830",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.18,
        "activeBacklogs": 1,
        "attendance": 98.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_71():
    payload = {
        "rollNo": "21CS424",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.92,
        "activeBacklogs": 0,
        "attendance": 31.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_72():
    payload = {
        "rollNo": "21CS107",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.48,
        "activeBacklogs": 0,
        "attendance": 76.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_73():
    payload = {
        "rollNo": "21CS280",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.15,
        "activeBacklogs": 0,
        "attendance": 32.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_74():
    payload = {
        "rollNo": "21CS271",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.19,
        "activeBacklogs": 1,
        "attendance": 36.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_75():
    payload = {
        "rollNo": "21CS680",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.89,
        "activeBacklogs": 1,
        "attendance": 97.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_76():
    payload = {
        "rollNo": "21CS927",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.84,
        "activeBacklogs": 2,
        "attendance": 97.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_77():
    payload = {
        "rollNo": "21CS763",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.42,
        "activeBacklogs": 0,
        "attendance": 86.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_78():
    payload = {
        "rollNo": "21CS349",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.92,
        "activeBacklogs": 3,
        "attendance": 67.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_79():
    payload = {
        "rollNo": "21CS627",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.92,
        "activeBacklogs": 5,
        "attendance": 60.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_80():
    payload = {
        "rollNo": "21CS574",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.58,
        "activeBacklogs": 1,
        "attendance": 84.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_81():
    payload = {
        "rollNo": "21CS769",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.28,
        "activeBacklogs": 2,
        "attendance": 79.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_82():
    payload = {
        "rollNo": "21CS164",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.92,
        "activeBacklogs": 1,
        "attendance": 47.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_83():
    payload = {
        "rollNo": "21CS981",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.2,
        "activeBacklogs": 5,
        "attendance": 98.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_84():
    payload = {
        "rollNo": "21CS784",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.76,
        "activeBacklogs": 1,
        "attendance": 62.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_85():
    payload = {
        "rollNo": "21CS371",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.21,
        "activeBacklogs": 0,
        "attendance": 31.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_86():
    payload = {
        "rollNo": "21CS437",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.82,
        "activeBacklogs": 4,
        "attendance": 95.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_87():
    payload = {
        "rollNo": "21CS124",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.75,
        "activeBacklogs": 4,
        "attendance": 55.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_88():
    payload = {
        "rollNo": "21CS830",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.33,
        "activeBacklogs": 0,
        "attendance": 39.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_89():
    payload = {
        "rollNo": "21CS624",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.59,
        "activeBacklogs": 5,
        "attendance": 30.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_90():
    payload = {
        "rollNo": "21CS859",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.3,
        "activeBacklogs": 3,
        "attendance": 52.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_91():
    payload = {
        "rollNo": "21CS398",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.51,
        "activeBacklogs": 4,
        "attendance": 30.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_92():
    payload = {
        "rollNo": "21CS864",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.88,
        "activeBacklogs": 1,
        "attendance": 59.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_93():
    payload = {
        "rollNo": "21CS457",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.98,
        "activeBacklogs": 3,
        "attendance": 59.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_94():
    payload = {
        "rollNo": "21CS823",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.63,
        "activeBacklogs": 1,
        "attendance": 78.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_95():
    payload = {
        "rollNo": "21CS127",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.04,
        "activeBacklogs": 1,
        "attendance": 34.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_96():
    payload = {
        "rollNo": "21CS362",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.8,
        "activeBacklogs": 0,
        "attendance": 43.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_97():
    payload = {
        "rollNo": "21CS205",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.6,
        "activeBacklogs": 4,
        "attendance": 80.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_98():
    payload = {
        "rollNo": "21CS466",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.14,
        "activeBacklogs": 0,
        "attendance": 65.04
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_99():
    payload = {
        "rollNo": "21CS945",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.29,
        "activeBacklogs": 0,
        "attendance": 93.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_100():
    payload = {
        "rollNo": "21CS174",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.14,
        "activeBacklogs": 0,
        "attendance": 59.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_101():
    payload = {
        "rollNo": "21CS323",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.19,
        "activeBacklogs": 1,
        "attendance": 88.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_102():
    payload = {
        "rollNo": "21CS404",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.1,
        "activeBacklogs": 2,
        "attendance": 76.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_103():
    payload = {
        "rollNo": "21CS124",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.51,
        "activeBacklogs": 4,
        "attendance": 96.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_104():
    payload = {
        "rollNo": "21CS897",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.85,
        "activeBacklogs": 3,
        "attendance": 86.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_105():
    payload = {
        "rollNo": "21CS743",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.03,
        "activeBacklogs": 2,
        "attendance": 83.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_106():
    payload = {
        "rollNo": "21CS564",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.88,
        "activeBacklogs": 4,
        "attendance": 36.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_107():
    payload = {
        "rollNo": "21CS345",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.11,
        "activeBacklogs": 4,
        "attendance": 69.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_108():
    payload = {
        "rollNo": "21CS736",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.08,
        "activeBacklogs": 0,
        "attendance": 58.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_109():
    payload = {
        "rollNo": "21CS568",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.16,
        "activeBacklogs": 3,
        "attendance": 32.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_110():
    payload = {
        "rollNo": "21CS692",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.32,
        "activeBacklogs": 1,
        "attendance": 62.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_111():
    payload = {
        "rollNo": "21CS493",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.96,
        "activeBacklogs": 4,
        "attendance": 56.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_112():
    payload = {
        "rollNo": "21CS716",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.69,
        "activeBacklogs": 5,
        "attendance": 39.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_113():
    payload = {
        "rollNo": "21CS831",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.34,
        "activeBacklogs": 4,
        "attendance": 99.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_114():
    payload = {
        "rollNo": "21CS815",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.36,
        "activeBacklogs": 2,
        "attendance": 62.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_115():
    payload = {
        "rollNo": "21CS265",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.49,
        "activeBacklogs": 3,
        "attendance": 76.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_116():
    payload = {
        "rollNo": "21CS501",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.53,
        "activeBacklogs": 1,
        "attendance": 50.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_117():
    payload = {
        "rollNo": "21CS155",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.07,
        "activeBacklogs": 3,
        "attendance": 32.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_118():
    payload = {
        "rollNo": "21CS165",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.45,
        "activeBacklogs": 3,
        "attendance": 84.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_119():
    payload = {
        "rollNo": "21CS921",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.29,
        "activeBacklogs": 0,
        "attendance": 35.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_120():
    payload = {
        "rollNo": "21CS199",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.16,
        "activeBacklogs": 4,
        "attendance": 50.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_121():
    payload = {
        "rollNo": "21CS612",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.59,
        "activeBacklogs": 1,
        "attendance": 42.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_122():
    payload = {
        "rollNo": "21CS949",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.35,
        "activeBacklogs": 5,
        "attendance": 66.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_123():
    payload = {
        "rollNo": "21CS519",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.35,
        "activeBacklogs": 1,
        "attendance": 42.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_124():
    payload = {
        "rollNo": "21CS686",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.01,
        "activeBacklogs": 5,
        "attendance": 62.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_125():
    payload = {
        "rollNo": "21CS633",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.99,
        "activeBacklogs": 5,
        "attendance": 77.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_126():
    payload = {
        "rollNo": "21CS646",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.87,
        "activeBacklogs": 2,
        "attendance": 70.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_127():
    payload = {
        "rollNo": "21CS795",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.18,
        "activeBacklogs": 4,
        "attendance": 92.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_128():
    payload = {
        "rollNo": "21CS459",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.29,
        "activeBacklogs": 1,
        "attendance": 33.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_129():
    payload = {
        "rollNo": "21CS138",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.26,
        "activeBacklogs": 2,
        "attendance": 60.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_130():
    payload = {
        "rollNo": "21CS291",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.68,
        "activeBacklogs": 2,
        "attendance": 80.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_131():
    payload = {
        "rollNo": "21CS474",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.7,
        "activeBacklogs": 0,
        "attendance": 60.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_132():
    payload = {
        "rollNo": "21CS312",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.69,
        "activeBacklogs": 0,
        "attendance": 36.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_133():
    payload = {
        "rollNo": "21CS855",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.73,
        "activeBacklogs": 2,
        "attendance": 47.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_134():
    payload = {
        "rollNo": "21CS673",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.86,
        "activeBacklogs": 2,
        "attendance": 67.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_135():
    payload = {
        "rollNo": "21CS513",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.75,
        "activeBacklogs": 2,
        "attendance": 67.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_136():
    payload = {
        "rollNo": "21CS509",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.22,
        "activeBacklogs": 3,
        "attendance": 76.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_137():
    payload = {
        "rollNo": "21CS279",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.45,
        "activeBacklogs": 1,
        "attendance": 59.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_138():
    payload = {
        "rollNo": "21CS819",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.11,
        "activeBacklogs": 1,
        "attendance": 95.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_139():
    payload = {
        "rollNo": "21CS309",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.0,
        "activeBacklogs": 0,
        "attendance": 64.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_140():
    payload = {
        "rollNo": "21CS698",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.18,
        "activeBacklogs": 1,
        "attendance": 37.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_141():
    payload = {
        "rollNo": "21CS140",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.8,
        "activeBacklogs": 0,
        "attendance": 69.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_142():
    payload = {
        "rollNo": "21CS353",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.4,
        "activeBacklogs": 2,
        "attendance": 62.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_143():
    payload = {
        "rollNo": "21CS642",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.42,
        "activeBacklogs": 4,
        "attendance": 68.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_144():
    payload = {
        "rollNo": "21CS799",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.31,
        "activeBacklogs": 4,
        "attendance": 33.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_145():
    payload = {
        "rollNo": "21CS137",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.43,
        "activeBacklogs": 5,
        "attendance": 80.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_146():
    payload = {
        "rollNo": "21CS798",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.75,
        "activeBacklogs": 1,
        "attendance": 50.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_147():
    payload = {
        "rollNo": "21CS492",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.05,
        "activeBacklogs": 3,
        "attendance": 72.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_148():
    payload = {
        "rollNo": "21CS463",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.54,
        "activeBacklogs": 4,
        "attendance": 85.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_149():
    payload = {
        "rollNo": "21CS411",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.86,
        "activeBacklogs": 2,
        "attendance": 41.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_150():
    payload = {
        "rollNo": "21CS699",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.26,
        "activeBacklogs": 4,
        "attendance": 50.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_151():
    payload = {
        "rollNo": "21CS751",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.84,
        "activeBacklogs": 0,
        "attendance": 43.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_152():
    payload = {
        "rollNo": "21CS807",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.38,
        "activeBacklogs": 4,
        "attendance": 39.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_153():
    payload = {
        "rollNo": "21CS409",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.92,
        "activeBacklogs": 3,
        "attendance": 32.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_154():
    payload = {
        "rollNo": "21CS154",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.28,
        "activeBacklogs": 5,
        "attendance": 50.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_155():
    payload = {
        "rollNo": "21CS821",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.45,
        "activeBacklogs": 5,
        "attendance": 33.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_156():
    payload = {
        "rollNo": "21CS578",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.79,
        "activeBacklogs": 4,
        "attendance": 86.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_157():
    payload = {
        "rollNo": "21CS467",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.46,
        "activeBacklogs": 3,
        "attendance": 80.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_158():
    payload = {
        "rollNo": "21CS961",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.05,
        "activeBacklogs": 5,
        "attendance": 53.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_159():
    payload = {
        "rollNo": "21CS605",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.34,
        "activeBacklogs": 5,
        "attendance": 52.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_160():
    payload = {
        "rollNo": "21CS903",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.58,
        "activeBacklogs": 5,
        "attendance": 43.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_161():
    payload = {
        "rollNo": "21CS377",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.3,
        "activeBacklogs": 4,
        "attendance": 70.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_162():
    payload = {
        "rollNo": "21CS424",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.55,
        "activeBacklogs": 4,
        "attendance": 64.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_163():
    payload = {
        "rollNo": "21CS239",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.41,
        "activeBacklogs": 5,
        "attendance": 69.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_164():
    payload = {
        "rollNo": "21CS491",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.39,
        "activeBacklogs": 2,
        "attendance": 74.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_165():
    payload = {
        "rollNo": "21CS820",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.24,
        "activeBacklogs": 3,
        "attendance": 66.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_166():
    payload = {
        "rollNo": "21CS828",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.35,
        "activeBacklogs": 4,
        "attendance": 99.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_167():
    payload = {
        "rollNo": "21CS613",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.14,
        "activeBacklogs": 0,
        "attendance": 40.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_168():
    payload = {
        "rollNo": "21CS516",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.21,
        "activeBacklogs": 1,
        "attendance": 77.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_169():
    payload = {
        "rollNo": "21CS418",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.37,
        "activeBacklogs": 2,
        "attendance": 61.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_170():
    payload = {
        "rollNo": "21CS759",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.63,
        "activeBacklogs": 5,
        "attendance": 79.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_171():
    payload = {
        "rollNo": "21CS360",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.14,
        "activeBacklogs": 3,
        "attendance": 35.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_172():
    payload = {
        "rollNo": "21CS696",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.82,
        "activeBacklogs": 0,
        "attendance": 63.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_173():
    payload = {
        "rollNo": "21CS447",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.18,
        "activeBacklogs": 4,
        "attendance": 56.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_174():
    payload = {
        "rollNo": "21CS783",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.67,
        "activeBacklogs": 1,
        "attendance": 80.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_175():
    payload = {
        "rollNo": "21CS257",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.38,
        "activeBacklogs": 5,
        "attendance": 72.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_176():
    payload = {
        "rollNo": "21CS219",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.44,
        "activeBacklogs": 2,
        "attendance": 59.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_177():
    payload = {
        "rollNo": "21CS399",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.53,
        "activeBacklogs": 1,
        "attendance": 60.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_178():
    payload = {
        "rollNo": "21CS277",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.09,
        "activeBacklogs": 1,
        "attendance": 92.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_179():
    payload = {
        "rollNo": "21CS409",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.73,
        "activeBacklogs": 0,
        "attendance": 91.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_180():
    payload = {
        "rollNo": "21CS232",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.61,
        "activeBacklogs": 0,
        "attendance": 91.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_181():
    payload = {
        "rollNo": "21CS208",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.77,
        "activeBacklogs": 2,
        "attendance": 43.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_182():
    payload = {
        "rollNo": "21CS468",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.23,
        "activeBacklogs": 3,
        "attendance": 94.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_183():
    payload = {
        "rollNo": "21CS716",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.49,
        "activeBacklogs": 1,
        "attendance": 33.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_184():
    payload = {
        "rollNo": "21CS327",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.26,
        "activeBacklogs": 5,
        "attendance": 56.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_185():
    payload = {
        "rollNo": "21CS651",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.58,
        "activeBacklogs": 0,
        "attendance": 83.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_186():
    payload = {
        "rollNo": "21CS899",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.36,
        "activeBacklogs": 3,
        "attendance": 40.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_187():
    payload = {
        "rollNo": "21CS279",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.24,
        "activeBacklogs": 3,
        "attendance": 75.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_188():
    payload = {
        "rollNo": "21CS782",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.15,
        "activeBacklogs": 2,
        "attendance": 79.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_189():
    payload = {
        "rollNo": "21CS247",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.53,
        "activeBacklogs": 1,
        "attendance": 91.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_190():
    payload = {
        "rollNo": "21CS594",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.64,
        "activeBacklogs": 5,
        "attendance": 93.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_191():
    payload = {
        "rollNo": "21CS840",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.54,
        "activeBacklogs": 2,
        "attendance": 98.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_192():
    payload = {
        "rollNo": "21CS516",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.28,
        "activeBacklogs": 5,
        "attendance": 53.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_193():
    payload = {
        "rollNo": "21CS835",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.21,
        "activeBacklogs": 5,
        "attendance": 76.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_194():
    payload = {
        "rollNo": "21CS491",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.35,
        "activeBacklogs": 2,
        "attendance": 94.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_195():
    payload = {
        "rollNo": "21CS475",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.75,
        "activeBacklogs": 1,
        "attendance": 78.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_196():
    payload = {
        "rollNo": "21CS912",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.5,
        "activeBacklogs": 5,
        "attendance": 65.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_197():
    payload = {
        "rollNo": "21CS341",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.92,
        "activeBacklogs": 2,
        "attendance": 96.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_198():
    payload = {
        "rollNo": "21CS359",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.48,
        "activeBacklogs": 4,
        "attendance": 99.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_199():
    payload = {
        "rollNo": "21CS882",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.44,
        "activeBacklogs": 3,
        "attendance": 36.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_200():
    payload = {
        "rollNo": "21CS602",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.93,
        "activeBacklogs": 1,
        "attendance": 99.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_201():
    payload = {
        "rollNo": "21CS867",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.34,
        "activeBacklogs": 5,
        "attendance": 62.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_202():
    payload = {
        "rollNo": "21CS194",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.81,
        "activeBacklogs": 2,
        "attendance": 74.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_203():
    payload = {
        "rollNo": "21CS545",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.29,
        "activeBacklogs": 5,
        "attendance": 32.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_204():
    payload = {
        "rollNo": "21CS334",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.19,
        "activeBacklogs": 2,
        "attendance": 99.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_205():
    payload = {
        "rollNo": "21CS323",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.03,
        "activeBacklogs": 3,
        "attendance": 91.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_206():
    payload = {
        "rollNo": "21CS227",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.18,
        "activeBacklogs": 2,
        "attendance": 54.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_207():
    payload = {
        "rollNo": "21CS187",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.29,
        "activeBacklogs": 4,
        "attendance": 33.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_208():
    payload = {
        "rollNo": "21CS969",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.62,
        "activeBacklogs": 1,
        "attendance": 85.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_209():
    payload = {
        "rollNo": "21CS878",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.32,
        "activeBacklogs": 1,
        "attendance": 50.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_210():
    payload = {
        "rollNo": "21CS494",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.09,
        "activeBacklogs": 5,
        "attendance": 57.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_211():
    payload = {
        "rollNo": "21CS557",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.56,
        "activeBacklogs": 2,
        "attendance": 59.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_212():
    payload = {
        "rollNo": "21CS156",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.07,
        "activeBacklogs": 2,
        "attendance": 82.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_213():
    payload = {
        "rollNo": "21CS398",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.84,
        "activeBacklogs": 5,
        "attendance": 51.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_214():
    payload = {
        "rollNo": "21CS609",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.18,
        "activeBacklogs": 4,
        "attendance": 87.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_215():
    payload = {
        "rollNo": "21CS892",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.74,
        "activeBacklogs": 5,
        "attendance": 88.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_216():
    payload = {
        "rollNo": "21CS911",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.43,
        "activeBacklogs": 0,
        "attendance": 85.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_217():
    payload = {
        "rollNo": "21CS592",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.48,
        "activeBacklogs": 2,
        "attendance": 83.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_218():
    payload = {
        "rollNo": "21CS411",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.42,
        "activeBacklogs": 0,
        "attendance": 59.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_219():
    payload = {
        "rollNo": "21CS726",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.06,
        "activeBacklogs": 2,
        "attendance": 85.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_220():
    payload = {
        "rollNo": "21CS206",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.7,
        "activeBacklogs": 4,
        "attendance": 30.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_221():
    payload = {
        "rollNo": "21CS187",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.53,
        "activeBacklogs": 1,
        "attendance": 96.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_222():
    payload = {
        "rollNo": "21CS578",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.61,
        "activeBacklogs": 2,
        "attendance": 31.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_223():
    payload = {
        "rollNo": "21CS570",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.05,
        "activeBacklogs": 1,
        "attendance": 88.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_224():
    payload = {
        "rollNo": "21CS771",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.92,
        "activeBacklogs": 0,
        "attendance": 50.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_225():
    payload = {
        "rollNo": "21CS229",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.36,
        "activeBacklogs": 1,
        "attendance": 79.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_226():
    payload = {
        "rollNo": "21CS874",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.31,
        "activeBacklogs": 1,
        "attendance": 35.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_227():
    payload = {
        "rollNo": "21CS977",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.83,
        "activeBacklogs": 1,
        "attendance": 50.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_228():
    payload = {
        "rollNo": "21CS868",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.35,
        "activeBacklogs": 1,
        "attendance": 83.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_229():
    payload = {
        "rollNo": "21CS733",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.32,
        "activeBacklogs": 2,
        "attendance": 95.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_230():
    payload = {
        "rollNo": "21CS381",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.68,
        "activeBacklogs": 1,
        "attendance": 90.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_231():
    payload = {
        "rollNo": "21CS479",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.96,
        "activeBacklogs": 3,
        "attendance": 47.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_232():
    payload = {
        "rollNo": "21CS701",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.99,
        "activeBacklogs": 3,
        "attendance": 72.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_233():
    payload = {
        "rollNo": "21CS101",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.46,
        "activeBacklogs": 2,
        "attendance": 79.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_234():
    payload = {
        "rollNo": "21CS286",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.5,
        "activeBacklogs": 1,
        "attendance": 31.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_235():
    payload = {
        "rollNo": "21CS731",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.76,
        "activeBacklogs": 0,
        "attendance": 38.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_236():
    payload = {
        "rollNo": "21CS981",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.89,
        "activeBacklogs": 3,
        "attendance": 66.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_237():
    payload = {
        "rollNo": "21CS847",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.28,
        "activeBacklogs": 3,
        "attendance": 38.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_238():
    payload = {
        "rollNo": "21CS938",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.08,
        "activeBacklogs": 3,
        "attendance": 67.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_239():
    payload = {
        "rollNo": "21CS146",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.99,
        "activeBacklogs": 3,
        "attendance": 63.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_240():
    payload = {
        "rollNo": "21CS869",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.57,
        "activeBacklogs": 2,
        "attendance": 41.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_241():
    payload = {
        "rollNo": "21CS242",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.55,
        "activeBacklogs": 4,
        "attendance": 47.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_242():
    payload = {
        "rollNo": "21CS974",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.88,
        "activeBacklogs": 0,
        "attendance": 37.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_243():
    payload = {
        "rollNo": "21CS417",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.15,
        "activeBacklogs": 0,
        "attendance": 51.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_244():
    payload = {
        "rollNo": "21CS965",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.52,
        "activeBacklogs": 2,
        "attendance": 59.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_245():
    payload = {
        "rollNo": "21CS670",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.45,
        "activeBacklogs": 2,
        "attendance": 63.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_246():
    payload = {
        "rollNo": "21CS926",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.65,
        "activeBacklogs": 2,
        "attendance": 80.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_247():
    payload = {
        "rollNo": "21CS302",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.39,
        "activeBacklogs": 4,
        "attendance": 48.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_248():
    payload = {
        "rollNo": "21CS581",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.54,
        "activeBacklogs": 3,
        "attendance": 67.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_1_249():
    payload = {
        "rollNo": "21CS686",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.25,
        "activeBacklogs": 3,
        "attendance": 56.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

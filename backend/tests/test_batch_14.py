import pytest
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_prediction_case_14_0():
    payload = {
        "rollNo": "21CS853",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.67,
        "activeBacklogs": 5,
        "attendance": 44.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_1():
    payload = {
        "rollNo": "21CS886",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.75,
        "activeBacklogs": 2,
        "attendance": 30.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_2():
    payload = {
        "rollNo": "21CS935",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.85,
        "activeBacklogs": 5,
        "attendance": 76.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_3():
    payload = {
        "rollNo": "21CS452",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.12,
        "activeBacklogs": 5,
        "attendance": 58.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_4():
    payload = {
        "rollNo": "21CS557",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.04,
        "activeBacklogs": 1,
        "attendance": 63.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_5():
    payload = {
        "rollNo": "21CS915",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.83,
        "activeBacklogs": 5,
        "attendance": 74.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_6():
    payload = {
        "rollNo": "21CS798",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.93,
        "activeBacklogs": 5,
        "attendance": 92.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_7():
    payload = {
        "rollNo": "21CS411",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.47,
        "activeBacklogs": 5,
        "attendance": 86.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_8():
    payload = {
        "rollNo": "21CS254",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.99,
        "activeBacklogs": 2,
        "attendance": 96.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_9():
    payload = {
        "rollNo": "21CS448",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.44,
        "activeBacklogs": 4,
        "attendance": 86.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_10():
    payload = {
        "rollNo": "21CS558",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.13,
        "activeBacklogs": 2,
        "attendance": 92.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_11():
    payload = {
        "rollNo": "21CS406",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.46,
        "activeBacklogs": 1,
        "attendance": 75.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_12():
    payload = {
        "rollNo": "21CS866",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.57,
        "activeBacklogs": 3,
        "attendance": 67.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_13():
    payload = {
        "rollNo": "21CS693",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.73,
        "activeBacklogs": 1,
        "attendance": 42.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_14():
    payload = {
        "rollNo": "21CS276",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.03,
        "activeBacklogs": 3,
        "attendance": 79.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_15():
    payload = {
        "rollNo": "21CS729",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.17,
        "activeBacklogs": 4,
        "attendance": 30.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_16():
    payload = {
        "rollNo": "21CS284",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.89,
        "activeBacklogs": 0,
        "attendance": 54.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_17():
    payload = {
        "rollNo": "21CS188",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.89,
        "activeBacklogs": 4,
        "attendance": 64.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_18():
    payload = {
        "rollNo": "21CS952",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.84,
        "activeBacklogs": 2,
        "attendance": 52.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_19():
    payload = {
        "rollNo": "21CS477",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.22,
        "activeBacklogs": 1,
        "attendance": 89.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_20():
    payload = {
        "rollNo": "21CS734",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.9,
        "activeBacklogs": 1,
        "attendance": 58.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_21():
    payload = {
        "rollNo": "21CS777",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.93,
        "activeBacklogs": 5,
        "attendance": 79.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_22():
    payload = {
        "rollNo": "21CS917",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.38,
        "activeBacklogs": 5,
        "attendance": 95.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_23():
    payload = {
        "rollNo": "21CS111",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.96,
        "activeBacklogs": 5,
        "attendance": 52.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_24():
    payload = {
        "rollNo": "21CS227",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.78,
        "activeBacklogs": 2,
        "attendance": 97.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_25():
    payload = {
        "rollNo": "21CS592",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.06,
        "activeBacklogs": 2,
        "attendance": 30.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_26():
    payload = {
        "rollNo": "21CS675",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.25,
        "activeBacklogs": 3,
        "attendance": 95.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_27():
    payload = {
        "rollNo": "21CS132",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.85,
        "activeBacklogs": 4,
        "attendance": 95.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_28():
    payload = {
        "rollNo": "21CS504",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.74,
        "activeBacklogs": 1,
        "attendance": 37.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_29():
    payload = {
        "rollNo": "21CS100",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.86,
        "activeBacklogs": 5,
        "attendance": 80.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_30():
    payload = {
        "rollNo": "21CS840",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.63,
        "activeBacklogs": 4,
        "attendance": 70.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_31():
    payload = {
        "rollNo": "21CS759",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.94,
        "activeBacklogs": 3,
        "attendance": 70.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_32():
    payload = {
        "rollNo": "21CS946",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.09,
        "activeBacklogs": 2,
        "attendance": 72.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_33():
    payload = {
        "rollNo": "21CS804",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.98,
        "activeBacklogs": 2,
        "attendance": 77.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_34():
    payload = {
        "rollNo": "21CS995",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.89,
        "activeBacklogs": 2,
        "attendance": 60.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_35():
    payload = {
        "rollNo": "21CS312",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.21,
        "activeBacklogs": 0,
        "attendance": 80.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_36():
    payload = {
        "rollNo": "21CS841",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.6,
        "activeBacklogs": 3,
        "attendance": 95.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_37():
    payload = {
        "rollNo": "21CS554",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.62,
        "activeBacklogs": 1,
        "attendance": 59.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_38():
    payload = {
        "rollNo": "21CS901",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.03,
        "activeBacklogs": 4,
        "attendance": 66.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_39():
    payload = {
        "rollNo": "21CS347",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.79,
        "activeBacklogs": 0,
        "attendance": 65.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_40():
    payload = {
        "rollNo": "21CS487",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.64,
        "activeBacklogs": 3,
        "attendance": 43.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_41():
    payload = {
        "rollNo": "21CS441",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.96,
        "activeBacklogs": 1,
        "attendance": 35.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_42():
    payload = {
        "rollNo": "21CS156",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.71,
        "activeBacklogs": 5,
        "attendance": 91.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_43():
    payload = {
        "rollNo": "21CS772",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.14,
        "activeBacklogs": 0,
        "attendance": 34.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_44():
    payload = {
        "rollNo": "21CS825",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.99,
        "activeBacklogs": 4,
        "attendance": 82.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_45():
    payload = {
        "rollNo": "21CS599",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.07,
        "activeBacklogs": 3,
        "attendance": 57.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_46():
    payload = {
        "rollNo": "21CS694",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.48,
        "activeBacklogs": 5,
        "attendance": 71.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_47():
    payload = {
        "rollNo": "21CS523",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.55,
        "activeBacklogs": 1,
        "attendance": 49.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_48():
    payload = {
        "rollNo": "21CS755",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.13,
        "activeBacklogs": 4,
        "attendance": 85.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_49():
    payload = {
        "rollNo": "21CS536",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.79,
        "activeBacklogs": 1,
        "attendance": 52.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_50():
    payload = {
        "rollNo": "21CS550",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.67,
        "activeBacklogs": 2,
        "attendance": 61.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_51():
    payload = {
        "rollNo": "21CS202",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.01,
        "activeBacklogs": 1,
        "attendance": 52.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_52():
    payload = {
        "rollNo": "21CS148",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.25,
        "activeBacklogs": 2,
        "attendance": 99.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_53():
    payload = {
        "rollNo": "21CS959",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.07,
        "activeBacklogs": 5,
        "attendance": 40.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_54():
    payload = {
        "rollNo": "21CS932",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.87,
        "activeBacklogs": 2,
        "attendance": 38.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_55():
    payload = {
        "rollNo": "21CS230",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.6,
        "activeBacklogs": 4,
        "attendance": 37.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_56():
    payload = {
        "rollNo": "21CS653",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.48,
        "activeBacklogs": 0,
        "attendance": 61.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_57():
    payload = {
        "rollNo": "21CS614",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.65,
        "activeBacklogs": 3,
        "attendance": 54.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_58():
    payload = {
        "rollNo": "21CS861",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.64,
        "activeBacklogs": 5,
        "attendance": 60.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_59():
    payload = {
        "rollNo": "21CS258",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.49,
        "activeBacklogs": 4,
        "attendance": 32.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_60():
    payload = {
        "rollNo": "21CS947",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.51,
        "activeBacklogs": 5,
        "attendance": 84.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_61():
    payload = {
        "rollNo": "21CS944",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.51,
        "activeBacklogs": 1,
        "attendance": 84.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_62():
    payload = {
        "rollNo": "21CS541",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.84,
        "activeBacklogs": 3,
        "attendance": 72.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_63():
    payload = {
        "rollNo": "21CS912",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.56,
        "activeBacklogs": 1,
        "attendance": 71.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_64():
    payload = {
        "rollNo": "21CS744",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.82,
        "activeBacklogs": 5,
        "attendance": 35.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_65():
    payload = {
        "rollNo": "21CS353",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.73,
        "activeBacklogs": 3,
        "attendance": 33.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_66():
    payload = {
        "rollNo": "21CS375",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.91,
        "activeBacklogs": 3,
        "attendance": 94.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_67():
    payload = {
        "rollNo": "21CS739",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.78,
        "activeBacklogs": 4,
        "attendance": 49.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_68():
    payload = {
        "rollNo": "21CS116",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.5,
        "activeBacklogs": 1,
        "attendance": 87.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_69():
    payload = {
        "rollNo": "21CS674",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.5,
        "activeBacklogs": 5,
        "attendance": 67.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_70():
    payload = {
        "rollNo": "21CS174",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.38,
        "activeBacklogs": 4,
        "attendance": 89.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_71():
    payload = {
        "rollNo": "21CS177",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.36,
        "activeBacklogs": 2,
        "attendance": 80.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_72():
    payload = {
        "rollNo": "21CS733",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.49,
        "activeBacklogs": 3,
        "attendance": 57.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_73():
    payload = {
        "rollNo": "21CS728",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.73,
        "activeBacklogs": 1,
        "attendance": 61.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_74():
    payload = {
        "rollNo": "21CS656",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.81,
        "activeBacklogs": 3,
        "attendance": 34.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_75():
    payload = {
        "rollNo": "21CS358",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.13,
        "activeBacklogs": 2,
        "attendance": 38.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_76():
    payload = {
        "rollNo": "21CS527",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.15,
        "activeBacklogs": 4,
        "attendance": 44.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_77():
    payload = {
        "rollNo": "21CS497",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.3,
        "activeBacklogs": 2,
        "attendance": 34.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_78():
    payload = {
        "rollNo": "21CS777",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.92,
        "activeBacklogs": 2,
        "attendance": 50.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_79():
    payload = {
        "rollNo": "21CS441",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.68,
        "activeBacklogs": 3,
        "attendance": 54.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_80():
    payload = {
        "rollNo": "21CS366",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.11,
        "activeBacklogs": 2,
        "attendance": 41.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_81():
    payload = {
        "rollNo": "21CS334",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.17,
        "activeBacklogs": 0,
        "attendance": 52.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_82():
    payload = {
        "rollNo": "21CS892",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.25,
        "activeBacklogs": 2,
        "attendance": 98.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_83():
    payload = {
        "rollNo": "21CS255",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.7,
        "activeBacklogs": 0,
        "attendance": 42.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_84():
    payload = {
        "rollNo": "21CS850",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.67,
        "activeBacklogs": 5,
        "attendance": 36.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_85():
    payload = {
        "rollNo": "21CS536",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.85,
        "activeBacklogs": 4,
        "attendance": 75.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_86():
    payload = {
        "rollNo": "21CS770",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.16,
        "activeBacklogs": 1,
        "attendance": 67.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_87():
    payload = {
        "rollNo": "21CS792",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.27,
        "activeBacklogs": 1,
        "attendance": 32.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_88():
    payload = {
        "rollNo": "21CS423",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.21,
        "activeBacklogs": 4,
        "attendance": 38.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_89():
    payload = {
        "rollNo": "21CS573",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.66,
        "activeBacklogs": 0,
        "attendance": 73.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_90():
    payload = {
        "rollNo": "21CS574",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.02,
        "activeBacklogs": 2,
        "attendance": 40.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_91():
    payload = {
        "rollNo": "21CS968",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.75,
        "activeBacklogs": 1,
        "attendance": 49.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_92():
    payload = {
        "rollNo": "21CS460",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.0,
        "activeBacklogs": 0,
        "attendance": 69.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_93():
    payload = {
        "rollNo": "21CS781",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.17,
        "activeBacklogs": 3,
        "attendance": 51.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_94():
    payload = {
        "rollNo": "21CS477",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.91,
        "activeBacklogs": 4,
        "attendance": 54.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_95():
    payload = {
        "rollNo": "21CS373",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.9,
        "activeBacklogs": 3,
        "attendance": 30.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_96():
    payload = {
        "rollNo": "21CS520",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.83,
        "activeBacklogs": 4,
        "attendance": 47.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_97():
    payload = {
        "rollNo": "21CS332",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.9,
        "activeBacklogs": 2,
        "attendance": 37.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_98():
    payload = {
        "rollNo": "21CS802",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.33,
        "activeBacklogs": 4,
        "attendance": 95.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_99():
    payload = {
        "rollNo": "21CS753",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.86,
        "activeBacklogs": 5,
        "attendance": 93.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_100():
    payload = {
        "rollNo": "21CS709",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.23,
        "activeBacklogs": 3,
        "attendance": 49.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_101():
    payload = {
        "rollNo": "21CS313",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.01,
        "activeBacklogs": 4,
        "attendance": 58.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_102():
    payload = {
        "rollNo": "21CS157",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.23,
        "activeBacklogs": 2,
        "attendance": 64.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_103():
    payload = {
        "rollNo": "21CS639",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.75,
        "activeBacklogs": 3,
        "attendance": 66.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_104():
    payload = {
        "rollNo": "21CS118",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.61,
        "activeBacklogs": 4,
        "attendance": 70.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_105():
    payload = {
        "rollNo": "21CS281",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.0,
        "activeBacklogs": 2,
        "attendance": 40.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_106():
    payload = {
        "rollNo": "21CS770",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.47,
        "activeBacklogs": 0,
        "attendance": 41.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_107():
    payload = {
        "rollNo": "21CS366",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.7,
        "activeBacklogs": 3,
        "attendance": 78.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_108():
    payload = {
        "rollNo": "21CS439",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.35,
        "activeBacklogs": 1,
        "attendance": 70.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_109():
    payload = {
        "rollNo": "21CS288",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.79,
        "activeBacklogs": 3,
        "attendance": 33.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_110():
    payload = {
        "rollNo": "21CS482",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.46,
        "activeBacklogs": 1,
        "attendance": 41.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_111():
    payload = {
        "rollNo": "21CS456",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.58,
        "activeBacklogs": 2,
        "attendance": 44.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_112():
    payload = {
        "rollNo": "21CS761",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.62,
        "activeBacklogs": 3,
        "attendance": 72.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_113():
    payload = {
        "rollNo": "21CS182",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.64,
        "activeBacklogs": 4,
        "attendance": 55.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_114():
    payload = {
        "rollNo": "21CS578",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.6,
        "activeBacklogs": 0,
        "attendance": 70.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_115():
    payload = {
        "rollNo": "21CS831",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.07,
        "activeBacklogs": 1,
        "attendance": 34.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_116():
    payload = {
        "rollNo": "21CS837",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.08,
        "activeBacklogs": 4,
        "attendance": 64.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_117():
    payload = {
        "rollNo": "21CS851",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.96,
        "activeBacklogs": 0,
        "attendance": 72.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_118():
    payload = {
        "rollNo": "21CS134",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.09,
        "activeBacklogs": 3,
        "attendance": 59.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_119():
    payload = {
        "rollNo": "21CS826",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.01,
        "activeBacklogs": 1,
        "attendance": 30.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_120():
    payload = {
        "rollNo": "21CS930",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.58,
        "activeBacklogs": 0,
        "attendance": 95.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_121():
    payload = {
        "rollNo": "21CS762",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.79,
        "activeBacklogs": 0,
        "attendance": 75.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_122():
    payload = {
        "rollNo": "21CS183",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.65,
        "activeBacklogs": 3,
        "attendance": 35.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_123():
    payload = {
        "rollNo": "21CS659",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.42,
        "activeBacklogs": 1,
        "attendance": 85.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_124():
    payload = {
        "rollNo": "21CS116",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.93,
        "activeBacklogs": 2,
        "attendance": 30.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_125():
    payload = {
        "rollNo": "21CS343",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.01,
        "activeBacklogs": 4,
        "attendance": 35.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_126():
    payload = {
        "rollNo": "21CS979",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.04,
        "activeBacklogs": 1,
        "attendance": 97.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_127():
    payload = {
        "rollNo": "21CS702",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.56,
        "activeBacklogs": 1,
        "attendance": 75.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_128():
    payload = {
        "rollNo": "21CS315",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.2,
        "activeBacklogs": 0,
        "attendance": 87.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_129():
    payload = {
        "rollNo": "21CS245",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.84,
        "activeBacklogs": 5,
        "attendance": 50.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_130():
    payload = {
        "rollNo": "21CS372",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.79,
        "activeBacklogs": 2,
        "attendance": 65.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_131():
    payload = {
        "rollNo": "21CS310",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.48,
        "activeBacklogs": 3,
        "attendance": 78.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_132():
    payload = {
        "rollNo": "21CS998",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.62,
        "activeBacklogs": 1,
        "attendance": 64.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_133():
    payload = {
        "rollNo": "21CS626",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.35,
        "activeBacklogs": 3,
        "attendance": 84.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_134():
    payload = {
        "rollNo": "21CS551",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.71,
        "activeBacklogs": 4,
        "attendance": 52.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_135():
    payload = {
        "rollNo": "21CS541",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.01,
        "activeBacklogs": 2,
        "attendance": 68.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_136():
    payload = {
        "rollNo": "21CS465",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.16,
        "activeBacklogs": 3,
        "attendance": 37.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_137():
    payload = {
        "rollNo": "21CS923",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.59,
        "activeBacklogs": 0,
        "attendance": 79.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_138():
    payload = {
        "rollNo": "21CS226",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.89,
        "activeBacklogs": 1,
        "attendance": 76.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_139():
    payload = {
        "rollNo": "21CS317",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.5,
        "activeBacklogs": 1,
        "attendance": 80.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_140():
    payload = {
        "rollNo": "21CS704",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.63,
        "activeBacklogs": 4,
        "attendance": 38.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_141():
    payload = {
        "rollNo": "21CS888",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.11,
        "activeBacklogs": 4,
        "attendance": 59.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_142():
    payload = {
        "rollNo": "21CS784",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.89,
        "activeBacklogs": 3,
        "attendance": 45.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_143():
    payload = {
        "rollNo": "21CS543",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.29,
        "activeBacklogs": 1,
        "attendance": 51.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_144():
    payload = {
        "rollNo": "21CS951",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.5,
        "activeBacklogs": 0,
        "attendance": 78.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_145():
    payload = {
        "rollNo": "21CS478",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.92,
        "activeBacklogs": 0,
        "attendance": 57.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_146():
    payload = {
        "rollNo": "21CS577",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.07,
        "activeBacklogs": 1,
        "attendance": 38.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_147():
    payload = {
        "rollNo": "21CS764",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.73,
        "activeBacklogs": 3,
        "attendance": 47.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_148():
    payload = {
        "rollNo": "21CS903",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.11,
        "activeBacklogs": 3,
        "attendance": 75.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_149():
    payload = {
        "rollNo": "21CS817",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.24,
        "activeBacklogs": 5,
        "attendance": 39.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_150():
    payload = {
        "rollNo": "21CS562",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.18,
        "activeBacklogs": 1,
        "attendance": 45.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_151():
    payload = {
        "rollNo": "21CS666",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.76,
        "activeBacklogs": 5,
        "attendance": 55.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_152():
    payload = {
        "rollNo": "21CS157",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.38,
        "activeBacklogs": 3,
        "attendance": 89.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_153():
    payload = {
        "rollNo": "21CS405",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.84,
        "activeBacklogs": 5,
        "attendance": 92.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_154():
    payload = {
        "rollNo": "21CS862",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.36,
        "activeBacklogs": 5,
        "attendance": 80.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_155():
    payload = {
        "rollNo": "21CS209",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.09,
        "activeBacklogs": 1,
        "attendance": 51.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_156():
    payload = {
        "rollNo": "21CS389",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.12,
        "activeBacklogs": 3,
        "attendance": 69.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_157():
    payload = {
        "rollNo": "21CS977",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.97,
        "activeBacklogs": 0,
        "attendance": 90.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_158():
    payload = {
        "rollNo": "21CS313",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.98,
        "activeBacklogs": 1,
        "attendance": 39.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_159():
    payload = {
        "rollNo": "21CS990",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.25,
        "activeBacklogs": 2,
        "attendance": 99.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_160():
    payload = {
        "rollNo": "21CS868",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.72,
        "activeBacklogs": 1,
        "attendance": 90.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_161():
    payload = {
        "rollNo": "21CS319",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.91,
        "activeBacklogs": 1,
        "attendance": 83.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_162():
    payload = {
        "rollNo": "21CS956",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.37,
        "activeBacklogs": 2,
        "attendance": 35.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_163():
    payload = {
        "rollNo": "21CS704",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.01,
        "activeBacklogs": 4,
        "attendance": 57.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_164():
    payload = {
        "rollNo": "21CS426",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.6,
        "activeBacklogs": 3,
        "attendance": 76.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_165():
    payload = {
        "rollNo": "21CS579",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.0,
        "activeBacklogs": 3,
        "attendance": 39.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_166():
    payload = {
        "rollNo": "21CS782",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.67,
        "activeBacklogs": 0,
        "attendance": 48.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_167():
    payload = {
        "rollNo": "21CS298",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.13,
        "activeBacklogs": 0,
        "attendance": 66.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_168():
    payload = {
        "rollNo": "21CS109",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.77,
        "activeBacklogs": 0,
        "attendance": 73.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_169():
    payload = {
        "rollNo": "21CS396",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.33,
        "activeBacklogs": 0,
        "attendance": 80.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_170():
    payload = {
        "rollNo": "21CS855",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.62,
        "activeBacklogs": 1,
        "attendance": 36.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_171():
    payload = {
        "rollNo": "21CS228",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.05,
        "activeBacklogs": 1,
        "attendance": 30.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_172():
    payload = {
        "rollNo": "21CS387",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.37,
        "activeBacklogs": 0,
        "attendance": 64.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_173():
    payload = {
        "rollNo": "21CS369",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.14,
        "activeBacklogs": 0,
        "attendance": 85.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_174():
    payload = {
        "rollNo": "21CS160",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.21,
        "activeBacklogs": 5,
        "attendance": 33.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_175():
    payload = {
        "rollNo": "21CS960",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.8,
        "activeBacklogs": 0,
        "attendance": 31.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_176():
    payload = {
        "rollNo": "21CS424",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.7,
        "activeBacklogs": 3,
        "attendance": 71.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_177():
    payload = {
        "rollNo": "21CS891",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.31,
        "activeBacklogs": 1,
        "attendance": 47.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_178():
    payload = {
        "rollNo": "21CS835",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.48,
        "activeBacklogs": 1,
        "attendance": 34.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_179():
    payload = {
        "rollNo": "21CS414",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.04,
        "activeBacklogs": 3,
        "attendance": 67.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_180():
    payload = {
        "rollNo": "21CS790",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.52,
        "activeBacklogs": 3,
        "attendance": 64.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_181():
    payload = {
        "rollNo": "21CS278",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.66,
        "activeBacklogs": 2,
        "attendance": 32.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_182():
    payload = {
        "rollNo": "21CS888",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.26,
        "activeBacklogs": 4,
        "attendance": 60.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_183():
    payload = {
        "rollNo": "21CS172",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.91,
        "activeBacklogs": 4,
        "attendance": 58.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_184():
    payload = {
        "rollNo": "21CS101",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.99,
        "activeBacklogs": 3,
        "attendance": 34.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_185():
    payload = {
        "rollNo": "21CS487",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.65,
        "activeBacklogs": 1,
        "attendance": 91.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_186():
    payload = {
        "rollNo": "21CS891",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.38,
        "activeBacklogs": 0,
        "attendance": 71.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_187():
    payload = {
        "rollNo": "21CS757",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.26,
        "activeBacklogs": 3,
        "attendance": 62.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_188():
    payload = {
        "rollNo": "21CS625",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.46,
        "activeBacklogs": 2,
        "attendance": 57.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_189():
    payload = {
        "rollNo": "21CS662",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.99,
        "activeBacklogs": 4,
        "attendance": 81.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_190():
    payload = {
        "rollNo": "21CS627",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.48,
        "activeBacklogs": 1,
        "attendance": 47.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_191():
    payload = {
        "rollNo": "21CS366",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.38,
        "activeBacklogs": 4,
        "attendance": 72.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_192():
    payload = {
        "rollNo": "21CS646",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.06,
        "activeBacklogs": 1,
        "attendance": 98.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_193():
    payload = {
        "rollNo": "21CS135",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.59,
        "activeBacklogs": 1,
        "attendance": 78.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_194():
    payload = {
        "rollNo": "21CS974",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.5,
        "activeBacklogs": 1,
        "attendance": 84.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_195():
    payload = {
        "rollNo": "21CS176",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.84,
        "activeBacklogs": 5,
        "attendance": 56.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_196():
    payload = {
        "rollNo": "21CS913",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.83,
        "activeBacklogs": 4,
        "attendance": 32.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_197():
    payload = {
        "rollNo": "21CS242",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.7,
        "activeBacklogs": 3,
        "attendance": 96.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_198():
    payload = {
        "rollNo": "21CS799",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.96,
        "activeBacklogs": 3,
        "attendance": 94.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_199():
    payload = {
        "rollNo": "21CS639",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.31,
        "activeBacklogs": 3,
        "attendance": 81.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_200():
    payload = {
        "rollNo": "21CS337",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.94,
        "activeBacklogs": 0,
        "attendance": 49.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_201():
    payload = {
        "rollNo": "21CS814",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.5,
        "activeBacklogs": 0,
        "attendance": 42.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_202():
    payload = {
        "rollNo": "21CS407",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.24,
        "activeBacklogs": 5,
        "attendance": 89.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_203():
    payload = {
        "rollNo": "21CS758",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.46,
        "activeBacklogs": 2,
        "attendance": 82.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_204():
    payload = {
        "rollNo": "21CS464",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.94,
        "activeBacklogs": 3,
        "attendance": 66.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_205():
    payload = {
        "rollNo": "21CS611",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.43,
        "activeBacklogs": 1,
        "attendance": 48.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_206():
    payload = {
        "rollNo": "21CS231",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.06,
        "activeBacklogs": 1,
        "attendance": 31.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_207():
    payload = {
        "rollNo": "21CS913",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.9,
        "activeBacklogs": 0,
        "attendance": 41.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_208():
    payload = {
        "rollNo": "21CS408",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.46,
        "activeBacklogs": 1,
        "attendance": 79.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_209():
    payload = {
        "rollNo": "21CS561",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.94,
        "activeBacklogs": 1,
        "attendance": 44.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_210():
    payload = {
        "rollNo": "21CS162",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.0,
        "activeBacklogs": 1,
        "attendance": 77.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_211():
    payload = {
        "rollNo": "21CS297",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.15,
        "activeBacklogs": 1,
        "attendance": 79.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_212():
    payload = {
        "rollNo": "21CS303",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.8,
        "activeBacklogs": 3,
        "attendance": 88.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_213():
    payload = {
        "rollNo": "21CS160",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.49,
        "activeBacklogs": 0,
        "attendance": 81.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_214():
    payload = {
        "rollNo": "21CS858",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.69,
        "activeBacklogs": 2,
        "attendance": 91.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_215():
    payload = {
        "rollNo": "21CS878",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.52,
        "activeBacklogs": 3,
        "attendance": 66.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_216():
    payload = {
        "rollNo": "21CS645",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.61,
        "activeBacklogs": 2,
        "attendance": 34.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_217():
    payload = {
        "rollNo": "21CS410",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.88,
        "activeBacklogs": 4,
        "attendance": 68.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_218():
    payload = {
        "rollNo": "21CS677",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.6,
        "activeBacklogs": 3,
        "attendance": 37.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_219():
    payload = {
        "rollNo": "21CS101",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.86,
        "activeBacklogs": 4,
        "attendance": 68.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_220():
    payload = {
        "rollNo": "21CS394",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.57,
        "activeBacklogs": 1,
        "attendance": 99.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_221():
    payload = {
        "rollNo": "21CS575",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.19,
        "activeBacklogs": 4,
        "attendance": 63.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_222():
    payload = {
        "rollNo": "21CS835",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.41,
        "activeBacklogs": 5,
        "attendance": 86.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_223():
    payload = {
        "rollNo": "21CS748",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.15,
        "activeBacklogs": 1,
        "attendance": 91.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_224():
    payload = {
        "rollNo": "21CS436",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.41,
        "activeBacklogs": 5,
        "attendance": 81.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_225():
    payload = {
        "rollNo": "21CS618",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.79,
        "activeBacklogs": 3,
        "attendance": 75.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_226():
    payload = {
        "rollNo": "21CS162",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.57,
        "activeBacklogs": 1,
        "attendance": 87.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_227():
    payload = {
        "rollNo": "21CS305",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.07,
        "activeBacklogs": 0,
        "attendance": 35.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_228():
    payload = {
        "rollNo": "21CS955",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.54,
        "activeBacklogs": 5,
        "attendance": 38.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_229():
    payload = {
        "rollNo": "21CS124",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.68,
        "activeBacklogs": 0,
        "attendance": 97.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_230():
    payload = {
        "rollNo": "21CS606",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.1,
        "activeBacklogs": 2,
        "attendance": 70.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_231():
    payload = {
        "rollNo": "21CS513",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.79,
        "activeBacklogs": 2,
        "attendance": 81.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_232():
    payload = {
        "rollNo": "21CS915",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.57,
        "activeBacklogs": 0,
        "attendance": 43.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_233():
    payload = {
        "rollNo": "21CS643",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.18,
        "activeBacklogs": 0,
        "attendance": 81.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_234():
    payload = {
        "rollNo": "21CS153",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.7,
        "activeBacklogs": 2,
        "attendance": 48.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_235():
    payload = {
        "rollNo": "21CS670",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.81,
        "activeBacklogs": 4,
        "attendance": 55.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_236():
    payload = {
        "rollNo": "21CS580",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.63,
        "activeBacklogs": 5,
        "attendance": 38.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_237():
    payload = {
        "rollNo": "21CS554",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.68,
        "activeBacklogs": 5,
        "attendance": 64.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_238():
    payload = {
        "rollNo": "21CS919",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.87,
        "activeBacklogs": 1,
        "attendance": 96.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_239():
    payload = {
        "rollNo": "21CS360",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.88,
        "activeBacklogs": 1,
        "attendance": 86.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_240():
    payload = {
        "rollNo": "21CS506",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.15,
        "activeBacklogs": 2,
        "attendance": 78.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_241():
    payload = {
        "rollNo": "21CS694",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.22,
        "activeBacklogs": 1,
        "attendance": 89.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_242():
    payload = {
        "rollNo": "21CS175",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.32,
        "activeBacklogs": 1,
        "attendance": 76.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_243():
    payload = {
        "rollNo": "21CS477",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.89,
        "activeBacklogs": 4,
        "attendance": 39.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_244():
    payload = {
        "rollNo": "21CS247",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.55,
        "activeBacklogs": 1,
        "attendance": 75.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_245():
    payload = {
        "rollNo": "21CS861",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.58,
        "activeBacklogs": 2,
        "attendance": 86.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_246():
    payload = {
        "rollNo": "21CS216",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.78,
        "activeBacklogs": 1,
        "attendance": 61.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_247():
    payload = {
        "rollNo": "21CS593",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.12,
        "activeBacklogs": 2,
        "attendance": 76.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_248():
    payload = {
        "rollNo": "21CS492",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.05,
        "activeBacklogs": 4,
        "attendance": 60.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_14_249():
    payload = {
        "rollNo": "21CS565",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.86,
        "activeBacklogs": 2,
        "attendance": 52.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

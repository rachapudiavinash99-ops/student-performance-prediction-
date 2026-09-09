import pytest
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_prediction_case_15_0():
    payload = {
        "rollNo": "21CS448",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.27,
        "activeBacklogs": 3,
        "attendance": 38.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_1():
    payload = {
        "rollNo": "21CS367",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.42,
        "activeBacklogs": 3,
        "attendance": 86.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_2():
    payload = {
        "rollNo": "21CS526",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.61,
        "activeBacklogs": 0,
        "attendance": 56.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_3():
    payload = {
        "rollNo": "21CS850",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.14,
        "activeBacklogs": 0,
        "attendance": 79.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_4():
    payload = {
        "rollNo": "21CS753",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.56,
        "activeBacklogs": 5,
        "attendance": 46.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_5():
    payload = {
        "rollNo": "21CS688",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.52,
        "activeBacklogs": 5,
        "attendance": 57.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_6():
    payload = {
        "rollNo": "21CS956",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.91,
        "activeBacklogs": 3,
        "attendance": 41.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_7():
    payload = {
        "rollNo": "21CS782",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.85,
        "activeBacklogs": 4,
        "attendance": 86.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_8():
    payload = {
        "rollNo": "21CS627",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.54,
        "activeBacklogs": 4,
        "attendance": 48.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_9():
    payload = {
        "rollNo": "21CS118",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.41,
        "activeBacklogs": 0,
        "attendance": 98.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_10():
    payload = {
        "rollNo": "21CS785",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.55,
        "activeBacklogs": 0,
        "attendance": 44.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_11():
    payload = {
        "rollNo": "21CS883",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.53,
        "activeBacklogs": 1,
        "attendance": 67.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_12():
    payload = {
        "rollNo": "21CS743",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.14,
        "activeBacklogs": 4,
        "attendance": 92.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_13():
    payload = {
        "rollNo": "21CS800",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.81,
        "activeBacklogs": 4,
        "attendance": 39.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_14():
    payload = {
        "rollNo": "21CS984",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.53,
        "activeBacklogs": 2,
        "attendance": 54.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_15():
    payload = {
        "rollNo": "21CS682",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.98,
        "activeBacklogs": 2,
        "attendance": 83.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_16():
    payload = {
        "rollNo": "21CS470",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.62,
        "activeBacklogs": 3,
        "attendance": 33.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_17():
    payload = {
        "rollNo": "21CS156",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.78,
        "activeBacklogs": 5,
        "attendance": 52.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_18():
    payload = {
        "rollNo": "21CS224",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.36,
        "activeBacklogs": 3,
        "attendance": 81.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_19():
    payload = {
        "rollNo": "21CS817",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.63,
        "activeBacklogs": 2,
        "attendance": 91.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_20():
    payload = {
        "rollNo": "21CS158",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.76,
        "activeBacklogs": 5,
        "attendance": 42.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_21():
    payload = {
        "rollNo": "21CS953",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.98,
        "activeBacklogs": 3,
        "attendance": 83.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_22():
    payload = {
        "rollNo": "21CS329",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.94,
        "activeBacklogs": 5,
        "attendance": 84.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_23():
    payload = {
        "rollNo": "21CS236",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.44,
        "activeBacklogs": 3,
        "attendance": 65.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_24():
    payload = {
        "rollNo": "21CS303",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.19,
        "activeBacklogs": 5,
        "attendance": 56.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_25():
    payload = {
        "rollNo": "21CS668",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.9,
        "activeBacklogs": 0,
        "attendance": 65.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_26():
    payload = {
        "rollNo": "21CS979",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.48,
        "activeBacklogs": 2,
        "attendance": 35.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_27():
    payload = {
        "rollNo": "21CS986",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.89,
        "activeBacklogs": 3,
        "attendance": 82.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_28():
    payload = {
        "rollNo": "21CS954",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.62,
        "activeBacklogs": 1,
        "attendance": 82.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_29():
    payload = {
        "rollNo": "21CS394",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.0,
        "activeBacklogs": 0,
        "attendance": 88.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_30():
    payload = {
        "rollNo": "21CS329",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.68,
        "activeBacklogs": 0,
        "attendance": 30.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_31():
    payload = {
        "rollNo": "21CS706",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.47,
        "activeBacklogs": 4,
        "attendance": 41.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_32():
    payload = {
        "rollNo": "21CS132",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.76,
        "activeBacklogs": 1,
        "attendance": 47.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_33():
    payload = {
        "rollNo": "21CS520",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.13,
        "activeBacklogs": 5,
        "attendance": 86.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_34():
    payload = {
        "rollNo": "21CS636",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.44,
        "activeBacklogs": 0,
        "attendance": 83.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_35():
    payload = {
        "rollNo": "21CS854",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.93,
        "activeBacklogs": 2,
        "attendance": 82.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_36():
    payload = {
        "rollNo": "21CS670",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.07,
        "activeBacklogs": 1,
        "attendance": 77.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_37():
    payload = {
        "rollNo": "21CS876",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.21,
        "activeBacklogs": 3,
        "attendance": 78.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_38():
    payload = {
        "rollNo": "21CS149",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.85,
        "activeBacklogs": 0,
        "attendance": 80.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_39():
    payload = {
        "rollNo": "21CS254",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.31,
        "activeBacklogs": 2,
        "attendance": 96.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_40():
    payload = {
        "rollNo": "21CS765",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.84,
        "activeBacklogs": 4,
        "attendance": 90.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_41():
    payload = {
        "rollNo": "21CS857",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.61,
        "activeBacklogs": 2,
        "attendance": 48.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_42():
    payload = {
        "rollNo": "21CS202",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.03,
        "activeBacklogs": 2,
        "attendance": 88.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_43():
    payload = {
        "rollNo": "21CS542",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.13,
        "activeBacklogs": 0,
        "attendance": 77.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_44():
    payload = {
        "rollNo": "21CS296",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.62,
        "activeBacklogs": 2,
        "attendance": 76.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_45():
    payload = {
        "rollNo": "21CS802",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.44,
        "activeBacklogs": 1,
        "attendance": 93.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_46():
    payload = {
        "rollNo": "21CS160",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.15,
        "activeBacklogs": 5,
        "attendance": 30.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_47():
    payload = {
        "rollNo": "21CS956",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.93,
        "activeBacklogs": 5,
        "attendance": 75.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_48():
    payload = {
        "rollNo": "21CS843",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.29,
        "activeBacklogs": 3,
        "attendance": 95.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_49():
    payload = {
        "rollNo": "21CS801",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.29,
        "activeBacklogs": 1,
        "attendance": 51.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_50():
    payload = {
        "rollNo": "21CS861",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.07,
        "activeBacklogs": 0,
        "attendance": 46.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_51():
    payload = {
        "rollNo": "21CS174",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.14,
        "activeBacklogs": 4,
        "attendance": 60.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_52():
    payload = {
        "rollNo": "21CS100",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.72,
        "activeBacklogs": 4,
        "attendance": 85.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_53():
    payload = {
        "rollNo": "21CS470",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.95,
        "activeBacklogs": 1,
        "attendance": 90.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_54():
    payload = {
        "rollNo": "21CS994",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.1,
        "activeBacklogs": 4,
        "attendance": 31.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_55():
    payload = {
        "rollNo": "21CS664",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.39,
        "activeBacklogs": 4,
        "attendance": 73.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_56():
    payload = {
        "rollNo": "21CS184",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.28,
        "activeBacklogs": 0,
        "attendance": 57.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_57():
    payload = {
        "rollNo": "21CS268",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.74,
        "activeBacklogs": 0,
        "attendance": 89.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_58():
    payload = {
        "rollNo": "21CS447",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.68,
        "activeBacklogs": 4,
        "attendance": 84.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_59():
    payload = {
        "rollNo": "21CS483",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.49,
        "activeBacklogs": 1,
        "attendance": 97.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_60():
    payload = {
        "rollNo": "21CS906",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.94,
        "activeBacklogs": 1,
        "attendance": 70.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_61():
    payload = {
        "rollNo": "21CS987",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.6,
        "activeBacklogs": 4,
        "attendance": 76.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_62():
    payload = {
        "rollNo": "21CS187",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.37,
        "activeBacklogs": 4,
        "attendance": 33.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_63():
    payload = {
        "rollNo": "21CS967",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.08,
        "activeBacklogs": 5,
        "attendance": 80.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_64():
    payload = {
        "rollNo": "21CS765",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.2,
        "activeBacklogs": 3,
        "attendance": 68.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_65():
    payload = {
        "rollNo": "21CS998",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.52,
        "activeBacklogs": 2,
        "attendance": 82.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_66():
    payload = {
        "rollNo": "21CS362",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.48,
        "activeBacklogs": 4,
        "attendance": 92.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_67():
    payload = {
        "rollNo": "21CS323",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.74,
        "activeBacklogs": 3,
        "attendance": 56.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_68():
    payload = {
        "rollNo": "21CS199",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.9,
        "activeBacklogs": 4,
        "attendance": 39.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_69():
    payload = {
        "rollNo": "21CS616",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.77,
        "activeBacklogs": 2,
        "attendance": 57.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_70():
    payload = {
        "rollNo": "21CS975",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.82,
        "activeBacklogs": 1,
        "attendance": 37.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_71():
    payload = {
        "rollNo": "21CS466",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.19,
        "activeBacklogs": 4,
        "attendance": 63.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_72():
    payload = {
        "rollNo": "21CS670",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.31,
        "activeBacklogs": 5,
        "attendance": 94.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_73():
    payload = {
        "rollNo": "21CS922",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.23,
        "activeBacklogs": 5,
        "attendance": 87.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_74():
    payload = {
        "rollNo": "21CS669",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.9,
        "activeBacklogs": 5,
        "attendance": 79.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_75():
    payload = {
        "rollNo": "21CS259",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.32,
        "activeBacklogs": 0,
        "attendance": 60.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_76():
    payload = {
        "rollNo": "21CS575",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.49,
        "activeBacklogs": 0,
        "attendance": 46.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_77():
    payload = {
        "rollNo": "21CS730",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.9,
        "activeBacklogs": 5,
        "attendance": 54.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_78():
    payload = {
        "rollNo": "21CS550",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.85,
        "activeBacklogs": 1,
        "attendance": 84.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_79():
    payload = {
        "rollNo": "21CS800",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.36,
        "activeBacklogs": 5,
        "attendance": 33.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_80():
    payload = {
        "rollNo": "21CS961",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.24,
        "activeBacklogs": 1,
        "attendance": 84.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_81():
    payload = {
        "rollNo": "21CS810",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.48,
        "activeBacklogs": 0,
        "attendance": 87.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_82():
    payload = {
        "rollNo": "21CS325",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.08,
        "activeBacklogs": 0,
        "attendance": 30.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_83():
    payload = {
        "rollNo": "21CS944",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.49,
        "activeBacklogs": 3,
        "attendance": 87.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_84():
    payload = {
        "rollNo": "21CS128",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.66,
        "activeBacklogs": 1,
        "attendance": 79.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_85():
    payload = {
        "rollNo": "21CS693",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.1,
        "activeBacklogs": 3,
        "attendance": 87.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_86():
    payload = {
        "rollNo": "21CS300",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.36,
        "activeBacklogs": 2,
        "attendance": 31.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_87():
    payload = {
        "rollNo": "21CS552",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.95,
        "activeBacklogs": 1,
        "attendance": 59.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_88():
    payload = {
        "rollNo": "21CS102",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.18,
        "activeBacklogs": 1,
        "attendance": 46.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_89():
    payload = {
        "rollNo": "21CS403",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.49,
        "activeBacklogs": 2,
        "attendance": 59.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_90():
    payload = {
        "rollNo": "21CS830",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.96,
        "activeBacklogs": 0,
        "attendance": 91.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_91():
    payload = {
        "rollNo": "21CS452",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.35,
        "activeBacklogs": 2,
        "attendance": 59.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_92():
    payload = {
        "rollNo": "21CS214",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.04,
        "activeBacklogs": 3,
        "attendance": 43.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_93():
    payload = {
        "rollNo": "21CS392",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.07,
        "activeBacklogs": 3,
        "attendance": 82.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_94():
    payload = {
        "rollNo": "21CS490",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.4,
        "activeBacklogs": 3,
        "attendance": 73.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_95():
    payload = {
        "rollNo": "21CS224",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.26,
        "activeBacklogs": 0,
        "attendance": 97.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_96():
    payload = {
        "rollNo": "21CS749",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.12,
        "activeBacklogs": 3,
        "attendance": 57.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_97():
    payload = {
        "rollNo": "21CS366",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.18,
        "activeBacklogs": 5,
        "attendance": 37.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_98():
    payload = {
        "rollNo": "21CS291",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.62,
        "activeBacklogs": 3,
        "attendance": 95.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_99():
    payload = {
        "rollNo": "21CS785",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.38,
        "activeBacklogs": 1,
        "attendance": 56.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_100():
    payload = {
        "rollNo": "21CS920",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.15,
        "activeBacklogs": 5,
        "attendance": 50.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_101():
    payload = {
        "rollNo": "21CS521",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.01,
        "activeBacklogs": 0,
        "attendance": 87.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_102():
    payload = {
        "rollNo": "21CS114",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.71,
        "activeBacklogs": 2,
        "attendance": 31.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_103():
    payload = {
        "rollNo": "21CS749",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.57,
        "activeBacklogs": 5,
        "attendance": 32.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_104():
    payload = {
        "rollNo": "21CS434",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.95,
        "activeBacklogs": 1,
        "attendance": 81.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_105():
    payload = {
        "rollNo": "21CS511",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.52,
        "activeBacklogs": 4,
        "attendance": 90.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_106():
    payload = {
        "rollNo": "21CS595",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.4,
        "activeBacklogs": 2,
        "attendance": 45.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_107():
    payload = {
        "rollNo": "21CS959",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.93,
        "activeBacklogs": 3,
        "attendance": 96.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_108():
    payload = {
        "rollNo": "21CS966",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.69,
        "activeBacklogs": 0,
        "attendance": 93.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_109():
    payload = {
        "rollNo": "21CS668",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.76,
        "activeBacklogs": 2,
        "attendance": 40.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_110():
    payload = {
        "rollNo": "21CS215",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.15,
        "activeBacklogs": 1,
        "attendance": 93.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_111():
    payload = {
        "rollNo": "21CS771",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.58,
        "activeBacklogs": 5,
        "attendance": 62.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_112():
    payload = {
        "rollNo": "21CS995",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.98,
        "activeBacklogs": 0,
        "attendance": 72.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_113():
    payload = {
        "rollNo": "21CS784",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.35,
        "activeBacklogs": 3,
        "attendance": 93.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_114():
    payload = {
        "rollNo": "21CS314",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.41,
        "activeBacklogs": 1,
        "attendance": 91.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_115():
    payload = {
        "rollNo": "21CS674",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.86,
        "activeBacklogs": 0,
        "attendance": 68.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_116():
    payload = {
        "rollNo": "21CS324",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.88,
        "activeBacklogs": 5,
        "attendance": 77.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_117():
    payload = {
        "rollNo": "21CS228",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.06,
        "activeBacklogs": 4,
        "attendance": 68.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_118():
    payload = {
        "rollNo": "21CS640",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.85,
        "activeBacklogs": 2,
        "attendance": 42.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_119():
    payload = {
        "rollNo": "21CS476",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.51,
        "activeBacklogs": 4,
        "attendance": 38.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_120():
    payload = {
        "rollNo": "21CS276",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.21,
        "activeBacklogs": 1,
        "attendance": 82.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_121():
    payload = {
        "rollNo": "21CS649",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.58,
        "activeBacklogs": 4,
        "attendance": 96.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_122():
    payload = {
        "rollNo": "21CS317",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.3,
        "activeBacklogs": 2,
        "attendance": 98.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_123():
    payload = {
        "rollNo": "21CS799",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.19,
        "activeBacklogs": 0,
        "attendance": 32.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_124():
    payload = {
        "rollNo": "21CS260",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.2,
        "activeBacklogs": 4,
        "attendance": 32.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_125():
    payload = {
        "rollNo": "21CS527",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.29,
        "activeBacklogs": 2,
        "attendance": 44.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_126():
    payload = {
        "rollNo": "21CS216",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.53,
        "activeBacklogs": 0,
        "attendance": 43.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_127():
    payload = {
        "rollNo": "21CS260",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.43,
        "activeBacklogs": 2,
        "attendance": 94.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_128():
    payload = {
        "rollNo": "21CS184",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.47,
        "activeBacklogs": 4,
        "attendance": 37.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_129():
    payload = {
        "rollNo": "21CS670",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.38,
        "activeBacklogs": 0,
        "attendance": 62.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_130():
    payload = {
        "rollNo": "21CS585",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.5,
        "activeBacklogs": 4,
        "attendance": 79.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_131():
    payload = {
        "rollNo": "21CS411",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.72,
        "activeBacklogs": 4,
        "attendance": 42.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_132():
    payload = {
        "rollNo": "21CS341",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.46,
        "activeBacklogs": 0,
        "attendance": 47.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_133():
    payload = {
        "rollNo": "21CS636",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.96,
        "activeBacklogs": 2,
        "attendance": 70.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_134():
    payload = {
        "rollNo": "21CS834",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.88,
        "activeBacklogs": 2,
        "attendance": 70.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_135():
    payload = {
        "rollNo": "21CS238",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.9,
        "activeBacklogs": 1,
        "attendance": 87.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_136():
    payload = {
        "rollNo": "21CS438",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.17,
        "activeBacklogs": 5,
        "attendance": 35.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_137():
    payload = {
        "rollNo": "21CS566",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.19,
        "activeBacklogs": 5,
        "attendance": 33.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_138():
    payload = {
        "rollNo": "21CS994",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.85,
        "activeBacklogs": 4,
        "attendance": 89.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_139():
    payload = {
        "rollNo": "21CS916",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.16,
        "activeBacklogs": 3,
        "attendance": 82.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_140():
    payload = {
        "rollNo": "21CS466",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.68,
        "activeBacklogs": 0,
        "attendance": 46.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_141():
    payload = {
        "rollNo": "21CS869",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.86,
        "activeBacklogs": 1,
        "attendance": 63.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_142():
    payload = {
        "rollNo": "21CS722",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.78,
        "activeBacklogs": 4,
        "attendance": 37.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_143():
    payload = {
        "rollNo": "21CS305",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.61,
        "activeBacklogs": 4,
        "attendance": 65.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_144():
    payload = {
        "rollNo": "21CS119",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.2,
        "activeBacklogs": 1,
        "attendance": 55.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_145():
    payload = {
        "rollNo": "21CS663",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.19,
        "activeBacklogs": 5,
        "attendance": 57.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_146():
    payload = {
        "rollNo": "21CS769",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.24,
        "activeBacklogs": 2,
        "attendance": 77.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_147():
    payload = {
        "rollNo": "21CS391",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.38,
        "activeBacklogs": 1,
        "attendance": 36.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_148():
    payload = {
        "rollNo": "21CS356",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.55,
        "activeBacklogs": 3,
        "attendance": 58.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_149():
    payload = {
        "rollNo": "21CS938",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.05,
        "activeBacklogs": 3,
        "attendance": 91.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_150():
    payload = {
        "rollNo": "21CS509",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.34,
        "activeBacklogs": 4,
        "attendance": 71.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_151():
    payload = {
        "rollNo": "21CS647",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.72,
        "activeBacklogs": 4,
        "attendance": 46.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_152():
    payload = {
        "rollNo": "21CS620",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.04,
        "activeBacklogs": 3,
        "attendance": 55.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_153():
    payload = {
        "rollNo": "21CS525",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.85,
        "activeBacklogs": 4,
        "attendance": 76.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_154():
    payload = {
        "rollNo": "21CS464",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.62,
        "activeBacklogs": 0,
        "attendance": 81.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_155():
    payload = {
        "rollNo": "21CS920",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.38,
        "activeBacklogs": 2,
        "attendance": 64.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_156():
    payload = {
        "rollNo": "21CS218",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.61,
        "activeBacklogs": 1,
        "attendance": 40.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_157():
    payload = {
        "rollNo": "21CS127",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.95,
        "activeBacklogs": 2,
        "attendance": 43.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_158():
    payload = {
        "rollNo": "21CS960",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.28,
        "activeBacklogs": 2,
        "attendance": 93.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_159():
    payload = {
        "rollNo": "21CS620",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.36,
        "activeBacklogs": 2,
        "attendance": 72.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_160():
    payload = {
        "rollNo": "21CS313",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.7,
        "activeBacklogs": 3,
        "attendance": 78.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_161():
    payload = {
        "rollNo": "21CS970",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.34,
        "activeBacklogs": 2,
        "attendance": 70.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_162():
    payload = {
        "rollNo": "21CS132",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.62,
        "activeBacklogs": 5,
        "attendance": 57.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_163():
    payload = {
        "rollNo": "21CS801",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.37,
        "activeBacklogs": 5,
        "attendance": 87.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_164():
    payload = {
        "rollNo": "21CS552",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.52,
        "activeBacklogs": 0,
        "attendance": 95.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_165():
    payload = {
        "rollNo": "21CS246",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.36,
        "activeBacklogs": 5,
        "attendance": 78.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_166():
    payload = {
        "rollNo": "21CS626",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.65,
        "activeBacklogs": 3,
        "attendance": 85.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_167():
    payload = {
        "rollNo": "21CS492",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.17,
        "activeBacklogs": 4,
        "attendance": 35.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_168():
    payload = {
        "rollNo": "21CS770",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.85,
        "activeBacklogs": 2,
        "attendance": 31.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_169():
    payload = {
        "rollNo": "21CS585",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.37,
        "activeBacklogs": 0,
        "attendance": 47.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_170():
    payload = {
        "rollNo": "21CS701",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.14,
        "activeBacklogs": 5,
        "attendance": 44.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_171():
    payload = {
        "rollNo": "21CS330",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.27,
        "activeBacklogs": 3,
        "attendance": 77.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_172():
    payload = {
        "rollNo": "21CS897",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.61,
        "activeBacklogs": 0,
        "attendance": 39.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_173():
    payload = {
        "rollNo": "21CS516",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.91,
        "activeBacklogs": 4,
        "attendance": 98.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_174():
    payload = {
        "rollNo": "21CS459",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.02,
        "activeBacklogs": 3,
        "attendance": 94.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_175():
    payload = {
        "rollNo": "21CS246",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.24,
        "activeBacklogs": 3,
        "attendance": 59.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_176():
    payload = {
        "rollNo": "21CS561",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.26,
        "activeBacklogs": 5,
        "attendance": 88.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_177():
    payload = {
        "rollNo": "21CS971",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.01,
        "activeBacklogs": 0,
        "attendance": 55.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_178():
    payload = {
        "rollNo": "21CS281",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.78,
        "activeBacklogs": 5,
        "attendance": 89.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_179():
    payload = {
        "rollNo": "21CS985",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.32,
        "activeBacklogs": 1,
        "attendance": 90.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_180():
    payload = {
        "rollNo": "21CS730",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.9,
        "activeBacklogs": 2,
        "attendance": 31.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_181():
    payload = {
        "rollNo": "21CS345",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.36,
        "activeBacklogs": 4,
        "attendance": 37.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_182():
    payload = {
        "rollNo": "21CS928",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.98,
        "activeBacklogs": 0,
        "attendance": 72.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_183():
    payload = {
        "rollNo": "21CS765",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.6,
        "activeBacklogs": 1,
        "attendance": 54.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_184():
    payload = {
        "rollNo": "21CS998",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.36,
        "activeBacklogs": 3,
        "attendance": 41.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_185():
    payload = {
        "rollNo": "21CS456",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.91,
        "activeBacklogs": 0,
        "attendance": 82.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_186():
    payload = {
        "rollNo": "21CS984",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.56,
        "activeBacklogs": 3,
        "attendance": 40.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_187():
    payload = {
        "rollNo": "21CS850",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.62,
        "activeBacklogs": 3,
        "attendance": 51.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_188():
    payload = {
        "rollNo": "21CS762",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.77,
        "activeBacklogs": 3,
        "attendance": 47.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_189():
    payload = {
        "rollNo": "21CS370",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.14,
        "activeBacklogs": 1,
        "attendance": 52.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_190():
    payload = {
        "rollNo": "21CS148",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.56,
        "activeBacklogs": 3,
        "attendance": 69.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_191():
    payload = {
        "rollNo": "21CS432",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.87,
        "activeBacklogs": 2,
        "attendance": 69.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_192():
    payload = {
        "rollNo": "21CS306",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.68,
        "activeBacklogs": 3,
        "attendance": 43.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_193():
    payload = {
        "rollNo": "21CS527",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.68,
        "activeBacklogs": 2,
        "attendance": 54.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_194():
    payload = {
        "rollNo": "21CS952",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.22,
        "activeBacklogs": 5,
        "attendance": 35.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_195():
    payload = {
        "rollNo": "21CS754",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.29,
        "activeBacklogs": 2,
        "attendance": 67.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_196():
    payload = {
        "rollNo": "21CS846",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.36,
        "activeBacklogs": 0,
        "attendance": 71.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_197():
    payload = {
        "rollNo": "21CS271",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.55,
        "activeBacklogs": 2,
        "attendance": 99.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_198():
    payload = {
        "rollNo": "21CS584",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.62,
        "activeBacklogs": 1,
        "attendance": 87.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_199():
    payload = {
        "rollNo": "21CS939",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.14,
        "activeBacklogs": 5,
        "attendance": 96.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_200():
    payload = {
        "rollNo": "21CS905",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.37,
        "activeBacklogs": 5,
        "attendance": 43.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_201():
    payload = {
        "rollNo": "21CS959",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.94,
        "activeBacklogs": 2,
        "attendance": 87.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_202():
    payload = {
        "rollNo": "21CS495",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.6,
        "activeBacklogs": 4,
        "attendance": 75.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_203():
    payload = {
        "rollNo": "21CS715",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.52,
        "activeBacklogs": 4,
        "attendance": 68.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_204():
    payload = {
        "rollNo": "21CS323",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.57,
        "activeBacklogs": 5,
        "attendance": 99.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_205():
    payload = {
        "rollNo": "21CS632",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.93,
        "activeBacklogs": 1,
        "attendance": 72.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_206():
    payload = {
        "rollNo": "21CS167",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 10.0,
        "activeBacklogs": 5,
        "attendance": 88.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_207():
    payload = {
        "rollNo": "21CS923",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.08,
        "activeBacklogs": 2,
        "attendance": 86.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_208():
    payload = {
        "rollNo": "21CS416",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.69,
        "activeBacklogs": 1,
        "attendance": 39.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_209():
    payload = {
        "rollNo": "21CS538",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.86,
        "activeBacklogs": 5,
        "attendance": 58.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_210():
    payload = {
        "rollNo": "21CS700",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.63,
        "activeBacklogs": 2,
        "attendance": 60.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_211():
    payload = {
        "rollNo": "21CS709",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.05,
        "activeBacklogs": 1,
        "attendance": 45.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_212():
    payload = {
        "rollNo": "21CS124",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.62,
        "activeBacklogs": 3,
        "attendance": 31.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_213():
    payload = {
        "rollNo": "21CS445",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.83,
        "activeBacklogs": 0,
        "attendance": 84.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_214():
    payload = {
        "rollNo": "21CS914",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.95,
        "activeBacklogs": 0,
        "attendance": 75.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_215():
    payload = {
        "rollNo": "21CS642",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.64,
        "activeBacklogs": 2,
        "attendance": 81.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_216():
    payload = {
        "rollNo": "21CS654",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.93,
        "activeBacklogs": 3,
        "attendance": 76.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_217():
    payload = {
        "rollNo": "21CS211",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.35,
        "activeBacklogs": 0,
        "attendance": 33.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_218():
    payload = {
        "rollNo": "21CS860",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.33,
        "activeBacklogs": 2,
        "attendance": 63.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_219():
    payload = {
        "rollNo": "21CS905",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.93,
        "activeBacklogs": 0,
        "attendance": 73.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_220():
    payload = {
        "rollNo": "21CS376",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.84,
        "activeBacklogs": 2,
        "attendance": 70.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_221():
    payload = {
        "rollNo": "21CS613",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.97,
        "activeBacklogs": 0,
        "attendance": 68.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_222():
    payload = {
        "rollNo": "21CS912",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.52,
        "activeBacklogs": 0,
        "attendance": 31.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_223():
    payload = {
        "rollNo": "21CS751",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.72,
        "activeBacklogs": 2,
        "attendance": 50.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_224():
    payload = {
        "rollNo": "21CS662",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.35,
        "activeBacklogs": 1,
        "attendance": 70.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_225():
    payload = {
        "rollNo": "21CS870",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.03,
        "activeBacklogs": 5,
        "attendance": 35.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_226():
    payload = {
        "rollNo": "21CS163",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.09,
        "activeBacklogs": 4,
        "attendance": 58.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_227():
    payload = {
        "rollNo": "21CS553",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.33,
        "activeBacklogs": 2,
        "attendance": 92.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_228():
    payload = {
        "rollNo": "21CS735",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.67,
        "activeBacklogs": 0,
        "attendance": 51.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_229():
    payload = {
        "rollNo": "21CS413",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.27,
        "activeBacklogs": 3,
        "attendance": 48.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_230():
    payload = {
        "rollNo": "21CS399",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.49,
        "activeBacklogs": 0,
        "attendance": 71.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_231():
    payload = {
        "rollNo": "21CS352",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.52,
        "activeBacklogs": 5,
        "attendance": 51.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_232():
    payload = {
        "rollNo": "21CS509",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.83,
        "activeBacklogs": 4,
        "attendance": 91.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_233():
    payload = {
        "rollNo": "21CS609",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.39,
        "activeBacklogs": 3,
        "attendance": 43.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_234():
    payload = {
        "rollNo": "21CS148",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.52,
        "activeBacklogs": 4,
        "attendance": 39.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_235():
    payload = {
        "rollNo": "21CS969",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.84,
        "activeBacklogs": 2,
        "attendance": 66.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_236():
    payload = {
        "rollNo": "21CS344",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.61,
        "activeBacklogs": 4,
        "attendance": 97.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_237():
    payload = {
        "rollNo": "21CS117",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.93,
        "activeBacklogs": 0,
        "attendance": 35.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_238():
    payload = {
        "rollNo": "21CS786",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.57,
        "activeBacklogs": 3,
        "attendance": 30.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_239():
    payload = {
        "rollNo": "21CS737",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.73,
        "activeBacklogs": 5,
        "attendance": 33.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_240():
    payload = {
        "rollNo": "21CS517",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.59,
        "activeBacklogs": 0,
        "attendance": 96.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_241():
    payload = {
        "rollNo": "21CS418",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.98,
        "activeBacklogs": 1,
        "attendance": 53.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_242():
    payload = {
        "rollNo": "21CS987",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.5,
        "activeBacklogs": 2,
        "attendance": 87.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_243():
    payload = {
        "rollNo": "21CS803",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.7,
        "activeBacklogs": 3,
        "attendance": 44.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_244():
    payload = {
        "rollNo": "21CS214",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.47,
        "activeBacklogs": 5,
        "attendance": 51.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_245():
    payload = {
        "rollNo": "21CS390",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.47,
        "activeBacklogs": 3,
        "attendance": 43.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_246():
    payload = {
        "rollNo": "21CS607",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.99,
        "activeBacklogs": 3,
        "attendance": 90.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_247():
    payload = {
        "rollNo": "21CS544",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.7,
        "activeBacklogs": 2,
        "attendance": 53.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_248():
    payload = {
        "rollNo": "21CS726",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.94,
        "activeBacklogs": 0,
        "attendance": 57.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_15_249():
    payload = {
        "rollNo": "21CS509",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.02,
        "activeBacklogs": 0,
        "attendance": 61.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

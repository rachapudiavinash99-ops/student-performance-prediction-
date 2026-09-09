import pytest
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_prediction_case_7_0():
    payload = {
        "rollNo": "21CS956",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.59,
        "activeBacklogs": 1,
        "attendance": 86.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_1():
    payload = {
        "rollNo": "21CS376",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.26,
        "activeBacklogs": 4,
        "attendance": 83.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_2():
    payload = {
        "rollNo": "21CS595",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.95,
        "activeBacklogs": 4,
        "attendance": 67.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_3():
    payload = {
        "rollNo": "21CS441",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.92,
        "activeBacklogs": 2,
        "attendance": 61.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_4():
    payload = {
        "rollNo": "21CS230",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.02,
        "activeBacklogs": 4,
        "attendance": 84.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_5():
    payload = {
        "rollNo": "21CS984",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.74,
        "activeBacklogs": 3,
        "attendance": 62.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_6():
    payload = {
        "rollNo": "21CS499",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.27,
        "activeBacklogs": 2,
        "attendance": 91.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_7():
    payload = {
        "rollNo": "21CS463",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.35,
        "activeBacklogs": 1,
        "attendance": 33.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_8():
    payload = {
        "rollNo": "21CS896",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.02,
        "activeBacklogs": 3,
        "attendance": 65.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_9():
    payload = {
        "rollNo": "21CS761",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.78,
        "activeBacklogs": 5,
        "attendance": 87.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_10():
    payload = {
        "rollNo": "21CS977",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.08,
        "activeBacklogs": 2,
        "attendance": 39.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_11():
    payload = {
        "rollNo": "21CS381",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.41,
        "activeBacklogs": 5,
        "attendance": 86.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_12():
    payload = {
        "rollNo": "21CS256",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.59,
        "activeBacklogs": 3,
        "attendance": 43.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_13():
    payload = {
        "rollNo": "21CS623",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.21,
        "activeBacklogs": 2,
        "attendance": 56.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_14():
    payload = {
        "rollNo": "21CS253",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.13,
        "activeBacklogs": 1,
        "attendance": 81.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_15():
    payload = {
        "rollNo": "21CS440",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.12,
        "activeBacklogs": 0,
        "attendance": 60.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_16():
    payload = {
        "rollNo": "21CS678",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.21,
        "activeBacklogs": 2,
        "attendance": 43.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_17():
    payload = {
        "rollNo": "21CS699",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.65,
        "activeBacklogs": 0,
        "attendance": 63.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_18():
    payload = {
        "rollNo": "21CS971",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.49,
        "activeBacklogs": 4,
        "attendance": 63.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_19():
    payload = {
        "rollNo": "21CS564",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.04,
        "activeBacklogs": 0,
        "attendance": 50.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_20():
    payload = {
        "rollNo": "21CS879",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.44,
        "activeBacklogs": 4,
        "attendance": 94.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_21():
    payload = {
        "rollNo": "21CS223",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.06,
        "activeBacklogs": 0,
        "attendance": 80.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_22():
    payload = {
        "rollNo": "21CS958",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.68,
        "activeBacklogs": 3,
        "attendance": 90.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_23():
    payload = {
        "rollNo": "21CS935",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.01,
        "activeBacklogs": 2,
        "attendance": 87.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_24():
    payload = {
        "rollNo": "21CS820",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.02,
        "activeBacklogs": 4,
        "attendance": 45.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_25():
    payload = {
        "rollNo": "21CS651",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.85,
        "activeBacklogs": 1,
        "attendance": 37.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_26():
    payload = {
        "rollNo": "21CS271",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.29,
        "activeBacklogs": 4,
        "attendance": 97.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_27():
    payload = {
        "rollNo": "21CS700",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.67,
        "activeBacklogs": 5,
        "attendance": 93.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_28():
    payload = {
        "rollNo": "21CS535",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.13,
        "activeBacklogs": 3,
        "attendance": 65.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_29():
    payload = {
        "rollNo": "21CS937",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.13,
        "activeBacklogs": 2,
        "attendance": 34.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_30():
    payload = {
        "rollNo": "21CS468",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.86,
        "activeBacklogs": 4,
        "attendance": 78.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_31():
    payload = {
        "rollNo": "21CS358",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.74,
        "activeBacklogs": 0,
        "attendance": 79.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_32():
    payload = {
        "rollNo": "21CS409",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.62,
        "activeBacklogs": 5,
        "attendance": 57.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_33():
    payload = {
        "rollNo": "21CS262",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.91,
        "activeBacklogs": 4,
        "attendance": 95.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_34():
    payload = {
        "rollNo": "21CS213",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.22,
        "activeBacklogs": 3,
        "attendance": 61.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_35():
    payload = {
        "rollNo": "21CS406",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.96,
        "activeBacklogs": 4,
        "attendance": 62.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_36():
    payload = {
        "rollNo": "21CS785",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.44,
        "activeBacklogs": 3,
        "attendance": 58.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_37():
    payload = {
        "rollNo": "21CS930",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.93,
        "activeBacklogs": 2,
        "attendance": 76.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_38():
    payload = {
        "rollNo": "21CS492",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.9,
        "activeBacklogs": 1,
        "attendance": 42.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_39():
    payload = {
        "rollNo": "21CS580",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.34,
        "activeBacklogs": 3,
        "attendance": 72.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_40():
    payload = {
        "rollNo": "21CS551",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.17,
        "activeBacklogs": 0,
        "attendance": 37.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_41():
    payload = {
        "rollNo": "21CS464",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.01,
        "activeBacklogs": 4,
        "attendance": 87.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_42():
    payload = {
        "rollNo": "21CS398",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.76,
        "activeBacklogs": 3,
        "attendance": 50.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_43():
    payload = {
        "rollNo": "21CS243",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.46,
        "activeBacklogs": 0,
        "attendance": 49.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_44():
    payload = {
        "rollNo": "21CS513",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.06,
        "activeBacklogs": 4,
        "attendance": 92.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_45():
    payload = {
        "rollNo": "21CS860",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.76,
        "activeBacklogs": 4,
        "attendance": 67.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_46():
    payload = {
        "rollNo": "21CS135",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.04,
        "activeBacklogs": 4,
        "attendance": 88.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_47():
    payload = {
        "rollNo": "21CS307",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.58,
        "activeBacklogs": 1,
        "attendance": 57.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_48():
    payload = {
        "rollNo": "21CS176",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.06,
        "activeBacklogs": 3,
        "attendance": 63.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_49():
    payload = {
        "rollNo": "21CS468",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.18,
        "activeBacklogs": 5,
        "attendance": 62.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_50():
    payload = {
        "rollNo": "21CS261",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.81,
        "activeBacklogs": 3,
        "attendance": 83.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_51():
    payload = {
        "rollNo": "21CS862",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.44,
        "activeBacklogs": 2,
        "attendance": 54.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_52():
    payload = {
        "rollNo": "21CS520",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.09,
        "activeBacklogs": 5,
        "attendance": 31.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_53():
    payload = {
        "rollNo": "21CS675",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.91,
        "activeBacklogs": 4,
        "attendance": 64.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_54():
    payload = {
        "rollNo": "21CS949",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.21,
        "activeBacklogs": 5,
        "attendance": 63.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_55():
    payload = {
        "rollNo": "21CS756",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.04,
        "activeBacklogs": 2,
        "attendance": 95.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_56():
    payload = {
        "rollNo": "21CS749",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.74,
        "activeBacklogs": 0,
        "attendance": 43.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_57():
    payload = {
        "rollNo": "21CS749",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.51,
        "activeBacklogs": 5,
        "attendance": 85.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_58():
    payload = {
        "rollNo": "21CS722",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.51,
        "activeBacklogs": 0,
        "attendance": 60.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_59():
    payload = {
        "rollNo": "21CS466",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.3,
        "activeBacklogs": 3,
        "attendance": 62.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_60():
    payload = {
        "rollNo": "21CS756",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.62,
        "activeBacklogs": 4,
        "attendance": 45.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_61():
    payload = {
        "rollNo": "21CS154",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.39,
        "activeBacklogs": 3,
        "attendance": 43.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_62():
    payload = {
        "rollNo": "21CS145",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.73,
        "activeBacklogs": 3,
        "attendance": 82.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_63():
    payload = {
        "rollNo": "21CS719",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.06,
        "activeBacklogs": 5,
        "attendance": 97.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_64():
    payload = {
        "rollNo": "21CS573",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.62,
        "activeBacklogs": 5,
        "attendance": 83.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_65():
    payload = {
        "rollNo": "21CS474",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.69,
        "activeBacklogs": 1,
        "attendance": 33.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_66():
    payload = {
        "rollNo": "21CS878",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.89,
        "activeBacklogs": 0,
        "attendance": 37.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_67():
    payload = {
        "rollNo": "21CS938",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.86,
        "activeBacklogs": 5,
        "attendance": 85.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_68():
    payload = {
        "rollNo": "21CS486",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.06,
        "activeBacklogs": 3,
        "attendance": 78.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_69():
    payload = {
        "rollNo": "21CS872",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.94,
        "activeBacklogs": 4,
        "attendance": 39.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_70():
    payload = {
        "rollNo": "21CS167",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.78,
        "activeBacklogs": 5,
        "attendance": 51.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_71():
    payload = {
        "rollNo": "21CS147",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.57,
        "activeBacklogs": 2,
        "attendance": 81.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_72():
    payload = {
        "rollNo": "21CS952",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.2,
        "activeBacklogs": 0,
        "attendance": 39.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_73():
    payload = {
        "rollNo": "21CS244",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.58,
        "activeBacklogs": 0,
        "attendance": 82.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_74():
    payload = {
        "rollNo": "21CS802",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.36,
        "activeBacklogs": 5,
        "attendance": 48.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_75():
    payload = {
        "rollNo": "21CS153",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.18,
        "activeBacklogs": 3,
        "attendance": 57.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_76():
    payload = {
        "rollNo": "21CS469",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.36,
        "activeBacklogs": 5,
        "attendance": 54.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_77():
    payload = {
        "rollNo": "21CS830",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.4,
        "activeBacklogs": 5,
        "attendance": 75.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_78():
    payload = {
        "rollNo": "21CS221",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.47,
        "activeBacklogs": 4,
        "attendance": 82.04
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_79():
    payload = {
        "rollNo": "21CS654",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.23,
        "activeBacklogs": 1,
        "attendance": 94.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_80():
    payload = {
        "rollNo": "21CS624",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.09,
        "activeBacklogs": 3,
        "attendance": 47.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_81():
    payload = {
        "rollNo": "21CS607",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.17,
        "activeBacklogs": 5,
        "attendance": 83.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_82():
    payload = {
        "rollNo": "21CS785",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.15,
        "activeBacklogs": 2,
        "attendance": 90.04
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_83():
    payload = {
        "rollNo": "21CS611",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.15,
        "activeBacklogs": 5,
        "attendance": 33.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_84():
    payload = {
        "rollNo": "21CS221",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.47,
        "activeBacklogs": 4,
        "attendance": 95.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_85():
    payload = {
        "rollNo": "21CS675",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.96,
        "activeBacklogs": 4,
        "attendance": 70.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_86():
    payload = {
        "rollNo": "21CS824",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.63,
        "activeBacklogs": 3,
        "attendance": 39.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_87():
    payload = {
        "rollNo": "21CS342",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.44,
        "activeBacklogs": 5,
        "attendance": 46.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_88():
    payload = {
        "rollNo": "21CS702",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.57,
        "activeBacklogs": 4,
        "attendance": 46.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_89():
    payload = {
        "rollNo": "21CS880",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.29,
        "activeBacklogs": 2,
        "attendance": 78.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_90():
    payload = {
        "rollNo": "21CS451",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.88,
        "activeBacklogs": 4,
        "attendance": 48.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_91():
    payload = {
        "rollNo": "21CS981",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.04,
        "activeBacklogs": 5,
        "attendance": 91.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_92():
    payload = {
        "rollNo": "21CS549",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.9,
        "activeBacklogs": 3,
        "attendance": 51.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_93():
    payload = {
        "rollNo": "21CS873",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.99,
        "activeBacklogs": 5,
        "attendance": 61.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_94():
    payload = {
        "rollNo": "21CS274",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.2,
        "activeBacklogs": 5,
        "attendance": 79.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_95():
    payload = {
        "rollNo": "21CS909",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.58,
        "activeBacklogs": 5,
        "attendance": 51.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_96():
    payload = {
        "rollNo": "21CS111",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.73,
        "activeBacklogs": 5,
        "attendance": 87.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_97():
    payload = {
        "rollNo": "21CS932",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.29,
        "activeBacklogs": 2,
        "attendance": 31.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_98():
    payload = {
        "rollNo": "21CS599",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.35,
        "activeBacklogs": 5,
        "attendance": 73.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_99():
    payload = {
        "rollNo": "21CS350",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.81,
        "activeBacklogs": 2,
        "attendance": 95.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_100():
    payload = {
        "rollNo": "21CS532",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.43,
        "activeBacklogs": 2,
        "attendance": 62.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_101():
    payload = {
        "rollNo": "21CS238",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.64,
        "activeBacklogs": 3,
        "attendance": 73.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_102():
    payload = {
        "rollNo": "21CS283",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.12,
        "activeBacklogs": 4,
        "attendance": 44.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_103():
    payload = {
        "rollNo": "21CS628",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.82,
        "activeBacklogs": 2,
        "attendance": 44.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_104():
    payload = {
        "rollNo": "21CS888",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.59,
        "activeBacklogs": 4,
        "attendance": 53.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_105():
    payload = {
        "rollNo": "21CS571",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.74,
        "activeBacklogs": 1,
        "attendance": 52.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_106():
    payload = {
        "rollNo": "21CS117",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.02,
        "activeBacklogs": 2,
        "attendance": 92.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_107():
    payload = {
        "rollNo": "21CS568",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.76,
        "activeBacklogs": 2,
        "attendance": 75.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_108():
    payload = {
        "rollNo": "21CS615",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.62,
        "activeBacklogs": 5,
        "attendance": 72.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_109():
    payload = {
        "rollNo": "21CS616",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.54,
        "activeBacklogs": 2,
        "attendance": 84.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_110():
    payload = {
        "rollNo": "21CS767",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.94,
        "activeBacklogs": 3,
        "attendance": 53.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_111():
    payload = {
        "rollNo": "21CS476",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.36,
        "activeBacklogs": 1,
        "attendance": 35.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_112():
    payload = {
        "rollNo": "21CS579",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.65,
        "activeBacklogs": 5,
        "attendance": 35.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_113():
    payload = {
        "rollNo": "21CS809",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.28,
        "activeBacklogs": 3,
        "attendance": 86.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_114():
    payload = {
        "rollNo": "21CS661",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.62,
        "activeBacklogs": 0,
        "attendance": 35.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_115():
    payload = {
        "rollNo": "21CS869",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.21,
        "activeBacklogs": 2,
        "attendance": 86.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_116():
    payload = {
        "rollNo": "21CS857",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.06,
        "activeBacklogs": 5,
        "attendance": 41.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_117():
    payload = {
        "rollNo": "21CS304",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.92,
        "activeBacklogs": 1,
        "attendance": 39.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_118():
    payload = {
        "rollNo": "21CS991",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.95,
        "activeBacklogs": 5,
        "attendance": 68.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_119():
    payload = {
        "rollNo": "21CS146",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.07,
        "activeBacklogs": 5,
        "attendance": 39.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_120():
    payload = {
        "rollNo": "21CS844",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.03,
        "activeBacklogs": 4,
        "attendance": 31.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_121():
    payload = {
        "rollNo": "21CS477",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.99,
        "activeBacklogs": 5,
        "attendance": 45.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_122():
    payload = {
        "rollNo": "21CS491",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.84,
        "activeBacklogs": 1,
        "attendance": 82.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_123():
    payload = {
        "rollNo": "21CS867",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.94,
        "activeBacklogs": 5,
        "attendance": 56.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_124():
    payload = {
        "rollNo": "21CS923",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.69,
        "activeBacklogs": 3,
        "attendance": 64.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_125():
    payload = {
        "rollNo": "21CS390",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.31,
        "activeBacklogs": 5,
        "attendance": 76.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_126():
    payload = {
        "rollNo": "21CS503",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.94,
        "activeBacklogs": 2,
        "attendance": 33.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_127():
    payload = {
        "rollNo": "21CS940",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.16,
        "activeBacklogs": 0,
        "attendance": 88.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_128():
    payload = {
        "rollNo": "21CS599",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.87,
        "activeBacklogs": 4,
        "attendance": 81.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_129():
    payload = {
        "rollNo": "21CS649",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.66,
        "activeBacklogs": 0,
        "attendance": 72.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_130():
    payload = {
        "rollNo": "21CS553",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.92,
        "activeBacklogs": 3,
        "attendance": 46.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_131():
    payload = {
        "rollNo": "21CS910",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.43,
        "activeBacklogs": 5,
        "attendance": 32.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_132():
    payload = {
        "rollNo": "21CS355",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.02,
        "activeBacklogs": 1,
        "attendance": 67.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_133():
    payload = {
        "rollNo": "21CS351",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.36,
        "activeBacklogs": 2,
        "attendance": 68.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_134():
    payload = {
        "rollNo": "21CS334",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.1,
        "activeBacklogs": 4,
        "attendance": 68.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_135():
    payload = {
        "rollNo": "21CS938",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.69,
        "activeBacklogs": 2,
        "attendance": 86.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_136():
    payload = {
        "rollNo": "21CS951",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.0,
        "activeBacklogs": 2,
        "attendance": 39.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_137():
    payload = {
        "rollNo": "21CS821",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.3,
        "activeBacklogs": 2,
        "attendance": 66.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_138():
    payload = {
        "rollNo": "21CS394",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.62,
        "activeBacklogs": 4,
        "attendance": 74.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_139():
    payload = {
        "rollNo": "21CS258",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.15,
        "activeBacklogs": 2,
        "attendance": 61.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_140():
    payload = {
        "rollNo": "21CS510",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.77,
        "activeBacklogs": 5,
        "attendance": 44.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_141():
    payload = {
        "rollNo": "21CS539",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.34,
        "activeBacklogs": 2,
        "attendance": 77.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_142():
    payload = {
        "rollNo": "21CS327",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.62,
        "activeBacklogs": 3,
        "attendance": 70.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_143():
    payload = {
        "rollNo": "21CS891",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.4,
        "activeBacklogs": 0,
        "attendance": 91.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_144():
    payload = {
        "rollNo": "21CS309",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.76,
        "activeBacklogs": 1,
        "attendance": 80.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_145():
    payload = {
        "rollNo": "21CS431",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.5,
        "activeBacklogs": 3,
        "attendance": 35.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_146():
    payload = {
        "rollNo": "21CS416",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.94,
        "activeBacklogs": 4,
        "attendance": 67.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_147():
    payload = {
        "rollNo": "21CS561",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.75,
        "activeBacklogs": 5,
        "attendance": 80.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_148():
    payload = {
        "rollNo": "21CS734",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.26,
        "activeBacklogs": 0,
        "attendance": 55.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_149():
    payload = {
        "rollNo": "21CS869",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.44,
        "activeBacklogs": 4,
        "attendance": 49.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_150():
    payload = {
        "rollNo": "21CS473",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.0,
        "activeBacklogs": 1,
        "attendance": 78.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_151():
    payload = {
        "rollNo": "21CS164",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.09,
        "activeBacklogs": 5,
        "attendance": 32.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_152():
    payload = {
        "rollNo": "21CS781",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.33,
        "activeBacklogs": 5,
        "attendance": 67.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_153():
    payload = {
        "rollNo": "21CS660",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.92,
        "activeBacklogs": 1,
        "attendance": 83.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_154():
    payload = {
        "rollNo": "21CS837",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.63,
        "activeBacklogs": 5,
        "attendance": 65.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_155():
    payload = {
        "rollNo": "21CS907",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.0,
        "activeBacklogs": 3,
        "attendance": 70.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_156():
    payload = {
        "rollNo": "21CS271",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.85,
        "activeBacklogs": 2,
        "attendance": 79.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_157():
    payload = {
        "rollNo": "21CS783",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.22,
        "activeBacklogs": 2,
        "attendance": 67.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_158():
    payload = {
        "rollNo": "21CS822",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.83,
        "activeBacklogs": 5,
        "attendance": 44.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_159():
    payload = {
        "rollNo": "21CS641",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.59,
        "activeBacklogs": 2,
        "attendance": 60.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_160():
    payload = {
        "rollNo": "21CS942",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.76,
        "activeBacklogs": 3,
        "attendance": 88.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_161():
    payload = {
        "rollNo": "21CS510",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.34,
        "activeBacklogs": 0,
        "attendance": 89.79
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_162():
    payload = {
        "rollNo": "21CS107",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.81,
        "activeBacklogs": 5,
        "attendance": 87.75
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_163():
    payload = {
        "rollNo": "21CS439",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.68,
        "activeBacklogs": 3,
        "attendance": 37.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_164():
    payload = {
        "rollNo": "21CS585",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.97,
        "activeBacklogs": 5,
        "attendance": 68.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_165():
    payload = {
        "rollNo": "21CS156",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.16,
        "activeBacklogs": 5,
        "attendance": 86.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_166():
    payload = {
        "rollNo": "21CS727",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.85,
        "activeBacklogs": 5,
        "attendance": 35.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_167():
    payload = {
        "rollNo": "21CS879",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.19,
        "activeBacklogs": 4,
        "attendance": 52.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_168():
    payload = {
        "rollNo": "21CS552",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.11,
        "activeBacklogs": 0,
        "attendance": 69.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_169():
    payload = {
        "rollNo": "21CS948",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.07,
        "activeBacklogs": 2,
        "attendance": 44.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_170():
    payload = {
        "rollNo": "21CS219",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.47,
        "activeBacklogs": 5,
        "attendance": 95.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_171():
    payload = {
        "rollNo": "21CS413",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.19,
        "activeBacklogs": 0,
        "attendance": 31.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_172():
    payload = {
        "rollNo": "21CS494",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.6,
        "activeBacklogs": 2,
        "attendance": 31.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_173():
    payload = {
        "rollNo": "21CS288",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.06,
        "activeBacklogs": 1,
        "attendance": 60.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_174():
    payload = {
        "rollNo": "21CS802",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.15,
        "activeBacklogs": 2,
        "attendance": 62.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_175():
    payload = {
        "rollNo": "21CS249",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.25,
        "activeBacklogs": 1,
        "attendance": 79.6
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_176():
    payload = {
        "rollNo": "21CS492",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.72,
        "activeBacklogs": 2,
        "attendance": 96.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_177():
    payload = {
        "rollNo": "21CS808",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.3,
        "activeBacklogs": 5,
        "attendance": 54.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_178():
    payload = {
        "rollNo": "21CS569",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.74,
        "activeBacklogs": 2,
        "attendance": 57.1
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_179():
    payload = {
        "rollNo": "21CS162",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.98,
        "activeBacklogs": 2,
        "attendance": 38.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_180():
    payload = {
        "rollNo": "21CS601",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.93,
        "activeBacklogs": 1,
        "attendance": 80.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_181():
    payload = {
        "rollNo": "21CS344",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.19,
        "activeBacklogs": 2,
        "attendance": 69.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_182():
    payload = {
        "rollNo": "21CS935",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.59,
        "activeBacklogs": 5,
        "attendance": 77.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_183():
    payload = {
        "rollNo": "21CS219",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.44,
        "activeBacklogs": 5,
        "attendance": 75.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_184():
    payload = {
        "rollNo": "21CS362",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.76,
        "activeBacklogs": 3,
        "attendance": 72.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_185():
    payload = {
        "rollNo": "21CS557",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.54,
        "activeBacklogs": 4,
        "attendance": 51.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_186():
    payload = {
        "rollNo": "21CS923",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.95,
        "activeBacklogs": 1,
        "attendance": 71.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_187():
    payload = {
        "rollNo": "21CS269",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.87,
        "activeBacklogs": 5,
        "attendance": 35.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_188():
    payload = {
        "rollNo": "21CS269",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.21,
        "activeBacklogs": 4,
        "attendance": 87.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_189():
    payload = {
        "rollNo": "21CS356",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.04,
        "activeBacklogs": 3,
        "attendance": 47.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_190():
    payload = {
        "rollNo": "21CS742",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.08,
        "activeBacklogs": 4,
        "attendance": 76.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_191():
    payload = {
        "rollNo": "21CS653",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.24,
        "activeBacklogs": 3,
        "attendance": 40.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_192():
    payload = {
        "rollNo": "21CS783",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.02,
        "activeBacklogs": 0,
        "attendance": 48.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_193():
    payload = {
        "rollNo": "21CS545",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.21,
        "activeBacklogs": 2,
        "attendance": 92.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_194():
    payload = {
        "rollNo": "21CS300",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.8,
        "activeBacklogs": 5,
        "attendance": 67.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_195():
    payload = {
        "rollNo": "21CS849",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.07,
        "activeBacklogs": 5,
        "attendance": 81.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_196():
    payload = {
        "rollNo": "21CS607",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.39,
        "activeBacklogs": 3,
        "attendance": 71.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_197():
    payload = {
        "rollNo": "21CS513",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.89,
        "activeBacklogs": 2,
        "attendance": 32.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_198():
    payload = {
        "rollNo": "21CS502",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.82,
        "activeBacklogs": 4,
        "attendance": 95.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_199():
    payload = {
        "rollNo": "21CS376",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.44,
        "activeBacklogs": 0,
        "attendance": 46.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_200():
    payload = {
        "rollNo": "21CS670",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.11,
        "activeBacklogs": 2,
        "attendance": 34.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_201():
    payload = {
        "rollNo": "21CS856",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.76,
        "activeBacklogs": 2,
        "attendance": 73.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_202():
    payload = {
        "rollNo": "21CS397",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.65,
        "activeBacklogs": 3,
        "attendance": 65.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_203():
    payload = {
        "rollNo": "21CS449",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.18,
        "activeBacklogs": 1,
        "attendance": 96.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_204():
    payload = {
        "rollNo": "21CS413",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.94,
        "activeBacklogs": 3,
        "attendance": 78.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_205():
    payload = {
        "rollNo": "21CS633",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.32,
        "activeBacklogs": 2,
        "attendance": 82.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_206():
    payload = {
        "rollNo": "21CS776",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.37,
        "activeBacklogs": 0,
        "attendance": 55.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_207():
    payload = {
        "rollNo": "21CS904",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.45,
        "activeBacklogs": 2,
        "attendance": 70.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_208():
    payload = {
        "rollNo": "21CS293",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.26,
        "activeBacklogs": 0,
        "attendance": 41.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_209():
    payload = {
        "rollNo": "21CS414",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.67,
        "activeBacklogs": 3,
        "attendance": 34.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_210():
    payload = {
        "rollNo": "21CS459",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.08,
        "activeBacklogs": 3,
        "attendance": 43.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_211():
    payload = {
        "rollNo": "21CS259",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.3,
        "activeBacklogs": 5,
        "attendance": 61.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_212():
    payload = {
        "rollNo": "21CS588",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.29,
        "activeBacklogs": 0,
        "attendance": 51.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_213():
    payload = {
        "rollNo": "21CS713",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.52,
        "activeBacklogs": 2,
        "attendance": 86.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_214():
    payload = {
        "rollNo": "21CS664",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.43,
        "activeBacklogs": 0,
        "attendance": 78.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_215():
    payload = {
        "rollNo": "21CS609",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.92,
        "activeBacklogs": 3,
        "attendance": 81.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_216():
    payload = {
        "rollNo": "21CS736",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.8,
        "activeBacklogs": 4,
        "attendance": 40.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_217():
    payload = {
        "rollNo": "21CS499",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.11,
        "activeBacklogs": 1,
        "attendance": 37.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_218():
    payload = {
        "rollNo": "21CS796",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.44,
        "activeBacklogs": 5,
        "attendance": 82.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_219():
    payload = {
        "rollNo": "21CS456",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.84,
        "activeBacklogs": 1,
        "attendance": 84.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_220():
    payload = {
        "rollNo": "21CS704",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.13,
        "activeBacklogs": 2,
        "attendance": 60.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_221():
    payload = {
        "rollNo": "21CS433",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.94,
        "activeBacklogs": 1,
        "attendance": 54.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_222():
    payload = {
        "rollNo": "21CS686",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.09,
        "activeBacklogs": 4,
        "attendance": 84.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_223():
    payload = {
        "rollNo": "21CS369",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.84,
        "activeBacklogs": 3,
        "attendance": 86.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_224():
    payload = {
        "rollNo": "21CS756",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.44,
        "activeBacklogs": 4,
        "attendance": 57.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_225():
    payload = {
        "rollNo": "21CS737",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.54,
        "activeBacklogs": 1,
        "attendance": 59.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_226():
    payload = {
        "rollNo": "21CS360",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.42,
        "activeBacklogs": 4,
        "attendance": 46.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_227():
    payload = {
        "rollNo": "21CS405",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.23,
        "activeBacklogs": 4,
        "attendance": 82.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_228():
    payload = {
        "rollNo": "21CS764",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.07,
        "activeBacklogs": 1,
        "attendance": 89.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_229():
    payload = {
        "rollNo": "21CS924",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.44,
        "activeBacklogs": 0,
        "attendance": 39.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_230():
    payload = {
        "rollNo": "21CS929",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.25,
        "activeBacklogs": 1,
        "attendance": 33.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_231():
    payload = {
        "rollNo": "21CS647",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.73,
        "activeBacklogs": 4,
        "attendance": 65.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_232():
    payload = {
        "rollNo": "21CS762",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.12,
        "activeBacklogs": 3,
        "attendance": 97.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_233():
    payload = {
        "rollNo": "21CS700",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.19,
        "activeBacklogs": 2,
        "attendance": 48.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_234():
    payload = {
        "rollNo": "21CS443",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.53,
        "activeBacklogs": 5,
        "attendance": 36.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_235():
    payload = {
        "rollNo": "21CS309",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.72,
        "activeBacklogs": 3,
        "attendance": 56.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_236():
    payload = {
        "rollNo": "21CS244",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.39,
        "activeBacklogs": 4,
        "attendance": 64.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_237():
    payload = {
        "rollNo": "21CS943",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.73,
        "activeBacklogs": 4,
        "attendance": 56.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_238():
    payload = {
        "rollNo": "21CS535",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.88,
        "activeBacklogs": 5,
        "attendance": 60.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_239():
    payload = {
        "rollNo": "21CS880",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.83,
        "activeBacklogs": 2,
        "attendance": 31.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_240():
    payload = {
        "rollNo": "21CS444",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.95,
        "activeBacklogs": 3,
        "attendance": 86.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_241():
    payload = {
        "rollNo": "21CS167",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.16,
        "activeBacklogs": 2,
        "attendance": 73.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_242():
    payload = {
        "rollNo": "21CS342",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.26,
        "activeBacklogs": 3,
        "attendance": 92.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_243():
    payload = {
        "rollNo": "21CS145",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.56,
        "activeBacklogs": 3,
        "attendance": 86.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_244():
    payload = {
        "rollNo": "21CS209",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.36,
        "activeBacklogs": 1,
        "attendance": 57.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_245():
    payload = {
        "rollNo": "21CS269",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.15,
        "activeBacklogs": 5,
        "attendance": 38.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_246():
    payload = {
        "rollNo": "21CS368",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.07,
        "activeBacklogs": 1,
        "attendance": 40.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_247():
    payload = {
        "rollNo": "21CS884",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.78,
        "activeBacklogs": 5,
        "attendance": 62.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_248():
    payload = {
        "rollNo": "21CS454",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.4,
        "activeBacklogs": 1,
        "attendance": 79.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_7_249():
    payload = {
        "rollNo": "21CS592",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.46,
        "activeBacklogs": 5,
        "attendance": 81.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

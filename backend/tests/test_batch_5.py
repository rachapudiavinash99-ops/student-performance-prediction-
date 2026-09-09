import pytest
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_prediction_case_5_0():
    payload = {
        "rollNo": "21CS362",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.05,
        "activeBacklogs": 5,
        "attendance": 30.55
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_1():
    payload = {
        "rollNo": "21CS553",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.67,
        "activeBacklogs": 5,
        "attendance": 37.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_2():
    payload = {
        "rollNo": "21CS733",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.98,
        "activeBacklogs": 1,
        "attendance": 42.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_3():
    payload = {
        "rollNo": "21CS492",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.37,
        "activeBacklogs": 5,
        "attendance": 37.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_4():
    payload = {
        "rollNo": "21CS653",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.83,
        "activeBacklogs": 1,
        "attendance": 95.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_5():
    payload = {
        "rollNo": "21CS897",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.76,
        "activeBacklogs": 2,
        "attendance": 94.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_6():
    payload = {
        "rollNo": "21CS869",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.35,
        "activeBacklogs": 0,
        "attendance": 97.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_7():
    payload = {
        "rollNo": "21CS478",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.59,
        "activeBacklogs": 4,
        "attendance": 81.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_8():
    payload = {
        "rollNo": "21CS208",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.6,
        "activeBacklogs": 0,
        "attendance": 50.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_9():
    payload = {
        "rollNo": "21CS546",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.94,
        "activeBacklogs": 5,
        "attendance": 99.51
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_10():
    payload = {
        "rollNo": "21CS824",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.2,
        "activeBacklogs": 3,
        "attendance": 85.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_11():
    payload = {
        "rollNo": "21CS586",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.06,
        "activeBacklogs": 4,
        "attendance": 38.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_12():
    payload = {
        "rollNo": "21CS407",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.56,
        "activeBacklogs": 1,
        "attendance": 77.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_13():
    payload = {
        "rollNo": "21CS716",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.64,
        "activeBacklogs": 3,
        "attendance": 80.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_14():
    payload = {
        "rollNo": "21CS122",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.47,
        "activeBacklogs": 4,
        "attendance": 43.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_15():
    payload = {
        "rollNo": "21CS229",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.49,
        "activeBacklogs": 5,
        "attendance": 53.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_16():
    payload = {
        "rollNo": "21CS977",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.74,
        "activeBacklogs": 5,
        "attendance": 87.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_17():
    payload = {
        "rollNo": "21CS472",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.35,
        "activeBacklogs": 0,
        "attendance": 47.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_18():
    payload = {
        "rollNo": "21CS902",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.17,
        "activeBacklogs": 3,
        "attendance": 60.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_19():
    payload = {
        "rollNo": "21CS740",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.42,
        "activeBacklogs": 3,
        "attendance": 65.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_20():
    payload = {
        "rollNo": "21CS911",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.86,
        "activeBacklogs": 3,
        "attendance": 93.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_21():
    payload = {
        "rollNo": "21CS297",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.26,
        "activeBacklogs": 5,
        "attendance": 91.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_22():
    payload = {
        "rollNo": "21CS613",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.27,
        "activeBacklogs": 4,
        "attendance": 96.96
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_23():
    payload = {
        "rollNo": "21CS998",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.04,
        "activeBacklogs": 2,
        "attendance": 78.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_24():
    payload = {
        "rollNo": "21CS262",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.27,
        "activeBacklogs": 5,
        "attendance": 65.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_25():
    payload = {
        "rollNo": "21CS990",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.13,
        "activeBacklogs": 3,
        "attendance": 49.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_26():
    payload = {
        "rollNo": "21CS249",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.77,
        "activeBacklogs": 4,
        "attendance": 86.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_27():
    payload = {
        "rollNo": "21CS227",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.84,
        "activeBacklogs": 2,
        "attendance": 79.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_28():
    payload = {
        "rollNo": "21CS721",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.43,
        "activeBacklogs": 5,
        "attendance": 67.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_29():
    payload = {
        "rollNo": "21CS333",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.94,
        "activeBacklogs": 1,
        "attendance": 45.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_30():
    payload = {
        "rollNo": "21CS342",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.3,
        "activeBacklogs": 0,
        "attendance": 64.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_31():
    payload = {
        "rollNo": "21CS834",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.62,
        "activeBacklogs": 0,
        "attendance": 42.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_32():
    payload = {
        "rollNo": "21CS974",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.92,
        "activeBacklogs": 1,
        "attendance": 91.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_33():
    payload = {
        "rollNo": "21CS641",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.41,
        "activeBacklogs": 1,
        "attendance": 39.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_34():
    payload = {
        "rollNo": "21CS615",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.49,
        "activeBacklogs": 4,
        "attendance": 75.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_35():
    payload = {
        "rollNo": "21CS604",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.37,
        "activeBacklogs": 5,
        "attendance": 41.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_36():
    payload = {
        "rollNo": "21CS840",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.35,
        "activeBacklogs": 4,
        "attendance": 59.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_37():
    payload = {
        "rollNo": "21CS485",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.66,
        "activeBacklogs": 1,
        "attendance": 76.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_38():
    payload = {
        "rollNo": "21CS433",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.9,
        "activeBacklogs": 0,
        "attendance": 60.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_39():
    payload = {
        "rollNo": "21CS306",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.26,
        "activeBacklogs": 3,
        "attendance": 77.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_40():
    payload = {
        "rollNo": "21CS778",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.06,
        "activeBacklogs": 5,
        "attendance": 74.09
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_41():
    payload = {
        "rollNo": "21CS591",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.25,
        "activeBacklogs": 2,
        "attendance": 39.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_42():
    payload = {
        "rollNo": "21CS852",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.67,
        "activeBacklogs": 0,
        "attendance": 84.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_43():
    payload = {
        "rollNo": "21CS774",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.38,
        "activeBacklogs": 0,
        "attendance": 72.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_44():
    payload = {
        "rollNo": "21CS597",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.06,
        "activeBacklogs": 1,
        "attendance": 43.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_45():
    payload = {
        "rollNo": "21CS990",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.68,
        "activeBacklogs": 1,
        "attendance": 99.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_46():
    payload = {
        "rollNo": "21CS111",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.56,
        "activeBacklogs": 0,
        "attendance": 50.07
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_47():
    payload = {
        "rollNo": "21CS709",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.89,
        "activeBacklogs": 5,
        "attendance": 43.34
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_48():
    payload = {
        "rollNo": "21CS369",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.74,
        "activeBacklogs": 0,
        "attendance": 52.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_49():
    payload = {
        "rollNo": "21CS779",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.55,
        "activeBacklogs": 5,
        "attendance": 37.77
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_50():
    payload = {
        "rollNo": "21CS371",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.96,
        "activeBacklogs": 4,
        "attendance": 99.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_51():
    payload = {
        "rollNo": "21CS250",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.43,
        "activeBacklogs": 5,
        "attendance": 90.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_52():
    payload = {
        "rollNo": "21CS438",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.12,
        "activeBacklogs": 0,
        "attendance": 42.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_53():
    payload = {
        "rollNo": "21CS509",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.44,
        "activeBacklogs": 1,
        "attendance": 75.63
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_54():
    payload = {
        "rollNo": "21CS884",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.92,
        "activeBacklogs": 5,
        "attendance": 65.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_55():
    payload = {
        "rollNo": "21CS772",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.09,
        "activeBacklogs": 2,
        "attendance": 80.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_56():
    payload = {
        "rollNo": "21CS313",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.06,
        "activeBacklogs": 1,
        "attendance": 58.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_57():
    payload = {
        "rollNo": "21CS742",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.45,
        "activeBacklogs": 0,
        "attendance": 54.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_58():
    payload = {
        "rollNo": "21CS660",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.04,
        "activeBacklogs": 5,
        "attendance": 75.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_59():
    payload = {
        "rollNo": "21CS498",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.57,
        "activeBacklogs": 1,
        "attendance": 58.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_60():
    payload = {
        "rollNo": "21CS956",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.28,
        "activeBacklogs": 3,
        "attendance": 92.32
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_61():
    payload = {
        "rollNo": "21CS559",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.19,
        "activeBacklogs": 4,
        "attendance": 78.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_62():
    payload = {
        "rollNo": "21CS928",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.27,
        "activeBacklogs": 1,
        "attendance": 44.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_63():
    payload = {
        "rollNo": "21CS841",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.79,
        "activeBacklogs": 3,
        "attendance": 32.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_64():
    payload = {
        "rollNo": "21CS185",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.8,
        "activeBacklogs": 0,
        "attendance": 94.23
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_65():
    payload = {
        "rollNo": "21CS555",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.6,
        "activeBacklogs": 1,
        "attendance": 95.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_66():
    payload = {
        "rollNo": "21CS347",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.13,
        "activeBacklogs": 3,
        "attendance": 78.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_67():
    payload = {
        "rollNo": "21CS284",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.77,
        "activeBacklogs": 4,
        "attendance": 47.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_68():
    payload = {
        "rollNo": "21CS610",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.14,
        "activeBacklogs": 5,
        "attendance": 30.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_69():
    payload = {
        "rollNo": "21CS813",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.4,
        "activeBacklogs": 3,
        "attendance": 67.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_70():
    payload = {
        "rollNo": "21CS560",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.12,
        "activeBacklogs": 4,
        "attendance": 79.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_71():
    payload = {
        "rollNo": "21CS680",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.15,
        "activeBacklogs": 3,
        "attendance": 93.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_72():
    payload = {
        "rollNo": "21CS300",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.47,
        "activeBacklogs": 4,
        "attendance": 93.18
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_73():
    payload = {
        "rollNo": "21CS909",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.35,
        "activeBacklogs": 5,
        "attendance": 99.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_74():
    payload = {
        "rollNo": "21CS439",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.29,
        "activeBacklogs": 4,
        "attendance": 80.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_75():
    payload = {
        "rollNo": "21CS624",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.61,
        "activeBacklogs": 5,
        "attendance": 90.87
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_76():
    payload = {
        "rollNo": "21CS125",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.42,
        "activeBacklogs": 3,
        "attendance": 86.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_77():
    payload = {
        "rollNo": "21CS409",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.33,
        "activeBacklogs": 4,
        "attendance": 85.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_78():
    payload = {
        "rollNo": "21CS335",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.59,
        "activeBacklogs": 2,
        "attendance": 49.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_79():
    payload = {
        "rollNo": "21CS826",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.4,
        "activeBacklogs": 3,
        "attendance": 77.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_80():
    payload = {
        "rollNo": "21CS931",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.38,
        "activeBacklogs": 1,
        "attendance": 54.08
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_81():
    payload = {
        "rollNo": "21CS960",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.65,
        "activeBacklogs": 3,
        "attendance": 32.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_82():
    payload = {
        "rollNo": "21CS249",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.39,
        "activeBacklogs": 2,
        "attendance": 56.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_83():
    payload = {
        "rollNo": "21CS197",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.16,
        "activeBacklogs": 0,
        "attendance": 97.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_84():
    payload = {
        "rollNo": "21CS792",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.83,
        "activeBacklogs": 1,
        "attendance": 68.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_85():
    payload = {
        "rollNo": "21CS200",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.97,
        "activeBacklogs": 1,
        "attendance": 36.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_86():
    payload = {
        "rollNo": "21CS856",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.27,
        "activeBacklogs": 4,
        "attendance": 70.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_87():
    payload = {
        "rollNo": "21CS250",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.81,
        "activeBacklogs": 0,
        "attendance": 65.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_88():
    payload = {
        "rollNo": "21CS854",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.91,
        "activeBacklogs": 5,
        "attendance": 72.26
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_89():
    payload = {
        "rollNo": "21CS577",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.95,
        "activeBacklogs": 1,
        "attendance": 83.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_90():
    payload = {
        "rollNo": "21CS186",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.9,
        "activeBacklogs": 4,
        "attendance": 84.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_91():
    payload = {
        "rollNo": "21CS567",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.08,
        "activeBacklogs": 5,
        "attendance": 65.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_92():
    payload = {
        "rollNo": "21CS479",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.91,
        "activeBacklogs": 1,
        "attendance": 46.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_93():
    payload = {
        "rollNo": "21CS952",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.48,
        "activeBacklogs": 3,
        "attendance": 61.93
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_94():
    payload = {
        "rollNo": "21CS230",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.02,
        "activeBacklogs": 3,
        "attendance": 62.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_95():
    payload = {
        "rollNo": "21CS920",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.26,
        "activeBacklogs": 2,
        "attendance": 90.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_96():
    payload = {
        "rollNo": "21CS834",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.54,
        "activeBacklogs": 0,
        "attendance": 44.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_97():
    payload = {
        "rollNo": "21CS641",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.14,
        "activeBacklogs": 0,
        "attendance": 94.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_98():
    payload = {
        "rollNo": "21CS233",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.89,
        "activeBacklogs": 2,
        "attendance": 93.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_99():
    payload = {
        "rollNo": "21CS408",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.39,
        "activeBacklogs": 4,
        "attendance": 86.03
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_100():
    payload = {
        "rollNo": "21CS629",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.34,
        "activeBacklogs": 5,
        "attendance": 36.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_101():
    payload = {
        "rollNo": "21CS568",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.07,
        "activeBacklogs": 4,
        "attendance": 79.65
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_102():
    payload = {
        "rollNo": "21CS768",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.53,
        "activeBacklogs": 1,
        "attendance": 38.72
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_103():
    payload = {
        "rollNo": "21CS486",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.62,
        "activeBacklogs": 2,
        "attendance": 47.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_104():
    payload = {
        "rollNo": "21CS982",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.56,
        "activeBacklogs": 2,
        "attendance": 93.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_105():
    payload = {
        "rollNo": "21CS464",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.33,
        "activeBacklogs": 1,
        "attendance": 30.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_106():
    payload = {
        "rollNo": "21CS435",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.4,
        "activeBacklogs": 2,
        "attendance": 67.98
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_107():
    payload = {
        "rollNo": "21CS782",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.7,
        "activeBacklogs": 1,
        "attendance": 53.84
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_108():
    payload = {
        "rollNo": "21CS307",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.28,
        "activeBacklogs": 4,
        "attendance": 35.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_109():
    payload = {
        "rollNo": "21CS106",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.4,
        "activeBacklogs": 3,
        "attendance": 89.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_110():
    payload = {
        "rollNo": "21CS399",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.81,
        "activeBacklogs": 5,
        "attendance": 52.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_111():
    payload = {
        "rollNo": "21CS118",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.68,
        "activeBacklogs": 5,
        "attendance": 70.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_112():
    payload = {
        "rollNo": "21CS286",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.22,
        "activeBacklogs": 4,
        "attendance": 65.24
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_113():
    payload = {
        "rollNo": "21CS359",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.86,
        "activeBacklogs": 3,
        "attendance": 40.25
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_114():
    payload = {
        "rollNo": "21CS574",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.54,
        "activeBacklogs": 2,
        "attendance": 67.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_115():
    payload = {
        "rollNo": "21CS516",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.57,
        "activeBacklogs": 0,
        "attendance": 48.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_116():
    payload = {
        "rollNo": "21CS988",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.17,
        "activeBacklogs": 2,
        "attendance": 73.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_117():
    payload = {
        "rollNo": "21CS677",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.61,
        "activeBacklogs": 4,
        "attendance": 94.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_118():
    payload = {
        "rollNo": "21CS424",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.07,
        "activeBacklogs": 3,
        "attendance": 48.28
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_119():
    payload = {
        "rollNo": "21CS714",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.3,
        "activeBacklogs": 3,
        "attendance": 61.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_120():
    payload = {
        "rollNo": "21CS339",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.3,
        "activeBacklogs": 3,
        "attendance": 49.91
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_121():
    payload = {
        "rollNo": "21CS624",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.57,
        "activeBacklogs": 0,
        "attendance": 39.78
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_122():
    payload = {
        "rollNo": "21CS900",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.7,
        "activeBacklogs": 0,
        "attendance": 71.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_123():
    payload = {
        "rollNo": "21CS307",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.54,
        "activeBacklogs": 5,
        "attendance": 41.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_124():
    payload = {
        "rollNo": "21CS856",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.88,
        "activeBacklogs": 1,
        "attendance": 44.33
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_125():
    payload = {
        "rollNo": "21CS630",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.96,
        "activeBacklogs": 4,
        "attendance": 72.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_126():
    payload = {
        "rollNo": "21CS830",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.47,
        "activeBacklogs": 1,
        "attendance": 38.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_127():
    payload = {
        "rollNo": "21CS908",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.0,
        "activeBacklogs": 1,
        "attendance": 85.29
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_128():
    payload = {
        "rollNo": "21CS161",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.51,
        "activeBacklogs": 0,
        "attendance": 34.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_129():
    payload = {
        "rollNo": "21CS436",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.16,
        "activeBacklogs": 2,
        "attendance": 55.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_130():
    payload = {
        "rollNo": "21CS238",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.28,
        "activeBacklogs": 3,
        "attendance": 39.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_131():
    payload = {
        "rollNo": "21CS756",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.37,
        "activeBacklogs": 4,
        "attendance": 45.57
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_132():
    payload = {
        "rollNo": "21CS107",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.06,
        "activeBacklogs": 4,
        "attendance": 39.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_133():
    payload = {
        "rollNo": "21CS619",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.15,
        "activeBacklogs": 4,
        "attendance": 71.37
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_134():
    payload = {
        "rollNo": "21CS705",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.13,
        "activeBacklogs": 4,
        "attendance": 74.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_135():
    payload = {
        "rollNo": "21CS140",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.49,
        "activeBacklogs": 3,
        "attendance": 51.45
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_136():
    payload = {
        "rollNo": "21CS621",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.26,
        "activeBacklogs": 4,
        "attendance": 30.36
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_137():
    payload = {
        "rollNo": "21CS493",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.13,
        "activeBacklogs": 0,
        "attendance": 59.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_138():
    payload = {
        "rollNo": "21CS563",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.4,
        "activeBacklogs": 1,
        "attendance": 49.66
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_139():
    payload = {
        "rollNo": "21CS108",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.58,
        "activeBacklogs": 1,
        "attendance": 52.97
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_140():
    payload = {
        "rollNo": "21CS793",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.65,
        "activeBacklogs": 4,
        "attendance": 75.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_141():
    payload = {
        "rollNo": "21CS795",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.27,
        "activeBacklogs": 3,
        "attendance": 48.81
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_142():
    payload = {
        "rollNo": "21CS424",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.32,
        "activeBacklogs": 2,
        "attendance": 47.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_143():
    payload = {
        "rollNo": "21CS356",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.83,
        "activeBacklogs": 3,
        "attendance": 47.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_144():
    payload = {
        "rollNo": "21CS845",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.9,
        "activeBacklogs": 2,
        "attendance": 80.58
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_145():
    payload = {
        "rollNo": "21CS264",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.43,
        "activeBacklogs": 0,
        "attendance": 41.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_146():
    payload = {
        "rollNo": "21CS514",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.32,
        "activeBacklogs": 5,
        "attendance": 65.71
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_147():
    payload = {
        "rollNo": "21CS743",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.92,
        "activeBacklogs": 5,
        "attendance": 61.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_148():
    payload = {
        "rollNo": "21CS427",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.82,
        "activeBacklogs": 4,
        "attendance": 37.21
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_149():
    payload = {
        "rollNo": "21CS575",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.92,
        "activeBacklogs": 0,
        "attendance": 31.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_150():
    payload = {
        "rollNo": "21CS310",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.32,
        "activeBacklogs": 2,
        "attendance": 35.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_151():
    payload = {
        "rollNo": "21CS869",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.07,
        "activeBacklogs": 0,
        "attendance": 30.7
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_152():
    payload = {
        "rollNo": "21CS999",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.14,
        "activeBacklogs": 5,
        "attendance": 79.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_153():
    payload = {
        "rollNo": "21CS359",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.63,
        "activeBacklogs": 5,
        "attendance": 68.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_154():
    payload = {
        "rollNo": "21CS897",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.0,
        "activeBacklogs": 0,
        "attendance": 30.04
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_155():
    payload = {
        "rollNo": "21CS583",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.03,
        "activeBacklogs": 1,
        "attendance": 31.5
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_156():
    payload = {
        "rollNo": "21CS946",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.03,
        "activeBacklogs": 1,
        "attendance": 76.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_157():
    payload = {
        "rollNo": "21CS598",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.8,
        "activeBacklogs": 4,
        "attendance": 61.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_158():
    payload = {
        "rollNo": "21CS745",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.93,
        "activeBacklogs": 3,
        "attendance": 51.95
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_159():
    payload = {
        "rollNo": "21CS449",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.25,
        "activeBacklogs": 5,
        "attendance": 33.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_160():
    payload = {
        "rollNo": "21CS506",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.56,
        "activeBacklogs": 3,
        "attendance": 92.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_161():
    payload = {
        "rollNo": "21CS642",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.87,
        "activeBacklogs": 2,
        "attendance": 61.06
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_162():
    payload = {
        "rollNo": "21CS126",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.46,
        "activeBacklogs": 1,
        "attendance": 86.94
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_163():
    payload = {
        "rollNo": "21CS648",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.07,
        "activeBacklogs": 1,
        "attendance": 77.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_164():
    payload = {
        "rollNo": "21CS436",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.49,
        "activeBacklogs": 4,
        "attendance": 83.14
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_165():
    payload = {
        "rollNo": "21CS522",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.93,
        "activeBacklogs": 1,
        "attendance": 91.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_166():
    payload = {
        "rollNo": "21CS612",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.51,
        "activeBacklogs": 3,
        "attendance": 37.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_167():
    payload = {
        "rollNo": "21CS993",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.49,
        "activeBacklogs": 3,
        "attendance": 97.43
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_168():
    payload = {
        "rollNo": "21CS110",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.2,
        "activeBacklogs": 4,
        "attendance": 57.92
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_169():
    payload = {
        "rollNo": "21CS675",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.71,
        "activeBacklogs": 2,
        "attendance": 30.19
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_170():
    payload = {
        "rollNo": "21CS716",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.35,
        "activeBacklogs": 5,
        "attendance": 97.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_171():
    payload = {
        "rollNo": "21CS943",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.92,
        "activeBacklogs": 1,
        "attendance": 82.83
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_172():
    payload = {
        "rollNo": "21CS823",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.36,
        "activeBacklogs": 3,
        "attendance": 98.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_173():
    payload = {
        "rollNo": "21CS662",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.68,
        "activeBacklogs": 3,
        "attendance": 65.15
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_174():
    payload = {
        "rollNo": "21CS566",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.39,
        "activeBacklogs": 0,
        "attendance": 93.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_175():
    payload = {
        "rollNo": "21CS797",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.1,
        "activeBacklogs": 0,
        "attendance": 68.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_176():
    payload = {
        "rollNo": "21CS891",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.25,
        "activeBacklogs": 0,
        "attendance": 60.16
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_177():
    payload = {
        "rollNo": "21CS849",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.89,
        "activeBacklogs": 2,
        "attendance": 31.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_178():
    payload = {
        "rollNo": "21CS238",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.55,
        "activeBacklogs": 1,
        "attendance": 49.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_179():
    payload = {
        "rollNo": "21CS327",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.79,
        "activeBacklogs": 4,
        "attendance": 55.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_180():
    payload = {
        "rollNo": "21CS666",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.67,
        "activeBacklogs": 1,
        "attendance": 97.01
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_181():
    payload = {
        "rollNo": "21CS448",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.06,
        "activeBacklogs": 0,
        "attendance": 36.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_182():
    payload = {
        "rollNo": "21CS506",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.73,
        "activeBacklogs": 2,
        "attendance": 94.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_183():
    payload = {
        "rollNo": "21CS878",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.12,
        "activeBacklogs": 3,
        "attendance": 71.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_184():
    payload = {
        "rollNo": "21CS341",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.27,
        "activeBacklogs": 0,
        "attendance": 31.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_185():
    payload = {
        "rollNo": "21CS127",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.07,
        "activeBacklogs": 3,
        "attendance": 63.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_186():
    payload = {
        "rollNo": "21CS208",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.29,
        "activeBacklogs": 1,
        "attendance": 78.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_187():
    payload = {
        "rollNo": "21CS459",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.67,
        "activeBacklogs": 1,
        "attendance": 68.85
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_188():
    payload = {
        "rollNo": "21CS653",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.05,
        "activeBacklogs": 1,
        "attendance": 72.86
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_189():
    payload = {
        "rollNo": "21CS217",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.55,
        "activeBacklogs": 1,
        "attendance": 93.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_190():
    payload = {
        "rollNo": "21CS912",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.57,
        "activeBacklogs": 1,
        "attendance": 44.76
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_191():
    payload = {
        "rollNo": "21CS344",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.32,
        "activeBacklogs": 2,
        "attendance": 43.68
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_192():
    payload = {
        "rollNo": "21CS179",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.67,
        "activeBacklogs": 3,
        "attendance": 65.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_193():
    payload = {
        "rollNo": "21CS856",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.01,
        "activeBacklogs": 0,
        "attendance": 33.99
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_194():
    payload = {
        "rollNo": "21CS548",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.54,
        "activeBacklogs": 5,
        "attendance": 73.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_195():
    payload = {
        "rollNo": "21CS139",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.82,
        "activeBacklogs": 0,
        "attendance": 87.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_196():
    payload = {
        "rollNo": "21CS587",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.63,
        "activeBacklogs": 4,
        "attendance": 95.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_197():
    payload = {
        "rollNo": "21CS317",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.48,
        "activeBacklogs": 5,
        "attendance": 98.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_198():
    payload = {
        "rollNo": "21CS738",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.33,
        "activeBacklogs": 2,
        "attendance": 74.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_199():
    payload = {
        "rollNo": "21CS755",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.33,
        "activeBacklogs": 0,
        "attendance": 83.8
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_200():
    payload = {
        "rollNo": "21CS768",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.6,
        "activeBacklogs": 1,
        "attendance": 86.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_201():
    payload = {
        "rollNo": "21CS932",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.66,
        "activeBacklogs": 2,
        "attendance": 42.17
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_202():
    payload = {
        "rollNo": "21CS438",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.68,
        "activeBacklogs": 1,
        "attendance": 36.73
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_203():
    payload = {
        "rollNo": "21CS842",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.41,
        "activeBacklogs": 5,
        "attendance": 37.42
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_204():
    payload = {
        "rollNo": "21CS475",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.28,
        "activeBacklogs": 4,
        "attendance": 87.05
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_205():
    payload = {
        "rollNo": "21CS694",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.02,
        "activeBacklogs": 1,
        "attendance": 74.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_206():
    payload = {
        "rollNo": "21CS230",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.85,
        "activeBacklogs": 4,
        "attendance": 39.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_207():
    payload = {
        "rollNo": "21CS977",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.06,
        "activeBacklogs": 0,
        "attendance": 89.82
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_208():
    payload = {
        "rollNo": "21CS414",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.18,
        "activeBacklogs": 3,
        "attendance": 47.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_209():
    payload = {
        "rollNo": "21CS760",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.18,
        "activeBacklogs": 3,
        "attendance": 68.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_210():
    payload = {
        "rollNo": "21CS337",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.52,
        "activeBacklogs": 1,
        "attendance": 69.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_211():
    payload = {
        "rollNo": "21CS552",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.95,
        "activeBacklogs": 3,
        "attendance": 68.44
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_212():
    payload = {
        "rollNo": "21CS723",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.35,
        "activeBacklogs": 5,
        "attendance": 55.4
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_213():
    payload = {
        "rollNo": "21CS914",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.73,
        "activeBacklogs": 1,
        "attendance": 79.89
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_214():
    payload = {
        "rollNo": "21CS958",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.68,
        "activeBacklogs": 2,
        "attendance": 58.52
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_215():
    payload = {
        "rollNo": "21CS121",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.11,
        "activeBacklogs": 2,
        "attendance": 38.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_216():
    payload = {
        "rollNo": "21CS911",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.47,
        "activeBacklogs": 0,
        "attendance": 96.88
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_217():
    payload = {
        "rollNo": "21CS411",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.11,
        "activeBacklogs": 4,
        "attendance": 76.53
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_218():
    payload = {
        "rollNo": "21CS617",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.97,
        "activeBacklogs": 0,
        "attendance": 58.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_219():
    payload = {
        "rollNo": "21CS268",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.51,
        "activeBacklogs": 2,
        "attendance": 42.74
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_220():
    payload = {
        "rollNo": "21CS779",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.51,
        "activeBacklogs": 2,
        "attendance": 60.64
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_221():
    payload = {
        "rollNo": "21CS585",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.27,
        "activeBacklogs": 0,
        "attendance": 54.56
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_222():
    payload = {
        "rollNo": "21CS715",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.78,
        "activeBacklogs": 2,
        "attendance": 36.02
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_223():
    payload = {
        "rollNo": "21CS444",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.56,
        "activeBacklogs": 5,
        "attendance": 61.12
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_224():
    payload = {
        "rollNo": "21CS189",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.62,
        "activeBacklogs": 3,
        "attendance": 53.59
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_225():
    payload = {
        "rollNo": "21CS698",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.82,
        "activeBacklogs": 5,
        "attendance": 68.67
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_226():
    payload = {
        "rollNo": "21CS208",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.61,
        "activeBacklogs": 1,
        "attendance": 43.61
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_227():
    payload = {
        "rollNo": "21CS677",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.76,
        "activeBacklogs": 4,
        "attendance": 95.41
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_228():
    payload = {
        "rollNo": "21CS162",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.76,
        "activeBacklogs": 2,
        "attendance": 53.69
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_229():
    payload = {
        "rollNo": "21CS404",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.81,
        "activeBacklogs": 2,
        "attendance": 54.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_230():
    payload = {
        "rollNo": "21CS735",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.03,
        "activeBacklogs": 2,
        "attendance": 40.9
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_231():
    payload = {
        "rollNo": "21CS393",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.73,
        "activeBacklogs": 3,
        "attendance": 84.39
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_232():
    payload = {
        "rollNo": "21CS223",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.7,
        "activeBacklogs": 5,
        "attendance": 41.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_233():
    payload = {
        "rollNo": "21CS242",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.15,
        "activeBacklogs": 1,
        "attendance": 70.13
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_234():
    payload = {
        "rollNo": "21CS125",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.27,
        "activeBacklogs": 2,
        "attendance": 95.35
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_235():
    payload = {
        "rollNo": "21CS891",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.39,
        "activeBacklogs": 0,
        "attendance": 67.31
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_236():
    payload = {
        "rollNo": "21CS229",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.82,
        "activeBacklogs": 3,
        "attendance": 97.3
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_237():
    payload = {
        "rollNo": "21CS329",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.29,
        "activeBacklogs": 3,
        "attendance": 96.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_238():
    payload = {
        "rollNo": "21CS307",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.79,
        "activeBacklogs": 3,
        "attendance": 75.46
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_239():
    payload = {
        "rollNo": "21CS673",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.12,
        "activeBacklogs": 3,
        "attendance": 92.62
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_240():
    payload = {
        "rollNo": "21CS643",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.21,
        "activeBacklogs": 0,
        "attendance": 97.38
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_241():
    payload = {
        "rollNo": "21CS179",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 5.04,
        "activeBacklogs": 5,
        "attendance": 55.54
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_242():
    payload = {
        "rollNo": "21CS105",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 8.97,
        "activeBacklogs": 3,
        "attendance": 52.22
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_243():
    payload = {
        "rollNo": "21CS811",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.9,
        "activeBacklogs": 4,
        "attendance": 48.48
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_244():
    payload = {
        "rollNo": "21CS882",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.18,
        "activeBacklogs": 0,
        "attendance": 95.0
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_245():
    payload = {
        "rollNo": "21CS460",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.39,
        "activeBacklogs": 2,
        "attendance": 85.49
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_246():
    payload = {
        "rollNo": "21CS294",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 7.25,
        "activeBacklogs": 2,
        "attendance": 79.2
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_247():
    payload = {
        "rollNo": "21CS537",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 6.6,
        "activeBacklogs": 2,
        "attendance": 33.11
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_248():
    payload = {
        "rollNo": "21CS607",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 4.92,
        "activeBacklogs": 2,
        "attendance": 43.27
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

def test_prediction_case_5_249():
    payload = {
        "rollNo": "21CS140",
        "branch": "CSE",
        "semester": "5",
        "cgpa": 9.54,
        "activeBacklogs": 2,
        "attendance": 30.47
    }
    response = client.post("/api/predictions/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "risk" in data
    assert "probability" in data

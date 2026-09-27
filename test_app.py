
from app import app, bookings


def client():
    app.config["TESTING"] = True
    bookings.clear()
    return app.test_client()


def test_health_route():
    response = client().get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_successful_booking():
    c = client()
    response = c.post("/book", data={
        "name": "Ira",
        "facility": "Gym",
        "date": "2099-01-01",
        "slot": "7:00 AM - 8:00 AM"
    })
    assert response.status_code == 302
    assert len(c.get("/api/bookings").json) == 1


def test_double_booking_rejected():
    c = client()
    data = {
        "name": "Student",
        "facility": "Gym",
        "date": "2099-01-01",
        "slot": "7:00 AM - 8:00 AM"
    }
    c.post("/book", data=data)
    response = c.post("/book", data=data)
    assert response.status_code == 409


def test_invalid_facility_rejected():
    response = client().post("/book", data={
        "name": "Student",
        "facility": "Swimming",
        "date": "2099-01-01",
        "slot": "7:00 AM - 8:00 AM"
    })
    assert response.status_code == 400

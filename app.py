
import os
from datetime import date
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

# Demo booking data, stored in memory
bookings = []

FACILITIES = ["Gym", "Badminton", "Basketball"]
SLOTS = ["7:00 AM - 8:00 AM", "8:00 AM - 9:00 AM",
         "5:00 PM - 6:00 PM", "6:00 PM - 7:00 PM"]

COMMIT = os.getenv("RENDER_GIT_COMMIT", "local")[:7]


@app.route("/")
def home():
    return render_template(
        "index.html",
        bookings=bookings,
        facilities=FACILITIES,
        slots=SLOTS,
        today=date.today().isoformat(),
        commit=COMMIT
    )


@app.route("/book", methods=["POST"])
def book():
    name = request.form.get("name", "").strip()
    facility = request.form.get("facility", "")
    booking_date = request.form.get("date", "")
    slot = request.form.get("slot", "")
    if not name:
        return "Please enter your name.", 400

    if facility not in facilities:
        return "Invalid facility selected.", 400

    if slot not in slots:
        return "Invalid time slot selected.", 400
    

    try:
        selected_date = date.fromisoformat(booking_date)
        if selected_date < date.today():
            return "Choose today or a future date", 400
    except ValueError:
        return "Invalid date", 400

    # Prevent double booking of the same facility,
    # date and time slot
    for booking in bookings:
        if (booking["facility"] == facility
                and booking["date"] == booking_date
                and booking["slot"] == slot):
            return "This slot is already booked!", 409

    bookings.append({
        "id": len(bookings) + 1,
        "name": name,
        "facility": facility,
        "date": booking_date,
        "slot": slot
    })

    return redirect("/")


@app.route("/api/bookings")
def api_bookings():
    return jsonify(bookings)


@app.route("/health")
def health():
    return jsonify({"status": "ok", "commit": COMMIT})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

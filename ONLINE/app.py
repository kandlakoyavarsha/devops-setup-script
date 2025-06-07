import streamlit as st

st.title(" Flight Booking Chatbot")

st.header("Book Your Flight Below")

from_location = st.text_input("From")
to_location = st.text_input("To")
num_seats = st.number_input("Number of Seats", min_value=1, step=1)
travel_date = st.date_input("Travel Date")


if st.button("Book Now"):
    if from_location and to_location and num_seats:
        st.success(f"Flight booked from **{from_location}** to **{to_location}** for **{num_seats}** seat(s) on **{travel_date}** ")
    else:
        st.error("Please fill all fields to book your flight.")

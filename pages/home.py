import streamlit as st
from streamlit_extras.grid import grid

import pandas as pd


def app():
    st.write("")

    stops = ["Airport",	"Meenambakkam",	"Nanganallur road",	"Arignar anna alandur metro", "Guindy", 
            "Little Mount",	"Saidapet",	"Nandanam",	"Teynampet",	"AG- DMS",	"Thousand light",
            "LIC",	"Government Estate",	"Dr. M. G. Ramachandran Central Metro",	"High court", "Mannadi",	
            "Washermenpet",	"Thyagaraya College",	"Tondiarpet",	"New Washermenpet",	"Toll Gate",	
            "Kaladipet",	"Thiruvotriyur Theredi",	"Thiruvotriyur",	"Wimco Nagar",	"Wimco Nagar Depot",	
            "Ekkattuthangal",	"Ashok Nagar",	"Vadapalani",	"Arumbakkam",	"Puratchi Thalaivi Dr. J. Jayalalitha CMBT Metro",	
            "Koyambedu",	"Thirumangalam",	"Anna Nagar Tower",	"Anna Nagar East",	"Shenoy Nagar",	
            "Pachiappas College",	"Kilpauk",	"Nehru Park",	"Egmore",	"St. Thomas Mount"]

    routes = ["blue-line", "green-line", "transit"]
    classes = ["Normal", "Deluxe", "A/C"]
    payment_types = ["Card", "Wallet", "UPI"]


    # col1, col2, col3 = st.columns([2, 5, 2])

    # # Column 2: Booking and Quick Access
    # with col2:

    with st.container(border= True):

        c1, c2 = st.columns(2)
        with c1:
            # Container: New Booking
            with st.container(border= True):
                st.subheader("New Booking")
                st.divider()

                depart = st.selectbox(label= "Depart From", options=stops, key= "depart")
                going = st.selectbox(label= "Going To", options=stops, key= "going")
                via = st.selectbox(label= "Via", options=routes, key= "via")

                column1, column2 = st.columns(2)
                # Column 1: Routes
                with column1:
                    # route_vis = st.button(label= "Route", key= "route")
                    url = "https://chennaimetrorail.org/wp-content/uploads/2022/05/Line-Map.pdf"
                    st.link_button(label="Route", url= url)
                
                # Column 2: Fare
                with column2:
                    fare = st.button(label= "Fare", key= "fare")

        with c2:
            # Container: Quick Access
            with st.container(border= True):
                st.subheader("Quick Services")
                st.divider()

                show_ticket = st.button(label= "Show Ticket", key= "show-ticket")
                history = st.button(label= "Booking History", key= "history")
                cancel = st.button(label= "Cancel Ticket", key= "cancel")
                balance = st.button(label= "Check Balance", key= "balance")


    # Spacings
    st.write("")
    st.write("")
    st.write("")


    # # Route
    # if route_vis:






    # Fare
    if fare:

        # Cost of trip
        fare_book = pd.read_csv("Data/metro/metro_fare.csv")

        stops_dict = {"Airport": 0,	"Meenambakkam": 1,	"Nanganallur road": 2,	"Arignar anna alandur metro": 3, "Guindy": 4, 
                    "Little Mount": 5,	"Saidapet":6,	"Nandanam":7,	"Teynampet":8,	"AG- DMS":9,	"Thousand light":10,
                    "LIC":11, "Government Estate":12,	"Dr. M. G. Ramachandran Central Metro":13,	"High court":14, "Mannadi":15,	
                    "Washermenpet":16,	"Thyagaraya College":17,	"Tondiarpet":18,	"New Washermenpet":19,	"Toll Gate":20,	
                    "Kaladipet":21,	"Thiruvotriyur Theredi":22,	"Thiruvotriyur":23,	"Wimco Nagar":24,	"Wimco Nagar Depot":25,	
                    "Ekkattuthangal":26,	"Ashok Nagar":27,	"Vadapalani":28,	"Arumbakkam":29,	"Puratchi Thalaivi Dr. J. Jayalalitha CMBT Metro":30,	
                    "Koyambedu":31,	"Thirumangalam":32,	"Anna Nagar Tower":33,	"Anna Nagar East":34,	"Shenoy Nagar":35,	
                    "Pachiappas College":36,	"Kilpauk":37,	"Nehru Park":38,	"Egmore":39,	"St. Thomas Mount":40}

        index_depart = stops_dict.get(depart)
        index_going = stops_dict.get(going)
        cost = fare_book.iloc[index_depart, index_going+1]

        # Dashboard
        with st.container(border= True):
            sc1, sc2 = st.columns(spec= 2, gap= "medium")
            with sc1:
                st.subheader("Ticket Booking")
                st.divider()

                sub1, sub2 = st.columns(2)
                with sub1:
                    adult_count = st.number_input(label= "Adult", value= 1, min_value= 1, max_value= 15, key= "adult")
                    
                with sub2:
                    child_count = st.number_input(label= "Child", value= 0, min_value= 0, max_value= 14, key= "child")
                
                t_type = st.selectbox(label= "Ticket Type (Class)", options= classes, index= 0, key= "type")
                payment = st.selectbox(label= "Payment Type", options= payment_types, index= 1, key= "payment")

            with sc2:
                st.subheader("Ticket Summary")
                st.divider()

                sub1, sub2 = st.columns(2)
                with sub1:
                    st.write("Source Station: ", depart)
                
                with sub2:
                    st.write("Destination Station: ", going)

                st.write("Via Route: ", via)

                st.write(f"Travel Time: " + "mins")

                sub1, sub2 = st.columns(2)
                with sub1:
                    st.write("Adult: ", adult_count)                
                    st.write("Ticket Type: ", t_type)
                    

                with sub2:
                    st.write("Child: ", child_count)
                    st.write("Payment type: ", payment)

            st.divider()
            cost_per_person = cost
            passengers = adult_count + child_count
            cost = passengers * cost_per_person
            st.write(f"Total Fare: ₹{cost}/-")

            st.divider()
            st.write("Ticket validity ends in 3 hrs")

            st.divider()
            book = st.button(label= "Book Ticket", key= "book")



app()


    # def fare_summary():
    #     mygrid = grid()

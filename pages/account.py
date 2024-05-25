import streamlit as st
from streamlit_extras.switch_page_button import switch_page

import pymysql
import pandas as pd


# from main import myconnection, cur



def app():

    # Create connection
    myconnection = pymysql.connect(
        host = "127.0.0.1",
        user = "root",
        passwd = "password"
    )
    cur = myconnection.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS UTS_db")
    cur.close()
    myconnection.close()

    # Connect to SQL database
    myconnection = pymysql.connect(
        host = '127.0.0.1',
        user='root',
        passwd='password',
        database = "UTS_db"
        )
    cur = myconnection.cursor()

    # Create SQL table
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
                email_id VARCHAR(255) PRIMARY KEY,
                password VARCHAR(255)
                )""")

    st.write("")
    st.write("")


    def sign_up_with_email_and_password(email, password, connection, cursor):
        try:
            # Insert Query
            cursor = connection.cursor()
            acc_insert_sql = f"INSERT INTO users (email_id, password) VALUES ('{email}', '{password}')"
            cursor.execute(acc_insert_sql)
            connection.commit()

            # Data Validation
            cursor.execute("SELECT email_id FROM users")
            email_result = cursor.fetchall()
            email_df = pd.DataFrame(email_result, columns=["Email"])

            emails_registered = email_df["Email"].values.tolist()

            if email in emails_registered:
                st.error("Account already exists. Please continue to login")
            
            else:
                st.success("Account successfully created.")

        except Exception as e:
            st.error("Error: ", e)
            return None


    def sign_in_with_email_and_password(email, password, connection, cursor):
        try:
            # Data Validation
            cursor = connection.cursor()
            cursor.execute(f"SELECT email_id, password FROM users WHERE email_id = '{email}' and password = '{password}' ")
            email_result = cursor.fetchone()
            email_df = pd.DataFrame(email_result, columns=["Email", "Password"])

            num_rows = email_df.shape[0]

            if num_rows == 0:
                st.success("User successfully logged in.")

        except:
            st.error("Email-ID/Password is invalid.")


    def set_new_password(email, password, connection, cursor):
        try:
            # Update password
            cursor.execute(f"UPDATE users SET password = '{password}' WHERE email_id = '{email}' ")
            cursor.commit()

            st.success("Password is set. Please login with the new password.")

        except Exception as e:
            st.error("Error: ", e)
            return None
            
    welcome = st.button(label= "Welcome to UTS...", key= "welcome")

    # if welcome:
    # Container : Account - login
    c1, c2, c3 = st.columns(3)
    with c2:
        st.subheader("UTS Account - Login")

        with st.container():

            actual_email = st.text_input("Email Address", key= "act_email")
            actual_password = st.text_input("Password", type="password", key= "act_pass")   

            c1, c2, c3 = st.columns([1,2, 2])
            # Column 1: Login
            with c1:
                login = st.button(label= "LOGIN", key= "login")
            
            # Column 2: Forgot password
            with c3:
                forgot_pass = st.button(label= "Forget Password ?", key= "forgot")

        sign_up = st.button(label= "Don't have an account?... Sign-up for free", key= "sign-up")


        if sign_up:
            # Container : Create My Acoount
            # c1, c2, c3 = st.columns(3)
            # with c2:
            st.subheader("Create My UTS Account")

            with st.form("Create Account"):

                create_email = st.text_input("Email Address", key= "cre_email")
                create_password = st.text_input("Password", type="password", key= "cre_pass")   

                submit = st.form_submit_button(label= "Submit")

                if submit:
                    sign_up_with_email_and_password(create_email, create_password, myconnection, cur)

        elif login:
            sign_in_with_email_and_password(actual_email, actual_password, myconnection, cur)
            # st.switch_page("pages/home.py")
        
        elif forgot_pass:
            # Container: Forgot Password
            with st.form("Forgot Password"):

                email_reg =  st.text_input("Email Address", key= "reg_mail")

                st.write("Type the new password")

                new_pass = st.text_input("New Password", type="password", key= "new_pass")
                confirm_pass = st.text_input("Confirm Password", type="password", key= "confirm_pass")

                if (len(confirm_pass) > 0) and (new_pass == confirm_pass):
                    st.success("Passwords match!")
                elif (len(new_pass) > 0) and (len(confirm_pass) > 0):
                    st.info("Passwords don't match")

                submit1 = st.form_submit_button(label= "Submit")

                if submit1:
                    set_new_password(email_reg, confirm_pass, myconnection, cur)








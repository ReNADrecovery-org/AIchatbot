import sqlite3


def get_modifiers(claim_id):
    try:
        conn = sqlite3.connect("./static/database.db")
        cursor = conn.cursor()
        sql_query = f"SELECT * FROM Modifiers WHERE ClaimID = {claim_id}"
        # Use a parameterized query to select all records with the given patient_id
        cursor.execute(sql_query)
        # Fetch all records
        records = cursor.fetchall()
        modifiers = []
        for record in records:
            modifiers.append(record[1])
        conn.close()
        print(modifiers)

        return modifiers
    except sqlite3.Error as e:
        print("SQLite error:", e)
        return []


def get_procedures(claim_id):
    try:
        conn = sqlite3.connect("./static/database.db")
        cursor = conn.cursor()
        sql_query = f"SELECT * FROM Procedures WHERE ClaimID = {claim_id}"
        # Use a parameterized query to select all records with the given patient_id
        cursor.execute(sql_query)
        # Fetch all records
        records = cursor.fetchall()
        procedures = []
        for record in records:
            procedures.append(record[1])
        conn.close()
        print(procedures)

        return procedures
    except sqlite3.Error as e:
        print("SQLite error:", e)
        return []


def get_patient_history(patient_id):
    try:
        conn = sqlite3.connect("./static/database.db")
        cursor = conn.cursor()
        sql_query = (
            f"SELECT * FROM patient_medical_history WHERE patient_id = {patient_id}"
        )
        # Use a parameterized query to select all records with the given patient_id
        cursor.execute(sql_query)
        # Fetch all records
        records = cursor.fetchall()
        question_answer = []
        for record in records:
            question_id = record[1]
            answer = record[2]
            question_answer.append(
                {
                    "question_id": question_id,
                    "answer": answer,
                    "last_modified_by": record[3],
                    "last_modified_date": record[4],
                }
            )

        patient_id = records[0][0]
        note_last_modified_by = records[0][5]
        note_last_modified_date = records[0][6]
        section_note = records[0][7]

        patient_info = {
            "patient_id": patient_id,
            "question_answer": question_answer,
            "note_last_modified_by": note_last_modified_by,
            "note_last_modified_date": note_last_modified_date,
            "section_note": section_note,
        }

        # Close the database connection
        conn.close()
        print(patient_info)

        return patient_info
    except sqlite3.Error as e:
        print("SQLite error:", e)
        return []

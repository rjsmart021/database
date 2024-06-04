from mysql.connector import Error

from connect_database import ConnectDatabase


def add_member(db):
    name = input("Enter name: ")
    id = int(input('Enter Member ID: '))
    age = int(input("Enter age: "))

    try:
        cursor = db.cursor()
        insert_command = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
        values = (id, name, age)
        cursor.execute(insert_command, values)
        db.commit()
        print("Member Added Successfully!!!")

    except Error as e:
        print(f"Error in adding member. Error msg: {e}")


def add_work_out_session(db):
    member_id = int(input("Enter member ID: "))
    session_id = int(input("Enter session ID: "))
    session_date = input("Enter session date (YYYY-MM-DD): ")
    session_time = input("Enter session time: ")
    activity = input("Enter activity: ")

    try:
        cursor = db.cursor()
        is_member_query = "select count(*) from Members where id=%s"
        cursor.execute(is_member_query, (member_id,))
        result = cursor.fetchone()
        if result[0] == 0:
            print("Member ID not exists")
            return
        insert_command = "INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity)" \
                         " VALUES (%s, %s, %s, %s, %s)"
        values = (session_id, member_id, session_date, session_time, activity)

        cursor.execute(insert_command, values)
        db.commit()
        print("Workout session Added Successfully!!!")

    except Error as e:
        print(f"Error in adding Session. Error msg: {e}")


def update_member_age(db):
    member_id = input("Enter member ID: ")
    new_age = input("Enter new age: ")
    try:
        cursor = db.cursor()
        sql = "UPDATE Members SET age = %s WHERE id = %s"
        val = (new_age, member_id)
        cursor.execute(sql, val)
        db.commit()
        if cursor.rowcount > 0:
            print("Member age updated successfully")
        else:
            print("Member does not exist")
    except Error as err:
        print(f"Error in updating member age: {err}")


def delete_workout_session(db):
    session_id = input("Enter session ID: ")
    try:
        cursor = db.cursor()
        sql = "DELETE FROM WorkoutSessions WHERE session_id = %s"
        val = (session_id,)
        cursor.execute(sql, val)
        db.commit()
        if cursor.rowcount > 0:
            print("Workout session deleted successfully")
        else:
            print("Session ID does not exist")
    except Error as err:
        print(f"Error deleting workout session: {err}")


def get_members_in_age_range(db, start_age, end_age):
    try:
        cursor = db.cursor()
        sql_query = "SELECT name, age FROM Members WHERE age BETWEEN %s AND %s"
        val = (start_age, end_age)
        cursor.execute(sql_query, val)
        results = cursor.fetchall()

        # Print the results
        for result in results:
            name, age = result
            print(f"Name: {name}, Age: {age}")

    except Error as err:
        print(f"Error retrieving members: {err}")


if __name__ == '__main__':
    db = ConnectDatabase(database='fitness_center').get_db()

    if db is None:
        print("no db connection established")
        exit(-1)

    # add_member(db)
    # add_work_out_session(db)
    # update_member_age(db)
    # delete_workout_session(db)
    get_members_in_age_range(db, 23, 29)

import sqlite3

class AdvancedUserOperations:
  def __init__(self):
    self.conn = sqlite3.connect("user_database.db")
    self.cursor = self.conn.cursor()
    self._create_user_table()

  def _create_user_table(self):
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        address TEXT
        )
    """
    self.cursor.execute(create_table_sql)
    self.conn.commit()
    

  def create_user_with_profile(self, name, email, password, age=None, gender=None, address=None):
    insert_user_sql = """
        INSERT INTO user (name, email, password, age, gender, address)
        VALUES (?, ?, ?, ?, ?, ?)
    """
    user_data = (name, email, password, age, gender, address)
    try:
        self.cursor.execute(insert_user_sql, user_data)
        self.conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error creating user: {e}")
        return False

  def retrieve_users_by_criteria(self, email=None, min_age=None, max_age=None, gender=None):
    select_users_sql = """
        SELECT * FROM user WHERE
        (? IS NULL OR email = ?) AND
        (? IS NULL OR age >= ?) AND
        (? IS NULL OR AGE <= ?) AND
        (? IS NULL OR  gender = ?)
    """
    criteria = (email, email, min_age, min_age, max_age, max_age, gender, gender)
    try:
        self.cursor.execute(select_users_sql, criteria)
        return self.cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error retrieving users: {e}")
        return None

  def update_user_profile(self, email, age=None, gender=None, address=None):
    update_user_sql = """
        UPDATE user
        SET age = COALESCE(?, age),
            gender = COALESCE(?, gender),
            address = COALESCE(?, address)
        WHERE email = ?
    """
    update_data = (age, gender, address, email)
    try:
       self.cursor.execute(update_user_sql, update_data)
       if self.cursor.rowcount > 0:
           self.conn.commit()
           return True
       else:
           print(f"No user found with email: {email}")
           return False
    except sqlite3.Error as e:
       print(f"Error updating user profile: {e}")
       return False

  def delete_users_by_criteria(self, email=None):
    delete_users_sql = """
        DELETE FROM user WHERE email = ?
    """
    try:
       self.cursor.execute(delete_users_sql, (email,))
       if self.cursor.rowcount > 0:
           self.conn.commit()
           return True
       else:
           print(f"No user found with email: {email}")
           return False
    except sqlite3.Error as e:
       print(f"Error deleteing user: {e}")
       return False

  def __del__(self):
    self.conn.close()  

if __name__ == "__main__":
    user_operations = AdvancedUserOperations()    
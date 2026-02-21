import psycopg2
from psycopg2 import pool
from config import Config

class DatabaseManager:
    def __init__(self):
        """Initializes the PostgreSQL connection pool using Config values."""
        try:
            # We use individual Config variables instead of a single DATABASE_URL
            self.connection_pool = pool.SimpleConnectionPool(
                1, 10,
                dbname=Config.DB_NAME,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                host=Config.DB_HOST,
                port=Config.DB_PORT
            )
            self._initialize_db()
            print("✅ DatabaseManager: Connected to PostgreSQL successfully.")
        except Exception as error:
            print(f"❌ DatabaseManager: Connection failed. Error: {error}")

    def _initialize_db(self):
        """Ensures the table exists with the correct columns, including meeting_name."""
        conn = self.connection_pool.getconn()
        try:
            cursor = conn.cursor()
            # This creates the table with the columns seen in your pgAdmin
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS appointments (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    phone VARCHAR(20),
                    appointment_time TIMESTAMP,
                    meeting_name VARCHAR(255)
                );
            """)
            conn.commit()
            cursor.close()
        except Exception as e:
            print(f"❌ Database Initialization Error: {e}")
        finally:
            self.connection_pool.putconn(conn)

    def log_appointment(self, name, phone, appointment_time, meeting_name):
        """
        Saves a confirmed meeting to the database.
        This matches your table schema: id, name, phone, appointment_time, meeting_name.
        """
        conn = self.connection_pool.getconn()
        if conn:
            try:
                cursor = conn.cursor()
                # SQL Query updated to include all required fields for your flow
                cursor.execute(
                    "INSERT INTO appointments (name, phone, appointment_time, meeting_name) VALUES (%s, %s, %s, %s)",
                    (name, phone, appointment_time, meeting_name)
                )
                conn.commit()
                cursor.close()
                print(f"✅ Database: Logged '{meeting_name}' for {name}")
                return True
            except Exception as e:
                print(f"❌ Database Log Error: {e}")
                conn.rollback()
                return False
            finally:
                self.connection_pool.putconn(conn)

    def close_all_connections(self):
        """Closes the connection pool."""
        if self.connection_pool:
            self.connection_pool.closeall()
            print("Database connections closed.")
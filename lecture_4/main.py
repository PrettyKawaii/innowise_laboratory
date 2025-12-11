import sqlite3
import os

def main():
    """
    Create and populate student grades database.
    """
    # Paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, 'school.db')
    sql_script_path = os.path.join(current_dir, 'script.sql')
    
    # Remove old DB if exists
    if os.path.exists(db_path):
        os.remove(db_path)
    
    # Connect to DB
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Read and execute SQL script
    with open(sql_script_path, 'r', encoding='utf-8') as f:
        sql_script = f.read()
    
    # Execute the entire script
    cursor.executescript(sql_script)
    conn.commit()
    
    print("Database created successfully")
    
    # Verify it worked
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print(f"Tables created: {[t[0] for t in tables]}")
    
    conn.close()

if __name__ == "__main__":
    main()
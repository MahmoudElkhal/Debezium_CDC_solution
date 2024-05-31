import psycopg2
import time

# Configuration for source and target databases
source_config = {
    'dbname': 'exampledb',
    'user': 'pfaa2024',
    'password': 'pfaa2024',
    'host': 'localhost',
    'port': '5432'
}

target_config = {
    'dbname': 'targetdb',
    'user': 'pfaa2024',
    'password': 'pfaa2024',
    'host': 'localhost',
    'port': '5433'
}

# Insert 1000 rows into the source database
def insert_rows():
    conn = psycopg2.connect(**source_config)
    cursor = conn.cursor()
    for i in range(1, 1001):
        cursor.execute(f"INSERT INTO public.unit1 VALUES ({i}, 'att1_test_row_{i}','att2_test_row_{i}','att3_test_row_{i}')")
    conn.commit()
    cursor.close()
    conn.close()

# Monitor the target database for the last inserted row
def monitor_target():
    conn = psycopg2.connect(**target_config)
    cursor = conn.cursor()
    start_time = time.time()
    
    while True:
        cursor.execute("SELECT * FROM public.unit1 WHERE id = 1000")
        row = cursor.fetchone()
        if row:
            end_time = time.time()
            break
        time.sleep(0.1)  # Poll every 100 ms
    
    cursor.close()
    conn.close()
    return start_time, end_time

# Main function to insert and monitor
def main():
    print("Inserting rows...")
    insert_rows()
    print("Monitoring target database...")
    start_time, end_time = monitor_target()
    total_time = end_time - start_time
    print(f"Total transaction time for 1000 inserts: {total_time:.3f} seconds")

if __name__ == "__main__":
    main()

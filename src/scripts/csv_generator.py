import sqlite3
import csv
from contextlib import closing

def create_csv(database_path, table_name, output_file):
    with closing(sqlite3.connect(database_path)) as conn:
        conn.row_factory = sqlite3.Row
        with closing(conn.cursor()) as c:
            c.execute("SELECT * FROM {}".format(table_name))
            items = [dict(row) for row in c.fetchall()]

        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)

            if table_name == 'customers':
                writer.writerow(['region', 'total_customers', 'affected_customers', 'created_at'])
                for item in items:
                    writer.writerow([item['region'], item['total_customers'], item['affected_customers'], item['created_at']])


            elif table_name == 'outages':
                writer.writerow(['region', 'area', 'zone', 'created_at'])
                for item in items:
                    writer.writerow([item['region'], item['area'], item['zone'], item['created_at']])

if __name__ == "__main__":
    create_csv('././data/raw/luma/luma_info.db', 'outages', '././data/clean/luma/luma_outages.csv')
    create_csv('././data/raw/luma/luma_info.db', 'customers', '././data/clean/luma/luma_customers.csv')

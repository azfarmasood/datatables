import os  
from datatables.app.controllers.scrap_tables_data import fetch_webpage
from datatables.app.controllers.exctract_data_from_tables import extract_table_data
from datatables.app.controllers.cleaning_data import clean_data
from datatables.app.controllers.data_analysis import analyze_data
from datatables.app.controllers.save_to_csv import save_to_csv

def main():
    """
    Scrapes employee data from DataTables demo page and saves it
    """
    url = 'https://datatables.net/examples/basic_init/zero_configuration.html'
    
    # The table ID on the demo page - we'll keep their original ID 'example'
    # but we're using it to get employee data
    table_id = 'example'
    
    # Create a data folder for our CSVs if it doesn't exist
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_folder = os.path.join(current_dir, 'data', 'csv')
    os.makedirs(csv_folder, exist_ok=True)
    
    # CSV paths
    raw_csv = os.path.join(csv_folder, 'employee_data_raw.csv')
    clean_csv = os.path.join(csv_folder, 'employee_data_clean.csv')
    
    try:
        # Grab the webpage
        soup = fetch_webpage(url)
        
        print("\n--- Getting employee data ---")
        df = extract_table_data(soup, table_id)
        save_to_csv(df, raw_csv)
        
        print("\n--- Cleaning up the data ---")
        clean_df = clean_data(df)
        
        print("\n--- Crunching some numbers ---")
        stats = analyze_data(clean_df)
        
        # Show what we found
        print("\n📊 Quick Summary:")
        print(f"Found data for {stats['total_employees']} employees")
        
        print("\nSalary Range:")
        for key, val in stats['salary_stats'].items():
            print(f"  - {key}: ${val:,.2f}")
            
        print("\nAge Stats:")
        for key, val in stats['age_stats'].items():
            print(f"  - {key}: {val}")
            
        print("\nOffice Breakdown:")
        for office, count in sorted(stats['employees_by_office'].items(), key=lambda x: x[1], reverse=True):
            print(f"  - {office}: {count} people")
        
        # Save the cleaned version
        save_to_csv(clean_df, clean_csv)
        
        print("\n✨ Done! Check the data folder for CSV files ✨")
        return True
        
    except Exception as e:
        print(f"\n❌ Oops! Something went wrong: {e}")
        return False

if __name__ == "__main__":
    main()

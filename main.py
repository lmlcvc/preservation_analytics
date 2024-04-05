import csv
import os


def clean_data(input_file, output_file):
    allowed_funding_sources = {'international organization', 'governmental', 'non-profit', 'private donors'}
    allowed_conditions = {'good', 'fair', 'poor'}
    allowed_designations = {'conserved', 'under consideration', 'endangered'}

    if not os.path.exists(output_file):
        # Input CSV file for reading
        with open(input_file, 'r', newline='') as infile:
            reader = csv.reader(infile)
            header = next(reader)  # Read the header row
            header = [col.strip().lower() for col in header]  # Convert header to lowercase and strip whitespace

            # Ensure expected columns are present
            expected_columns = ['site_id', 'site_name', 'site_age_years', 'geographical_location', 'funding_source',
                                'conservation_technique', 'condition', 'designation']
            for column in expected_columns:
                if column not in header:
                    print(f"Error: '{column}' column is missing from the CSV file.")
                    return

            # Output CSV file for writing
            with open(output_file, 'w', newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(header)

                for row in reader:
                    # Clean data by stripping whitespace
                    row = [col.strip() for col in row]

                    # Convert specific column values to lowercase
                    funding_source_index = header.index('funding_source')
                    condition_index = header.index('condition')
                    designation_index = header.index('designation')
                    row[funding_source_index] = row[funding_source_index].lower()
                    row[condition_index] = row[condition_index].lower()
                    row[designation_index] = row[designation_index].lower()

                    # Check if values are allowed for specific columns
                    if row[funding_source_index] not in allowed_funding_sources:
                        print(f"Warning: Invalid funding source '{row[funding_source_index]}' found in row: {row}")
                    if row[condition_index] not in allowed_conditions:
                        print(f"Warning: Invalid condition '{row[condition_index]}' found in row: {row}")
                    if row[designation_index] not in allowed_designations:
                        print(f"Warning: Invalid designation '{row[designation_index]}' found in row: {row}")

                    # Write the cleaned row to the output file
                    writer.writerow(row)


if __name__ == "__main__":
    clean_data('dataset.csv', 'cleaned_dataset.csv')

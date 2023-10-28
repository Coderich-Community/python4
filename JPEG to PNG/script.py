import spire.xls as xls

def convert_jpeg_to_png(input_file_path, output_file_path):
    workbook = xls.Workbook()
    workbook.LoadFromFile(input_file_path)

    # Convert JPEG to PNG by calling Workbook.save() method.
    workbook.save(output_file_path, Format=xls.ExcelFormat.PNG)

    # Get the conversion result.
    conversion_result = workbook.SaveResult

    return conversion_result

if __name__ == "__main__":
    input_file_path = "input.jpg"
    output_file_path = "output.png"

    conversion_result = convert_jpeg_to_png(input_file_path, output_file_path)

    if conversion_result:
        print("The JPEG file was successfully converted to PNG.")
    else:
        print("An error occurred while converting the JPEG file to PNG.")

def celsius_converter(f_temp):
    celsius = (float(f_temp)-32)*5/9
    return round(celsius,2)
def parse_and_clean(line):
    line=line.strip()
    if line =="":
        return None
    parts = line.split("|")
    if len(parts) !=5:
        return None 
    parts=[part.strip() for part in parts]
    if parts[4] !="ACTIVE":
        return None
    if parts[2] in  ["N/A", "ERROR"]:
        return None
    return parts
skipped_lines = 0
with open ("environmental_raw.txt", "r") as infile, open ("cleaned_output.csv","w") as outfile:
    for line in infile:
        result = parse_and_clean(line)
        if result is None:
            skipped_lines +=1
        else:
            celsius = celsius_converter(result[2])
            result [2] = str(celsius)
            outfile.write(",".join (result)+"\n")
print(f"Skipped corrupted lines:{skipped_lines}")

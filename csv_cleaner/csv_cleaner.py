import argparse, csv

def add_arg():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--input", required = True)
    arg_parser.add_argument("--output", required = True)
    arg_parser.add_argument("--columns", nargs = "+", required = True)
    arg_parser.add_argument("--summary", action = "store_true")
    arg_parser.add_argument("--drop-missing", action = "store_true")

    return arg_parser.parse_args()

def read_csv(input_path):
    with open(input_path, "r", encoding = "utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)
    
def is_missing(mem, field_list):
    for field in field_list:
        if field not in mem:
            return True
        if mem[field] == None or mem[field].strip() == "":
            return True
    return False
        

def drop_missing(csv_list, field_list, is_drop_missing):
    if not is_drop_missing:
        return csv_list
    
    csv_list = [mem for mem in csv_list if not is_missing(mem, field_list)]
    return csv_list

def print_summary(csv_list, field_list):
    print("row count :", len(csv_list))
    print("col fields :", [field for field in field_list])

def save_csv(output_path, csv_list, field_list):
    with open(output_path, "w", encoding = "utf-8", newline = "") as file:
        writer = csv.DictWriter(file, fieldnames = field_list, extrasaction = "ignore")
        writer.writeheader()
        writer.writerows(csv_list)
    
def main():
    args = add_arg()
    csv_list = read_csv(args.input)
    csv_list = drop_missing(csv_list, args.columns, args.drop_missing)
    save_csv(args.output, csv_list, args.columns)
    if args.summary:
        print_summary(csv_list, args.columns)

if __name__ == "__main__":
    main()
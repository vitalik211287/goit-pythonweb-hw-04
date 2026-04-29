import argparse
import pathlib

# parser = argparse.ArgumentParser(description="Sort files by extension")

# parser.add_argument('source', help='Path to source folder')
# parser.add_argument('destination', help='Path to destination folder')

# args = parser.parse_args()

# print("Source:", args.source)
# print("Destination:", args.destination)
# def sumarize(a, b):
#     print(a + b)

# sumarize(args.a, args.b)

p = pathlib.Path("example.txt")
p.write_text("Hello, world!")
print(p.read_text()) 
print("Exists:", p.exists())


# def read_folder(folder_path):
#     with open(folder_path, 'r') as folder:
#         print(folder.read())

# def copy_file(source_path, destination_path):
#     pass


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='File operations')
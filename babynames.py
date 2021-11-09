import re

rankedMales = {}
rankedFemales = {}


def extract_names(filename):
    '''
    Called by main to iterate through multiple file names.
    Provides code to names and rank numbers from a given html file
    '''
    with open(filename) as f:
        count = 0
        year = 0
        #iterate line by line in the file
        for line in f:
            # Extract the year
            # We can observe a standard pattern in the html files, so:
            match = re.match(pattern='<h3 align="center">Popularity in (\d+)</h3>', string=line)
            if match is not None:
                year = match.group(1)
                print("Year:", year)

            # Extract names and rank numbers
            match = re.match(pattern='<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',string=line)
            if match is not None:
                rank = match.group(1)
                male_name = match.group(2)
                female_name = match.group(3)
                rankedMales[male_name] = [year, rank]
                rankedFemales[female_name] = [year, rank]
                print(rank, male_name, female_name)

            if count == 30:
                break


def main():
    for year in range(1990, 2009, 2):
        extract_names(f"baby{year}.html")


if __name__ == "__main__":
    main()

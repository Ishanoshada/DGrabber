import requests
from re import findall
import time

class DomainGrabber:
    def __init__(self):
        self.domains = []

    def search_domains(self, keyword):
        try:
            response = requests.get(f'https://website.informer.com/search.php?query={keyword}')
            response.raise_for_status()  # Check for HTTP errors
            matches = findall('data-domain="(.*)"', response.text)
            for site in matches:
                self.domains.append(site)
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while fetching data for '{keyword}': {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def get_user_input(self):
        try:
            source = input("\n\tEnter 'file' to input keywords from a file, or 'manual' for manual input: ")

            if source.lower() == 'file':
                file_path = input("\n\tEnter the file path with keywords (one keyword per line): ")
                with open(file_path, 'r') as f:
                    keywords = [line.strip() for line in f.readlines()]
            elif source.lower() == 'manual':
                num_keywords = int(input("\n\tEnter the number of keywords: "))
                keywords = []
                for i in range(num_keywords):
                    keyword = input(f"\tEnter keyword {i + 1}: ")
                    keywords.append(keyword)
            else:
                print("Invalid input. Please enter 'file' or 'manual'.")
                return []

            return keywords
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []

    def save_domains_to_file(self, file_name='Domains.txt'):
        try:
            with open(file_name, 'w') as f:
                for domain in self.domains:
                    f.write(domain + '\n')
            print("Domains saved to file successfully.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def print_domains(self):
        try:
            for domain in self.domains:
                print(domain)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def run(self):
        try:
            banner = """
 ██████████     █████████                      █████     █████                       
░░███░░░░███   ███░░░░░███                    ░░███     ░░███                        
 ░███   ░░███ ███     ░░░  ████████   ██████   ░███████  ░███████   ██████  ████████ 
 ░███    ░███░███         ░░███░░███ ░░░░░███  ░███░░███ ░███░░███ ███░░███░░███░░███
 ░███    ░███░███    █████ ░███ ░░░   ███████  ░███ ░███ ░███ ░███░███████  ░███ ░░░ 
 ░███    ███ ░░███  ░░███  ░███      ███░░███  ░███ ░███ ░███ ░███░███░░░   ░███     
 ██████████   ░░█████████  █████    ░░████████ ████████  ████████ ░░██████  █████    
░░░░░░░░░░     ░░░░░░░░░  ░░░░░      ░░░░░░░░ ░░░░░░░░  ░░░░░░░░   ░░░░░░  ░░░░░     
                                                                            
            """
        
            print(banner)

            keywords = self.get_user_input()

            if keywords:
                for keyword in keywords:
                    self.search_domains(keyword)

                self.save_domains_to_file()
                self.print_domains()

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    grabber = DomainGrabber()
    grabber.run()

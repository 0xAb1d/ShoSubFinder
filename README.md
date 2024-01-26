# ShoSubFinder
### ShoSubFinder is a powerful and specialized reconnaissance tool to discover subdomains for a specified domain, organization, or ASN by leveraging the extensive database of Shodan. Whether you're conducting a security assessment, gathering intelligence for a research project, or simply exploring the digital landscape, ShoSubFinder is your reliable companion. It provides a flexible and streamlined approach to uncovering the subdomains of targets through passive reconnaissance techniques.

## Features
- **Domain Search**: Look for subdomains related to a specific domain.
- **Organization Search**: Find subdomains associated with a particular organization.
- **ASN Search**: Discover subdomains linked to a specific ASN.
- **Combination Searches**: Combine the above searches to get comprehensive results.
- **Export to File**: Easily save the list of found subdomains to a file for further analysis.

## Prerequisites
Before you start using ShoSubFinder, ensure you have the following:
- Python 3.x installed on your system.
- Shodan Python library installed. You can install it using `pip install shodan`.
- An active Shodan API key. You can obtain it by registering on [Shodan's website](https://www.shodan.io/).

## Installation
1. Clone the repository to your local machine:
```
git clone https://github.com/MrNeutr1n0/ShoSubFinder.git
```
2. Navigate to the cloned directory:
```
cd ShoSubFinder
```
3. Install the required Python libraries:
```
pip install -r requirements.txt
```

## Configuration
Insert your Shodan API in `config.yaml`
```yaml
shodan_api_key: "YOUR_SHODAN_API_KEY_HERE"
```

## Usage
### Options

- `-d`, `--domain`: Define the domain/hostname you want to search.
- `-org`, `--organization`: Define the organization name you want to search (use quotes).
- `-asn`, `--asn`: Define the ASN number you want to search (use quotes).
- `-o`, `--output`: Define the output file to save the results (required).

Here are some examples of how to use it:

- To find subdomains for a specific domain and save the results to a file:
```
python shosubfinder.py -d example.com -o results.txt
```
- To find subdomains for a specific organization:
```
python shosubfinder.py -org "Example Org" -o results.txt
```
- To perform a combined search using domain, ASN, and organization, and save the results:
```
python shosubfinder.py -d example.com -asn "AS1234" -org "Example Org" -o results.txt
```

## Disclaimer
ShoSubFinder is developed for educational and professional purposes. Please use ShoSubFinder responsibly. You are responsible for your actions. Misuse of this tool can lead to potential legal consequences. The developer assumes no liability and is not responsible for any misuse or damage caused by this program.


## License
The ShoSubFinder is distributed under the MIT License. See [MIT License](LICENSE) for more information.


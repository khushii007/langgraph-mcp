import yaml

# Load YAML from a file
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

print("Loaded config:")
print(config)

# Dump dictionary into YAML
data = {'name': 'Khushi', 'devops': True}
with open("output.yaml", "w") as file:
    yaml.dump(data, file)

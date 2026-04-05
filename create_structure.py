import os

# Create all necessary directories
directories = [
    'models',
    'artifacts',
    'logs',
    'Sepsis_Data/raw',
    'Sepsis_Data/processed',
    'Sepsis_Data/external',
    'tests',
    'tests/test_components',
    'tests/test_pipeline',
    'app',
    'app/templates',
    'app/static'
]

for directory in directories:
    os.makedirs(directory, exist_ok=True)
    print(f'Created: {directory}')

print('\n✓ All directories created successfully!')

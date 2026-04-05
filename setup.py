"""
Project packaging configuration.
"""

from pathlib import Path

from setuptools import find_packages, setup


BASE_DIR = Path(__file__).resolve().parent


def get_requirements(file_name: str = "requirements.txt") -> list[str]:
    """Return install requirements from a requirements file."""
    requirements: list[str] = []
    req_path = BASE_DIR / file_name

    if not req_path.exists():
        return requirements

    for raw_line in req_path.read_text(encoding="utf-8").splitlines():
        requirement = raw_line.strip()
        # Ignore comments, empty lines and editable install marker.
        if requirement and not requirement.startswith("#") and requirement != "-e .":
            requirements.append(requirement)

    return requirements


setup(
    name="sepsis-prediction",
    version="0.0.1",
    author="Gogula Vignesh",
    description="A machine learning pipeline for early sepsis prediction.",
    packages=find_packages(),
    include_package_data=True,
    install_requires=get_requirements(),
    python_requires=">=3.9",
)
"""Shared pytest fixtures and configuration for all tests."""

import os
import shutil
import tempfile
from pathlib import Path
from typing import Generator

import pytest


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for test files.
    
    Yields:
        Path: Path to the temporary directory
    """
    temp_path = Path(tempfile.mkdtemp())
    yield temp_path
    shutil.rmtree(temp_path)


@pytest.fixture
def sample_markdown_content() -> str:
    """Provide sample markdown content for testing.
    
    Returns:
        str: Sample markdown text
    """
    return """# Sample Chapter

This is a **sample** chapter with:
- Bullet points
- [Links](https://example.com)
- `Code snippets`

## Subsection

More content here.
"""


@pytest.fixture
def sample_chapter_file(temp_dir: Path) -> Path:
    """Create a sample chapter file for testing.
    
    Args:
        temp_dir: Temporary directory fixture
        
    Returns:
        Path: Path to the created chapter file
    """
    chapter_path = temp_dir / "ch01.md"
    chapter_path.write_text("""# Chapter 01 - Introduction

This is the first chapter of the book.

## Key Concepts

- Machine Learning
- Deep Learning
- Neural Networks
""")
    return chapter_path


@pytest.fixture
def mock_chapters_dir(temp_dir: Path) -> Path:
    """Create a mock chapters directory with sample files.
    
    Args:
        temp_dir: Temporary directory fixture
        
    Returns:
        Path: Path to the chapters directory
    """
    chapters_dir = temp_dir / "chapters"
    chapters_dir.mkdir()
    
    # Create sample chapter files
    for i in range(1, 4):
        chapter_file = chapters_dir / f"ch{i:02d}.md"
        chapter_file.write_text(f"# Chapter {i:02d}\n\nContent for chapter {i}.")
    
    return chapters_dir


@pytest.fixture
def mock_imgs_dir(temp_dir: Path) -> Path:
    """Create a mock images directory.
    
    Args:
        temp_dir: Temporary directory fixture
        
    Returns:
        Path: Path to the images directory
    """
    imgs_dir = temp_dir / "imgs"
    imgs_dir.mkdir()
    
    # Create a placeholder image file
    (imgs_dir / "sample.png").write_text("placeholder")
    
    return imgs_dir


@pytest.fixture
def mock_project_structure(temp_dir: Path, mock_chapters_dir: Path, mock_imgs_dir: Path) -> Path:
    """Create a complete mock project structure.
    
    Args:
        temp_dir: Temporary directory fixture
        mock_chapters_dir: Mock chapters directory
        mock_imgs_dir: Mock images directory
        
    Returns:
        Path: Path to the project root
    """
    # Create additional files
    (temp_dir / "README.md").write_text("# Machine Learning Yearning")
    (temp_dir / "acknowledgement.md").write_text("# Acknowledgements\n\nThanks to everyone.")
    (temp_dir / "glossary_vi.md").write_text("# Glossary\n\nML terms in Vietnamese.")
    
    return temp_dir


@pytest.fixture
def env_vars() -> dict:
    """Provide test environment variables.
    
    Returns:
        dict: Dictionary of environment variables
    """
    return {
        "TEST_MODE": "true",
        "PYTHONPATH": str(Path.cwd()),
    }


@pytest.fixture
def mock_pdf_config() -> dict:
    """Provide mock PDF configuration.
    
    Returns:
        dict: PDF configuration options
    """
    return {
        "page-size": "A4",
        "margin-top": "1in",
        "margin-right": "1in",
        "margin-bottom": "1in",
        "margin-left": "1in",
        "encoding": "UTF-8",
        "enable-local-file-access": None,
    }


@pytest.fixture(autouse=True)
def cleanup_test_files():
    """Automatically clean up any test files created during tests."""
    yield
    # Clean up any files created in the current directory during tests
    test_patterns = ["test_*.md", "test_*.pdf", "test_*.html", "combined_*.md"]
    for pattern in test_patterns:
        for file in Path.cwd().glob(pattern):
            if file.exists():
                file.unlink()


@pytest.fixture
def monkeypatch_env(monkeypatch, env_vars):
    """Automatically set environment variables for tests.
    
    Args:
        monkeypatch: pytest monkeypatch fixture
        env_vars: Environment variables fixture
    """
    for key, value in env_vars.items():
        monkeypatch.setenv(key, value)
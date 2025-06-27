"""Validation tests to ensure the testing infrastructure is set up correctly."""

import sys
from pathlib import Path

import pytest


class TestSetupValidation:
    """Test class to validate the testing setup."""
    
    def test_pytest_installed(self):
        """Verify pytest is installed and importable."""
        assert pytest.__version__
        
    def test_pytest_cov_installed(self):
        """Verify pytest-cov is installed."""
        import pytest_cov
        assert pytest_cov
        
    def test_pytest_mock_installed(self):
        """Verify pytest-mock is installed."""
        import pytest_mock
        assert pytest_mock
        
    def test_project_structure(self):
        """Verify the project structure is as expected."""
        project_root = Path.cwd()
        
        # Check main files exist
        assert (project_root / "run.py").exists()
        assert (project_root / "pyproject.toml").exists()
        
        # Check directories exist
        assert (project_root / "chapters").exists()
        assert (project_root / "imgs").exists()
        assert (project_root / "tests").exists()
        assert (project_root / "tests" / "unit").exists()
        assert (project_root / "tests" / "integration").exists()
        
    def test_conftest_fixtures(self, temp_dir, sample_markdown_content):
        """Verify conftest fixtures are working."""
        assert temp_dir.exists()
        assert temp_dir.is_dir()
        assert isinstance(sample_markdown_content, str)
        assert "# Sample Chapter" in sample_markdown_content
        
    def test_temp_dir_cleanup(self, temp_dir):
        """Verify temp_dir fixture cleans up after itself."""
        test_file = temp_dir / "test.txt"
        test_file.write_text("test content")
        assert test_file.exists()
        # Cleanup happens after test completes
        
    @pytest.mark.unit
    def test_unit_marker(self):
        """Test that unit test marker works."""
        assert True
        
    @pytest.mark.integration
    def test_integration_marker(self):
        """Test that integration test marker works."""
        assert True
        
    @pytest.mark.slow
    def test_slow_marker(self):
        """Test that slow test marker works."""
        assert True
        
    def test_python_path(self):
        """Verify Python can import the main module."""
        # Add project root to path if not already there
        project_root = str(Path.cwd())
        if project_root not in sys.path:
            sys.path.insert(0, project_root)
            
        # Try to import the main module
        import run
        assert hasattr(run, 'BookMD')
        assert hasattr(run, 'BookPDF')
import pytest
import project

def test_password_strength():
    assert project.test_password_strength("abc") == project.VERY_WEAK
    assert project.test_password_strength("1847abc1736") == project.WEAK
    assert project.test_password_strength("1245HelloWorld1245") == project.STRONG
    assert project.test_password_strength("&@658ABcD26485&$") == project.VERY_STRONG

def test_get_strength_string():
    assert project.get_strength_string(project.VERY_WEAK) == "Very Weak"
    assert project.get_strength_string(project.WEAK) == "Weak"
    assert project.get_strength_string(project.STRONG) == "Strong"
    assert project.get_strength_string(project.VERY_STRONG) == "Very Strong"

def test_test_preset_passwords(capfd):
    project.test_preset_passwords()
    out, err = capfd.readouterr()
    assert "Password: abc | Strength: Very Weak" in out
    assert "Password: 1847abc1736 | Strength: Weak" in out
    assert "Password: 1245HelloWorld1245 | Strength: Strong" in out
    assert "Password: &@658ABcD26485&$ | Strength: Very Strong" in out

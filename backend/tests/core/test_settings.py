from app.core.settings import Settings


def test_settings_initialization():
    # Test valid initialization
    settings = Settings(
        ml_api_secret_api_key="test_secret_key",
        database_url="test_database_url",
        blob_read_write_token="test_blob_token",
    )
    assert settings.app_name == "Baynext API"
    assert settings.ml_api_secret_api_key.get_secret_value() == "test_secret_key"
    assert settings.database_url.get_secret_value() == "test_database_url"
    assert settings.blob_read_write_token.get_secret_value() == "test_blob_token"


def test_settings_env_file_loading(monkeypatch):
    # Mock environment variable
    ml_api_secret_api_key = "env_secret_key"
    monkeypatch.setenv("ML_API_SECRET_API_KEY", ml_api_secret_api_key)

    # Test loading from environment variable
    settings = Settings()
    assert settings.ml_api_secret_api_key.get_secret_value() == ml_api_secret_api_key

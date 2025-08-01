from platformdirs import user_data_dir
from pathlib import Path
import json

class Config:
    APP_NAME = "EverAfter"
    APP_AUTHOR = "kelbwah"
    DATA_DIR = Path(user_data_dir(APP_NAME, APP_AUTHOR))
    DATA_LOCATION = DATA_DIR / "settings.json"
    FACTORY_SETTINGS = {
        "WINDOW_WIDTH": 1280,
        "WINDOW_HEIGHT": 720,
        "MASTER_SOUND_LEVEL": 100,
        "MUSIC_SOUND_LEVEL": 100,
        "SHOW_FPS": True,
    }

    _cached_settings = None

    @staticmethod
    def _get_factory_settings():
        return Config.FACTORY_SETTINGS
    
    @staticmethod
    def _write_to_data_dir(data):
        Config.DATA_DIR.mkdir(parents=True, exist_ok=True)
        with Config.DATA_LOCATION.open("w") as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def update_settings(new_settings):
        Config._write_to_data_dir(new_settings)
    
    @staticmethod
    def reset_settings():
        Config.update_settings(Config.FACTORY_SETTINGS)

    @staticmethod
    def load_settings():
        if Config._cached_settings is not None:
            return Config._cached_settings
        
        settings = None

        if not Config.DATA_DIR.exists():
            Config._write_to_data_dir(Config._get_factory_settings())
            settings = Config._get_factory_settings()
        else:
            with Config.DATA_LOCATION.open("r") as f:
                settings = json.load(f)
        
        print("not grabbing settings from cache...")
        Config._cached_settings = settings
        return settings

    @staticmethod
    def get_setting(setting):
        return Config.load_settings()[setting]
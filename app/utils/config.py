from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str

    ADMIN_IDS: str

    DATABASE_URL: str

    DEFAULT_GIFT_NAME: str

    DEFAULT_GIFT_PRICE: int

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    @property
    def admins(self) -> list[int]:
        return [int(x.strip()) for x in self.ADMIN_IDS.split(",")]


settings = Settings()

from app.utils.config import settings

print(settings.BOT_TOKEN)
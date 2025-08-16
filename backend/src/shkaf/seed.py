from uuid import UUID, uuid4

from sqlalchemy.ext.asyncio import AsyncSession

from shkaf.models import (
    Closet,
    ClothingPieceFabric,
    ClothingPieceSize,
    ClothingPieceStatus,
    Color,
    WeatherSeason,
)


async def register_user_seed(user_id: UUID, session: AsyncSession) -> None:
    colors: list = [
        Color(id=uuid4(), user_id=user_id, name_en="Red", name_mk="Црвена", hex="#FF0000"),
        Color(id=uuid4(), user_id=user_id, name_en="Green", name_mk="Зелена", hex="#00FF00"),
        Color(id=uuid4(), user_id=user_id, name_en="Blue", name_mk="Сина", hex="#0000FF"),
        Color(id=uuid4(), user_id=user_id, name_en="Black", name_mk="Црна", hex="#000000"),
        Color(id=uuid4(), user_id=user_id, name_en="White", name_mk="Бела", hex="#FFFFFF"),
        Color(id=uuid4(), user_id=user_id, name_en="Yellow", name_mk="Жолта", hex="#FFFF00"),
        Color(id=uuid4(), user_id=user_id, name_en="Purple", name_mk="Виолетова", hex="#800080"),
        Color(id=uuid4(), user_id=user_id, name_en="Pink", name_mk="Розова", hex="#FFC0CB"),
    ]
    seasons: list = [
        WeatherSeason(id=uuid4(), user_id=user_id, name_en="Spring", name_mk="Пролет"),
        WeatherSeason(id=uuid4(), user_id=user_id, name_en="Summer", name_mk="Лето"),
        WeatherSeason(id=uuid4(), user_id=user_id, name_en="Autumn", name_mk="Есен"),
        WeatherSeason(id=uuid4(), user_id=user_id, name_en="Winter", name_mk="Зима"),
    ]
    statuses: list = [
        ClothingPieceStatus(id=uuid4(), user_id=user_id, name_en="Ready", name_mk="Подготвено"),
        ClothingPieceStatus(id=uuid4(), user_id=user_id, name_en="Dirty", name_mk="Валкано"),
        ClothingPieceStatus(id=uuid4(), user_id=user_id, name_en="Laundry", name_mk="Перење"),
        ClothingPieceStatus(id=uuid4(), user_id=user_id, name_en="Worn Out", name_mk="Износено"),
        ClothingPieceStatus(id=uuid4(), user_id=user_id, name_en="Sell", name_mk="Продај"),
        ClothingPieceStatus(id=uuid4(), user_id=user_id, name_en="Donate", name_mk="Донирај"),
        ClothingPieceStatus(id=uuid4(), user_id=user_id, name_en="Throw Away", name_mk="Фрли"),
    ]
    fabrics: list = [
        ClothingPieceFabric(id=uuid4(), user_id=user_id, name_en="Cotton", name_mk="Памук"),
        ClothingPieceFabric(id=uuid4(), user_id=user_id, name_en="Polyester", name_mk="Полиестер"),
        ClothingPieceFabric(id=uuid4(), user_id=user_id, name_en="Denim", name_mk="Деним"),
        ClothingPieceFabric(id=uuid4(), user_id=user_id, name_en="Linen", name_mk="Лен"),
        ClothingPieceFabric(id=uuid4(), user_id=user_id, name_en="Silk", name_mk="Свила"),
        ClothingPieceFabric(id=uuid4(), user_id=user_id, name_en="Wool", name_mk="Волна"),
        ClothingPieceFabric(id=uuid4(), user_id=user_id, name_en="Fur", name_mk="Крзно"),
        ClothingPieceFabric(id=uuid4(), user_id=user_id, name_en="Spandex", name_mk="Спандекс"),
    ]
    sizes: list = [
        ClothingPieceSize(id=uuid4(), user_id=user_id, name_en="XS", name_mk="XS"),
        ClothingPieceSize(id=uuid4(), user_id=user_id, name_en="S", name_mk="S"),
        ClothingPieceSize(id=uuid4(), user_id=user_id, name_en="M", name_mk="M"),
        ClothingPieceSize(id=uuid4(), user_id=user_id, name_en="L", name_mk="L"),
        ClothingPieceSize(id=uuid4(), user_id=user_id, name_en="XL", name_mk="XL"),
        ClothingPieceSize(id=uuid4(), user_id=user_id, name_en="XXL", name_mk="XXL"),
    ]
    session.add_all(colors + seasons + statuses + fabrics + sizes)

    closet = Closet(user_id=user_id, name="Мојот шкаф")
    session.add(closet)

    await session.commit()

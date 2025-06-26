from enum import StrEnum


class ClothingPieceStatusEnum(StrEnum):
    LAUNDRY = "LAUNDRY"
    WORN_OUT = "WORN_OUT"
    DIRTY = "DIRTY"
    READY = "READY"
    SELL = "SELL"
    DONATE = "DONATE"
    THROW_AWAY = "THROW_AWAY"


class ClothingPieceFabricEnum(StrEnum):
    COTTON = "COTTON"
    POLYESTER = "POLYESTER"
    DENIM = "DENIM"
    LINEN = "LINEN"
    SILK = "SILK"
    WOOL = "WOOL"
    FUR = "FUR"
    SPANDEX = "SPANDEX"
